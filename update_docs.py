#!/usr/bin/env python3
"""
UniFi API Docs Updater
======================
Espelha automaticamente TODA a documentação oficial da API UniFi
(https://developer.ui.com) - organizada por aplicação e por versão.

Como funciona (sem navegador, só stdlib):
  1. Baixa o sitemap.xml oficial e descobre todos os pares {app}/{versao}.
  2. Para cada par, baixa o payload RSC (Next.js) de uma página com o header
     `RSC: 1` e extrai o objeto `fullSpec` - que é o **OpenAPI completo** daquela
     versão (todos os paths, schemas, exemplos).
  3. Salva `<app>/<versao>/openapi.json` (fonte da verdade) e gera
     `<app>/<versao>/reference.md` (referência legível por humanos e LLMs).
  4. Gera índices para consumo por LLM: `catalog.json` e `llms.txt`.

USO:
  python update_docs.py                      # tudo (todas as versões)
  python update_docs.py --latest-only        # só a versão mais recente de cada app
  python update_docs.py --app network        # só um app
  python update_docs.py --app protect --version v7.1.46
  python update_docs.py --dry-run            # não escreve nada
"""

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from xml.etree import ElementTree as ET

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ORIGIN = "https://developer.ui.com"
SITEMAP = f"{ORIGIN}/sitemap.xml"
WORKERS = 8
METHODS = ["get", "post", "put", "delete", "patch", "head", "options"]

# proxy interno usado pelo Cloud Connector para cada app (modo local)
APP_PROXY = {"network": "network", "protect": "protect", "mobility": "mobility"}

UA = "Mozilla/5.0 (compatible; unifi-api-docs/1.0; +https://github.com/opastorello/unifi-api-docs)"


# ── HTTP ────────────────────────────────────────────────────────────────────────

def http_get(url, rsc=False, timeout=40):
    headers = {"User-Agent": UA, "Accept": "*/*"}
    if rsc:
        headers["RSC"] = "1"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


# ── Descoberta via sitemap ──────────────────────────────────────────────────────

def discover():
    """Retorna {app: {version: {'pages': [paths], 'lastmod': str}}}."""
    xml = http_get(SITEMAP)
    # remove namespace pra simplificar
    xml = re.sub(r'xmlns="[^"]+"', "", xml, count=1)
    root = ET.fromstring(xml)
    catalog = {}
    for url in root.findall(".//url"):
        loc = url.findtext("loc") or ""
        lastmod = url.findtext("lastmod") or ""
        path = loc.replace(ORIGIN, "").strip("/")
        if not path:
            continue
        parts = path.split("/")
        if len(parts) < 2 or not re.match(r"^v\d+\.", parts[1]):
            continue
        app, version = parts[0], parts[1]
        node = catalog.setdefault(app, {}).setdefault(version, {"pages": [], "lastmod": ""})
        node["pages"].append("/" + path)
        if lastmod > node["lastmod"]:
            node["lastmod"] = lastmod
    return catalog


def version_key(v):
    nums = re.findall(r"\d+", v)
    return tuple(int(n) for n in nums)


# ── Extração do OpenAPI embutido (fullSpec) ─────────────────────────────────────

def _balanced(t, start):
    depth = 0
    in_str = False
    esc = False
    for i in range(start, len(t)):
        c = t[i]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    return t[start:i + 1]
    return None


def extract_spec(pages):
    """Tenta extrair o fullSpec do RSC das páginas até conseguir."""
    # endpoints costumam estar à frente; tenta gettingstarted primeiro (rápido) e depois outras
    ordered = sorted(pages, key=lambda p: (0 if p.endswith(("gettingstarted", "getting-started")) else 1, len(p)))
    for page in ordered:
        try:
            t = http_get(ORIGIN + page, rsc=True)
        except Exception:
            continue
        k = t.find('"fullSpec":')
        if k < 0:
            continue
        brace = t.find("{", k)
        obj = _balanced(t, brace)
        if not obj:
            continue
        try:
            return json.loads(obj)
        except Exception:
            continue
    return None


# ── OpenAPI → Markdown ──────────────────────────────────────────────────────────

def clean(text):
    if not text:
        return ""
    t = text.replace("<br/>", "\n").replace("<br>", "\n")
    t = t.replace("—", "-")  # travessao (em dash) vindo da origem -> hifen
    return re.sub(r"\n{3,}", "\n\n", t).strip()


def deref(schema, spec):
    comp = spec.get("components", {}).get("schemas", {})
    if isinstance(schema, dict) and "$ref" in schema:
        name = schema["$ref"].split("/")[-1]
        return name, comp.get(name, {})
    return None, schema


def scalar_desc(s):
    bits = []
    t = s.get("type")
    if isinstance(t, list):
        t = "|".join(str(x) for x in t)
    if t:
        bits.append(f"`{t}`")
    if s.get("format"):
        bits.append(f"({s['format']})")
    if s.get("nullable"):
        bits.append("nullable")
    if "enum" in s:
        bits.append("enum: " + ", ".join(str(v) for v in s["enum"][:12]))
    if "default" in s:
        bits.append(f"default={s['default']}")
    ex = s.get("example")
    if ex is not None and not isinstance(ex, (dict, list)):
        bits.append(f"ex: `{ex}`")
    return " ".join(bits)


def render_schema(schema, spec, depth=0, max_depth=6, visited=None, lines=None, indent=0):
    if lines is None:
        lines = []
    if visited is None:
        visited = frozenset()
    pad = "  " * indent
    name, schema = deref(schema, spec)
    if name:
        if name in visited:
            lines.append(f"{pad}- _(ref recursiva → `{name}`)_")
            return lines
        visited = visited | {name}
    if not isinstance(schema, dict):
        return lines
    if "allOf" in schema:
        for sub in schema["allOf"]:
            render_schema(sub, spec, depth, max_depth, visited, lines, indent)
    if "oneOf" in schema or "anyOf" in schema:
        key = "oneOf" if "oneOf" in schema else "anyOf"
        disc = schema.get("discriminator", {})
        inv = {v.split("/")[-1]: k for k, v in disc.get("mapping", {}).items()}
        lines.append(f"{pad}- _um de ({disc.get('propertyName','variantes')}):_")
        for sub in schema[key]:
            sn, _ = deref(sub, spec)
            lines.append(f"{pad}  - **{inv.get(sn, sn or 'variante')}**:")
            render_schema(sub, spec, depth + 1, max_depth, visited, lines, indent + 2)
        return lines
    t = schema.get("type")
    if t == "object" or "properties" in schema:
        req = set(schema.get("required", []))
        disc = schema.get("discriminator", {})
        mapping = disc.get("mapping", {})
        if mapping:
            variants = ", ".join(f"`{k}`→`{v.split('/')[-1]}`" for k, v in mapping.items())
            lines.append(f"{pad}- _variantes por `{disc.get('propertyName')}`: {variants} (ver openapi.json)_")
        for pname, pval in schema.get("properties", {}).items():
            _, pres = deref(pval, spec)
            mark = " **(obrigatório)**" if pname in req else ""
            sd = scalar_desc(pres)
            desc = clean(pres.get("description", "")).replace("\n", " ")
            if len(desc) > 160:
                desc = desc[:157] + "…"
            extra = " - ".join(x for x in [sd, desc] if x)
            lines.append(f"{pad}- `{pname}`{mark}" + (f": {extra}" if extra else ""))
            pt = pres.get("type")
            nested = pt == "object" or "properties" in pres or "oneOf" in pres or "anyOf" in pres or "allOf" in pres or pt == "array"
            if depth < max_depth and nested:
                render_schema(pval, spec, depth + 1, max_depth, visited, lines, indent + 1)
    elif t == "array":
        ind, ires = deref(schema.get("items", {}), spec)
        label = f"`{ind}`" if ind else f"`{ires.get('type','obj')}`"
        lines.append(f"{pad}- _array de_ {label}:")
        if depth < max_depth:
            render_schema(schema.get("items", {}), spec, depth + 1, max_depth, visited, lines, indent + 1)
    else:
        sd = scalar_desc(schema)
        if sd:
            lines.append(f"{pad}- {sd}")
    return lines


def schema_block(schema, spec, max_depth=6):
    if not schema:
        return "_(sem corpo)_"
    lines = render_schema(schema, spec, max_depth=max_depth)
    return "\n".join(lines) if lines else "_(estrutura vazia)_"


def params_table(params, spec):
    if not params:
        return ""
    rows = ["| Parâmetro | Em | Obrig. | Tipo | Descrição |", "|---|---|---|---|---|"]
    for p in params:
        _, p = deref(p, spec)
        s = p.get("schema", {})
        typ = s.get("type", "")
        if isinstance(typ, list):
            typ = "|".join(str(x) for x in typ)
        if s.get("format"):
            typ += f" ({s['format']})"
        if "enum" in s:
            typ += " enum"
        d = clean(p.get("description", "")).replace("\n", " ")
        if s.get("default") is not None:
            d = (d + f" (default {s['default']})").strip()
        rows.append(f"| `{p.get('name')}` | {p.get('in')} | {'sim' if p.get('required') else 'não'} | {typ} | {d} |")
    return "\n".join(rows)


def curl_examples(app, server_url, method, path, has_body):
    """Gera exemplos cURL. server_url relativo → app local; absoluto → cloud direto."""
    m = method.upper()
    body = ' \\\n     -H "Content-Type: application/json" -d \'{ ... }\'' if has_body else ""
    if server_url.startswith("http"):  # site-manager (cloud direto)
        return [("Cloud", f'curl -X {m} "{server_url}{path}" \\\n     -H "X-API-Key: $UNIFI_SM_KEY"{body}')]
    # network / protect / mobility → local + remoto
    proxy = APP_PROXY.get(app, app)
    local = f'curl -X {m} "https://$UNIFI_HOST/proxy/{proxy}{server_url}{path}" \\\n     -H "X-API-KEY: $UNIFI_API_KEY"{body}'
    remote = f'curl -X {m} "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/{proxy}{server_url}{path}" \\\n     -H "X-API-Key: $UNIFI_SM_KEY"{body}'
    return [("Local", local), ("Remoto (Cloud Connector)", remote)]


def build_reference(app, version, spec, lastmod):
    info = spec.get("info", {})
    servers = spec.get("servers", [{}])
    server_url = servers[0].get("url", "") if servers else ""
    sec = spec.get("components", {}).get("securitySchemes") or {}
    sec_hdr = next((v.get("name") for v in sec.values() if v.get("in") == "header"), None)
    paths = spec.get("paths", {})

    # agrupa por tag
    tag_defs = spec.get("tags", [])
    tag_order = [t["name"] for t in tag_defs] or ["Endpoints"]
    by_tag = {}
    for path, item in paths.items():
        for m in METHODS:
            if m in item:
                op = item[m]
                for tg in (op.get("tags") or ["Endpoints"]):
                    by_tag.setdefault(tg, []).append((path, m, op))
    for tg in by_tag:
        if tg not in tag_order:
            tag_order.append(tg)

    n_ops = sum(len(v) for v in by_tag.values())
    o = []
    W = o.append
    W(f"# {info.get('title','UniFi API')} - {version} - Referência\n")
    W(f"> Espelho automático de [`developer.ui.com/{app}/{version}`]({ORIGIN}/{app}/{version}).")
    W(f"> OpenAPI `{spec.get('openapi','?')}` · {n_ops} operações em {len(paths)} paths · atualizado na origem em `{lastmod or '?'}`.")
    if sec_hdr:
        W(f"> Autenticação: header `{sec_hdr}`.")
    W("")
    W(f"**OpenAPI completo (fonte da verdade):** [`openapi.json`](./openapi.json)\n")

    # prosa das tags (getting started etc.)
    for t in tag_defs:
        d = clean(t.get("description", ""))
        if d and not d.startswith("$") and not by_tag.get(t["name"]):
            W(f"## {t['name']}\n\n{d}\n")

    # índice
    W("## Índice de endpoints\n")
    W("| Categoria | Método | Path | Operação |")
    W("|---|---|---|---|")
    for tg in tag_order:
        for path, m, op in by_tag.get(tg, []):
            W(f"| {tg} | `{m.upper()}` | `{path}` | {op.get('summary','')} |")
    W("")

    # detalhe
    for tg in tag_order:
        ops = by_tag.get(tg, [])
        if not ops:
            continue
        W(f"\n---\n\n## {tg}\n")
        td = next((clean(t.get("description", "")) for t in tag_defs if t["name"] == tg), "")
        if td and not td.startswith("$"):
            W(td + "\n")
        for path, m, op in ops:
            # Header da op: para app por-console (server relativo '/integration') mostra só o
            # path (ex.: 'GET /v1/sites') — limpo; o endpoint completo Local/Remoto vem nos
            # exemplos cURL abaixo. Para app cloud (server absoluto) mostra a URL completa.
            head = f"{server_url}{path}" if server_url.startswith("http") else path
            W(f"\n### {op.get('summary') or op.get('operationId') or (m.upper()+' '+path)}\n")
            W(f"`{m.upper()} {head}`  ·  operationId: `{op.get('operationId','')}`\n")
            d = clean(op.get("description", ""))
            if d:
                W(d + "\n")
            params = op.get("parameters", [])
            if params:
                W("**Parâmetros**\n")
                W(params_table(params, spec) + "\n")
            rb = op.get("requestBody", {})
            sch = rb.get("content", {}).get("application/json", {}).get("schema")
            if sch:
                W("**Corpo da requisição** (`application/json`)\n")
                W(schema_block(sch, spec) + "\n")
            resps = op.get("responses", {})
            ok = next((c for c in ("200", "201", "202", "204") if c in resps), None)
            if ok:
                rsch = resps[ok].get("content", {}).get("application/json", {}).get("schema")
                W(f"**Resposta {ok}**" + (f" - {clean(resps[ok].get('description',''))}" if resps[ok].get("description") else "") + "\n")
                if rsch:
                    W(schema_block(rsch, spec, max_depth=5) + "\n")
            errs = sorted(c for c in resps if c not in ("200", "201", "202", "204"))
            if errs:
                W("**Erros possíveis:** " + ", ".join("`" + c + "`" for c in errs) + "\n")
            ex = curl_examples(app, server_url, m, path, bool(sch))
            W("<details><summary>Exemplo cURL</summary>\n")
            for label, code in ex:
                W(f"```bash\n# {label}\n{code}\n```")
            W("</details>\n")
    n_categories = len([t for t in tag_order if by_tag.get(t)])
    return "\n".join(o), n_ops, tag_order, n_categories


# ── Escrita / hash ──────────────────────────────────────────────────────────────

def write_if_changed(relpath, content, dry):
    full = os.path.join(BASE_DIR, relpath)
    new_h = hashlib.md5(content.encode("utf-8")).hexdigest()
    status = "NEW"
    if os.path.exists(full):
        with open(full, encoding="utf-8") as f:
            old = f.read()
        if hashlib.md5(old.encode("utf-8")).hexdigest() == new_h:
            return "UNCHANGED"
        status = "UPDATED"
    if not dry:
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(content)
    return status


# ── Por versão ──────────────────────────────────────────────────────────────────

def process_version(app, version, node, dry):
    spec = extract_spec(node["pages"])
    if not spec:
        return {"app": app, "version": version, "error": "sem fullSpec"}
    info = spec.get("info", {})
    spec_json = json.dumps(spec, indent=2, ensure_ascii=False)
    s1 = write_if_changed(f"{app}/{version}/openapi.json", spec_json, dry)
    ref, n_ops, tags, n_categories = build_reference(app, version, spec, node["lastmod"])
    s2 = write_if_changed(f"{app}/{version}/reference.md", ref, dry)
    return {
        "app": app, "version": version, "title": info.get("title", ""),
        "spec_version": info.get("version", version), "openapi": spec.get("openapi", ""),
        "paths": len(spec.get("paths", {})), "operations": n_ops, "categories": n_categories,
        "tags": [t for t in tags], "lastmod": node["lastmod"],
        "status": {"openapi.json": s1, "reference.md": s2},
    }


# ── Índices LLM ───────────────────────────────────────────────────────────────

def build_indexes(results, catalog, dry):
    ok = [r for r in results if "error" not in r]
    apps = {}
    for r in ok:
        apps.setdefault(r["app"], []).append(r)
    for a in apps:
        apps[a].sort(key=lambda r: version_key(r["version"]), reverse=True)

    # data de modificação mais recente na origem (determinístico - sem relógio local,
    # pra o CI só commitar quando a documentação realmente mudar)
    source_lastmod = max((r.get("lastmod") or "" for r in ok), default="")

    # catalog.json (indice estruturado para LLMs/ferramentas)
    catalog_obj = {
        "source": ORIGIN,
        "source_lastmod": source_lastmod,
        "apps": {
            a: {
                "latest": apps[a][0]["version"],
                "versions": [
                    {
                        "version": r["version"], "openapi": f"{a}/{r['version']}/openapi.json",
                        "reference": f"{a}/{r['version']}/reference.md",
                        "operations": r["operations"], "paths": r["paths"],
                        "categories": r.get("categories", 0),
                        "spec_version": r["spec_version"], "lastmod": r["lastmod"],
                    } for r in apps[a]
                ],
            } for a in sorted(apps)
        },
    }
    write_if_changed("catalog.json", json.dumps(catalog_obj, indent=2, ensure_ascii=False), dry)

    # llms.txt (padrão llmstxt.org)
    L = []
    L.append("# UniFi API - Documentação (espelho automático)")
    L.append("")
    L.append("> Espelho automático e versionado da documentação oficial da API UniFi "
             "(https://developer.ui.com), pronto para consumo por humanos e por IAs/LLMs. "
             "Cada versão de cada aplicação tem o OpenAPI completo (`openapi.json`) e uma "
             "referência em Markdown (`reference.md`). Atualizado por CI.")
    L.append("")
    L.append("Aplicações: " + ", ".join(sorted(apps.keys())) + ".")
    L.append("Modos de acesso: **Local** (`https://<console>/proxy/<app>/integration/...`, header "
             "`X-API-KEY`) e **Remoto/Cloud Connector** "
             "(`https://api.ui.com/v1/connector/consoles/{id}/<app>/integration/...`, header `X-API-Key`).")
    L.append("")
    for a in sorted(apps.keys()):
        versions = apps[a]
        L.append(f"## {a} (mais recente: {versions[0]['version']})")
        for r in versions:
            tag = " (latest)" if r is versions[0] else ""
            L.append(f"- [{a} {r['version']}{tag}]({ORIGIN}/{a}/{r['version']}): "
                     f"{r['operations']} operações - OpenAPI `{a}/{r['version']}/openapi.json` · "
                     f"referência `{a}/{r['version']}/reference.md`")
        L.append("")
    write_if_changed("llms.txt", "\n".join(L), dry)
    return catalog_obj


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description="Atualiza o espelho da documentação da API UniFi")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--app", help="limita a um app (network, protect, site-manager, mobility)")
    ap.add_argument("--version", help="limita a uma versão (requer --app)")
    ap.add_argument("--latest-only", action="store_true", help="só a versão mais recente de cada app")
    ap.add_argument("--workers", type=int, default=WORKERS)
    args = ap.parse_args()

    print(f"{'[DRY] ' if args.dry_run else ''}Descobrindo via sitemap…")
    catalog = discover()

    jobs = []
    for app, versions in catalog.items():
        if args.app and app != args.app:
            continue
        vlist = sorted(versions.keys(), key=version_key, reverse=True)
        if args.version:
            vlist = [v for v in vlist if v == args.version]
        elif args.latest_only:
            vlist = vlist[:1]
        for v in vlist:
            jobs.append((app, v, versions[v]))

    print(f"Alvos: {len(jobs)} versões - " +
          ", ".join(sorted({a for a, _, _ in jobs})))

    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(process_version, a, v, n, args.dry_run): (a, v) for a, v, n in jobs}
        for fut in as_completed(futs):
            a, v = futs[fut]
            try:
                r = fut.result()
            except Exception as e:
                r = {"app": a, "version": v, "error": str(e)}
            results.append(r)
            if "error" in r:
                print(f"  [ERRO] {a}/{v}: {r['error']}")
            else:
                st = ",".join(f"{k}={s}" for k, s in r["status"].items())
                print(f"  [OK]   {a}/{v}: {r['operations']} ops - {st}")

    if not args.app and not args.version:
        build_indexes(results, catalog, args.dry_run)
        print("  Índices: catalog.json, llms.txt")

    ok = [r for r in results if "error" not in r]
    errs = [r for r in results if "error" in r]
    print(f"\n{'-'*50}\n  Versões OK: {len(ok)} · erros: {len(errs)} · "
          f"operações totais: {sum(r['operations'] for r in ok)}")
    if args.dry_run:
        print("  (dry-run: nada foi escrito)")
    return 1 if errs and len(errs) == len(results) else 0


if __name__ == "__main__":
    sys.exit(main())

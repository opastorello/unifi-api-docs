#!/usr/bin/env python3
"""Atualiza badges e o catálogo dos READMEs (PT e EN) a partir do catalog.json."""

import json
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ORIGIN = "https://developer.ui.com"
SKIP_DIRS = {".git", "__pycache__", ".github", "_site"}
APP_ORDER = ["network", "protect", "site-manager", "mobility"]

L = {
    "pt": {
        "b_files": "arquivos", "b_versions": "versoes", "b_in": "em", "b_apps": "apps",
        "b_ops": "operacoes", "b_updated": "atualizado",
        "sum_head": "| App | Última versão | Categorias | Operações | Paths | OpenAPI | Referência | Doc oficial |",
        "hist_head": "| Versão | Categorias | Operações | Paths | Modificado | OpenAPI | Referência | Doc oficial |",
        "hist_summary": "📜 Histórico completo - {n} versões",
        "doc": "origem", "ok": "README", "none": "-",
    },
    "en": {
        "b_files": "files", "b_versions": "versions", "b_in": "in", "b_apps": "apps",
        "b_ops": "operations", "b_updated": "updated",
        "sum_head": "| App | Latest | Categories | Operations | Paths | OpenAPI | Reference | Official docs |",
        "hist_head": "| Version | Categories | Operations | Paths | Updated | OpenAPI | Reference | Official docs |",
        "hist_summary": "📜 Full version history - {n} versions",
        "doc": "docs", "ok": "README.en", "none": "-",
    },
}

SUM_ALIGN = "|---|---|---:|---:|---:|---|---|---|"
HIST_ALIGN = "|---|---:|---:|---:|---|---|---|---|"


def version_key(v):
    return tuple(int(n) for n in re.findall(r"\d+", v))


def count_files():
    total = 0
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        total += len(files)
    return total


def doc_link(lang, app, version):
    return f"[{L[lang]['doc']}]({ORIGIN}/{app}/{version})"


def build_badges(lang, n_files, n_versions, n_apps, n_ops, date_badge):
    t = L[lang]
    return " ".join([
        f"![{t['b_files']}](https://img.shields.io/badge/{t['b_files']}-{n_files}-blue)",
        f"![{t['b_versions']}](https://img.shields.io/badge/{t['b_versions']}-{n_versions}_{t['b_in']}_{n_apps}_{t['b_apps']}-orange)",
        f"![{t['b_ops']}](https://img.shields.io/badge/{t['b_ops']}-{n_ops}-blueviolet)",
        f"![{t['b_updated']}](https://img.shields.io/badge/{t['b_updated']}-{date_badge}-brightgreen)",
    ])


def build_catalog_md(catalog, lang):
    t = L[lang]
    apps = catalog.get("apps", {})
    order = [a for a in APP_ORDER if a in apps] + sorted(a for a in apps if a not in APP_ORDER)
    out = []

    # resumo: última versão de cada app
    out.append(t["sum_head"])
    out.append(SUM_ALIGN)
    for a in order:
        d = apps[a]
        v0 = d["versions"][0]
        cats = v0.get("categories", t["none"])
        out.append(
            f"| **{a}** | `{d['latest']}` | {cats} | {v0['operations']} | {v0['paths']} "
            f"| [json]({v0['openapi']}) | [md]({v0['reference']}) | {doc_link(lang, a, d['latest'])} |"
        )
    out.append("")

    # histórico completo (dobrável) - apps com mais de uma versão
    total = sum(len(d["versions"]) for d in apps.values())
    out.append("<details>")
    out.append(f"<summary><b>{t['hist_summary'].format(n=total)}</b></summary>")
    out.append("")
    for a in order:
        d = apps[a]
        if len(d["versions"]) <= 1:
            continue
        out.append(f"**{a}**")
        out.append("")
        out.append(t["hist_head"])
        out.append(HIST_ALIGN)
        for v in d["versions"]:
            star = " ⭐" if v["version"] == d["latest"] else ""
            lastmod = (v.get("lastmod") or "")[:10]
            cats = v.get("categories", t["none"])
            out.append(
                f"| `{v['version']}`{star} | {cats} | {v['operations']} | {v['paths']} | {lastmod} "
                f"| [json]({v['openapi']}) | [md]({v['reference']}) | {doc_link(lang, a, v['version'])} |"
            )
        out.append("")
    out.append("</details>")
    return "\n".join(out)


def replace_block(text, start, end, body):
    return re.sub(
        rf"({re.escape(start)}).*?({re.escape(end)})",
        lambda m: m.group(1) + "\n" + body + "\n" + m.group(2),
        text,
        flags=re.S,
    )


def main():
    catalog_path = os.path.join(BASE_DIR, "catalog.json")
    if not os.path.exists(catalog_path):
        print("catalog.json nao encontrado - rode update_docs.py primeiro.")
        return
    with open(catalog_path, encoding="utf-8") as f:
        catalog = json.load(f)

    apps = catalog.get("apps", {})
    n_apps = len(apps)
    n_versions = sum(len(a["versions"]) for a in apps.values())
    n_ops = sum(v["operations"] for a in apps.values() for v in a["versions"])
    n_files = count_files()
    date = (catalog.get("source_lastmod") or "")[:10] or "?"
    date_badge = date.replace("-", "--")

    for fname, lang in [("README.md", "pt"), ("README.en.md", "en")]:
        path = os.path.join(BASE_DIR, fname)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            text = original = f.read()
        text = replace_block(text, "<!-- badges:start -->", "<!-- badges:end -->",
                             build_badges(lang, n_files, n_versions, n_apps, n_ops, date_badge))
        text = replace_block(text, "<!-- catalog:start -->", "<!-- catalog:end -->",
                             build_catalog_md(catalog, lang))
        if text != original:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"{fname} atualizado - {n_versions} versoes, {n_ops} operacoes, {date}")
        else:
            print(f"{fname} sem mudancas")


if __name__ == "__main__":
    main()

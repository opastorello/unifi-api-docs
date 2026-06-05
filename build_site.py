#!/usr/bin/env python3
"""
Gera o site estatico (GitHub Pages) do espelho da API UniFi.
Identidade UniFi (ui.com): fonte UI Sans, azul de marca, navegacao em pills.
- Tema claro/escuro (toggle, auto pela preferencia do sistema, sincronizado com o Scalar).
- Idioma PT/EN (toggle, auto pelo idioma do navegador).
- Landing: 4 apps com filtro por pills, acento por app, secao Local x Remoto (copiar), bloco LLM.
- Uma pagina por versao com Scalar (referencia interativa, 'Test Request').
Saida em _site/.
"""
import json
import os
import re
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(BASE, "_site")
ORIGIN = "https://developer.ui.com"
SITE_URL = "https://opastorello.github.io/unifi-api-docs/"
APP_ORDER = ["network", "protect", "site-manager", "mobility"]
APP_LABEL = {"network": "Network", "protect": "Protect",
             "site-manager": "Site Manager", "mobility": "Mobility"}
APP_ICON = {"network": "🌐", "protect": "🎥", "site-manager": "☁️", "mobility": "📱"}
APP_ACCENT = {"network": "214,100%,60%", "protect": "270,70%,62%",
              "site-manager": "190,85%,46%", "mobility": "150,55%,45%"}
FONT = '<link rel="stylesheet" href="https://fonts.svc.ui.com/ui-sans-all.css">'
THEME_KEY, LANG_KEY = "uad-theme", "uad-lang"

THEME_INIT = f"""<script>
(function(){{
  var t=localStorage.getItem('{THEME_KEY}')||(matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light');
  var l=localStorage.getItem('{LANG_KEY}')||(((navigator.language||'pt').toLowerCase().slice(0,2)==='pt')?'pt':'en');
  var d=document.documentElement; d.dataset.theme=t; d.dataset.lang=l; d.lang=(l==='pt'?'pt-BR':'en');
}})();
</script>"""

# dicionario de traducoes (consumido por JS no client)
I18N = {
  "pt": {
    "sub": "Referência interativa e versionada — Network · Protect · Site Manager · Mobility",
    "apps": "apps", "versions": "versões", "operations": "operações", "source": "origem",
    "warnPre": "Espelho não oficial — fonte autoritativa:",
    "connTitle": "🔌 Dois modos de acesso (o diferencial)",
    "localCap": "header X-API-KEY · chave no console → Integrations",
    "remoteCap": "header X-API-Key · funciona atrás de CGNAT",
    "localTitle": "🏠 Local", "remoteTitle": "☁️ Remoto (Cloud Connector)",
    "all": "Todas", "cats": "categorias", "recent": "Mais recente",
    "openDocs": "Abrir docs", "older": "Versões anteriores",
    "mcpTitle": "🔌 Servidor MCP (use a API por IA)",
    "mcpDesc": "Quer operar a UniFi via IA/agentes? O <b>unifi-mcp</b> é um servidor MCP completo construído sobre estas specs — Local + Remoto (Cloud Connector), leitura e escrita, com passthrough auto-atualizável.",
    "mcpBtn": "Ver unifi-mcp no GitHub →",
    "llmTitle": "🤖 Para LLMs / agentes",
    "llmPre": "Índices legíveis por máquina:",
    "llmPost": "Para detalhes exatos, use o openapi.json de cada versão.",
    "footer1": 'Gerado automaticamente das specs OpenAPI · renderizado com <a href="https://scalar.com" target="_blank">Scalar</a> · fonte UI Sans (UniFi)',
    "footer2": "Ver no GitHub", "copy": "copiar", "copied": "copiado ✓",
    "desc": {
      "network": "Sites, devices, clients, redes/VLANs, WiFi, firewall, ACL, switching, DNS, hotspot, VPN, DPI.",
      "protect": "Cameras, viewers, live views, PTZ, lights, arm-profiles e eventos (WebSocket).",
      "site-manager": "Nuvem multi-site: hosts, sites, devices, ISP metrics, SD-WAN e Cloud Connector.",
      "mobility": "UniFi Connect / Mobility: workspaces, devices e clientes.",
    },
  },
  "en": {
    "sub": "Interactive, versioned reference — Network · Protect · Site Manager · Mobility",
    "apps": "apps", "versions": "versions", "operations": "operations", "source": "source",
    "warnPre": "Unofficial mirror — authoritative source:",
    "connTitle": "🔌 Two access modes (the differentiator)",
    "localCap": "header X-API-KEY · key in the console → Integrations",
    "remoteCap": "header X-API-Key · works behind CGNAT",
    "localTitle": "🏠 Local", "remoteTitle": "☁️ Remote (Cloud Connector)",
    "all": "All", "cats": "categories", "recent": "Latest",
    "openDocs": "Open docs", "older": "Older versions",
    "mcpTitle": "🔌 MCP server (drive the API with AI)",
    "mcpDesc": "Want to operate UniFi via AI/agents? <b>unifi-mcp</b> is a full MCP server built on these specs — Local + Remote (Cloud Connector), read and write, with an auto-updating passthrough.",
    "mcpBtn": "See unifi-mcp on GitHub →",
    "llmTitle": "🤖 For LLMs / agents",
    "llmPre": "Machine-readable indexes:",
    "llmPost": "For exact details, use each version's openapi.json.",
    "footer1": 'Generated automatically from the OpenAPI specs · rendered with <a href="https://scalar.com" target="_blank">Scalar</a> · UI Sans font (UniFi)',
    "footer2": "View on GitHub", "copy": "copy", "copied": "copied ✓",
    "desc": {
      "network": "Sites, devices, clients, networks/VLANs, WiFi, firewall, ACL, switching, DNS, hotspot, VPN, DPI.",
      "protect": "Cameras, viewers, live views, PTZ, lights, arm-profiles and events (WebSocket).",
      "site-manager": "Multi-site cloud: hosts, sites, devices, ISP metrics, SD-WAN and Cloud Connector.",
      "mobility": "UniFi Connect / Mobility: workspaces, devices and clients.",
    },
  },
}


def vkey(v):
    return tuple(int(n) for n in re.findall(r"\d+", v))


_RSC_PLACEHOLDER = re.compile(r"^\$[0-9a-f]+$")


def sanitize_spec(app, ver, spec):
    """Saneia a cópia exibida no site (não toca o openapi.json fonte):
    - remove descrições que são placeholders RSC não resolvidos ($1b, $1c, …);
    - garante info.version coerente com a pasta (ex.: Protect vem '0.0.0' da origem).
    """
    info = spec.setdefault("info", {})
    d = info.get("description")
    if isinstance(d, str) and _RSC_PLACEHOLDER.match(d.strip()):
        info["description"] = ""
    iv = str(info.get("version") or "").strip()
    if not iv or iv == "0.0.0":
        info["version"] = ver.lstrip("v")  # mostra a versão real no Scalar
    for t in spec.get("tags", []):
        td = t.get("description")
        if isinstance(td, str) and _RSC_PLACEHOLDER.match(td.strip()):
            t["description"] = ""
    return spec


def fix_servers(app, spec):
    """Reescreve `servers` p/ os endpoints REAIS (em vez do '/integration' relativo,
    que no GitHub Pages resolveria para o domínio do site).

    Apps por-console (network/protect) rodam atrás de /integration: damos dois
    servidores — Local (console direto) e Remoto (Cloud Connector) — com variáveis
    que o usuário preenche. Apps já com server absoluto (site-manager, mobility)
    são mantidos como na spec. Specs sem `servers` (algumas versões antigas do
    Protect) também recebem os dois servidores reais (default seg='integration').
    """
    # Apps cujo acesso é por-console (proxy /integration). Os demais
    # (site-manager, mobility) só usam server absoluto e nunca são reescritos.
    CONSOLE_APPS = {"network", "protect"}
    servers = spec.get("servers") or []
    first = (servers[0].get("url") if servers else "") or ""
    if first.startswith("http"):
        return spec  # já é absoluto (api.ui.com) — mantém
    if app not in CONSOLE_APPS:
        return spec  # cloud sem server absoluto: não há proxy a montar
    seg = first.strip("/") or "integration"  # relativo ('/integration') ou ausente
    spec["servers"] = [
        {
            "url": "https://{host}/proxy/" + app + "/" + seg,
            "description": "Local — console direto na LAN (header X-API-KEY)",
            "variables": {"host": {"default": "192.168.1.1", "description": "IP/host do console UniFi"}},
        },
        {
            "url": "https://api.ui.com/v1/connector/consoles/{consoleId}/" + app + "/" + seg,
            "description": "Remoto — Cloud Connector via Site Manager (header X-API-Key)",
            "variables": {"consoleId": {"default": "CONSOLE_ID", "description": "id do console (GET /v1/hosts)"}},
        },
    ]
    return spec


def scalar_page(app, version):
    title = f"UniFi {APP_LABEL.get(app, app)} API {version}"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><text y='14' font-size='14'>📡</text></svg>">
  {FONT}
  {THEME_INIT}
  <style>
    body {{ margin:0 }}
    .topbar {{ font:14px "UI Sans",Lato,sans-serif; display:flex; gap:14px; align-items:center; padding:9px 18px; border-bottom:1px solid var(--ln) }}
    html[data-theme=light] .topbar {{ background:#fff; color:#212327; --ln:#e9ebee; --lnk:hsl(214,90%,45%); --pb:#eef6ff; --pbd:#cfe3ff; --pc:hsl(214,90%,42%) }}
    html[data-theme=dark]  .topbar {{ background:#131416; color:#e6e8ea; --ln:#2a2d33; --lnk:hsl(214,100%,72%); --pb:#10254a; --pbd:#234a86; --pc:hsl(214,100%,78%) }}
    .topbar a {{ color:var(--lnk); text-decoration:none; font-weight:500 }}
    .topbar a:hover {{ text-decoration:underline }}
    .topbar .sp {{ flex:1 }}
    .vpill {{ border-radius:999px; padding:2px 11px; font-size:12px; font-weight:600; background:var(--pb); border:1px solid var(--pbd); color:var(--pc) }}
    .tt {{ cursor:pointer; background:none; border:1px solid var(--ln); border-radius:8px; padding:3px 9px; font-size:14px; color:inherit }}
    .light-mode {{ --scalar-color-accent:hsl(214,90%,45%); --scalar-background-accent:hsla(214,100%,64%,.12) }}
    .dark-mode  {{ --scalar-color-accent:hsl(214,100%,66%); --scalar-background-accent:hsla(214,100%,64%,.16) }}
    :root {{ --scalar-font:"UI Sans",Lato,sans-serif; --scalar-font-code:'SF Mono',Consolas,monospace }}
  </style>
</head>
<body>
  <div class="topbar">
    <a href="../../index.html">&larr; UniFi API Docs</a>
    <span class="vpill">{APP_LABEL.get(app, app)} {version}</span>
    <span class="sp"></span>
    <a href="./openapi.json">openapi.json</a>
    <a href="{ORIGIN}/{app}/{version}" target="_blank">doc &nearr;</a>
    <button class="tt" id="tt" title="Theme" onclick="(function(){{var n=document.documentElement.dataset.theme==='dark'?'light':'dark';localStorage.setItem('{THEME_KEY}',n);location.reload();}})()"></button>
  </div>
  <script id="api-reference" data-url="./openapi.json"></script>
  <script>
    var THEME=document.documentElement.dataset.theme;
    document.getElementById('tt').textContent = THEME==='dark'?'☀️':'🌙';
    document.getElementById("api-reference").dataset.configuration =
      JSON.stringify({{ theme:"default", forceDarkModeState:THEME, hideDownloadButton:false, metaData:{{title:"{title}"}} }});
  </script>
  <script src="https://cdn.jsdelivr.net/npm/@scalar/api-reference"></script>
</body>
</html>
"""


def landing(catalog):
    apps = catalog.get("apps", {})
    order = [a for a in APP_ORDER if a in apps] + sorted(a for a in apps if a not in APP_ORDER)
    n_apps = len(apps)
    n_versions = sum(len(d["versions"]) for d in apps.values())
    n_ops = sum(v["operations"] for d in apps.values() for v in d["versions"])
    src_date = (catalog.get("source_lastmod") or "")[:10]

    pills = '<button class="pill active" data-f="all" onclick="flt(this,\'all\')"><span data-i18n="all"></span></button>'
    pills += "".join(
        f'<button class="pill" data-f="{a}" onclick="flt(this,\'{a}\')">{APP_ICON.get(a,"")} {APP_LABEL.get(a,a)}</button>'
        for a in order
    )

    cards = []
    for a in order:
        d = apps[a]
        vs = d["versions"]
        latest = vs[0]
        acc = APP_ACCENT.get(a, "214,100%,60%")
        older = "".join(
            f'<div class="vrow"><span class="vnum">{v["version"]}</span>'
            f'<span class="vmeta">{v["operations"]} ops</span>'
            f'<a class="b xs" href="{a}/{v["version"]}/index.html">Docs</a>'
            f'<a class="b xs ghost" href="{a}/{v["version"]}/openapi.json">JSON</a></div>'
            for v in vs[1:]
        )
        toggle = (f'<button class="tg" onclick="tg(this)"><span data-i18n="older"></span> ({len(vs)-1}) ▾</button>'
                  f'<div class="vlist">{older}</div>') if len(vs) > 1 else ""
        cards.append(f"""
      <div class="card" data-app="{a}" style="--acc:hsl({acc}); --acc-soft:hsla({acc},.12)">
        <div class="chead">
          <div class="ic">{APP_ICON.get(a,'📦')}</div>
          <div><h2>{APP_LABEL.get(a,a)}</h2><span class="vc">{len(vs)} <span data-i18n="versions"></span> · {latest['categories']} <span data-i18n="cats"></span></span></div>
        </div>
        <p class="desc" data-desc="{a}"></p>
        <div class="latest">
          <span class="llabel" data-i18n="recent"></span>
          <div class="lrow"><span class="lver">{latest['version']}</span><span class="lops">{latest['operations']} ops · {latest['paths']} paths</span></div>
          <div class="lbtns">
            <a class="b primary" href="{a}/{latest['version']}/index.html" data-i18n="openDocs"></a>
            <a class="b ghost" href="{a}/{latest['version']}/openapi.json">JSON</a>
          </div>
        </div>
        {toggle}
      </div>""")

    return PAGE.format(
        font=FONT, theme_init=THEME_INIT, theme_key=THEME_KEY, lang_key=LANG_KEY,
        i18n=json.dumps(I18N, ensure_ascii=False),
        n_apps=n_apps, n_versions=n_versions, n_ops=n_ops, src_date=src_date,
        pills=pills, cards="".join(cards), origin=ORIGIN,
    )


PAGE = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>UniFi API Docs — interactive reference (all versions)</title>
<meta name="description" content="Interactive, versioned reference for the UniFi APIs: Network, Protect, Site Manager and Mobility. Local and Remote (Cloud Connector). OpenAPI + Scalar.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><text y='14' font-size='14'>📡</text></svg>">
{font}
{theme_init}
<style>
  html[data-theme=light] {{
    --bg:#ffffff; --soft:#f5f7f9; --card:#ffffff; --line:#e7e9ec; --txt:#212327; --body:#56595e; --mut:#80868f;
    --blue:hsl(214,100%,60%); --blue-ink:hsl(214,90%,43%); --blue-hover:hsl(214,90%,50%);
    --hero:radial-gradient(900px 380px at 50% -120px, #e9f2ff 0%, #fff 70%); --shadow:0 1px 2px rgba(16,24,40,.04); --shadow-h:0 14px 34px rgba(16,24,40,.10);
    --warnbg:#fff8e6; --warnbd:#ffe3a3; --warnfg:#8a6d18;
  }}
  html[data-theme=dark] {{
    --bg:#131416; --soft:#1b1d22; --card:#1a1c21; --line:#2a2d33; --txt:#eef0f2; --body:#aeb4bc; --mut:#7e858f;
    --blue:hsl(214,100%,64%); --blue-ink:hsl(214,100%,73%); --blue-hover:hsl(214,88%,58%);
    --hero:radial-gradient(900px 420px at 50% -140px, #14305c 0%, #131416 62%); --shadow:0 1px 2px rgba(0,0,0,.3); --shadow-h:0 16px 40px rgba(0,0,0,.5);
    --warnbg:rgba(250,204,21,.08); --warnbd:rgba(250,204,21,.22); --warnfg:#f4d77a;
  }}
  * {{ box-sizing:border-box; margin:0; padding:0 }}
  body {{ font-family:"UI Sans",Lato,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif; background:var(--bg); color:var(--body); min-height:100vh; -webkit-font-smoothing:antialiased; transition:background .2s,color .2s }}
  .nav {{ position:sticky; top:0; z-index:20; display:flex; align-items:center; gap:10px; padding:.7rem 1.2rem; background:color-mix(in srgb, var(--bg) 86%, transparent); backdrop-filter:blur(8px); border-bottom:1px solid var(--line) }}
  .nav .brand {{ font-weight:800; color:var(--txt); display:flex; gap:.45rem; align-items:center; font-size:1.02rem }}
  .nav .sp {{ flex:1 }}
  .nav a {{ color:var(--mut); text-decoration:none; font-size:.9rem; font-weight:600 }}
  .nav a:hover {{ color:var(--txt) }}
  .ctrl {{ cursor:pointer; background:var(--card); border:1px solid var(--line); border-radius:9px; padding:.35rem .6rem; font-size:.85rem; font-weight:700; line-height:1; color:var(--txt) }}
  .ctrl:hover {{ border-color:var(--blue) }}
  .hero {{ background:var(--hero); padding:3rem 1.2rem 1.4rem; text-align:center }}
  .wrap {{ max-width:1060px; margin:0 auto; padding:0 1.2rem }}
  .logo {{ font-size:2.2rem }}
  h1 {{ font-size:2.6rem; font-weight:800; letter-spacing:-.025em; color:var(--txt); margin:.3rem 0 }}
  .sub {{ color:var(--mut); font-size:1.06rem }}
  .stats {{ display:flex; gap:.5rem; justify-content:center; flex-wrap:wrap; margin-top:1rem }}
  .stat {{ background:var(--card); border:1px solid var(--line); border-radius:999px; padding:.4rem .9rem; font-size:.84rem; color:var(--mut) }}
  .stat b {{ color:var(--txt) }}
  .warn {{ max-width:1060px; margin:1.2rem auto 0; background:var(--warnbg); border:1px solid var(--warnbd); color:var(--warnfg); border-radius:10px; padding:.55rem .9rem; font-size:.84rem; text-align:center }}
  .warn a {{ color:var(--warnfg) }}
  .conn {{ background:var(--soft); border:1px solid var(--line); border-radius:18px; padding:1.1rem 1.2rem; margin:1.4rem auto 0 }}
  .conn h3 {{ font-size:1.05rem; color:var(--txt); margin-bottom:.7rem }}
  .modes {{ display:grid; grid-template-columns:1fr 1fr; gap:.8rem }}
  @media (max-width:760px) {{ .modes {{ grid-template-columns:1fr }} }}
  .mode {{ background:var(--card); border:1px solid var(--line); border-radius:12px; padding:.8rem .9rem }}
  .mode .t {{ font-weight:700; color:var(--txt); margin-bottom:.45rem }}
  .crow {{ display:flex; align-items:center; gap:.45rem }}
  code.url {{ font-family:'SF Mono',Consolas,monospace; font-size:.76rem; color:var(--blue-ink); background:var(--bg); border:1px solid var(--line); border-radius:7px; padding:.35rem .5rem; flex:1; min-width:0; white-space:nowrap; overflow-x:auto }}
  code.k {{ font-family:'SF Mono',Consolas,monospace; color:var(--blue-ink) }}
  .cap {{ display:block; margin-top:.4rem; color:var(--mut); font-size:.78rem }}
  .cp {{ flex:none; cursor:pointer; background:var(--card); border:1px solid var(--line); border-radius:7px; padding:.3rem .55rem; font-size:.72rem; color:var(--mut) }}
  .cp:hover {{ color:var(--txt); border-color:var(--blue) }}
  .pills {{ display:flex; flex-wrap:wrap; gap:.5rem; justify-content:center; margin:1.6rem auto 1.2rem }}
  .pill {{ font-family:inherit; cursor:pointer; background:var(--card); border:1px solid var(--line); color:var(--body); border-radius:999px; padding:.5rem 1.05rem; font-size:.9rem; font-weight:600; transition:all .15s }}
  .pill:hover {{ border-color:#9db4d4 }}
  .pill.active {{ color:var(--blue-ink); border-color:var(--blue); box-shadow:0 0 0 1px var(--blue) inset }}
  .grid {{ display:grid; grid-template-columns:1fr 1fr; gap:1.1rem }}
  @media (max-width:760px) {{ .grid {{ grid-template-columns:1fr }} }}
  .card {{ position:relative; background:var(--card); border:1px solid var(--line); border-radius:18px; padding:1.2rem; box-shadow:var(--shadow); transition:transform .15s, box-shadow .15s; overflow:hidden }}
  .card::before {{ content:""; position:absolute; left:0; top:0; height:3px; width:100%; background:var(--acc); opacity:.9 }}
  .card:hover {{ transform:translateY(-3px); box-shadow:var(--shadow-h) }}
  .chead {{ display:flex; gap:.8rem; align-items:center }}
  .ic {{ width:46px; height:46px; display:flex; align-items:center; justify-content:center; font-size:1.5rem; background:var(--acc-soft); border-radius:13px }}
  .chead h2 {{ font-size:1.25rem; color:var(--txt) }}
  .vc {{ color:var(--mut); font-size:.8rem }}
  .desc {{ color:var(--body); font-size:.88rem; margin:.7rem 0 .9rem; min-height:2.4em }}
  .latest {{ background:var(--soft); border:1px solid var(--line); border-radius:13px; padding:.85rem }}
  .llabel {{ font-size:.7rem; text-transform:uppercase; letter-spacing:.06em; color:var(--mut) }}
  .lrow {{ display:flex; align-items:baseline; gap:.6rem; margin-top:.2rem }}
  .lver {{ font-size:1.6rem; font-weight:800; color:var(--txt) }}
  .lops {{ color:var(--mut); font-size:.8rem }}
  .lbtns {{ display:flex; gap:.5rem; margin-top:.7rem }}
  .b {{ padding:.5rem .95rem; border-radius:9px; text-decoration:none; font-size:.86rem; font-weight:700; white-space:nowrap }}
  .b.primary {{ background:var(--blue); color:#fff }}
  .b.primary:hover {{ background:var(--blue-hover) }}
  .b.ghost {{ background:var(--card); border:1px solid var(--line); color:var(--body) }}
  .b.ghost:hover {{ border-color:var(--blue); color:var(--txt) }}
  .tg {{ width:100%; margin-top:.8rem; padding:.6rem; background:var(--card); border:1px solid var(--line); border-radius:9px; color:var(--mut); cursor:pointer; font-size:.84rem; font-family:inherit }}
  .tg:hover {{ color:var(--txt); border-color:var(--blue) }}
  .vlist {{ display:none; margin-top:.5rem }}
  .vlist.open {{ display:block }}
  .vrow {{ display:flex; gap:.5rem; align-items:center; padding:.45rem .6rem; border-radius:8px; background:var(--soft); margin-bottom:.4rem }}
  .vnum {{ font-family:'SF Mono',Consolas,monospace; font-size:.82rem; color:var(--txt) }}
  .vmeta {{ flex:1; color:var(--mut); font-size:.72rem }}
  .b.xs {{ padding:.28rem .6rem; font-size:.74rem; font-weight:600 }}
  .llm {{ background:var(--soft); border:1px dashed #9db4d4; border-radius:16px; padding:1.1rem 1.2rem; margin:1.6rem auto 0 }}
  .llm h3 {{ font-size:1.05rem; color:var(--txt); margin-bottom:.4rem }}
  .llm a, .llm code {{ color:var(--blue-ink) }}
  .mcp {{ display:flex; align-items:center; gap:1rem; flex-wrap:wrap; justify-content:space-between;
          background:linear-gradient(135deg, var(--blue-soft), var(--soft)); border:1px solid var(--blue);
          border-radius:18px; padding:1.1rem 1.3rem; margin:1.6rem auto 0 }}
  .mcp h3 {{ font-size:1.1rem; color:var(--txt); margin-bottom:.3rem }}
  .mcp .mcpd {{ color:var(--body); font-size:.9rem; max-width:64ch }}
  .mcp .mcpd b {{ color:var(--txt) }}
  .mcpbtn {{ flex:none; background:var(--blue); color:#fff; text-decoration:none; font-weight:700;
             font-size:.9rem; padding:.6rem 1.1rem; border-radius:10px; white-space:nowrap }}
  .mcpbtn:hover {{ background:var(--blue-hover) }}
  footer {{ text-align:center; color:var(--mut); font-size:.84rem; margin:2rem auto 2.4rem; line-height:1.8 }}
  footer a {{ color:var(--blue-ink); text-decoration:none }}
</style>
</head>
<body>
  <nav class="nav">
    <span class="brand">📡 UniFi API Docs</span>
    <span class="sp"></span>
    <a href="https://github.com/opastorello/unifi-api-docs" target="_blank">GitHub</a>
    <button class="ctrl" id="lt" title="PT / EN" onclick="toggleLang()"></button>
    <button class="ctrl" id="tt" title="Light / Dark" onclick="toggleTheme()"></button>
  </nav>

  <div class="hero">
    <div class="logo">📡</div>
    <h1>UniFi API Docs</h1>
    <p class="sub" data-i18n="sub"></p>
    <div class="stats">
      <span class="stat"><b>{n_apps}</b> <span data-i18n="apps"></span></span>
      <span class="stat"><b>{n_versions}</b> <span data-i18n="versions"></span></span>
      <span class="stat"><b>{n_ops}</b> <span data-i18n="operations"></span></span>
      <span class="stat"><span data-i18n="source"></span> <b data-date="{src_date}"></b></span>
    </div>
  </div>

  <div class="wrap">
    <div class="warn"><span data-i18n="warnPre"></span> <a href="{origin}">developer.ui.com</a></div>

    <div class="conn">
      <h3 data-i18n="connTitle"></h3>
      <div class="modes">
        <div class="mode"><div class="t" data-i18n="localTitle"></div>
          <div class="crow"><code class="url" id="c1">https://&lt;console&gt;/proxy/&lt;app&gt;/integration/v1/</code><button class="cp" data-i18n="copy" onclick="cp('c1',this)"></button></div>
          <small class="cap" data-i18n="localCap"></small></div>
        <div class="mode"><div class="t" data-i18n="remoteTitle"></div>
          <div class="crow"><code class="url" id="c2">https://api.ui.com/v1/connector/consoles/{{id}}/&lt;app&gt;/integration/v1/</code><button class="cp" data-i18n="copy" onclick="cp('c2',this)"></button></div>
          <small class="cap" data-i18n="remoteCap"></small></div>
      </div>
    </div>

    <div class="mcp">
      <div>
        <h3 data-i18n="mcpTitle"></h3>
        <p class="mcpd" data-i18n-html="mcpDesc"></p>
      </div>
      <a class="mcpbtn" href="https://github.com/opastorello/unifi-mcp" target="_blank" data-i18n="mcpBtn"></a>
    </div>

    <nav class="pills">{pills}</nav>

    <div class="grid" id="grid">{cards}
    </div>

    <div class="llm">
      <h3 data-i18n="llmTitle"></h3>
      <p style="color:var(--body); font-size:.9rem"><span data-i18n="llmPre"></span> <a href="llms.txt">llms.txt</a> · <a href="catalog.json">catalog.json</a> · <a href="skill.md">skill.md</a>. <span data-i18n="llmPost"></span></p>
    </div>

    <footer>
      <p data-i18n-html="footer1"></p>
      <p><a href="https://github.com/opastorello/unifi-api-docs" data-i18n="footer2"></a></p>
    </footer>
  </div>
<script>
  var I18N={i18n}, TK='{theme_key}', LK='{lang_key}';
  function paintToggles(){{
    var d=document.documentElement;
    document.getElementById('tt').textContent = d.dataset.theme==='dark'?'☀️':'🌙';
    document.getElementById('lt').textContent = d.dataset.lang.toUpperCase();
  }}
  function applyLang(l){{
    var t=I18N[l]||I18N.en, d=document.documentElement;
    d.dataset.lang=l; d.lang=(l==='pt'?'pt-BR':'en'); localStorage.setItem(LK,l);
    document.querySelectorAll('[data-i18n]').forEach(function(e){{ var k=e.dataset.i18n; if(t[k]!=null) e.textContent=t[k]; }});
    document.querySelectorAll('[data-i18n-html]').forEach(function(e){{ var k=e.dataset.i18nHtml; if(t[k]!=null) e.innerHTML=t[k]; }});
    document.querySelectorAll('[data-desc]').forEach(function(e){{ e.textContent=t.desc[e.dataset.desc]||''; }});
    document.querySelectorAll('[data-date]').forEach(function(e){{
      var iso=e.dataset.date; try{{ e.textContent=new Date(iso+'T00:00:00').toLocaleDateString(l==='pt'?'pt-BR':'en-US',{{day:'2-digit',month:'short',year:'numeric'}}); }}catch(_){{ e.textContent=iso; }}
    }});
    paintToggles();
  }}
  function toggleLang(){{ applyLang(document.documentElement.dataset.lang==='pt'?'en':'pt'); }}
  function toggleTheme(){{ var n=document.documentElement.dataset.theme==='dark'?'light':'dark'; document.documentElement.dataset.theme=n; localStorage.setItem(TK,n); paintToggles(); }}
  function tg(b){{ b.nextElementSibling.classList.toggle('open'); }}
  function flt(btn,f){{
    document.querySelectorAll('.pills .pill').forEach(function(p){{ p.classList.toggle('active',p===btn); }});
    document.querySelectorAll('#grid .card').forEach(function(c){{ c.style.display=(f==='all'||c.dataset.app===f)?'':'none'; }});
  }}
  function cp(id,btn){{ var t=I18N[document.documentElement.dataset.lang]; navigator.clipboard.writeText(document.getElementById(id).textContent).then(function(){{ btn.textContent=t.copied; setTimeout(function(){{btn.textContent=t.copy;}},1200); }}); }}
  applyLang(document.documentElement.dataset.lang);
</script>
</body>
</html>
"""


def main():
    catalog = json.load(open(os.path.join(BASE, "catalog.json"), encoding="utf-8"))
    if os.path.isdir(SITE):
        shutil.rmtree(SITE)
    os.makedirs(SITE)

    n = 0
    for app, d in catalog["apps"].items():
        for v in d["versions"]:
            ver = v["version"]
            dest = os.path.join(SITE, app, ver)
            os.makedirs(dest, exist_ok=True)
            spec = json.load(open(os.path.join(BASE, v["openapi"]), encoding="utf-8"))
            sanitize_spec(app, ver, spec)
            fix_servers(app, spec)
            with open(os.path.join(dest, "openapi.json"), "w", encoding="utf-8") as sf:
                json.dump(spec, sf, ensure_ascii=False)
            with open(os.path.join(dest, "index.html"), "w", encoding="utf-8") as f:
                f.write(scalar_page(app, ver))
            n += 1

    with open(os.path.join(SITE, "index.html"), "w", encoding="utf-8") as f:
        f.write(landing(catalog))
    for extra in ("llms.txt", "catalog.json", "skill.md"):
        src = os.path.join(BASE, extra)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(SITE, extra))
    open(os.path.join(SITE, ".nojekyll"), "w").close()

    print(f"_site gerado: {n} páginas de versão + landing + índices")


if __name__ == "__main__":
    main()

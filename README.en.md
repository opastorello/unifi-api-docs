# 📡 UniFi API Docs

**🌐 Languages:** English · [Português](./README.md)
**🔗 Site (interactive reference):** <https://opastorello.github.io/unifi-api-docs/>

An **automatic, versioned** mirror of the official UniFi API documentation
([developer.ui.com](https://developer.ui.com)), ready for humans and AIs/LLMs (Markdown + OpenAPI).

<!-- badges:start -->
![files](https://img.shields.io/badge/files-101-blue) ![versions](https://img.shields.io/badge/versions-39_in_6_apps-orange) ![operations](https://img.shields.io/badge/operations-1525-blueviolet) ![updated](https://img.shields.io/badge/updated-2026--08--06-brightgreen)
<!-- badges:end -->

> ⚠️ **Unofficial** mirror, kept for reference and automation. The authoritative source is always [developer.ui.com](https://developer.ui.com).

---

## What it is

For each **application** (Site Manager, Network, Protect, Mobility) and each published **version**, this repo stores:

- **`<app>/<version>/openapi.json`** - the full **OpenAPI** spec (all paths, schemas, examples). Source of truth.
- **`<app>/<version>/reference.md`** - a Markdown reference generated from the OpenAPI (index, parameters, body, response and **Local**/**Remote** cURL examples).

Quick-access indexes:

- **[`llms.txt`](./llms.txt)** - index following the [llmstxt.org](https://llmstxt.org) convention, made for LLMs.
- **[`catalog.json`](./catalog.json)** - JSON catalog (apps → versions → counts).
- **[`skill.md`](./skill.md)** - ready-to-use skill for agents querying the API.

> ℹ️ The `openapi.json` files are a **faithful** mirror of the source. Some of Ubiquiti's 3.1.0 specs have minor OpenAPI-schema deviations (e.g. empty `info.license` on Network; a missing `description` on Protect), kept as published. They are valid, usable JSON - only strict validators complain.

---

## Connection modes (Local × Remote)

The per-app APIs (Network / Protect / Mobility) run **locally on each console** and can be reached two ways:

| | 🏠 Local | ☁️ Remote (Cloud Connector) |
|---|---|---|
| **Header** | `X-API-KEY` | `X-API-Key` |
| **Key** | console → *Integrations* | unifi.ui.com → *Settings → API Keys* |
| **Local network?** | required | not needed (works behind CGNAT) |
| **Requirement** | - | console firmware ≥ 5.0.3 |

**🏠 Local** - straight to the console:

```bash
curl -H "X-API-KEY: $LOCAL_KEY" \
  "https://<console>/proxy/<app>/integration/v1/…"
```

**☁️ Remote** - via cloud, no local network access:

```bash
curl -H "X-API-Key: $SITE_MANAGER_KEY" \
  "https://api.ui.com/v1/connector/consoles/{id}/<app>/integration/v1/…"
```

The path after `/integration` is **identical** in both modes. **Site Manager** is the multi-site cloud API (`https://api.ui.com/v1/…`) and includes the **Cloud Connector** used by Remote mode.

---

## 📚 Catalog

<!-- catalog:start -->
| App | Latest | Categories | Operations | Paths | OpenAPI | Reference | Official docs |
|---|---|---:|---:|---:|---|---|---|
| **network** | `v10.4.57` | 13 | 73 | 44 | [json](network/v10.4.57/openapi.json) | [md](network/v10.4.57/reference.md) | [docs](https://developer.ui.com/network/v10.4.57) |
| **protect** | `v7.1.87` | 22 | 73 | 54 | [json](protect/v7.1.87/openapi.json) | [md](protect/v7.1.87/reference.md) | [docs](https://developer.ui.com/protect/v7.1.87) |
| **site-manager** | `v1.0.0` | 1 | 9 | 9 | [json](site-manager/v1.0.0/openapi.json) | [md](site-manager/v1.0.0/reference.md) | [docs](https://developer.ui.com/site-manager/v1.0.0) |
| **mobility** | `v1.0.0` | 4 | 8 | 7 | [json](mobility/v1.0.0/openapi.json) | [md](mobility/v1.0.0/reference.md) | [docs](https://developer.ui.com/mobility/v1.0.0) |
| **carrier-fabric** | `v1.0.0` | 3 | 11 | 8 | [json](carrier-fabric/v1.0.0/openapi.json) | [md](carrier-fabric/v1.0.0/reference.md) | [docs](https://developer.ui.com/carrier-fabric/v1.0.0) |
| **innerspace** | `v1.3.23` | 1 | 5 | 1 | [json](innerspace/v1.3.23/openapi.json) | [md](innerspace/v1.3.23/reference.md) | [docs](https://developer.ui.com/innerspace/v1.3.23) |

<details>
<summary><b>📜 Full version history - 39 versions</b></summary>

**network**

| Version | Categories | Operations | Paths | Updated | OpenAPI | Reference | Official docs |
|---|---:|---:|---:|---|---|---|---|
| `v10.4.57` ⭐ | 13 | 73 | 44 | 2026-08-06 | [json](network/v10.4.57/openapi.json) | [md](network/v10.4.57/reference.md) | [docs](https://developer.ui.com/network/v10.4.57) |
| `v10.3.58` | 13 | 73 | 44 | 2026-08-06 | [json](network/v10.3.58/openapi.json) | [md](network/v10.3.58/reference.md) | [docs](https://developer.ui.com/network/v10.3.58) |
| `v10.1.84` | 12 | 67 | 38 | 2026-08-06 | [json](network/v10.1.84/openapi.json) | [md](network/v10.1.84/reference.md) | [docs](https://developer.ui.com/network/v10.1.84) |
| `v10.0.162` | 11 | 50 | 32 | 2026-08-06 | [json](network/v10.0.162/openapi.json) | [md](network/v10.0.162/reference.md) | [docs](https://developer.ui.com/network/v10.0.162) |
| `v9.5.21` | 5 | 15 | 12 | 2026-08-06 | [json](network/v9.5.21/openapi.json) | [md](network/v9.5.21/reference.md) | [docs](https://developer.ui.com/network/v9.5.21) |
| `v9.4.19` | 5 | 15 | 12 | 2026-08-06 | [json](network/v9.4.19/openapi.json) | [md](network/v9.4.19/reference.md) | [docs](https://developer.ui.com/network/v9.4.19) |
| `v9.4.17` | 5 | 15 | 12 | 2026-08-06 | [json](network/v9.4.17/openapi.json) | [md](network/v9.4.17/reference.md) | [docs](https://developer.ui.com/network/v9.4.17) |
| `v9.3.45` | 5 | 15 | 12 | 2026-08-06 | [json](network/v9.3.45/openapi.json) | [md](network/v9.3.45/reference.md) | [docs](https://developer.ui.com/network/v9.3.45) |
| `v9.3.43` | 5 | 15 | 12 | 2026-08-06 | [json](network/v9.3.43/openapi.json) | [md](network/v9.3.43/reference.md) | [docs](https://developer.ui.com/network/v9.3.43) |
| `v9.2.87` | 5 | 15 | 12 | 2026-08-06 | [json](network/v9.2.87/openapi.json) | [md](network/v9.2.87/reference.md) | [docs](https://developer.ui.com/network/v9.2.87) |
| `v9.2.86` | 5 | 15 | 12 | 2026-08-06 | [json](network/v9.2.86/openapi.json) | [md](network/v9.2.86/reference.md) | [docs](https://developer.ui.com/network/v9.2.86) |
| `v9.1.120` | 5 | 15 | 12 | 2026-08-06 | [json](network/v9.1.120/openapi.json) | [md](network/v9.1.120/reference.md) | [docs](https://developer.ui.com/network/v9.1.120) |

**protect**

| Version | Categories | Operations | Paths | Updated | OpenAPI | Reference | Official docs |
|---|---:|---:|---:|---|---|---|---|
| `v7.1.87` ⭐ | 22 | 73 | 54 | 2026-08-06 | [json](protect/v7.1.87/openapi.json) | [md](protect/v7.1.87/reference.md) | [docs](https://developer.ui.com/protect/v7.1.87) |
| `v7.1.83` | 22 | 73 | 54 | 2026-08-06 | [json](protect/v7.1.83/openapi.json) | [md](protect/v7.1.83/reference.md) | [docs](https://developer.ui.com/protect/v7.1.83) |
| `v7.1.77` | 22 | 73 | 54 | 2026-08-06 | [json](protect/v7.1.77/openapi.json) | [md](protect/v7.1.77/reference.md) | [docs](https://developer.ui.com/protect/v7.1.77) |
| `v7.1.76` | 22 | 73 | 54 | 2026-08-06 | [json](protect/v7.1.76/openapi.json) | [md](protect/v7.1.76/reference.md) | [docs](https://developer.ui.com/protect/v7.1.76) |
| `v7.1.75` | 22 | 73 | 54 | 2026-08-06 | [json](protect/v7.1.75/openapi.json) | [md](protect/v7.1.75/reference.md) | [docs](https://developer.ui.com/protect/v7.1.75) |
| `v7.1.74` | 22 | 73 | 54 | 2026-08-06 | [json](protect/v7.1.74/openapi.json) | [md](protect/v7.1.74/reference.md) | [docs](https://developer.ui.com/protect/v7.1.74) |
| `v7.1.73` | 22 | 73 | 54 | 2026-08-06 | [json](protect/v7.1.73/openapi.json) | [md](protect/v7.1.73/reference.md) | [docs](https://developer.ui.com/protect/v7.1.73) |
| `v7.1.69` | 22 | 73 | 54 | 2026-08-06 | [json](protect/v7.1.69/openapi.json) | [md](protect/v7.1.69/reference.md) | [docs](https://developer.ui.com/protect/v7.1.69) |
| `v7.0.107` | 12 | 35 | 25 | 2026-08-06 | [json](protect/v7.0.107/openapi.json) | [md](protect/v7.0.107/reference.md) | [docs](https://developer.ui.com/protect/v7.0.107) |
| `v7.0.104` | 12 | 35 | 25 | 2026-08-06 | [json](protect/v7.0.104/openapi.json) | [md](protect/v7.0.104/reference.md) | [docs](https://developer.ui.com/protect/v7.0.104) |
| `v7.0.94` | 12 | 35 | 25 | 2026-08-06 | [json](protect/v7.0.94/openapi.json) | [md](protect/v7.0.94/reference.md) | [docs](https://developer.ui.com/protect/v7.0.94) |
| `v6.2.88` | 12 | 35 | 25 | 2026-08-06 | [json](protect/v6.2.88/openapi.json) | [md](protect/v6.2.88/reference.md) | [docs](https://developer.ui.com/protect/v6.2.88) |
| `v6.2.87` | 12 | 35 | 25 | 2026-08-06 | [json](protect/v6.2.87/openapi.json) | [md](protect/v6.2.87/reference.md) | [docs](https://developer.ui.com/protect/v6.2.87) |
| `v6.2.83` | 12 | 35 | 25 | 2026-08-06 | [json](protect/v6.2.83/openapi.json) | [md](protect/v6.2.83/reference.md) | [docs](https://developer.ui.com/protect/v6.2.83) |
| `v6.2.72` | 12 | 35 | 25 | 2026-08-06 | [json](protect/v6.2.72/openapi.json) | [md](protect/v6.2.72/reference.md) | [docs](https://developer.ui.com/protect/v6.2.72) |
| `v6.1.79` | 12 | 35 | 25 | 2026-08-06 | [json](protect/v6.1.79/openapi.json) | [md](protect/v6.1.79/reference.md) | [docs](https://developer.ui.com/protect/v6.1.79) |
| `v6.1.78` | 12 | 35 | 25 | 2026-08-06 | [json](protect/v6.1.78/openapi.json) | [md](protect/v6.1.78/reference.md) | [docs](https://developer.ui.com/protect/v6.1.78) |
| `v6.1.75` | 12 | 35 | 25 | 2026-08-06 | [json](protect/v6.1.75/openapi.json) | [md](protect/v6.1.75/reference.md) | [docs](https://developer.ui.com/protect/v6.1.75) |
| `v6.1.68` | 12 | 35 | 25 | 2026-08-06 | [json](protect/v6.1.68/openapi.json) | [md](protect/v6.1.68/reference.md) | [docs](https://developer.ui.com/protect/v6.1.68) |
| `v6.1.65` | 12 | 35 | 25 | 2026-08-06 | [json](protect/v6.1.65/openapi.json) | [md](protect/v6.1.65/reference.md) | [docs](https://developer.ui.com/protect/v6.1.65) |
| `v6.0.53` | 12 | 35 | 25 | 2026-08-06 | [json](protect/v6.0.53/openapi.json) | [md](protect/v6.0.53/reference.md) | [docs](https://developer.ui.com/protect/v6.0.53) |
| `v6.0.47` | 12 | 35 | 25 | 2026-08-06 | [json](protect/v6.0.47/openapi.json) | [md](protect/v6.0.47/reference.md) | [docs](https://developer.ui.com/protect/v6.0.47) |
| `v5.3.48` | 12 | 35 | 25 | 2026-08-06 | [json](protect/v5.3.48/openapi.json) | [md](protect/v5.3.48/reference.md) | [docs](https://developer.ui.com/protect/v5.3.48) |

</details>
<!-- catalog:end -->

---

## Updating

```bash
python update_docs.py                 # every version of every app
python update_docs.py --latest-only   # only the latest version of each app
python update_docs.py --app network   # a specific app
python update_docs.py --dry-run       # show what would change, without writing
python update_readme.py               # refresh badges + catalog in the READMEs
python validate.py                    # validate integrity (JSON, catalog, links)
```

No browser or credentials required: `update_docs.py` reads the official `sitemap.xml`, discovers the `app/version` pairs, downloads each page's RSC payload (`RSC: 1` header) and extracts the embedded full OpenAPI. Pure Python standard library.

## 🤖 Automatic updates (CI)

The [`.github/workflows/update-docs.yml`](./.github/workflows/update-docs.yml) workflow runs daily (and on demand), regenerates everything and commits **only when the upstream docs change** - so new versions show up on their own as soon as Ubiquiti publishes them.

# 📡 UniFi API Docs

**🌐 Idiomas:** Português · [English](./README.en.md)
**🔗 Site (referência interativa):** <https://opastorello.github.io/unifi-api-docs/>

Espelho **automático e versionado** da documentação oficial da API UniFi
([developer.ui.com](https://developer.ui.com)), pronto para humanos e IAs/LLMs (Markdown + OpenAPI).

<!-- badges:start -->
![arquivos](https://img.shields.io/badge/arquivos-95-blue) ![versoes](https://img.shields.io/badge/versoes-36_em_4_apps-orange) ![operacoes](https://img.shields.io/badge/operacoes-1436-blueviolet) ![atualizado](https://img.shields.io/badge/atualizado-2026--07--08-brightgreen)
<!-- badges:end -->

> ⚠️ Espelho **não oficial**, mantido para consulta e automação. A fonte autoritativa é sempre [developer.ui.com](https://developer.ui.com).

> 🔌 **Servidor MCP:** estas specs alimentam o [**opastorello/unifi-mcp**](https://github.com/opastorello/unifi-mcp) — um servidor MCP completo da UniFi (Local + Remoto via Cloud Connector) com passthrough auto-atualizável sobre a Integration v1.

---

## O que é

Para cada **aplicação** (Site Manager, Network, Protect, Mobility) e cada **versão** publicada, este repositório guarda:

- **`<app>/<versão>/openapi.json`** - a especificação **OpenAPI completa** (todos os paths, schemas, exemplos). É a fonte da verdade.
- **`<app>/<versão>/reference.md`** - referência em Markdown gerada do OpenAPI (índice, parâmetros, corpo, resposta e exemplos cURL **Local** e **Remoto**).

Índices para consumo rápido:

- **[`llms.txt`](./llms.txt)** - índice no padrão [llmstxt.org](https://llmstxt.org), pensado para LLMs.
- **[`catalog.json`](./catalog.json)** - catálogo em JSON (apps → versões → contagens).
- **[`skill.md`](./skill.md)** - skill pronta para agentes consultarem a API.

> ℹ️ Os `openapi.json` são espelho **fiel** da origem. Algumas versões 3.1.0 da Ubiquiti têm pequenos desvios do schema OpenAPI (ex.: `info.license` vazio na Network; um `description` ausente na Protect), preservados como na origem. São JSON válidos e usáveis - apenas validadores estritos acusam.

---

## Modos de conexão (Local × Remoto)

As APIs por aplicação (Network / Protect / Mobility) rodam **localmente em cada console** e podem ser acessadas de dois jeitos:

| | 🏠 Local | ☁️ Remoto (Cloud Connector) |
|---|---|---|
| **Header** | `X-API-KEY` | `X-API-Key` |
| **Chave** | console → *Integrations* | unifi.ui.com → *Settings → API Keys* |
| **Rede local?** | necessária | dispensada (ok atrás de CGNAT) |
| **Requisito** | - | firmware ≥ 5.0.3 |

**🏠 Local** - direto no console:

```bash
curl -H "X-API-KEY: $CHAVE_LOCAL" \
  "https://<console>/proxy/<app>/integration/v1/…"
```

**☁️ Remoto** - via nuvem, sem acesso à rede local:

```bash
curl -H "X-API-Key: $CHAVE_SITE_MANAGER" \
  "https://api.ui.com/v1/connector/consoles/{id}/<app>/integration/v1/…"
```

O caminho após `/integration` é **idêntico** nos dois modos. O **Site Manager** é a API de nuvem multi-site (`https://api.ui.com/v1/…`) e inclui o **Cloud Connector** usado pelo modo Remoto.

---

## 📚 Catálogo

<!-- catalog:start -->
| App | Última versão | Categorias | Operações | Paths | OpenAPI | Referência | Doc oficial |
|---|---|---:|---:|---:|---|---|---|
| **network** | `v10.3.58` | 13 | 73 | 44 | [json](network/v10.3.58/openapi.json) | [md](network/v10.3.58/reference.md) | [origem](https://developer.ui.com/network/v10.3.58) |
| **protect** | `v7.1.87` | 22 | 73 | 54 | [json](protect/v7.1.87/openapi.json) | [md](protect/v7.1.87/reference.md) | [origem](https://developer.ui.com/protect/v7.1.87) |
| **site-manager** | `v1.0.0` | 1 | 9 | 9 | [json](site-manager/v1.0.0/openapi.json) | [md](site-manager/v1.0.0/reference.md) | [origem](https://developer.ui.com/site-manager/v1.0.0) |
| **mobility** | `v1.0.0` | 4 | 8 | 7 | [json](mobility/v1.0.0/openapi.json) | [md](mobility/v1.0.0/reference.md) | [origem](https://developer.ui.com/mobility/v1.0.0) |

<details>
<summary><b>📜 Histórico completo - 36 versões</b></summary>

**network**

| Versão | Categorias | Operações | Paths | Modificado | OpenAPI | Referência | Doc oficial |
|---|---:|---:|---:|---|---|---|---|
| `v10.3.58` ⭐ | 13 | 73 | 44 | 2026-07-08 | [json](network/v10.3.58/openapi.json) | [md](network/v10.3.58/reference.md) | [origem](https://developer.ui.com/network/v10.3.58) |
| `v10.1.84` | 12 | 67 | 38 | 2026-07-08 | [json](network/v10.1.84/openapi.json) | [md](network/v10.1.84/reference.md) | [origem](https://developer.ui.com/network/v10.1.84) |
| `v10.0.162` | 11 | 50 | 32 | 2026-07-08 | [json](network/v10.0.162/openapi.json) | [md](network/v10.0.162/reference.md) | [origem](https://developer.ui.com/network/v10.0.162) |
| `v9.5.21` | 5 | 15 | 12 | 2026-07-08 | [json](network/v9.5.21/openapi.json) | [md](network/v9.5.21/reference.md) | [origem](https://developer.ui.com/network/v9.5.21) |
| `v9.4.19` | 5 | 15 | 12 | 2026-07-08 | [json](network/v9.4.19/openapi.json) | [md](network/v9.4.19/reference.md) | [origem](https://developer.ui.com/network/v9.4.19) |
| `v9.4.17` | 5 | 15 | 12 | 2026-07-08 | [json](network/v9.4.17/openapi.json) | [md](network/v9.4.17/reference.md) | [origem](https://developer.ui.com/network/v9.4.17) |
| `v9.3.45` | 5 | 15 | 12 | 2026-07-08 | [json](network/v9.3.45/openapi.json) | [md](network/v9.3.45/reference.md) | [origem](https://developer.ui.com/network/v9.3.45) |
| `v9.3.43` | 5 | 15 | 12 | 2026-07-08 | [json](network/v9.3.43/openapi.json) | [md](network/v9.3.43/reference.md) | [origem](https://developer.ui.com/network/v9.3.43) |
| `v9.2.87` | 5 | 15 | 12 | 2026-07-08 | [json](network/v9.2.87/openapi.json) | [md](network/v9.2.87/reference.md) | [origem](https://developer.ui.com/network/v9.2.87) |
| `v9.2.86` | 5 | 15 | 12 | 2026-07-08 | [json](network/v9.2.86/openapi.json) | [md](network/v9.2.86/reference.md) | [origem](https://developer.ui.com/network/v9.2.86) |
| `v9.1.120` | 5 | 15 | 12 | 2026-07-08 | [json](network/v9.1.120/openapi.json) | [md](network/v9.1.120/reference.md) | [origem](https://developer.ui.com/network/v9.1.120) |

**protect**

| Versão | Categorias | Operações | Paths | Modificado | OpenAPI | Referência | Doc oficial |
|---|---:|---:|---:|---|---|---|---|
| `v7.1.87` ⭐ | 22 | 73 | 54 | 2026-07-08 | [json](protect/v7.1.87/openapi.json) | [md](protect/v7.1.87/reference.md) | [origem](https://developer.ui.com/protect/v7.1.87) |
| `v7.1.83` | 22 | 73 | 54 | 2026-07-08 | [json](protect/v7.1.83/openapi.json) | [md](protect/v7.1.83/reference.md) | [origem](https://developer.ui.com/protect/v7.1.83) |
| `v7.1.77` | 22 | 73 | 54 | 2026-07-08 | [json](protect/v7.1.77/openapi.json) | [md](protect/v7.1.77/reference.md) | [origem](https://developer.ui.com/protect/v7.1.77) |
| `v7.1.76` | 22 | 73 | 54 | 2026-07-08 | [json](protect/v7.1.76/openapi.json) | [md](protect/v7.1.76/reference.md) | [origem](https://developer.ui.com/protect/v7.1.76) |
| `v7.1.75` | 22 | 73 | 54 | 2026-07-08 | [json](protect/v7.1.75/openapi.json) | [md](protect/v7.1.75/reference.md) | [origem](https://developer.ui.com/protect/v7.1.75) |
| `v7.1.74` | 22 | 73 | 54 | 2026-07-08 | [json](protect/v7.1.74/openapi.json) | [md](protect/v7.1.74/reference.md) | [origem](https://developer.ui.com/protect/v7.1.74) |
| `v7.1.73` | 22 | 73 | 54 | 2026-07-08 | [json](protect/v7.1.73/openapi.json) | [md](protect/v7.1.73/reference.md) | [origem](https://developer.ui.com/protect/v7.1.73) |
| `v7.1.69` | 22 | 73 | 54 | 2026-07-08 | [json](protect/v7.1.69/openapi.json) | [md](protect/v7.1.69/reference.md) | [origem](https://developer.ui.com/protect/v7.1.69) |
| `v7.0.107` | 12 | 35 | 25 | 2026-07-08 | [json](protect/v7.0.107/openapi.json) | [md](protect/v7.0.107/reference.md) | [origem](https://developer.ui.com/protect/v7.0.107) |
| `v7.0.104` | 12 | 35 | 25 | 2026-07-08 | [json](protect/v7.0.104/openapi.json) | [md](protect/v7.0.104/reference.md) | [origem](https://developer.ui.com/protect/v7.0.104) |
| `v7.0.94` | 12 | 35 | 25 | 2026-07-08 | [json](protect/v7.0.94/openapi.json) | [md](protect/v7.0.94/reference.md) | [origem](https://developer.ui.com/protect/v7.0.94) |
| `v6.2.88` | 12 | 35 | 25 | 2026-07-08 | [json](protect/v6.2.88/openapi.json) | [md](protect/v6.2.88/reference.md) | [origem](https://developer.ui.com/protect/v6.2.88) |
| `v6.2.87` | 12 | 35 | 25 | 2026-07-08 | [json](protect/v6.2.87/openapi.json) | [md](protect/v6.2.87/reference.md) | [origem](https://developer.ui.com/protect/v6.2.87) |
| `v6.2.83` | 12 | 35 | 25 | 2026-07-08 | [json](protect/v6.2.83/openapi.json) | [md](protect/v6.2.83/reference.md) | [origem](https://developer.ui.com/protect/v6.2.83) |
| `v6.2.72` | 12 | 35 | 25 | 2026-07-08 | [json](protect/v6.2.72/openapi.json) | [md](protect/v6.2.72/reference.md) | [origem](https://developer.ui.com/protect/v6.2.72) |
| `v6.1.79` | 12 | 35 | 25 | 2026-07-08 | [json](protect/v6.1.79/openapi.json) | [md](protect/v6.1.79/reference.md) | [origem](https://developer.ui.com/protect/v6.1.79) |
| `v6.1.78` | 12 | 35 | 25 | 2026-07-08 | [json](protect/v6.1.78/openapi.json) | [md](protect/v6.1.78/reference.md) | [origem](https://developer.ui.com/protect/v6.1.78) |
| `v6.1.75` | 12 | 35 | 25 | 2026-07-08 | [json](protect/v6.1.75/openapi.json) | [md](protect/v6.1.75/reference.md) | [origem](https://developer.ui.com/protect/v6.1.75) |
| `v6.1.68` | 12 | 35 | 25 | 2026-07-08 | [json](protect/v6.1.68/openapi.json) | [md](protect/v6.1.68/reference.md) | [origem](https://developer.ui.com/protect/v6.1.68) |
| `v6.1.65` | 12 | 35 | 25 | 2026-07-08 | [json](protect/v6.1.65/openapi.json) | [md](protect/v6.1.65/reference.md) | [origem](https://developer.ui.com/protect/v6.1.65) |
| `v6.0.53` | 12 | 35 | 25 | 2026-07-08 | [json](protect/v6.0.53/openapi.json) | [md](protect/v6.0.53/reference.md) | [origem](https://developer.ui.com/protect/v6.0.53) |
| `v6.0.47` | 12 | 35 | 25 | 2026-07-08 | [json](protect/v6.0.47/openapi.json) | [md](protect/v6.0.47/reference.md) | [origem](https://developer.ui.com/protect/v6.0.47) |
| `v5.3.48` | 12 | 35 | 25 | 2026-07-08 | [json](protect/v5.3.48/openapi.json) | [md](protect/v5.3.48/reference.md) | [origem](https://developer.ui.com/protect/v5.3.48) |

</details>
<!-- catalog:end -->

---

## Como atualizar

```bash
python update_docs.py                 # todas as versões de todos os apps
python update_docs.py --latest-only   # só a versão mais recente de cada app
python update_docs.py --app network   # um app específico
python update_docs.py --dry-run       # mostra o que mudaria, sem escrever
python update_readme.py               # atualiza badges + catálogo dos READMEs
python validate.py                    # valida integridade (JSON, catálogo, links)
```

Não precisa de navegador nem de credenciais: o `update_docs.py` lê o `sitemap.xml` oficial, descobre os pares `app/versão`, baixa o payload RSC de cada página (header `RSC: 1`) e extrai o OpenAPI completo embutido. Tudo com a biblioteca padrão do Python.

## 🤖 Atualização automática (CI)

O workflow [`.github/workflows/update-docs.yml`](./.github/workflows/update-docs.yml) roda diariamente (e sob demanda), regenera tudo e faz commit **apenas quando a documentação muda na origem** - então versões novas aparecem sozinhas assim que a Ubiquiti as publica.

---
name: unifi-api
description: >
  Consultar a API oficial da UniFi (Site Manager, Network, Protect, Mobility) -
  endpoints, parâmetros, schemas, autenticação e acesso local vs remoto (Cloud Connector).
  Use ao integrar com consoles UniFi, gerar chamadas HTTP, ou tirar dúvidas sobre versões da API.
---

# Skill: UniFi API

## Visão geral

A Ubiquiti expõe uma API REST oficial dividida em **4 aplicações**, cada uma versionada:

| App | O que cobre | Base (server) | Versionamento |
|---|---|---|---|
| **site-manager** | Nuvem multi-site: hosts, sites, devices, ISP metrics, SD-WAN, **Cloud Connector** | `https://api.ui.com` | `v1.0.0` |
| **network** | Rede de cada site: sites, devices, clients, networks/VLANs, WiFi, firewall, ACL, switching, DNS, hotspot, VPN, DPI | `/integration` (por console) | `v9.x`–`v10.x` |
| **protect** | Vídeo: cameras, viewers, live views, PTZ, lights, arm-profiles, eventos (WebSocket) | `/integration` (por console) | `v5.x`–`v7.x` |
| **mobility** | UniFi Connect / Mobility | `/integration` (por console) | `v1.0.0` |

> **Como achar o que precisa neste repositório:** comece por **`catalog.json`** (apps → versões →
> contagens) ou **`llms.txt`**. Para uma versão, leia **`<app>/<versão>/openapi.json`** (spec
> completa, melhor para parsing) ou **`<app>/<versão>/reference.md`** (leitura humana). Use sempre a versão
> que corresponde ao firmware do console; se não souber, use a **mais recente** (campo `latest`).

## Autenticação

Toda chamada usa um header de API key. **Qual chave depende do modo de acesso:**

- **Local** - chave gerada no **console** (UI local → *Integrations* → Create API Key).
  Header: `X-API-KEY`.
- **Remoto / Cloud** - chave gerada em **unifi.ui.com → Settings → API Keys**.
  Header: `X-API-Key`. É a chave do **Site Manager** e a usada pelo Cloud Connector.

Escopo da chave remota: chave de conta pessoal acessa só os consoles do dono; chave de
**organização** acessa qualquer console da org.

## Modos de acesso (Local vs Remoto)

Para `network`, `protect` e `mobility` (que rodam no console), há dois caminhos:

```
# LOCAL - precisa de rota de rede até o console
{MÉTODO} https://<console>/proxy/<app>/integration/v1/<recurso>
Header:  X-API-KEY: <chave-local>

# REMOTO - via Cloud Connector, NÃO precisa de acesso à rede local
{MÉTODO} https://api.ui.com/v1/connector/consoles/{consoleId}/<app>/integration/v1/<recurso>
Header:  X-API-Key: <chave-site-manager>
```

- O caminho depois de `/integration` é **idêntico** nos dois modos.
- `{consoleId}` vem de `GET https://api.ui.com/v1/hosts` (Site Manager), campo `id`.
- Requisitos do Cloud Connector: firmware do console ≥ 5.0.3; ~800 ms de latência extra.
- O **site-manager** é cloud direto: `https://api.ui.com/v1/...` com `X-API-Key` (sem `/connector`).

## Convenções (Network/Protect)

- **Paginação** (listagens): query `offset` (default 0), `limit` (default 25, máx 200).
- **Filtragem**: query `filter` com sintaxe `<prop>.<func>(<args>)`, combináveis com
  `and(...)`, `or(...)`, `not(...)`. Funções: `eq, ne, gt, ge, lt, le, like, in, notIn,
  isNull, isNotNull, contains, containsAny, containsAll, containsExactly, isEmpty`.
  Strings entre aspas simples; `like` usa `*` (qualquer nº de chars) e `.` (1 char).
- **Erros**: corpo padronizado com `statusCode`, `statusName`, `message`, `requestPath`, `timestamp`.

## Receita rápida

```bash
# 1) descobrir consoles (remoto)
curl -H "X-API-Key: $SM" https://api.ui.com/v1/hosts

# 2) listar sites de um console (remoto)
curl -H "X-API-Key: $SM" \
  "https://api.ui.com/v1/connector/consoles/$CID/network/integration/v1/sites"

# 3) o mesmo, local
curl -H "X-API-KEY: $LOCAL" \
  "https://192.168.1.1/proxy/network/integration/v1/sites"
```

## Notas

- Espelho atualizado por CI a partir de `developer.ui.com`; a fonte oficial prevalece.
- Para detalhes exatos de um endpoint (schema do corpo, enums, exemplos), abra o
  `openapi.json` da versão - ele contém o spec completo, incluindo o que a referência resume.

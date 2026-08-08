# UniFi Site Manager API - v1.3.23 - Referência

> Espelho automático de [`developer.ui.com/innerspace/v1.3.23`](https://developer.ui.com/innerspace/v1.3.23).
> OpenAPI `3.0.3` · 5 operações em 1 paths · atualizado na origem em `2026-08-06T02:11:15.183Z`.
> Autenticação: header `X-API-Key`.

**OpenAPI completo (fonte da verdade):** [`openapi.json`](./openapi.json)

## Índice de endpoints

| Categoria | Método | Path | Operação |
|---|---|---|---|
| cloud-connector | `GET` | `/v1/connector/consoles/{id}/*path` | Connector - GET |
| cloud-connector | `POST` | `/v1/connector/consoles/{id}/*path` | Connector - POST |
| cloud-connector | `PUT` | `/v1/connector/consoles/{id}/*path` | Connector - PUT |
| cloud-connector | `DELETE` | `/v1/connector/consoles/{id}/*path` | Connector - DELETE |
| cloud-connector | `PATCH` | `/v1/connector/consoles/{id}/*path` | Connector - PATCH |


---

## cloud-connector


### Connector - GET

`GET https://api.ui.com/v1/connector/consoles/{id}/*path`  ·  operationId: `ConnectorGet`

$21

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | Host ID to proxy the request to |
| `path` | path | sim | string | API path to proxy |

**Resposta 200** - 200

_(estrutura vazia)_

**Erros possíveis:** `400`, `401`, `403`, `408`, `429`, `500`, `502`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X GET "https://api.ui.com/v1/connector/consoles/{id}/*path" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Connector - POST

`POST https://api.ui.com/v1/connector/consoles/{id}/*path`  ·  operationId: `ConnectorPost`

$23

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | Host ID to proxy the request to |
| `path` | path | sim | string | API path to proxy |

**Corpo da requisição** (`application/json`)

_(estrutura vazia)_

**Resposta 200** - 200

_(estrutura vazia)_

**Erros possíveis:** `400`, `401`, `403`, `408`, `429`, `500`, `502`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X POST "https://api.ui.com/v1/connector/consoles/{id}/*path" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Connector - PUT

`PUT https://api.ui.com/v1/connector/consoles/{id}/*path`  ·  operationId: `ConnectorPut`

$24

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | Host ID to proxy the request to |
| `path` | path | sim | string | API path to proxy |

**Corpo da requisição** (`application/json`)

_(estrutura vazia)_

**Resposta 200** - 200

_(estrutura vazia)_

**Erros possíveis:** `400`, `401`, `403`, `408`, `429`, `500`, `502`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X PUT "https://api.ui.com/v1/connector/consoles/{id}/*path" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Connector - DELETE

`DELETE https://api.ui.com/v1/connector/consoles/{id}/*path`  ·  operationId: `ConnectorDelete`

$20

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | Host ID to proxy the request to |
| `path` | path | sim | string | API path to proxy |

**Resposta 200** - 200

_(estrutura vazia)_

**Erros possíveis:** `400`, `401`, `403`, `408`, `429`, `500`, `502`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X DELETE "https://api.ui.com/v1/connector/consoles/{id}/*path" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Connector - PATCH

`PATCH https://api.ui.com/v1/connector/consoles/{id}/*path`  ·  operationId: `ConnectorPatch`

$22

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | Host ID to proxy the request to |
| `path` | path | sim | string | API path to proxy |

**Corpo da requisição** (`application/json`)

_(estrutura vazia)_

**Resposta 200** - 200

_(estrutura vazia)_

**Erros possíveis:** `400`, `401`, `403`, `408`, `429`, `500`, `502`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X PATCH "https://api.ui.com/v1/connector/consoles/{id}/*path" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>

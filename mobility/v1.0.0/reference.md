# UniFi Mobility API - v1.0.0 - Referência

> Espelho automático de [`developer.ui.com/mobility/v1.0.0`](https://developer.ui.com/mobility/v1.0.0).
> OpenAPI `3.0.3` · 8 operações em 7 paths · atualizado na origem em `2026-06-25T08:38:50.888Z`.
> Autenticação: header `X-API-Key`.

**OpenAPI completo (fonte da verdade):** [`openapi.json`](./openapi.json)

## Índice de endpoints

| Categoria | Método | Path | Operação |
|---|---|---|---|
| Workspaces | `GET` | `/v1/mobility/workspaces` | List workspaces |
| Workspaces | `GET` | `/v1/mobility/workspaces/{workspaceID}/admins` | List workspace admins |
| Devices | `GET` | `/v1/mobility/workspaces/{workspaceID}/devices` | List devices |
| Devices | `GET` | `/v1/mobility/workspaces/{workspaceID}/devices/{deviceID}` | Get device detail |
| Clients | `GET` | `/v1/mobility/workspaces/{workspaceID}/devices/{deviceID}/clients` | List device clients |
| Device Configuration | `PUT` | `/v1/mobility/workspaces/{workspaceID}/devices/{deviceID}` | Update device name |
| Device Configuration | `PUT` | `/v1/mobility/workspaces/{workspaceID}/devices/{deviceID}/network` | Update LAN / DHCP settings |
| Device Configuration | `PUT` | `/v1/mobility/workspaces/{workspaceID}/devices/{deviceID}/wireless` | Update WiFi settings |


---

## Workspaces

Workspace listing and admin management
A workspace represents a mobility cloud site (admin account).


### List workspaces

`GET https://api.ui.com/v1/mobility/workspaces`  ·  operationId: `listWorkspaces`

Returns all workspaces visible to the authenticated user.
Only workspaces with active membership are returned.

**Scope**: `read:mobility`

**Resposta 200** - Workspace list.

**Erros possíveis:** `400`, `401`, `403`, `429`, `500`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X GET "https://api.ui.com/v1/mobility/workspaces" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### List workspace admins

`GET https://api.ui.com/v1/mobility/workspaces/{workspaceID}/admins`  ·  operationId: `listWorkspaceAdmins`

Returns all admins for a workspace with their permission levels.

The caller must have active membership. Only mobility permissions are exposed.

Admins are sorted: owner first, then active > pending > inactive > declined.

**Scope**: `read:mobility`

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `workspaceID` | path | sim | string (uuid) | Workspace UUID. Obtain from API call: GET /v1/mobility/workspaces |

**Resposta 200** - Admin list.

**Erros possíveis:** `400`, `401`, `403`, `404`, `429`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X GET "https://api.ui.com/v1/mobility/workspaces/{workspaceID}/admins" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Devices

Device listing and detail
Returns UniFi Mobile Router devices registered in a workspace.


### List devices

`GET https://api.ui.com/v1/mobility/workspaces/{workspaceID}/devices`  ·  operationId: `listDevices`

Returns a paginated list of devices in the workspace.
Each item contains identity and status fields only.
Use `getDevice` for full detail.

**Scope**: `read:mobility`

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `workspaceID` | path | sim | string (uuid) | Workspace UUID. Obtain from API call: GET /v1/mobility/workspaces |
| `limit` | query | não | integer | Maximum records per page. Capped at 200. (default 200) |
| `offset` | query | não | integer | Number of records to skip. (default 0) |

**Resposta 200** - Paginated device list.

**Erros possíveis:** `400`, `401`, `403`, `429`, `500`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X GET "https://api.ui.com/v1/mobility/workspaces/{workspaceID}/devices" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get device detail

`GET https://api.ui.com/v1/mobility/workspaces/{workspaceID}/devices/{deviceID}`  ·  operationId: `getDevice`

Returns full detail for a single device, including WAN, cellular,
WiFi, VPN, firewall rules, subscription, and GPS location.

**Scope**: `read:mobility`

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `workspaceID` | path | sim | string (uuid) | Workspace UUID. Obtain from API call: GET /v1/mobility/workspaces |
| `deviceID` | path | sim | string (uuid) | Device UUID. Obtain from API call: GET /v1/mobility/workspaces/{workspaceID}/devices |

**Resposta 200** - Full device detail.

**Erros possíveis:** `401`, `403`, `404`, `429`, `500`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X GET "https://api.ui.com/v1/mobility/workspaces/{workspaceID}/devices/{deviceID}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Clients

Clients connected to a device


### List device clients

`GET https://api.ui.com/v1/mobility/workspaces/{workspaceID}/devices/{deviceID}/clients`  ·  operationId: `listDeviceClients`

Returns a paginated list of all clients associated with a device,
including ONLINE, OFFLINE, and BLOCKED clients.

`wifi_experience` is omitted for wired clients (`type = WIRED`).

**Scope**: `read:mobility`

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `workspaceID` | path | sim | string (uuid) | Workspace UUID. Obtain from API call: GET /v1/mobility/workspaces |
| `deviceID` | path | sim | string (uuid) | Device UUID. Obtain from API call: GET /v1/mobility/workspaces/{workspaceID}/devices |
| `limit` | query | não | integer | Maximum records per page. Capped at 200. (default 200) |
| `offset` | query | não | integer | Number of records to skip. (default 0) |

**Resposta 200** - Paginated client list.

**Erros possíveis:** `400`, `401`, `403`, `404`, `429`, `500`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X GET "https://api.ui.com/v1/mobility/workspaces/{workspaceID}/devices/{deviceID}/clients" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Device Configuration

Write operations for device settings
All write operations require `write:mobility` scope and workspace **Admin** permission.


### Update device name

`PUT https://api.ui.com/v1/mobility/workspaces/{workspaceID}/devices/{deviceID}`  ·  operationId: `updateDeviceName`

Updates the user-assigned display name of a device.

**Scope**: `write:mobility`

**Permission**: workspace **Admin** (Viewers receive 403)

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `workspaceID` | path | sim | string (uuid) | Workspace UUID. Obtain from API call: GET /v1/mobility/workspaces |
| `deviceID` | path | sim | string (uuid) | Device UUID. Obtain from API call: GET /v1/mobility/workspaces/{workspaceID}/devices |

**Corpo da requisição** (`application/json`)

- `name` **(obrigatório)**: `string` ex: `Branch Office Router` - New device name (1-32 characters).

**Resposta 204** - Name updated successfully. No response body.

**Erros possíveis:** `400`, `401`, `403`, `404`, `429`, `500`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X PUT "https://api.ui.com/v1/mobility/workspaces/{workspaceID}/devices/{deviceID}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Update LAN / DHCP settings

`PUT https://api.ui.com/v1/mobility/workspaces/{workspaceID}/devices/{deviceID}/network`  ·  operationId: `updateDeviceNetwork`

Partial update - only provided fields are modified.
WAN, IPv6, and InternetSource are not configurable.

**Scope**: `write:mobility`

**Permission**: workspace **Admin**

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `workspaceID` | path | sim | string (uuid) | Workspace UUID. Obtain from API call: GET /v1/mobility/workspaces |
| `deviceID` | path | sim | string (uuid) | Device UUID. Obtain from API call: GET /v1/mobility/workspaces/{workspaceID}/devices |

**Corpo da requisição** (`application/json`)

- `host_address`: `string` (ipv4) nullable ex: `192.168.10.1`
- `dhcp_mode`: `string` nullable enum: dhcp, none ex: `dhcp` - `dhcp` = enabled, `none` = disabled.
- `dhcp_range_start`: `string` (ipv4) nullable ex: `192.168.10.100`
- `dhcp_range_stop`: `string` (ipv4) nullable ex: `192.168.10.200`
- `dhcp_lease_time`: `integer` nullable ex: `86400` - Seconds. `0` = infinite.

**Resposta 204** - Network settings updated successfully. No response body.

**Erros possíveis:** `400`, `401`, `403`, `404`, `429`, `500`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X PUT "https://api.ui.com/v1/mobility/workspaces/{workspaceID}/devices/{deviceID}/network" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Update WiFi settings

`PUT https://api.ui.com/v1/mobility/workspaces/{workspaceID}/devices/{deviceID}/wireless`  ·  operationId: `updateDeviceWireless`

Replaces the WiFi SSID and password. Both fields are required.
Channel, TX power, and security protocol are not configurable.

**Scope**: `write:mobility`

**Permission**: workspace **Admin**

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `workspaceID` | path | sim | string (uuid) | Workspace UUID. Obtain from API call: GET /v1/mobility/workspaces |
| `deviceID` | path | sim | string (uuid) | Device UUID. Obtain from API call: GET /v1/mobility/workspaces/{workspaceID}/devices |

**Corpo da requisição** (`application/json`)

- `ssid` **(obrigatório)**: `string` ex: `MyNetwork`
- `password` **(obrigatório)**: `string` ex: `securepass123` - WPA2-PSK password.

**Resposta 204** - WiFi settings updated successfully. No response body.

**Erros possíveis:** `400`, `401`, `403`, `404`, `429`, `500`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X PUT "https://api.ui.com/v1/mobility/workspaces/{workspaceID}/devices/{deviceID}/wireless" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>

# UniFi Mobility API - v1.0.0 - Referência

> Espelho automático de [`developer.ui.com/mobility/v1.0.0`](https://developer.ui.com/mobility/v1.0.0).
> OpenAPI `3.0.3` · 8 operações em 7 paths · atualizado na origem em `2026-08-12T11:31:34.156Z`.
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

- `total`: `integer` - Total number of records matching the query, ignoring pagination.
- `offset`: `integer` - Number of records skipped (echoes the `offset` query parameter).
- `limit`: `integer` - Page size applied (echoes the `limit` query parameter).
- `httpStatusCode` **(obrigatório)**: `integer` - HTTP status code.
- `traceId` **(obrigatório)**: `string` - Matches `X-Request-ID` if provided, otherwise auto-generated.
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `workspace_id` **(obrigatório)**: `string` (uuid) ex: `a1b2c3d4-e5f6-7890-abcd-ef1234567890`
    - `workspace_name` **(obrigatório)**: `string` ex: `John's Cloud`
    - `is_owner` **(obrigatório)**: `boolean` ex: `True`
    - `status` **(obrigatório)**: `string` enum: ACTIVE, PENDING, INACTIVE, DECLINED ex: `ACTIVE`

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

- `total`: `integer` - Total number of records matching the query, ignoring pagination.
- `offset`: `integer` - Number of records skipped (echoes the `offset` query parameter).
- `limit`: `integer` - Page size applied (echoes the `limit` query parameter).
- `httpStatusCode` **(obrigatório)**: `integer` - HTTP status code.
- `traceId` **(obrigatório)**: `string` - Matches `X-Request-ID` if provided, otherwise auto-generated.
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `name` **(obrigatório)**: `string` ex: `John Doe`
    - `email` **(obrigatório)**: `string` (email) ex: `john@example.com`
    - `status` **(obrigatório)**: `string` enum: ACTIVE, PENDING, INACTIVE, DECLINED ex: `ACTIVE`
    - `is_owner` **(obrigatório)**: `boolean` ex: `True`
    - `permissions` **(obrigatório)**: `object` nullable - Mobility permissions for the admin. `null` when the admin has no role bindings (e.g. pending invitation).
      - `umr`: `string` enum: ALL, VIEW_ONLY, NONE ex: `ALL` - Mobile Routing permission level. - `ALL` - can view and configure devices (admin) - `VIEW_ONLY` - read-only access (viewer) - `NONE` - no access

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

- `total`: `integer` - Total number of records matching the query, ignoring pagination.
- `offset`: `integer` - Number of records skipped (echoes the `offset` query parameter).
- `limit`: `integer` - Page size applied (echoes the `limit` query parameter).
- `httpStatusCode` **(obrigatório)**: `integer` - HTTP status code.
- `traceId` **(obrigatório)**: `string` - Matches `X-Request-ID` if provided, otherwise auto-generated.
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `id` **(obrigatório)**: `string` (uuid) ex: `550e8400-e29b-41d4-a716-446655440000`
    - `name` **(obrigatório)**: `string` ex: `Office Router`
    - `model` **(obrigatório)**: `string` enum: UMR, UMR Industrial, UMR Ultra ex: `UMR` - Hardware model name. - `UMR` - UMR Flex EU/US - `UMR Industrial` - UMR Industrial EU/US - `UMR Ultra` - UMR Ultra EU/US/ROW
    - `state` **(obrigatório)**: `string` enum: CONNECTED, DISCONNECTED, ADOPTING, ADOPTING_TIMEOUT, DOWNLOADING, UPGRADING, RESTARTING, FACTORY_RESET, GETTING_READY, RESTORING, NULL, DELETING ex: `CONNECTED` - Current device state.  | Value | Description | |-------|-------------| | `CONNECTED` | Online and communicating normally | | `DISCONNECTED` | Lost connection…
    - `firmware_version` **(obrigatório)**: `string` ex: `3.1.14`
    - `mac_address` **(obrigatório)**: `string` ex: `00:1A:2B:3C:4D:5E` - Primary MAC address in upper-case colon-separated format. Empty string when not yet initialised.

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

- `data` **(obrigatório)**
  - `id` **(obrigatório)**: `string` (uuid) ex: `550e8400-e29b-41d4-a716-446655440000`
  - `name` **(obrigatório)**: `string` ex: `Office Router`
  - `model` **(obrigatório)**: `string` enum: UMR, UMR Industrial, UMR Ultra ex: `UMR` - Hardware model name. - `UMR` - UMR Flex EU/US - `UMR Industrial` - UMR Industrial EU/US - `UMR Ultra` - UMR Ultra EU/US/ROW
  - `state` **(obrigatório)**: `string` enum: CONNECTED, DISCONNECTED, ADOPTING, ADOPTING_TIMEOUT, DOWNLOADING, UPGRADING, RESTARTING, FACTORY_RESET, GETTING_READY, RESTORING, NULL, DELETING ex: `CONNECTED` - Current device state.  | Value | Description | |-------|-------------| | `CONNECTED` | Online and communicating normally | | `DISCONNECTED` | Lost connection…
  - `firmware_version` **(obrigatório)**: `string` ex: `3.1.14`
  - `mac_address` **(obrigatório)**: `string` ex: `00:1A:2B:3C:4D:5E` - Primary MAC address in upper-case colon-separated format. Empty string when not yet initialised.
  - `wan_source`: `string` enum: LTE, WAN, WIFIWAN,  ex: `LTE` - Active WAN interface. Empty when no WAN connected.
  - `wan_ip`: `string` ex: `203.0.113.42` - Public WAN IP. Empty when not connected.
  - `enabled_wans`: `array` - Enabled WAN interfaces sorted by priority (index 0 = highest).
    - _array de_ `string`:
      - `string` enum: LTE, WAN, WIFIWAN
  - `isp`: `string` ex: `AT&T`
  - `lte_signal_level`: `string` enum: NO_SIGNAL, POOR, FAIR, STRONG,  ex: `FAIR` - LTE signal quality derived from RSSI (dBm).  | Value | RSSI range | Description | |-------|-----------|-------------| | `NO_SIGNAL` | < -111 dBm | No usable …
  - `cellular_data_usage_bytes`: `integer` (int64) ex: `524288000` - Data consumed in the current billing cycle, in bytes.
  - `cellular_data_limit_bytes`: `integer` (int64) ex: `5368709120` - Data cap in bytes for the current billing cycle. `-1` means unlimited. `0` is not a valid value.
  - `memory_usage_percent`: `integer` ex: `42`
  - `uptime_seconds`: `integer` (int64) ex: `86400` - Seconds since last boot. `0` when state is not `CONNECTED`.
  - `client_count`: `integer` ex: `5`
  - `host_address`: `string` ex: `192.168.1.1` - LAN gateway IP. Contains WAN IP in `WANBRIDGE` mode.
  - `poe_passthrough`: `boolean` ex: `False`
  - `device_mode`: `string` enum: ROUTER, WANBRIDGE, LTEPASS ex: `ROUTER` - - `ROUTER` - standard NAT router - `WANBRIDGE` - WAN bridge mode - `LTEPASS` - LTE passthrough
  - `wifi_enabled`: `boolean` ex: `True`
  - `wifi_ssid`: `string` ex: `UniFi-LTE`
  - `tx_power_level`: `string` enum: HIGH, MEDIUM, LOW,  ex: `HIGH` - Empty when Wireless record is not initialised.
  - `vpn_profile_name`: `string` ex: `HQ-VPN` - Empty when no VPN is configured.
  - `vpn_status`: `string` enum: CONNECTING, CONNECTED, DISCONNECTED, FAILED,  ex: `CONNECTED` - - `CONNECTING` - tunnel being established - `CONNECTED` - tunnel active - `DISCONNECTED` - configured but not connected - `FAILED` - connection failed - `""`…
  - `firewall_rule_names`: `array`
    - _array de_ `string`:
      - `string`
  - `routing_rule_names`: `array`
    - _array de_ `string`:
      - `string`
  - `ddns_profile_names`: `array`
    - _array de_ `string`:
      - `string`
  - `subscription_plan`: `string` enum: FREE_TRIAL, 1GB, 5GB, 20GB, 2GB, CLOUD,  ex: `5GB` - Active data plan. Empty when no subscription.  | Value | Description | |-------|-------------| | `FREE_TRIAL` | Free trial | | `1GB` | Monthly 1 GB | | `5GB`…
  - `subscription_status`: `string` enum: ACTIVE, INACTIVE, PENDING, FAILED ex: `ACTIVE` - Derived priority: FAILED > PENDING > ACTIVE > INACTIVE. A subscription cancelled at period end remains `ACTIVE` until expiry.
  - `location`: Omitted (not null) when no GPS fix is available.
    - `latitude` **(obrigatório)**: `number` (float) ex: `37.7749` - WGS-84 latitude in decimal degrees.
    - `longitude` **(obrigatório)**: `number` (float) ex: `-122.4194` - WGS-84 longitude in decimal degrees.
    - `last_updated` **(obrigatório)**: `integer` (int64) ex: `1709712000000` - Unix timestamp in milliseconds of the last GPS fix.
- `httpStatusCode` **(obrigatório)**: `integer` - HTTP status code.
- `traceId` **(obrigatório)**: `string` - Matches `X-Request-ID` if provided, otherwise auto-generated.

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

- `total`: `integer` - Total number of records matching the query, ignoring pagination.
- `offset`: `integer` - Number of records skipped (echoes the `offset` query parameter).
- `limit`: `integer` - Page size applied (echoes the `limit` query parameter).
- `httpStatusCode` **(obrigatório)**: `integer` - HTTP status code.
- `traceId` **(obrigatório)**: `string` - Matches `X-Request-ID` if provided, otherwise auto-generated.
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `mac` **(obrigatório)**: `string` ex: `AA:BB:CC:DD:EE:FF` - MAC address in upper-case colon-separated format.
    - `name` **(obrigatório)**: `string` ex: `John's iPhone`
    - `type` **(obrigatório)**: `string` enum: WIRED, WIRELESS ex: `WIRELESS`
    - `connection_status` **(obrigatório)**: `string` enum: ONLINE, OFFLINE, BLOCKED ex: `ONLINE` - - `ONLINE` - actively connected - `OFFLINE` - previously connected, no longer seen - `BLOCKED` - network access blocked; `is_blocked` will be `true`
    - `ip_address` **(obrigatório)**: `string` ex: `192.168.1.100` - Empty when unknown.
    - `is_blocked` **(obrigatório)**: `boolean` ex: `False`
    - `wifi_experience`: `integer` nullable ex: `85` - WiFi experience score (0-100). **Omitted** for wired clients.

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

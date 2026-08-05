# UniFi Network API - v9.1.120 - Referência

> Espelho automático de [`developer.ui.com/network/v9.1.120`](https://developer.ui.com/network/v9.1.120).
> OpenAPI `3.1.0` · 15 operações em 12 paths · atualizado na origem em `2026-08-04T14:16:46.226Z`.

**OpenAPI completo (fonte da verdade):** [`openapi.json`](./openapi.json)

## Índice de endpoints

| Categoria | Método | Path | Operação |
|---|---|---|---|
| Hotspot Vouchers | `GET` | `/v1/sites/{siteId}/hotspot/vouchers` | List Vouchers |
| Hotspot Vouchers | `POST` | `/v1/sites/{siteId}/hotspot/vouchers` | Generate Vouchers |
| Hotspot Vouchers | `DELETE` | `/v1/sites/{siteId}/hotspot/vouchers` | Delete Vouchers |
| Hotspot Vouchers | `GET` | `/v1/sites/{siteId}/hotspot/vouchers/{voucherId}` | Get Voucher Details |
| Hotspot Vouchers | `DELETE` | `/v1/sites/{siteId}/hotspot/vouchers/{voucherId}` | Delete Voucher |
| Devices | `POST` | `/v1/sites/{siteId}/devices/{deviceId}/interfaces/ports/{portIdx}/actions` | Execute Port Action |
| Devices | `POST` | `/v1/sites/{siteId}/devices/{deviceId}/actions` | Execute Device Action |
| Devices | `GET` | `/v1/sites/{siteId}/devices` | List Devices |
| Devices | `GET` | `/v1/sites/{siteId}/devices/{deviceId}` | Get Device Details |
| Devices | `GET` | `/v1/sites/{siteId}/devices/{deviceId}/statistics/latest` | Get Latest Device Statistics |
| Clients | `POST` | `/v1/sites/{siteId}/clients/{clientId}/actions` | Execute Client Action |
| Clients | `GET` | `/v1/sites/{siteId}/clients` | List Connected Clients |
| Clients | `GET` | `/v1/sites/{siteId}/clients/{clientId}` | Get Connected Client Details |
| Sites | `GET` | `/v1/sites` | List Local Sites |
| About application | `GET` | `/v1/info` | Get Application Info |


---

## Hotspot Vouchers


### List Vouchers

`GET /v1/sites/{siteId}/hotspot/vouchers`  ·  operationId: `getVouchers`

List Hotspot vouchers (paginated)

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`id`|`UUID`|`eq` `ne` `in` `notIn`|
|`createdAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
|`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
|`code`|`STRING`|`eq` `ne` `in` `notIn`|
|`authorizedGuestLimit`|`NUMBER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
|`authorizedGuestCount`|`NUMBER`|`eq` `ne` `gt` `ge` `lt` `le`|
|`activatedAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
|`expiresAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
|`expired`|`BOOLEAN`|`eq` `ne`|
|`timeLimitMinutes`|`NUMBER`|`eq` `ne` `gt` `ge` `lt` `le`|
|`dataUsageLimitMBytes`|`NUMBER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
|`rxRateLimitKbps`|`NUMBER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
|`txRateLimitKbps`|`NUMBER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não |  (int32) | (default 0) |
| `limit` | query | não |  (int32) | (default 100) |
| `filter` | query | não | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`
- `data` **(obrigatório)**: `array`
  - _array de_ `obj`:
    - `id` **(obrigatório)**: `string` (uuid)
    - `createdAt` **(obrigatório)**: `string` (date-time)
    - `name` **(obrigatório)**: `string` ex: `hotel-guest` - Voucher note, may contain duplicate values across multiple vouchers
    - `code` **(obrigatório)**: `string` ex: `4861409510` - Secret code to active the voucher using the Hotspot portal
    - `authorizedGuestLimit`: `integer` (int64) ex: `1` - (Optional) limit for how many different guests can use the same voucher to authorize network access
    - `authorizedGuestCount` **(obrigatório)**: `integer` (int64) ex: `0` - For how many guests the voucher has been used to authorize network access
    - `activatedAt`: `string` (date-time) - (Optional) timestamp when the voucher has been activated (authorization time of the first guest)
    - `expiresAt`: `string` (date-time) - (Optional) timestamp when the voucher will become expired. All guests using the voucher will be unauthorized from network access
    - `expired` **(obrigatório)**: `boolean` - Whether the voucher has been expired and can no longer be used to authorize network access
    - `timeLimitMinutes` **(obrigatório)**: `integer` (int64) ex: `1440` - How long (in minutes) the voucher will provide access to the network since authorization of the first guest. Subsequently connected guests, if allowed, will …
    - `dataUsageLimitMBytes`: `integer` (int64) ex: `1024` - (Optional) data usage limit in megabytes
    - `rxRateLimitKbps`: `integer` (int64) ex: `1000` - (Optional) download rate limit in kilobits per second
    - `txRateLimitKbps`: `integer` (int64) ex: `1000` - (Optional) upload rate limit in kilobits per second

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/hotspot/vouchers" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/hotspot/vouchers" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Generate Vouchers

`POST /v1/sites/{siteId}/hotspot/vouchers`  ·  operationId: `createVouchers`

Generate one or more Hotspot vouchers

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- `count`: `integer` (int32) default=1 - Number of vouchers to generate
- `name` **(obrigatório)**: `string` - Voucher note, duplicated across all generated vouchers
- `authorizedGuestLimit`: `integer` (int64) ex: `1` - (Optional) limit for how many different guests can use the same voucher to authorize network access
- `timeLimitMinutes` **(obrigatório)**: `integer` (int64) - How long (in minutes) the voucher will provide access to the network since authorization of the first guest. Subsequently connected guests, if allowed, will …
- `dataUsageLimitMBytes`: `integer` (int64) - (Optional) data usage limit in megabytes
- `rxRateLimitKbps`: `integer` (int64) - (Optional) download rate limit in kilobits per second
- `txRateLimitKbps`: `integer` (int64) - (Optional) upload rate limit in kilobits per second

**Resposta 201** - Created

- `vouchers`: `array`
  - _array de_ `obj`:
    - `id` **(obrigatório)**: `string` (uuid)
    - `createdAt` **(obrigatório)**: `string` (date-time)
    - `name` **(obrigatório)**: `string` ex: `hotel-guest` - Voucher note, may contain duplicate values across multiple vouchers
    - `code` **(obrigatório)**: `string` ex: `4861409510` - Secret code to active the voucher using the Hotspot portal
    - `authorizedGuestLimit`: `integer` (int64) ex: `1` - (Optional) limit for how many different guests can use the same voucher to authorize network access
    - `authorizedGuestCount` **(obrigatório)**: `integer` (int64) ex: `0` - For how many guests the voucher has been used to authorize network access
    - `activatedAt`: `string` (date-time) - (Optional) timestamp when the voucher has been activated (authorization time of the first guest)
    - `expiresAt`: `string` (date-time) - (Optional) timestamp when the voucher will become expired. All guests using the voucher will be unauthorized from network access
    - `expired` **(obrigatório)**: `boolean` - Whether the voucher has been expired and can no longer be used to authorize network access
    - `timeLimitMinutes` **(obrigatório)**: `integer` (int64) ex: `1440` - How long (in minutes) the voucher will provide access to the network since authorization of the first guest. Subsequently connected guests, if allowed, will …
    - `dataUsageLimitMBytes`: `integer` (int64) ex: `1024` - (Optional) data usage limit in megabytes
    - `rxRateLimitKbps`: `integer` (int64) ex: `1000` - (Optional) download rate limit in kilobits per second
    - `txRateLimitKbps`: `integer` (int64) ex: `1000` - (Optional) upload rate limit in kilobits per second

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/hotspot/vouchers" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/hotspot/vouchers" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Delete Vouchers

`DELETE /v1/sites/{siteId}/hotspot/vouchers`  ·  operationId: `deleteVouchers`

Delete Hotspot vouchers by filter

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`id`|`UUID`|`eq` `ne` `in` `notIn`|
|`createdAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
|`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
|`code`|`STRING`|`eq` `ne` `in` `notIn`|
|`authorizedGuestLimit`|`NUMBER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
|`authorizedGuestCount`|`NUMBER`|`eq` `ne` `gt` `ge` `lt` `le`|
|`activatedAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
|`expiresAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
|`expired`|`BOOLEAN`|`eq` `ne`|
|`timeLimitMinutes`|`NUMBER`|`eq` `ne` `gt` `ge` `lt` `le`|
|`dataUsageLimitMBytes`|`NUMBER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
|`rxRateLimitKbps`|`NUMBER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
|`txRateLimitKbps`|`NUMBER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `filter` | query | sim | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `vouchersDeleted`: `integer` (int64)

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X DELETE "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/hotspot/vouchers" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X DELETE "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/hotspot/vouchers" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get Voucher Details

`GET /v1/sites/{siteId}/hotspot/vouchers/{voucherId}`  ·  operationId: `getVoucher`

Get details of a specific Hotspot voucher

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `voucherId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `id` **(obrigatório)**: `string` (uuid)
- `createdAt` **(obrigatório)**: `string` (date-time)
- `name` **(obrigatório)**: `string` ex: `hotel-guest` - Voucher note, may contain duplicate values across multiple vouchers
- `code` **(obrigatório)**: `string` ex: `4861409510` - Secret code to active the voucher using the Hotspot portal
- `authorizedGuestLimit`: `integer` (int64) ex: `1` - (Optional) limit for how many different guests can use the same voucher to authorize network access
- `authorizedGuestCount` **(obrigatório)**: `integer` (int64) ex: `0` - For how many guests the voucher has been used to authorize network access
- `activatedAt`: `string` (date-time) - (Optional) timestamp when the voucher has been activated (authorization time of the first guest)
- `expiresAt`: `string` (date-time) - (Optional) timestamp when the voucher will become expired. All guests using the voucher will be unauthorized from network access
- `expired` **(obrigatório)**: `boolean` - Whether the voucher has been expired and can no longer be used to authorize network access
- `timeLimitMinutes` **(obrigatório)**: `integer` (int64) ex: `1440` - How long (in minutes) the voucher will provide access to the network since authorization of the first guest. Subsequently connected guests, if allowed, will …
- `dataUsageLimitMBytes`: `integer` (int64) ex: `1024` - (Optional) data usage limit in megabytes
- `rxRateLimitKbps`: `integer` (int64) ex: `1000` - (Optional) download rate limit in kilobits per second
- `txRateLimitKbps`: `integer` (int64) ex: `1000` - (Optional) upload rate limit in kilobits per second

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/hotspot/vouchers/{voucherId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/hotspot/vouchers/{voucherId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Delete Voucher

`DELETE /v1/sites/{siteId}/hotspot/vouchers/{voucherId}`  ·  operationId: `deleteVoucher`

Delete a specific Hotspot voucher

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `voucherId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `vouchersDeleted`: `integer` (int64)

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X DELETE "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/hotspot/vouchers/{voucherId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X DELETE "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/hotspot/vouchers/{voucherId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Devices


### Execute Port Action

`POST /v1/sites/{siteId}/devices/{deviceId}/interfaces/ports/{portIdx}/actions`  ·  operationId: `executePortAction`

Execute an action on a specific port. Request body should contain action name and input arguments, if apply.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `portIdx` | path | sim | integer (int32) |  |
| `siteId` | path | sim | string (uuid) |  |
| `deviceId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- _variantes por `action`: `POWER_CYCLE`→`Port PoE power-cycle request` (ver openapi.json)_
- `action` **(obrigatório)**: `string`

**Resposta 200** - OK

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/devices/{deviceId}/interfaces/ports/{portIdx}/actions" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/devices/{deviceId}/interfaces/ports/{portIdx}/actions" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Execute Device Action

`POST /v1/sites/{siteId}/devices/{deviceId}/actions`  ·  operationId: `executeDeviceAction`

Execute an action on a specific adopted device. Request body should contain action name and input arguments, if apply.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `siteId` | path | sim | string (uuid) |  |
| `deviceId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- _variantes por `action`: `RESTART`→`Device restart request` (ver openapi.json)_
- `action` **(obrigatório)**: `string`

**Resposta 200** - OK

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/devices/{deviceId}/actions" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/devices/{deviceId}/actions" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### List Devices

`GET /v1/sites/{siteId}/devices`  ·  operationId: `getDeviceOverviewPage`

List adopted devices of a site (paginated). Response contains basic information about site's adopted devices.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não |  (int32) | (default 0) |
| `limit` | query | não |  (int32) | (default 25) |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`
- `data` **(obrigatório)**: `array`
  - _array de_ `obj`:
    - `id` **(obrigatório)**: `string` (uuid)
    - `name` **(obrigatório)**: `string` ex: `IW HD`
    - `model` **(obrigatório)**: `string` ex: `UHDIW`
    - `macAddress` **(obrigatório)**: `string` ex: `94:2a:6f:26:c6:ca`
    - `ipAddress` **(obrigatório)**: `string` ex: `192.168.1.55`
    - `state` **(obrigatório)**: `string` enum: ONLINE, OFFLINE, PENDING_ADOPTION, UPDATING, GETTING_READY, ADOPTING, DELETING, CONNECTION_INTERRUPTED, ISOLATED
    - `features` **(obrigatório)**: `array`
      - _array de_ `string`:
        - `string` enum: switching, accessPoint, gateway
    - `interfaces` **(obrigatório)**: `array`
      - _array de_ `string`:
        - `string` enum: ports, radios

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/devices" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/devices" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get Device Details

`GET /v1/sites/{siteId}/devices/{deviceId}`  ·  operationId: `getDeviceDetails`

Get detailed information about a specific adopted device. Response includes more information about a single device, as well as more detailed information about device features, such as switch ports and/or access point radios

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `siteId` | path | sim | string (uuid) |  |
| `deviceId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `id` **(obrigatório)**: `string` (uuid)
- `name` **(obrigatório)**: `string` ex: `IW HD`
- `model` **(obrigatório)**: `string` ex: `UHDIW`
- `supported` **(obrigatório)**: `boolean`
- `macAddress` **(obrigatório)**: `string` ex: `94:2a:6f:26:c6:ca`
- `ipAddress` **(obrigatório)**: `string` ex: `192.168.1.55`
- `state` **(obrigatório)**: `string` enum: ONLINE, OFFLINE, PENDING_ADOPTION, UPDATING, GETTING_READY, ADOPTING, DELETING, CONNECTION_INTERRUPTED, ISOLATED
- `firmwareVersion`: `string` ex: `6.6.55`
- `firmwareUpdatable` **(obrigatório)**: `boolean`
- `adoptedAt`: `string` (date-time)
- `provisionedAt`: `string` (date-time)
- `configurationId` **(obrigatório)**: `string` ex: `7596498d2f367dc2`
- `uplink`: Uplink interface is device's connection to the parent device in the network topology
  - `deviceId` **(obrigatório)**: `string` (uuid)
- `features` **(obrigatório)**
  - `switching`
  - `accessPoint`
- `interfaces` **(obrigatório)**
  - `ports`: `array`
    - _array de_ `obj`:
      - `idx` **(obrigatório)**: `integer` (int32) ex: `1`
      - `state` **(obrigatório)**: `string` enum: UP, DOWN, UNKNOWN
      - `connector` **(obrigatório)**: `string` enum: RJ45, SFP, SFPPLUS, SFP28, QSFP28
      - `maxSpeedMbps` **(obrigatório)**: `integer` (int32) ex: `10000`
      - `speedMbps`: `integer` (int32) ex: `1000`
      - `poe`
        - `standard` **(obrigatório)**: `string` enum: 802.3af, 802.3at, 802.3bt ex: `802.3bt`
        - `type` **(obrigatório)**: `integer` (int32) enum: 1, 2, 3, 4 ex: `3`
        - `enabled` **(obrigatório)**: `boolean` - Whether the PoE feature is enabled on the port
        - `state` **(obrigatório)**: `string` enum: UP, DOWN, LIMITED, UNKNOWN - Whether the port currently supplies power to the (connected) device.
  - `radios`: `array`
    - _array de_ `obj`:
      - `wlanStandard` **(obrigatório)**: `string` enum: 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, 802.11ax, 802.11be
      - `frequencyGHz` **(obrigatório)**: `string` enum: 2.4, 5, 6, 60
      - `channelWidthMHz` **(obrigatório)**: `integer` (int32) ex: `40`
      - `channel`: `integer` (int32) ex: `36`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/devices/{deviceId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/devices/{deviceId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get Latest Device Statistics

`GET /v1/sites/{siteId}/devices/{deviceId}/statistics/latest`  ·  operationId: `getDeviceLatestStatistics`

Get latest (live) statistics of a specific adopted device. Response contains latest readings from a single device, such as CPU and memory utilization, uptime, uplink tx/rx rates etc

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `siteId` | path | sim | string (uuid) |  |
| `deviceId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `uptimeSec`: `integer` (int64)
- `lastHeartbeatAt`: `string` (date-time)
- `nextHeartbeatAt`: `string` (date-time)
- `loadAverage1Min`: `number` (double)
- `loadAverage5Min`: `number` (double)
- `loadAverage15Min`: `number` (double)
- `cpuUtilizationPct`: `number` (double)
- `memoryUtilizationPct`: `number` (double)
- `uplink`
  - `txRateBps`: `integer` (int64)
  - `rxRateBps`: `integer` (int64)
- `interfaces` **(obrigatório)**
  - `radios`: `array`
    - _array de_ `obj`:
      - `frequencyGHz` **(obrigatório)**: `string` enum: 2.4, 5, 6, 60
      - `txRetriesPct`: `number` (double)

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/devices/{deviceId}/statistics/latest" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/devices/{deviceId}/statistics/latest" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Clients


### Execute Client Action

`POST /v1/sites/{siteId}/clients/{clientId}/actions`  ·  operationId: `executeConnectedClientAction`

Execute an action on a specific connected client. Request body should contain action name and input arguments, if apply.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `clientId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- _variantes por `action`: `AUTHORIZE_GUEST_ACCESS`→`Guest access authorization request`, `UNAUTHORIZE_GUEST_ACCESS`→`Guest access unauthorization request` (ver openapi.json)_
- `action` **(obrigatório)**: `string`

**Resposta 200** - OK

- _variantes por `action`: `AUTHORIZE_GUEST_ACCESS`→`Guest access authorization response`, `UNAUTHORIZE_GUEST_ACCESS`→`Guest access unauthorization response` (ver openapi.json)_
- `action` **(obrigatório)**: `string`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/clients/{clientId}/actions" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/clients/{clientId}/actions" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### List Connected Clients

`GET /v1/sites/{siteId}/clients`  ·  operationId: `getConnectedClientOverviewPage`

List connected clients of a site (paginated). Clients are either physical devices (computers, smartphones, connected by wire or wirelessly), or active VPN connections.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`id`|`UUID`|`eq` `ne` `in` `notIn`|
|`type`|`STRING`|`eq` `ne` `in` `notIn`|
|`macAddress`|`STRING`|`isNull` `isNotNull` `eq` `ne` `in` `notIn`|
|`ipAddress`|`STRING`|`isNull` `isNotNull` `eq` `ne` `in` `notIn`|
|`connectedAt`|`TIMESTAMP`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
|`access.type`|`STRING`|`eq` `ne` `in` `notIn`|
|`access.authorized`|`BOOLEAN`|`isNull` `isNotNull` `eq` `ne`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não |  (int32) | (default 0) |
| `limit` | query | não |  (int32) | (default 25) |
| `filter` | query | não | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`
- `data` **(obrigatório)**: `array`
  - _array de_ `obj`:
    - _variantes por `type`: `WIRED`→`Wired client overview`, `WIRELESS`→`Wireless client overview`, `VPN`→`VPN client (connection) overview`, `TELEPORT`→`Teleport client (connection) overview` (ver openapi.json)_
    - `id` **(obrigatório)**: `string` (uuid)
    - `name` **(obrigatório)**: `string`
    - `connectedAt`: `string` (date-time)
    - `ipAddress`: `string`
    - `access` **(obrigatório)**
    - `type` **(obrigatório)**: `string`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/clients" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/clients" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get Connected Client Details

`GET /v1/sites/{siteId}/clients/{clientId}`  ·  operationId: `getConnectedClientDetails`

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `clientId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- _variantes por `type`: `WIRED`→`Wired client details`, `WIRELESS`→`Wireless client details`, `VPN`→`VPN client (connection) details`, `TELEPORT`→`Teleport client (connection) details` (ver openapi.json)_
- `id` **(obrigatório)**: `string` (uuid)
- `name` **(obrigatório)**: `string`
- `connectedAt`: `string` (date-time)
- `ipAddress`: `string`
- `access` **(obrigatório)**
- `type` **(obrigatório)**: `string`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/clients/{clientId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/clients/{clientId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Sites


### List Local Sites

`GET /v1/sites`  ·  operationId: `getSiteOverviewPage`

List local sites managed by this Network application (paginated).
Setups using Multi-Site option enabled will return all created sites
while if option is disabled it will return just the default site.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`id`|`UUID`|`eq` `ne` `in` `notIn`|
|`internalReference`|`STRING`|`eq` `ne` `in` `notIn`|
|`name`|`STRING`|`eq` `ne` `in` `notIn`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não |  (int32) | (default 0) |
| `limit` | query | não |  (int32) | (default 25) |
| `filter` | query | não | string |  |

**Resposta 200** - OK

- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`
- `data` **(obrigatório)**: `array`
  - _array de_ `obj`:
    - `id` **(obrigatório)**: `string` (uuid)
    - `internalReference` **(obrigatório)**: `string` - Internal unique name of the site used in older APIs
    - `name` **(obrigatório)**: `string`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## About application


### Get Application Info

`GET /v1/info`  ·  operationId: `getInfo`

Get generic information about the Network application

**Resposta 200** - OK

- `applicationVersion` **(obrigatório)**: `string` ex: `9.1.0`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/info" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/info" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>

# UniFi Site Manager API - v1.0.0 - Referência

> Espelho automático de [`developer.ui.com/site-manager/v1.0.0`](https://developer.ui.com/site-manager/v1.0.0).
> OpenAPI `3.0.3` · 9 operações em 9 paths · atualizado na origem em `2026-06-25T08:38:50.888Z`.
> Autenticação: header `X-API-Key`.

**OpenAPI completo (fonte da verdade):** [`openapi.json`](./openapi.json)

## Índice de endpoints

| Categoria | Método | Path | Operação |
|---|---|---|---|
| Endpoints | `GET` | `/v1/devices` | List Devices |
| Endpoints | `GET` | `/v1/hosts` | List Hosts |
| Endpoints | `GET` | `/v1/hosts/{id}` | Get Host by ID |
| Endpoints | `GET` | `/v1/isp-metrics/{type}` | Get ISP Metrics |
| Endpoints | `POST` | `/v1/isp-metrics/{type}/query` | Query ISP Metrics |
| Endpoints | `GET` | `/v1/sd-wan-configs` | List SD-WAN Configs |
| Endpoints | `GET` | `/v1/sd-wan-configs/{id}` | Get SD-WAN Config by ID |
| Endpoints | `GET` | `/v1/sd-wan-configs/{id}/status` | Get SD-WAN Config Status |
| Endpoints | `GET` | `/v1/sites` | List Sites |


---

## Endpoints


### List Devices

`GET https://api.ui.com/v1/devices`  ·  operationId: `listDevices`

Retrieves a list of UniFi devices managed by hosts where the UI account making the API call is the owner or a super admin. 

**Note**: The structure of the `devices.uidb` field may vary depending on the UniFi OS or Network Server version. The example provided is based on UniFi OS 4.1.13.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `hostIds[]` | query | não | array | List of host IDs to filter the results |
| `time` | query | não | string | Last processed timestamp of devices in RFC3339 format |
| `pageSize` | query | não | string | Number of items to return per page |
| `nextToken` | query | não | string | Token for pagination to retrieve the next set of results |

**Resposta 200** - 200

- `code`: Error code from upstream
- `data`: `array` - Generic response data, specific schema depends on the endpoint
  - _array de_ `object`:
    - `hostId`: `string` - Unique identifier of the host device
    - `hostName`: `string` - Name of the host device
    - `devices`: `array` - Array of devices managed by this host
      - _array de_ `object`:
        - `id`: `string` - Unique identifier of the device
        - `mac`: `string` - MAC address of the device
        - `name`: `string` - User-defined name of the device
        - `model`: `string` - Model name of the device
        - `shortname`: `string` - Short identifier of the device model (e.g., UDMPROSE)
        - `ip`: `string` - IP address of the device
        - `productLine`: `string` nullable - Product line of the device (network, protect, etc.)
        - `status`: `string` - Current connection status of the device (online, offline, etc.)
        - `version`: `string` - Current firmware version of the device
        - `firmwareStatus`: `string` - Status of device firmware (upToDate, updateAvailable, etc.)
        - `updateAvailable`: `string` nullable - Version of firmware update available for the device, if any
        - `isConsole`: `boolean` nullable - Indicates if the device is a console device
        - `isManaged`: `boolean` nullable - Indicates if the device is managed by the controller
        - `startupTime`: `string` (date-time) nullable - Time when the device was last started in RFC3339 format
        - `adoptionTime`: `string` nullable - Time when the device was adopted in RFC3339 format
        - `note`: `string` nullable - User-defined notes for the device
        - `uidb`: UI-specific metadata including images and identifiers
    - `updatedAt`: `string` (date-time) - Last update time in RFC3339 format
- `httpStatusCode`: `integer` - HTTP status code
- `traceId`: `string` - Request trace identifier
- `nextToken`: `string` - Pagination token for fetching the next set of results

**Erros possíveis:** `400`, `401`, `429`, `500`, `502`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X GET "https://api.ui.com/v1/devices" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### List Hosts

`GET https://api.ui.com/v1/hosts`  ·  operationId: `listHosts`

Retrieves a list of all hosts associated with the UI account making the API call. 

**Note**: The structure of `userData` and `reportedState` fields may vary depending on the UniFi OS or Network Server version. The example provided is based on UniFi OS 4.1.13.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `pageSize` | query | não | string | Number of items to return per page |
| `nextToken` | query | não | string | Token for pagination to retrieve the next set of results |

**Resposta 200** - 200

- `code`: Error code from upstream
- `data`: `array` - Generic response data, specific schema depends on the endpoint
  - _array de_ `object`:
    - `id`: `string` - Unique identifier of the host device
    - `hardwareId`: `string` - Hardware identifier of the device
    - `type`: `string` - Type of the device (console, network-server)
    - `ipAddress`: `string` - Current IP address of the device
    - `owner`: `boolean` - Indicates if the current user is the owner of this device
    - `isBlocked`: `boolean` - Indicates if the device is blocked from cloud access
    - `registrationTime`: `string` (date-time) - Time in RFC3339 format when the device was registered to the cloud
    - `lastConnectionStateChange`: `string` (date-time) - Time in RFC3339 format when the connection state last changed
    - `latestBackupTime`: `string` (date-time) - Time in RFC3339 format of the latest device backup
    - `userData`: User-specific data associated with the device including permissions and role information
    - `reportedState`: Device's reported state information
- `httpStatusCode`: `integer` - HTTP status code
- `traceId`: `string` - Request trace identifier
- `nextToken`: `string` - Pagination token for fetching the next set of results

**Erros possíveis:** `401`, `429`, `500`, `502`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X GET "https://api.ui.com/v1/hosts" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get Host by ID

`GET https://api.ui.com/v1/hosts/{id}`  ·  operationId: `getHostByID`

Retrieves detailed information about a specific host by ID. 

**Note**: The structure of the `userData` and `reportedState` fields may vary depending on the UniFi OS or Network Server version. The example provided is based on UniFi OS 4.1.13.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | Unique identifier of the host |

**Resposta 200** - 200

- `data`: `object` - Generic response data, specific schema depends on the endpoint
  - `id`: `string` - Unique identifier of the host device
  - `hardwareId`: `string` - Hardware identifier of the device
  - `type`: `string` - Type of the device (console, network-server)
  - `ipAddress`: `string` - Current IP address of the device
  - `owner`: `boolean` - Indicates if the current user is the owner of this device
  - `isBlocked`: `boolean` - Indicates if the device is blocked from cloud access
  - `registrationTime`: `string` (date-time) - Time in RFC3339 format when the device was registered to the cloud
  - `lastConnectionStateChange`: `string` (date-time) - Time in RFC3339 format when the connection state last changed
  - `latestBackupTime`: `string` (date-time) - Time in RFC3339 format of the latest device backup
  - `userData`: User-specific data associated with the device including permissions and role information
  - `reportedState`: Device's reported state information
- `httpStatusCode`: `integer` - HTTP status code
- `traceId`: `string` - Request trace identifier

**Erros possíveis:** `401`, `404`, `429`, `500`, `502`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X GET "https://api.ui.com/v1/hosts/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get ISP Metrics

`GET https://api.ui.com/v1/isp-metrics/{type}`  ·  operationId: `getISPMetrics`

Retrieves ISP metrics data for all sites linked to the UI account's API key. 5-minute interval metrics are available for at least 24 hours, and 1-hour interval metrics are available for at least 30 days.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `type` | path | sim | string | Specifies whether metrics are returned using `5m` or `1h` intervals |
| `beginTimestamp` | query | não | string | The earliest timestamp to retrieve data from (RFC3339 format) |
| `endTimestamp` | query | não | string | The latest timestamp to retrieve data up to (RFC3339 format) |
| `duration` | query | não | string | Specifies the time range of metrics to retrieve, starting from when the request is made. Supports `24h` for 5-minute metrics, and `7d` or `30d` for 1-hour metrics. This parameter **cannot** be used with `beginTimestamp` or `endTimestamp`. |

**Resposta 200** - 200

- `data`: `array` - Generic response data, specific schema depends on the endpoint
  - _array de_ `object`:
    - `metricType`: `string`
    - `periods`: `array`
      - _array de_ `object`:
        - `data`: `object`
          - `wan`: `object`
        - `metricTime`: `string` (date-time)
        - `version`: `string`
    - `hostId`: `string`
    - `siteId`: `string`
- `httpStatusCode`: `integer` - HTTP status code
- `traceId`: `string` - Request trace identifier

**Erros possíveis:** `400`, `401`, `429`, `500`, `502`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X GET "https://api.ui.com/v1/isp-metrics/{type}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Query ISP Metrics

`POST https://api.ui.com/v1/isp-metrics/{type}/query`  ·  operationId: `queryISPMetrics`

Retrieves ISP metrics data based on specific query parameters. 5-minute interval metrics are available for at least 24 hours, and 1-hour interval metrics are available for at least 30 days. 

**Note:** If the UI account lacks access to all requested sites, a 502 error is returned. If partial access is granted, the response will include `status: partialSuccess`.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `type` | path | sim | string | Specifies whether metrics are returned using `5m` or `1h` intervals |

**Corpo da requisição** (`application/json`)

- `sites`: `array`
  - _array de_ `object`:
    - `beginTimestamp`: `string` (date-time)
    - `hostId` **(obrigatório)**: `string`
    - `endTimestamp`: `string` (date-time)
    - `siteId` **(obrigatório)**: `string`

**Resposta 200** - 200

- `data`: `object` nullable - Generic response data, specific schema depends on the endpoint
  - `metrics`: `array`
    - _array de_ `object`:
      - `metricType`: `string`
      - `periods`: `array`
        - _array de_ `object`:
          - `data`: `object`
          - `metricTime`: `string` (date-time)
          - `version`: `string`
      - `hostId`: `string`
      - `siteId`: `string`
  - `message`: `string` nullable
  - `status`: `string` nullable
- `httpStatusCode`: `integer` - HTTP status code
- `traceId`: `string` - Request trace identifier

**Erros possíveis:** `400`, `401`, `429`, `500`, `502`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X POST "https://api.ui.com/v1/isp-metrics/{type}/query" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### List SD-WAN Configs

`GET https://api.ui.com/v1/sd-wan-configs`  ·  operationId: `listSDWanConfigs`

Retrieves a list of all hub-and-spoke SD-WAN configurations associated with the UI account making the API call.

**Resposta 200** - 200

- `data`: `array` - Generic response data, specific schema depends on the endpoint
  - _array de_ `object`:
    - `id`: `string` - Unique identifier of the SD-WAN config
    - `name`: `string` - Name of the SD-WAN config
    - `type`: `string` enum: ['sdwan-hbsp'] - Type of SD-WAN config - Currently only supports sdwan-hbsp
- `httpStatusCode`: `integer` - HTTP status code
- `traceId`: `string` - Request trace identifier

**Erros possíveis:** `401`, `429`, `500`, `502`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X GET "https://api.ui.com/v1/sd-wan-configs" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get SD-WAN Config by ID

`GET https://api.ui.com/v1/sd-wan-configs/{id}`  ·  operationId: `getSDWanConfigByID`

Retrieves detailed information about a specific SD-WAN configuration by ID.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | Unique identifier of the SD-WAN configuration |

**Resposta 200** - 200

- `data`: `object` nullable - Generic response data, specific schema depends on the endpoint
  - `id`: `string` - Unique identifier of the SD-WAN config
  - `name`: `string` - Name of the SD-WAN config
  - `type`: `string` enum: ['sdwan-hbsp'] - Type of SD-WAN config - Currently only supports sdwan-hbsp
  - `variant`: `string` enum: ['distributed', 'failover', 'single'] - Variant of SD-WAN configuration
  - `settings`: `object` - Advanced settings
    - `hubsInterconnect`: `boolean` nullable
    - `spokeToHubTunnelsMode`: `string` enum: ['maxResiliency', 'redundant', 'scalable']
    - `spokesAutoScaleAndNatEnabled`: `boolean` - Auto-assigns subnet and routes; otherwise, users enter them manually.
    - `spokesAutoScaleAndNatRange`: `string` nullable - Subnet in CIDR format, Example: 172.16.0.0/12
    - `spokesIsolate`: `boolean` - Setting for NET: Spokes can reach hubs but not other spokes.
    - `spokeStandardSettingsEnabled`: `boolean` - Enable spoke standard settings
    - `spokeStandardSettingsValues`: `object` nullable - Spoke standard settings
      - `primaryWan`: `string` nullable - Example: 'WAN'
      - `wanFailover`: `boolean` nullable - Use fail over WAN.
    - `spokeToHubRouting`: `string` nullable enum: ['custom', 'geo']
  - `hubs`: `array`
    - _array de_ `object`:
      - `id`: `string`
      - `hostId`: `string`
      - `siteId`: `string`
      - `networkIds`: `array` - Ids of networks belonging to the hub
        - _array de_ `string`:
          - `string`
      - `routes`: `array` - Subnets in CIDR format: 10.0.0.0/24
        - _array de_ `string`:
          - `string`
      - `primaryWan`: `string` - Example: 'WAN'
      - `wanFailover`: `boolean` - Use fail over WAN.
  - `spokes`: `array`
    - _array de_ `object`:
      - `id`: `string`
      - `hostId`: `string`
      - `siteId`: `string`
      - `networkIds`: `array` - Ids of networks belonging to the spoke
        - _array de_ `string`:
          - `string`
      - `routes`: `array` - Subnets in CIDR format: 10.0.0.0/24
        - _array de_ `string`:
          - `string`
      - `primaryWan`: `string` - Example: 'WAN'
      - `wanFailover`: `boolean` - Use fail over WAN.
      - `hubsPriority`: `array` - Non-null for distributed topology and spokeToHubRouting=custom
        - _array de_ `string`:
          - `string`
- `httpStatusCode`: `integer` - HTTP status code
- `traceId`: `string` - Request trace identifier

**Erros possíveis:** `401`, `404`, `429`, `500`, `502`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X GET "https://api.ui.com/v1/sd-wan-configs/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get SD-WAN Config Status

`GET https://api.ui.com/v1/sd-wan-configs/{id}/status`  ·  operationId: `getSDWanConfigStatus`

Retrieves the status of a specific SD-WAN configuration, including deployment progress, errors, and associated hubs.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | Unique identifier of the SD-WAN configuration |

**Resposta 200** - 200

- `data`: `object` nullable - Generic response data, specific schema depends on the endpoint
  - `id`: `string` - Unique identifier of the SD-WAN configuration
  - `fingerprint`: `string` - A unique identifier representing the current state of the configuration.
  - `updatedAt`: `integer` (int64) - The timestamp of the last update to the SD-WAN configuration.
  - `hubs`: `array` - List of hubs in SD-WAN configuration
    - _array de_ `object`:
      - `id`: `string` - Unique identifier of the hub
      - `hostId`: `string`
      - `siteId`: `string`
      - `name`: `string`
      - `primaryWanStatus`: `object`
        - `ip`: `string` - IP format: 10.0.0.1
        - `latency`: `number` (double) nullable
        - `internetIssues`: `array` - If WAN experience issues
          - _array de_ `object`:
        - `wanId`: `string`
      - `secondaryWanStatus`: `object`
        - `ip`: `string` - IP format: 10.0.0.1
        - `latency`: `number` (double) nullable
        - `internetIssues`: `array` - If WAN experience issues
          - _array de_ `object`:
        - `wanId`: `string`
      - `errors`: `array`
        - _array de_ `object`:
      - `warnings`: `array`
        - _array de_ `object`:
      - `numberOfTunnelsUsedByOtherFeatures`: `integer`
      - `networks`: `array`
        - _array de_ `object`:
          - `networkId`: `string`
          - `name`: `string`
          - `errors`: `array`
          - `warnings`: `array`
      - `routes`: `array`
        - _array de_ `object`:
          - `routeValue`: `string` - subnet in CIDR format: 10.0.0.0/24
          - `errors`: `array`
          - `warnings`: `array`
      - `applyStatus`: `string` enum: ['ok', 'creating', 'updating', 'removing', 'createFailed', 'updateFailed', 'removeFailed'] - The current status of the hub configuration application.
  - `spokes`: `array` - A list of spokes associated with the SD-WAN config.
    - _array de_ `object`:
      - `id`: `string`
      - `hostId`: `string`
      - `siteId`: `string`
      - `name`: `string`
      - `primaryWanStatus`: `object`
        - `ip`: `string` - IP format: 10.0.0.1
        - `latency`: `number` (double) nullable
        - `internetIssues`: `array` - If WAN experience issues
          - _array de_ `object`:
        - `wanId`: `string`
      - `secondaryWanStatus`: `object`
        - `ip`: `string` - IP format: 10.0.0.1
        - `latency`: `number` (double) nullable
        - `internetIssues`: `array` - If WAN experience issues
          - _array de_ `object`:
        - `wanId`: `string`
      - `errors`: `array`
        - _array de_ `object`:
      - `warnings`: `array`
        - _array de_ `object`:
      - `numberOfTunnelsUsedByOtherFeatures`: `integer`
      - `networks`: `array`
        - _array de_ `object`:
          - `networkId`: `string`
          - `name`: `string`
          - `errors`: `array` - A list of error messages related to the network, if any.
          - `warnings`: `array` - A list of warning messages related to the network, if any.
      - `routes`: `array`
        - _array de_ `object`:
          - `routeValue`: `string` - subnet in CIDR format: 10.0.0.0/24
          - `errors`: `array`
          - `warnings`: `array`
      - `connections`: `array`
        - _array de_ `object`:
          - `hubId`: `string`
          - `tunnels`: `array`
      - `applyStatus`: `string` enum: ['ok', 'creating', 'updating', 'removing', 'createFailed', 'updateFailed', 'removeFailed'] - The current status of the hub configuration application.
  - `lastGeneratedAt`: `integer` (int64) - The timestamp of the last generation of the SD-WAN configuration.
  - `generateStatus`: `string` enum: ['OK', 'GENERATING', 'GENERATE_FAILED'] - The status of the configuration generation process.
  - `errors`: `array` - A list of error messages related to the configuration, if any.
    - _array de_ `object`:
  - `warnings`: `array` - A list of warning messages related to the configuration, if any.
    - _array de_ `object`:
- `httpStatusCode`: `integer` - HTTP status code
- `traceId`: `string` - Request trace identifier

**Erros possíveis:** `401`, `404`, `429`, `500`, `502`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X GET "https://api.ui.com/v1/sd-wan-configs/{id}/status" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### List Sites

`GET https://api.ui.com/v1/sites`  ·  operationId: `listSites`

Retrieves a list of all sites (from hosts running the UniFi Network application) associated with the UI account making the API call. 

**Note**: The structure of the `meta` and `statistics` fields may vary depending on the UniFi Network version. The example provided is based on UniFi OS 4.1.13.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `pageSize` | query | não | string | Number of items to return per page |
| `nextToken` | query | não | string | Token for pagination to retrieve the next set of results |

**Resposta 200** - 200

- `code`: Error code from upstream
- `data`: `array` - Generic response data, specific schema depends on the endpoint
  - _array de_ `object`:
    - `siteId`: `string` - Unique identifier of the site
    - `hostId`: `string` - Unique identifier of the host device managing this site
    - `meta`: Site metadata including name, description, timezone, and gateway MAC address. Structure may vary depending on the UniFi Network version
    - `statistics`: Site statistics including device counts, client counts, and network performance metrics. Structure may vary depending on the UniFi Network version
    - `permission`: `string` - Permission level of the current user for this site (admin, readonly, etc.)
    - `isOwner`: `boolean` - Indicates if the current user is the owner of this site
- `httpStatusCode`: `integer` - HTTP status code
- `traceId`: `string` - Request trace identifier
- `nextToken`: `string` - Pagination token for fetching the next set of results

**Erros possíveis:** `401`, `429`, `500`, `502`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X GET "https://api.ui.com/v1/sites" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>

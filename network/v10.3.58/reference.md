# UniFi Network API - v10.3.58 - Referência

> Espelho automático de [`developer.ui.com/network/v10.3.58`](https://developer.ui.com/network/v10.3.58).
> OpenAPI `3.1.0` · 73 operações em 44 paths · atualizado na origem em `2026-08-12T11:31:34.156Z`.

**OpenAPI completo (fonte da verdade):** [`openapi.json`](./openapi.json)

## Índice de endpoints

| Categoria | Método | Path | Operação |
|---|---|---|---|
| Application Info | `GET` | `/v1/info` | Get Application Info |
| Sites | `GET` | `/v1/sites` | List Local Sites |
| UniFi Devices | `GET` | `/v1/pending-devices` | List Devices Pending Adoption |
| UniFi Devices | `GET` | `/v1/sites/{siteId}/devices` | List Adopted Devices |
| UniFi Devices | `POST` | `/v1/sites/{siteId}/devices` | Adopt Devices |
| UniFi Devices | `GET` | `/v1/sites/{siteId}/devices/{deviceId}` | Get Adopted Device Details |
| UniFi Devices | `DELETE` | `/v1/sites/{siteId}/devices/{deviceId}` | Remove (Unadopt) Device |
| UniFi Devices | `POST` | `/v1/sites/{siteId}/devices/{deviceId}/actions` | Execute Adopted Device Action |
| UniFi Devices | `POST` | `/v1/sites/{siteId}/devices/{deviceId}/interfaces/ports/{portIdx}/actions` | Execute Port Action |
| UniFi Devices | `GET` | `/v1/sites/{siteId}/devices/{deviceId}/statistics/latest` | Get Latest Adopted Device Statistics |
| Clients | `GET` | `/v1/sites/{siteId}/clients` | List Connected Clients |
| Clients | `GET` | `/v1/sites/{siteId}/clients/{clientId}` | Get Connected Client Details |
| Clients | `POST` | `/v1/sites/{siteId}/clients/{clientId}/actions` | Execute Client Action |
| Networks | `GET` | `/v1/sites/{siteId}/networks` | List Networks |
| Networks | `POST` | `/v1/sites/{siteId}/networks` | Create Network |
| Networks | `GET` | `/v1/sites/{siteId}/networks/{networkId}` | Get Network Details |
| Networks | `PUT` | `/v1/sites/{siteId}/networks/{networkId}` | Update Network |
| Networks | `DELETE` | `/v1/sites/{siteId}/networks/{networkId}` | Delete Network |
| Networks | `GET` | `/v1/sites/{siteId}/networks/{networkId}/references` | Get Network References |
| WiFi Broadcasts | `GET` | `/v1/sites/{siteId}/wifi/broadcasts` | List Wifi Broadcasts |
| WiFi Broadcasts | `POST` | `/v1/sites/{siteId}/wifi/broadcasts` | Create Wifi Broadcast |
| WiFi Broadcasts | `GET` | `/v1/sites/{siteId}/wifi/broadcasts/{wifiBroadcastId}` | Get Wifi Broadcast Details |
| WiFi Broadcasts | `PUT` | `/v1/sites/{siteId}/wifi/broadcasts/{wifiBroadcastId}` | Update Wifi Broadcast |
| WiFi Broadcasts | `DELETE` | `/v1/sites/{siteId}/wifi/broadcasts/{wifiBroadcastId}` | Delete Wifi Broadcast |
| Hotspot | `GET` | `/v1/sites/{siteId}/hotspot/vouchers` | List Vouchers |
| Hotspot | `POST` | `/v1/sites/{siteId}/hotspot/vouchers` | Generate Vouchers |
| Hotspot | `DELETE` | `/v1/sites/{siteId}/hotspot/vouchers` | Delete Vouchers |
| Hotspot | `GET` | `/v1/sites/{siteId}/hotspot/vouchers/{voucherId}` | Get Voucher Details |
| Hotspot | `DELETE` | `/v1/sites/{siteId}/hotspot/vouchers/{voucherId}` | Delete Voucher |
| Firewall | `GET` | `/v1/sites/{siteId}/firewall/policies` | List Firewall Policies |
| Firewall | `POST` | `/v1/sites/{siteId}/firewall/policies` | Create Firewall Policy |
| Firewall | `GET` | `/v1/sites/{siteId}/firewall/policies/ordering` | Get User-Defined Firewall Policy Ordering |
| Firewall | `PUT` | `/v1/sites/{siteId}/firewall/policies/ordering` | Reorder User-Defined Firewall Policies |
| Firewall | `GET` | `/v1/sites/{siteId}/firewall/policies/{firewallPolicyId}` | Get Firewall Policy |
| Firewall | `PUT` | `/v1/sites/{siteId}/firewall/policies/{firewallPolicyId}` | Update Firewall Policy |
| Firewall | `DELETE` | `/v1/sites/{siteId}/firewall/policies/{firewallPolicyId}` | Delete Firewall Policy |
| Firewall | `PATCH` | `/v1/sites/{siteId}/firewall/policies/{firewallPolicyId}` | Patch Firewall Policy |
| Firewall | `GET` | `/v1/sites/{siteId}/firewall/zones` | List Firewall Zones |
| Firewall | `POST` | `/v1/sites/{siteId}/firewall/zones` | Create Custom Firewall Zone |
| Firewall | `GET` | `/v1/sites/{siteId}/firewall/zones/{firewallZoneId}` | Get Firewall Zone |
| Firewall | `PUT` | `/v1/sites/{siteId}/firewall/zones/{firewallZoneId}` | Update Firewall Zone |
| Firewall | `DELETE` | `/v1/sites/{siteId}/firewall/zones/{firewallZoneId}` | Delete Custom Firewall Zone |
| Access Control (ACL Rules) | `GET` | `/v1/sites/{siteId}/acl-rules` | List ACL Rules |
| Access Control (ACL Rules) | `POST` | `/v1/sites/{siteId}/acl-rules` | Create ACL Rule |
| Access Control (ACL Rules) | `GET` | `/v1/sites/{siteId}/acl-rules/ordering` | Get User-Defined ACL Rule Ordering |
| Access Control (ACL Rules) | `PUT` | `/v1/sites/{siteId}/acl-rules/ordering` | Reorder User-Defined ACL Rules |
| Access Control (ACL Rules) | `GET` | `/v1/sites/{siteId}/acl-rules/{aclRuleId}` | Get ACL Rule |
| Access Control (ACL Rules) | `PUT` | `/v1/sites/{siteId}/acl-rules/{aclRuleId}` | Update ACL Rule |
| Access Control (ACL Rules) | `DELETE` | `/v1/sites/{siteId}/acl-rules/{aclRuleId}` | Delete ACL Rule |
| Switching | `GET` | `/v1/sites/{siteId}/switching/lags` | List LAGs |
| Switching | `GET` | `/v1/sites/{siteId}/switching/lags/{lagId}` | Get LAG Details |
| Switching | `GET` | `/v1/sites/{siteId}/switching/mc-lag-domains` | List MC-LAG Domains |
| Switching | `GET` | `/v1/sites/{siteId}/switching/mc-lag-domains/{mcLagDomainId}` | Get MC-LAG Domain |
| Switching | `GET` | `/v1/sites/{siteId}/switching/switch-stacks` | List Switch Stacks |
| Switching | `GET` | `/v1/sites/{siteId}/switching/switch-stacks/{switchStackId}` | Get Switch Stack |
| DNS Policies | `GET` | `/v1/sites/{siteId}/dns/policies` | List DNS Policies |
| DNS Policies | `POST` | `/v1/sites/{siteId}/dns/policies` | Create DNS Policy |
| DNS Policies | `GET` | `/v1/sites/{siteId}/dns/policies/{dnsPolicyId}` | Get DNS Policy |
| DNS Policies | `PUT` | `/v1/sites/{siteId}/dns/policies/{dnsPolicyId}` | Update DNS Policy |
| DNS Policies | `DELETE` | `/v1/sites/{siteId}/dns/policies/{dnsPolicyId}` | Delete DNS Policy |
| Traffic Matching Lists | `GET` | `/v1/sites/{siteId}/traffic-matching-lists` | List Traffic Matching Lists |
| Traffic Matching Lists | `POST` | `/v1/sites/{siteId}/traffic-matching-lists` | Create Traffic Matching List |
| Traffic Matching Lists | `GET` | `/v1/sites/{siteId}/traffic-matching-lists/{trafficMatchingListId}` | Get Traffic Matching List |
| Traffic Matching Lists | `PUT` | `/v1/sites/{siteId}/traffic-matching-lists/{trafficMatchingListId}` | Update Traffic Matching List |
| Traffic Matching Lists | `DELETE` | `/v1/sites/{siteId}/traffic-matching-lists/{trafficMatchingListId}` | Delete Traffic Matching List |
| Supporting Resources | `GET` | `/v1/countries` | List Countries |
| Supporting Resources | `GET` | `/v1/dpi/applications` | List DPI Applications |
| Supporting Resources | `GET` | `/v1/dpi/categories` | List DPI Application Categories |
| Supporting Resources | `GET` | `/v1/sites/{siteId}/device-tags` | List Device Tags |
| Supporting Resources | `GET` | `/v1/sites/{siteId}/radius/profiles` | List Radius Profiles |
| Supporting Resources | `GET` | `/v1/sites/{siteId}/vpn/servers` | List VPN Servers |
| Supporting Resources | `GET` | `/v1/sites/{siteId}/vpn/site-to-site-tunnels` | List Site-To-Site VPN Tunnels |
| Supporting Resources | `GET` | `/v1/sites/{siteId}/wans` | List WAN Interfaces |


---

## Application Info

Returns general details about the UniFi Network application,
including version and runtime metadata. Useful for integration validation.


### Get Application Info

`GET /v1/info`  ·  operationId: `getInfo`

Retrieve general information about the UniFi Network application.

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


---

## Sites

Endpoints for listing and managing UniFi sites within a local Network application.
Site ID is required for most other API requests.


### List Local Sites

`GET /v1/sites`  ·  operationId: `getSiteOverviewPage`

Retrieve a paginated list of local sites managed by this Network application.
Site ID is required for other UniFi Network API calls.

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
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `id` **(obrigatório)**: `string` (uuid)
    - `internalReference` **(obrigatório)**: `string` - Internal unique name of the site used in older APIs
    - `name` **(obrigatório)**: `string`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

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

## UniFi Devices

Endpoints to list, inspect, and interact with UniFi devices, including adopted and pending devices.
Provides device stats, port control, and actions.


### List Devices Pending Adoption

`GET /v1/pending-devices`  ·  operationId: `getPendingDevicePage`

Retrieve a paginated list of devices pending adoption, including basic device information.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`macAddress`|`STRING`|`eq` `ne` `in` `notIn`|
|`ipAddress`|`STRING`|`eq` `ne` `in` `notIn`|
|`model`|`STRING`|`eq` `ne` `in` `notIn`|
|`state`|`STRING`|`eq` `ne` `in` `notIn`|
|`supported`|`BOOLEAN`|`eq` `ne`|
|`firmwareVersion`|`STRING`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le` `like` `in` `notIn`|
|`firmwareUpdatable`|`BOOLEAN`|`eq` `ne`|
|`features`|`SET(STRING)`|`isEmpty` `contains` `containsAny` `containsAll` `containsExactly`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `adoptionTargetSiteIds` **(obrigatório)**: `array`
      - _array de_ `string`:
        - `string` (uuid)
    - `features` **(obrigatório)**: `array`
      - _array de_ `string`:
        - `string` enum: switching, accessPoint, gateway
    - `firmwareUpdatable` **(obrigatório)**: `boolean`
    - `firmwareVersion`: `string` ex: `6.6.55`
    - `ipAddress` **(obrigatório)**: `string` ex: `192.168.1.55`
    - `macAddress` **(obrigatório)**: `string` ex: `94:2a:6f:26:c6:ca`
    - `model` **(obrigatório)**: `string` ex: `UHDIW`
    - `state` **(obrigatório)**: `string` enum: ONLINE, OFFLINE, PENDING_ADOPTION, UPDATING, GETTING_READY, ADOPTING, DELETING, CONNECTION_INTERRUPTED, ISOLATED, U5G_INCORRECT_TOPOLOGY
    - `supported` **(obrigatório)**: `boolean`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/pending-devices" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/pending-devices" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### List Adopted Devices

`GET /v1/sites/{siteId}/devices`  ·  operationId: `getAdoptedDeviceOverviewPage`

Retrieve a paginated list of all adopted devices on a site, including basic device information.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`id`|`UUID`|`eq` `ne` `in` `notIn`|
|`macAddress`|`STRING`|`eq` `ne` `in` `notIn`|
|`ipAddress`|`STRING`|`eq` `ne` `in` `notIn`|
|`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
|`model`|`STRING`|`eq` `ne` `in` `notIn`|
|`state`|`STRING`|`eq` `ne` `in` `notIn`|
|`supported`|`BOOLEAN`|`eq` `ne`|
|`firmwareVersion`|`STRING`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le` `like` `in` `notIn`|
|`firmwareUpdatable`|`BOOLEAN`|`eq` `ne`|
|`features`|`SET(STRING)`|`isEmpty` `contains` `containsAny` `containsAll` `containsExactly`|
|`interfaces`|`SET(STRING)`|`isEmpty` `contains` `containsAny` `containsAll` `containsExactly`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `features` **(obrigatório)**: `array`
      - _array de_ `string`:
        - `string` enum: switching, accessPoint, gateway
    - `firmwareUpdatable` **(obrigatório)**: `boolean`
    - `firmwareVersion`: `string` ex: `6.6.55`
    - `id` **(obrigatório)**: `string` (uuid)
    - `interfaces` **(obrigatório)**: `array`
      - _array de_ `string`:
        - `string` enum: ports, radios
    - `ipAddress` **(obrigatório)**: `string` ex: `192.168.1.55`
    - `macAddress` **(obrigatório)**: `string` ex: `94:2a:6f:26:c6:ca`
    - `model` **(obrigatório)**: `string` ex: `UHDIW`
    - `name` **(obrigatório)**: `string` ex: `IW HD`
    - `state` **(obrigatório)**: `string` enum: ONLINE, OFFLINE, PENDING_ADOPTION, UPDATING, GETTING_READY, ADOPTING, DELETING, CONNECTION_INTERRUPTED, ISOLATED, U5G_INCORRECT_TOPOLOGY
    - `supported` **(obrigatório)**: `boolean`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

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


### Adopt Devices

`POST /v1/sites/{siteId}/devices`  ·  operationId: `adoptDevice`

Adopt a device to a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- `ignoreDeviceLimit` **(obrigatório)**: `boolean`
- `macAddress` **(obrigatório)**: `string`

**Resposta 200** - OK

- `adoptedAt`: `string` (date-time)
- `configurationId` **(obrigatório)**: `string` ex: `7596498d2f367dc2`
- `features` **(obrigatório)**: `object`
  - `accessPoint`
  - `switching`: `object`
    - `lags` **(obrigatório)**: `array`
      - _array de_ `object`:
        - `id` **(obrigatório)**: `string` (uuid)
        - `metadata` **(obrigatório)**
          - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `DERIVED`→`IntegrationDerivedSiteToSiteTunnelMetadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
        - `portIdxs` **(obrigatório)**: `array`
          - _array de_ `integer`:
- `firmwareUpdatable` **(obrigatório)**: `boolean`
- `firmwareVersion`: `string` ex: `6.6.55`
- `id` **(obrigatório)**: `string` (uuid)
- `interfaces` **(obrigatório)**: `object`
  - `ports`: `array`
    - _array de_ `object`:
      - `connector` **(obrigatório)**: `string` enum: RJ45, SFP, SFPPLUS, SFP28, QSFP28
      - `idx` **(obrigatório)**: `integer` (int32) ex: `1`
      - `maxSpeedMbps` **(obrigatório)**: `integer` (int32) ex: `10000`
      - `poe`: `object`
        - `enabled` **(obrigatório)**: `boolean` - Whether the PoE feature is enabled on the port
        - `standard` **(obrigatório)**: `string` enum: 802.3af, 802.3at, 802.3bt ex: `802.3bt`
        - `state` **(obrigatório)**: `string` enum: UP, DOWN, LIMITED, UNKNOWN - Whether the port currently supplies power to the (connected) device.
        - `type` **(obrigatório)**: `integer` (int32) enum: 1, 2, 3, 4 ex: `3`
      - `speedMbps`: `integer` (int32) ex: `1000`
      - `state` **(obrigatório)**: `string` enum: UP, DOWN, UNKNOWN
  - `radios`: `array`
    - _array de_ `object`:
      - `channel`: `integer` (int32) ex: `36`
      - `channelWidthMHz` **(obrigatório)**: `integer` (int32) ex: `40`
      - `frequencyGHz` **(obrigatório)**: `number` enum: 2.4, 5, 6, 60
      - `wlanStandard` **(obrigatório)**: `string` enum: 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, 802.11ax, 802.11be
- `ipAddress` **(obrigatório)**: `string` ex: `192.168.1.55`
- `macAddress` **(obrigatório)**: `string` ex: `94:2a:6f:26:c6:ca`
- `model` **(obrigatório)**: `string` ex: `UHDIW`
- `name` **(obrigatório)**: `string` ex: `IW HD`
- `provisionedAt`: `string` (date-time)
- `state` **(obrigatório)**: `string` enum: ONLINE, OFFLINE, PENDING_ADOPTION, UPDATING, GETTING_READY, ADOPTING, DELETING, CONNECTION_INTERRUPTED, ISOLATED, U5G_INCORRECT_TOPOLOGY
- `supported` **(obrigatório)**: `boolean`
- `uplink`: `object` - Uplink interface is device's connection to the parent device in the network topology
  - `deviceId` **(obrigatório)**: `string` (uuid)

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/devices" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/devices" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get Adopted Device Details

`GET /v1/sites/{siteId}/devices/{deviceId}`  ·  operationId: `getAdoptedDeviceDetails`

Retrieve detailed information about a specific adopted device, including firmware versioning, uplink state, details about device features and interfaces (ports, radios) and other key attributes.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `siteId` | path | sim | string (uuid) |  |
| `deviceId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `adoptedAt`: `string` (date-time)
- `configurationId` **(obrigatório)**: `string` ex: `7596498d2f367dc2`
- `features` **(obrigatório)**: `object`
  - `accessPoint`
  - `switching`: `object`
    - `lags` **(obrigatório)**: `array`
      - _array de_ `object`:
        - `id` **(obrigatório)**: `string` (uuid)
        - `metadata` **(obrigatório)**
          - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `DERIVED`→`IntegrationDerivedSiteToSiteTunnelMetadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
        - `portIdxs` **(obrigatório)**: `array`
          - _array de_ `integer`:
- `firmwareUpdatable` **(obrigatório)**: `boolean`
- `firmwareVersion`: `string` ex: `6.6.55`
- `id` **(obrigatório)**: `string` (uuid)
- `interfaces` **(obrigatório)**: `object`
  - `ports`: `array`
    - _array de_ `object`:
      - `connector` **(obrigatório)**: `string` enum: RJ45, SFP, SFPPLUS, SFP28, QSFP28
      - `idx` **(obrigatório)**: `integer` (int32) ex: `1`
      - `maxSpeedMbps` **(obrigatório)**: `integer` (int32) ex: `10000`
      - `poe`: `object`
        - `enabled` **(obrigatório)**: `boolean` - Whether the PoE feature is enabled on the port
        - `standard` **(obrigatório)**: `string` enum: 802.3af, 802.3at, 802.3bt ex: `802.3bt`
        - `state` **(obrigatório)**: `string` enum: UP, DOWN, LIMITED, UNKNOWN - Whether the port currently supplies power to the (connected) device.
        - `type` **(obrigatório)**: `integer` (int32) enum: 1, 2, 3, 4 ex: `3`
      - `speedMbps`: `integer` (int32) ex: `1000`
      - `state` **(obrigatório)**: `string` enum: UP, DOWN, UNKNOWN
  - `radios`: `array`
    - _array de_ `object`:
      - `channel`: `integer` (int32) ex: `36`
      - `channelWidthMHz` **(obrigatório)**: `integer` (int32) ex: `40`
      - `frequencyGHz` **(obrigatório)**: `number` enum: 2.4, 5, 6, 60
      - `wlanStandard` **(obrigatório)**: `string` enum: 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, 802.11ax, 802.11be
- `ipAddress` **(obrigatório)**: `string` ex: `192.168.1.55`
- `macAddress` **(obrigatório)**: `string` ex: `94:2a:6f:26:c6:ca`
- `model` **(obrigatório)**: `string` ex: `UHDIW`
- `name` **(obrigatório)**: `string` ex: `IW HD`
- `provisionedAt`: `string` (date-time)
- `state` **(obrigatório)**: `string` enum: ONLINE, OFFLINE, PENDING_ADOPTION, UPDATING, GETTING_READY, ADOPTING, DELETING, CONNECTION_INTERRUPTED, ISOLATED, U5G_INCORRECT_TOPOLOGY
- `supported` **(obrigatório)**: `boolean`
- `uplink`: `object` - Uplink interface is device's connection to the parent device in the network topology
  - `deviceId` **(obrigatório)**: `string` (uuid)

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


### Remove (Unadopt) Device

`DELETE /v1/sites/{siteId}/devices/{deviceId}`  ·  operationId: `removeDevice`

Removes (unadopts) an adopted device from the site. If the device is online, it will be reset to factory defaults.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `siteId` | path | sim | string (uuid) |  |
| `deviceId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X DELETE "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/devices/{deviceId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X DELETE "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/devices/{deviceId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Execute Adopted Device Action

`POST /v1/sites/{siteId}/devices/{deviceId}/actions`  ·  operationId: `executeAdoptedDeviceAction`

Perform an action on an specific adopted device. The request body must include the action name and any applicable input arguments.

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


### Execute Port Action

`POST /v1/sites/{siteId}/devices/{deviceId}/interfaces/ports/{portIdx}/actions`  ·  operationId: `executePortAction`

Perform an action on a specific device port. The request body must include the action name and any applicable input arguments.

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


### Get Latest Adopted Device Statistics

`GET /v1/sites/{siteId}/devices/{deviceId}/statistics/latest`  ·  operationId: `getAdoptedDeviceLatestStatistics`

Retrieve the latest real-time statistics of a specific adopted device, such as uptime, data transmission rates, CPU and memory utilization.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `siteId` | path | sim | string (uuid) |  |
| `deviceId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `cpuUtilizationPct`: `number` (double)
- `interfaces` **(obrigatório)**: `object`
  - `radios`: `array`
    - _array de_ `object`:
      - `frequencyGHz` **(obrigatório)**: `number` enum: 2.4, 5, 6, 60
      - `txRetriesPct`: `number` (double)
- `lastHeartbeatAt`: `string` (date-time)
- `loadAverage15Min`: `number` (double)
- `loadAverage1Min`: `number` (double)
- `loadAverage5Min`: `number` (double)
- `memoryUtilizationPct`: `number` (double)
- `nextHeartbeatAt`: `string` (date-time)
- `uplink`: `object`
  - `rxRateBps`: `integer` (int64)
  - `txRateBps`: `integer` (int64)
- `uptimeSec`: `integer` (int64)

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

Endpoints for viewing and managing connected clients (wired, wireless, VPN, and guest).
Supports actions such as authorizing or unauthorizing guest access.


### List Connected Clients

`GET /v1/sites/{siteId}/clients`  ·  operationId: `getConnectedClientOverviewPage`

Retrieve a paginated list of all connected clients on a site, including physical devices (computers, smartphones) and active VPN connections.

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
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - _variantes por `type`: `TELEPORT`→`Teleport client (connection) overview`, `VPN`→`VPN client (connection) overview`, `WIRED`→`Wired client overview`, `WIRELESS`→`Wireless client overview` (ver openapi.json)_
    - `access` **(obrigatório)**
    - `connectedAt`: `string` (date-time)
    - `id` **(obrigatório)**: `string` (uuid)
    - `ipAddress`: `string`
    - `name` **(obrigatório)**: `string`
    - `type` **(obrigatório)**: `string`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

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

Retrieve detailed information about a specific connected client, including name, IP address, MAC address, connection type and access information.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `clientId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- _variantes por `type`: `TELEPORT`→`Teleport client (connection) details`, `VPN`→`VPN client (connection) details`, `WIRED`→`Wired client details`, `WIRELESS`→`Wireless client details` (ver openapi.json)_
- `access` **(obrigatório)**
- `connectedAt`: `string` (date-time)
- `id` **(obrigatório)**: `string` (uuid)
- `ipAddress`: `string`
- `name` **(obrigatório)**: `string`
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


### Execute Client Action

`POST /v1/sites/{siteId}/clients/{clientId}/actions`  ·  operationId: `executeConnectedClientAction`

Perform an action on a specific connected client. The request body must include the action name and any applicable input arguments.

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


---

## Networks

Endpoints for creating, updating, deleting, and inspecting network configurations
including VLANs, DHCP, NAT, and IPv4/IPv6 settings.


### List Networks

`GET /v1/sites/{siteId}/networks`  ·  operationId: `getNetworksOverviewPage`

Retrieve a paginated list of all Networks on a site.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`management`|`STRING`|`eq` `ne` `in` `notIn`|
|`id`|`UUID`|`eq` `ne` `in` `notIn`|
|`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
|`enabled`|`BOOLEAN`|`eq` `ne`|
|`vlanId`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le` `in` `notIn`|
|`deviceId`|`UUID`|`eq` `ne` `in` `notIn` `isNull` `isNotNull`|
|`metadata.origin`|`STRING`|`eq` `ne` `in` `notIn`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - _variantes por `management`: `GATEWAY`→`Gateway managed network overview`, `SWITCH`→`Switch managed network overview`, `UNMANAGED`→`Unmanaged network overview` (ver openapi.json)_
    - `default` **(obrigatório)**: `boolean`
    - `enabled` **(obrigatório)**: `boolean`
    - `id` **(obrigatório)**: `string` (uuid)
    - `management` **(obrigatório)**: `string`
    - `metadata` **(obrigatório)**: Orchestrated or System-defined configurable network support
      - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
    - `name` **(obrigatório)**: `string` ex: `Default Network`
    - `vlanId` **(obrigatório)**: `integer` (int32) - VLAN ID. Must be 1 for the default network and >= 2 for additional networks.
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/networks" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/networks" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Create Network

`POST /v1/sites/{siteId}/networks`  ·  operationId: `createNetwork`

Create a new network on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- _variantes por `management`: `GATEWAY`→`IntegrationGatewayManagedNetworkCreateUpdateDto`, `SWITCH`→`IntegrationSwitchManagedNetworkCreateUpdateDto`, `UNMANAGED`→`IntegrationUnmanagedNetworkCreateUpdateDto` (ver openapi.json)_
- `dhcpGuarding`: `object` - DHCP Guarding settings for this Network. If this field is omitted or null, the feature is disabled
  - `trustedDhcpServerIpAddresses` **(obrigatório)**: `array` - List of trusted DHCP server IP addresses.
    - _array de_ `string`:
      - `string`
- `enabled` **(obrigatório)**: `boolean`
- `management` **(obrigatório)**: `string`
- `name` **(obrigatório)**: `string` ex: `Default Network`
- `vlanId` **(obrigatório)**: `integer` (int32) - VLAN ID. Must be 1 for the default network and >= 2 for additional networks.

**Resposta 201** - Created

- _variantes por `management`: `GATEWAY`→`Gateway managed network details`, `SWITCH`→`Switch managed network details`, `UNMANAGED`→`Unmanaged network details` (ver openapi.json)_
- `default` **(obrigatório)**: `boolean`
- `dhcpGuarding`: `object` - DHCP Guarding settings for this Network. If this field is omitted or null, the feature is disabled
  - `trustedDhcpServerIpAddresses` **(obrigatório)**: `array` - List of trusted DHCP server IP addresses.
    - _array de_ `string`:
      - `string`
- `enabled` **(obrigatório)**: `boolean`
- `id` **(obrigatório)**: `string` (uuid)
- `management` **(obrigatório)**: `string`
- `metadata` **(obrigatório)**: Orchestrated or System-defined configurable network support
  - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `name` **(obrigatório)**: `string` ex: `Default Network`
- `vlanId` **(obrigatório)**: `integer` (int32) - VLAN ID. Must be 1 for the default network and >= 2 for additional networks.

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/networks" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/networks" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get Network Details

`GET /v1/sites/{siteId}/networks/{networkId}`  ·  operationId: `getNetworkDetails`

Retrieve detailed information about a specific network.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `networkId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- _variantes por `management`: `GATEWAY`→`Gateway managed network details`, `SWITCH`→`Switch managed network details`, `UNMANAGED`→`Unmanaged network details` (ver openapi.json)_
- `default` **(obrigatório)**: `boolean`
- `dhcpGuarding`: `object` - DHCP Guarding settings for this Network. If this field is omitted or null, the feature is disabled
  - `trustedDhcpServerIpAddresses` **(obrigatório)**: `array` - List of trusted DHCP server IP addresses.
    - _array de_ `string`:
      - `string`
- `enabled` **(obrigatório)**: `boolean`
- `id` **(obrigatório)**: `string` (uuid)
- `management` **(obrigatório)**: `string`
- `metadata` **(obrigatório)**: Orchestrated or System-defined configurable network support
  - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `name` **(obrigatório)**: `string` ex: `Default Network`
- `vlanId` **(obrigatório)**: `integer` (int32) - VLAN ID. Must be 1 for the default network and >= 2 for additional networks.

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/networks/{networkId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/networks/{networkId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Update Network

`PUT /v1/sites/{siteId}/networks/{networkId}`  ·  operationId: `updateNetwork`

Update an existing network on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `networkId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- _variantes por `management`: `GATEWAY`→`IntegrationGatewayManagedNetworkCreateUpdateDto`, `SWITCH`→`IntegrationSwitchManagedNetworkCreateUpdateDto`, `UNMANAGED`→`IntegrationUnmanagedNetworkCreateUpdateDto` (ver openapi.json)_
- `dhcpGuarding`: `object` - DHCP Guarding settings for this Network. If this field is omitted or null, the feature is disabled
  - `trustedDhcpServerIpAddresses` **(obrigatório)**: `array` - List of trusted DHCP server IP addresses.
    - _array de_ `string`:
      - `string`
- `enabled` **(obrigatório)**: `boolean`
- `management` **(obrigatório)**: `string`
- `name` **(obrigatório)**: `string` ex: `Default Network`
- `vlanId` **(obrigatório)**: `integer` (int32) - VLAN ID. Must be 1 for the default network and >= 2 for additional networks.

**Resposta 200** - OK

- _variantes por `management`: `GATEWAY`→`Gateway managed network details`, `SWITCH`→`Switch managed network details`, `UNMANAGED`→`Unmanaged network details` (ver openapi.json)_
- `default` **(obrigatório)**: `boolean`
- `dhcpGuarding`: `object` - DHCP Guarding settings for this Network. If this field is omitted or null, the feature is disabled
  - `trustedDhcpServerIpAddresses` **(obrigatório)**: `array` - List of trusted DHCP server IP addresses.
    - _array de_ `string`:
      - `string`
- `enabled` **(obrigatório)**: `boolean`
- `id` **(obrigatório)**: `string` (uuid)
- `management` **(obrigatório)**: `string`
- `metadata` **(obrigatório)**: Orchestrated or System-defined configurable network support
  - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `name` **(obrigatório)**: `string` ex: `Default Network`
- `vlanId` **(obrigatório)**: `integer` (int32) - VLAN ID. Must be 1 for the default network and >= 2 for additional networks.

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PUT "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/networks/{networkId}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PUT "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/networks/{networkId}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Delete Network

`DELETE /v1/sites/{siteId}/networks/{networkId}`  ·  operationId: `deleteNetwork`

Delete an existing network on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `networkId` | path | sim | string (uuid) |  |
| `force` | query | não | boolean | (default False) |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X DELETE "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/networks/{networkId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X DELETE "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/networks/{networkId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get Network References

`GET /v1/sites/{siteId}/networks/{networkId}/references`  ·  operationId: `getNetworkReferences`

Retrieve references to a specific network.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `networkId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `referenceResources` **(obrigatório)**: `array` - List of network reference resources
  - _array de_ `object`:
    - `referenceCount` **(obrigatório)**: `integer` (int32) - Number of references of this type
    - `references`: `array` - List of references, present only if resourceType has API model defined
      - _array de_ `object`:
        - `referenceId` **(obrigatório)**: `string` (uuid)
    - `resourceType` **(obrigatório)**: `string` enum: CLIENT, DEVICE, STATIC_ROUTE, OSPF_ROUTE, NEXT_AI, WIFI, NAT_RULE, SD_WAN

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/networks/{networkId}/references" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/networks/{networkId}/references" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## WiFi Broadcasts

Endpoints to create, update, or remove WiFi networks (SSIDs).
Supports configuration of security, band steering, multicast filtering, and captive portals.


### List Wifi Broadcasts

`GET /v1/sites/{siteId}/wifi/broadcasts`  ·  operationId: `getWifiBroadcastPage`

$20

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - _variantes por `type`: `IOT_OPTIMIZED`→`IntegrationIotOptimizedWifiBroadcastOverviewDto`, `STANDARD`→`IntegrationStandardWifiBroadcastOverviewDto` (ver openapi.json)_
    - `broadcastingDeviceFilter`: Defines the custom scope of devices that will broadcast this WiFi network. If null, the WiFi network will be broadcast by all Access Point capable devices.
      - _variantes por `type`: `DEVICES`→`IntegrationWifiDevicesFilterDto`, `DEVICE_TAGS`→`IntegrationWifiDeviceTagsFilterDto` (ver openapi.json)_
      - `type` **(obrigatório)**: `string`
    - `enabled` **(obrigatório)**: `boolean`
    - `id` **(obrigatório)**: `string` (uuid)
    - `metadata` **(obrigatório)**
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
    - `name` **(obrigatório)**: `string`
    - `network`
      - _variantes por `type`: `NATIVE`→`IntegrationWifiNativeNetworkDto`, `SPECIFIC`→`IntegrationWifiSpecificNetworkDto` (ver openapi.json)_
      - `type` **(obrigatório)**: `string`
    - `securityConfiguration` **(obrigatório)**
      - _variantes por `type`: `OPEN`→`IntegrationWifiOpenSecurityConfigurationOverviewDto`, `WPA2_ENTERPRISE`→`IntegrationWifiWpa2EnterpriseSecurityConfigurationOverviewDto`, `WPA2_PERSONAL`→`IntegrationWifiWpa2PersonalSecurityConfigurationOverviewDto`, `WPA2_WPA3_ENTERPRISE`→`IntegrationWifiWpa2Wpa3EnterpriseSecurityConfigurationOverviewDto`, `WPA2_WPA3_PERSONAL`→`IntegrationWifiWpa2Wpa3PersonalSecurityConfigurationOverviewDto`, `WPA3_ENTERPRISE`→`IntegrationWifiWpa3EnterpriseSecurityConfigurationOverviewDto`, `WPA3_PERSONAL`→`IntegrationWifiWpa3PersonalSecurityConfigurationOverviewDto` (ver openapi.json)_
      - `type` **(obrigatório)**: `string`
    - `type` **(obrigatório)**: `string`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/wifi/broadcasts" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/wifi/broadcasts" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Create Wifi Broadcast

`POST /v1/sites/{siteId}/wifi/broadcasts`  ·  operationId: `createWifiBroadcast`

Create a new Wifi Broadcast on the specified site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- _variantes por `type`: `IOT_OPTIMIZED`→`IntegrationIotOptimizedWifiBroadcastCreateUpdateDto`, `STANDARD`→`IntegrationStandardWifiBroadcastCreateUpdateDto` (ver openapi.json)_
- `basicDataRateKbpsByFrequencyGHz`: `object`
  - `5` **(obrigatório)**: `integer` (int32) enum: 6000, 9000, 12000, 24000 ex: `6000`
  - `2.4` **(obrigatório)**: `integer` (int32) enum: 1000, 2000, 5500, 6000, 9000, 11000, 12000, 24000 ex: `2000`
- `blackoutScheduleConfiguration`: `object`
  - `days` **(obrigatório)**: `array`
    - _array de_ `object`:
      - _variantes por `type`: `ALL_DAY`→`IntegrationWifiBlackoutScheduleConfigurationPerAllDayDto`, `TIME_RANGE`→`IntegrationWifiBlackoutScheduleConfigurationPerDayWithTimeRangeDto` (ver openapi.json)_
      - `day` **(obrigatório)**: `string` enum: SUN, MON, TUE, WED, THU, FRI, SAT
      - `type` **(obrigatório)**: `string`
- `broadcastingDeviceFilter`: Defines the custom scope of devices that will broadcast this WiFi network. If null, the WiFi network will be broadcast by all Access Point capable devices.
  - _variantes por `type`: `DEVICES`→`IntegrationWifiDevicesFilterDto`, `DEVICE_TAGS`→`IntegrationWifiDeviceTagsFilterDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `clientFilteringPolicy`: `object` - Client connection filtering policy. Allow/restrict access to the WiFi network based on client device MAC addresses.
  - `action` **(obrigatório)**: `string` enum: ALLOW, BLOCK
  - `macAddressFilter` **(obrigatório)**: `array`
    - _array de_ `string`:
      - `string`
- `clientIsolationEnabled` **(obrigatório)**: `boolean`
- `enabled` **(obrigatório)**: `boolean`
- `hideName` **(obrigatório)**: `boolean`
- `mdnsProxyConfiguration`
  - _variantes por `mode`: `AUTO`→`IntegrationWifiMdnsProxyAutoConfigurationDto`, `CUSTOM`→`IntegrationWifiMdnsProxyCustomConfigurationDto` (ver openapi.json)_
  - `mode` **(obrigatório)**: `string`
- `multicastFilteringPolicy`
  - _variantes por `action`: `ALLOW`→`IntegrationWifiMulticastFilteringAllowPolicyDto`, `BLOCK`→`IntegrationWifiMulticastFilteringBlockPolicyDto` (ver openapi.json)_
  - `action` **(obrigatório)**: `string`
- `multicastToUnicastConversionEnabled` **(obrigatório)**: `boolean`
- `name` **(obrigatório)**: `string`
- `network`
  - _variantes por `type`: `NATIVE`→`IntegrationWifiNativeNetworkDto`, `SPECIFIC`→`IntegrationWifiSpecificNetworkDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `securityConfiguration` **(obrigatório)**: `object`
  - _variantes por `type`: `OPEN`→`IntegrationWifiOpenSecurityConfigurationDetailDto`, `WPA2_ENTERPRISE`→`IntegrationWifiWpa2EnterpriseSecurityConfigurationDetailDto`, `WPA2_PERSONAL`→`IntegrationWifiWpa2PersonalSecurityConfigurationDetailDto`, `WPA2_WPA3_ENTERPRISE`→`IntegrationWifiWpa2Wpa3EnterpriseSecurityConfigurationDetailDto`, `WPA2_WPA3_PERSONAL`→`IntegrationWifiWpa2Wpa3PersonalSecurityConfigurationDetailDto`, `WPA3_ENTERPRISE`→`IntegrationWifiWpa3EnterpriseSecurityConfigurationDetailDto`, `WPA3_PERSONAL`→`IntegrationWifiWpa3PersonalSecurityConfigurationDetailDto` (ver openapi.json)_
  - `radiusConfiguration`
  - `type` **(obrigatório)**: `string`
- `type` **(obrigatório)**: `string`
- `uapsdEnabled` **(obrigatório)**: `boolean` - Indicates whether Unscheduled Automatic Power Save Delivery (U-APSD) is enabled

**Resposta 201** - Created

- _variantes por `type`: `IOT_OPTIMIZED`→`IntegrationIotOptimizedWifiBroadcastDetailDto`, `STANDARD`→`IntegrationStandardWifiBroadcastDetailDto` (ver openapi.json)_
- `basicDataRateKbpsByFrequencyGHz`: `object`
  - `5` **(obrigatório)**: `integer` (int32) enum: 6000, 9000, 12000, 24000 ex: `6000`
  - `2.4` **(obrigatório)**: `integer` (int32) enum: 1000, 2000, 5500, 6000, 9000, 11000, 12000, 24000 ex: `2000`
- `blackoutScheduleConfiguration`: `object`
  - `days` **(obrigatório)**: `array`
    - _array de_ `object`:
      - _variantes por `type`: `ALL_DAY`→`IntegrationWifiBlackoutScheduleConfigurationPerAllDayDto`, `TIME_RANGE`→`IntegrationWifiBlackoutScheduleConfigurationPerDayWithTimeRangeDto` (ver openapi.json)_
      - `day` **(obrigatório)**: `string` enum: SUN, MON, TUE, WED, THU, FRI, SAT
      - `type` **(obrigatório)**: `string`
- `broadcastingDeviceFilter`: Defines the custom scope of devices that will broadcast this WiFi network. If null, the WiFi network will be broadcast by all Access Point capable devices.
  - _variantes por `type`: `DEVICES`→`IntegrationWifiDevicesFilterDto`, `DEVICE_TAGS`→`IntegrationWifiDeviceTagsFilterDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `clientFilteringPolicy`: `object` - Client connection filtering policy. Allow/restrict access to the WiFi network based on client device MAC addresses.
  - `action` **(obrigatório)**: `string` enum: ALLOW, BLOCK
  - `macAddressFilter` **(obrigatório)**: `array`
    - _array de_ `string`:
      - `string`
- `clientIsolationEnabled` **(obrigatório)**: `boolean`
- `enabled` **(obrigatório)**: `boolean`
- `hideName` **(obrigatório)**: `boolean`
- `id` **(obrigatório)**: `string` (uuid)
- `mdnsProxyConfiguration`
  - _variantes por `mode`: `AUTO`→`IntegrationWifiMdnsProxyAutoConfigurationDto`, `CUSTOM`→`IntegrationWifiMdnsProxyCustomConfigurationDto` (ver openapi.json)_
  - `mode` **(obrigatório)**: `string`
- `metadata` **(obrigatório)**
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `multicastFilteringPolicy`
  - _variantes por `action`: `ALLOW`→`IntegrationWifiMulticastFilteringAllowPolicyDto`, `BLOCK`→`IntegrationWifiMulticastFilteringBlockPolicyDto` (ver openapi.json)_
  - `action` **(obrigatório)**: `string`
- `multicastToUnicastConversionEnabled` **(obrigatório)**: `boolean`
- `name` **(obrigatório)**: `string`
- `network`
  - _variantes por `type`: `NATIVE`→`IntegrationWifiNativeNetworkDto`, `SPECIFIC`→`IntegrationWifiSpecificNetworkDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `securityConfiguration` **(obrigatório)**: `object`
  - _variantes por `type`: `OPEN`→`IntegrationWifiOpenSecurityConfigurationDetailDto`, `WPA2_ENTERPRISE`→`IntegrationWifiWpa2EnterpriseSecurityConfigurationDetailDto`, `WPA2_PERSONAL`→`IntegrationWifiWpa2PersonalSecurityConfigurationDetailDto`, `WPA2_WPA3_ENTERPRISE`→`IntegrationWifiWpa2Wpa3EnterpriseSecurityConfigurationDetailDto`, `WPA2_WPA3_PERSONAL`→`IntegrationWifiWpa2Wpa3PersonalSecurityConfigurationDetailDto`, `WPA3_ENTERPRISE`→`IntegrationWifiWpa3EnterpriseSecurityConfigurationDetailDto`, `WPA3_PERSONAL`→`IntegrationWifiWpa3PersonalSecurityConfigurationDetailDto` (ver openapi.json)_
  - `radiusConfiguration`
  - `type` **(obrigatório)**: `string`
- `type` **(obrigatório)**: `string`
- `uapsdEnabled` **(obrigatório)**: `boolean` - Indicates whether Unscheduled Automatic Power Save Delivery (U-APSD) is enabled

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/wifi/broadcasts" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/wifi/broadcasts" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get Wifi Broadcast Details

`GET /v1/sites/{siteId}/wifi/broadcasts/{wifiBroadcastId}`  ·  operationId: `getWifiBroadcastDetails`

Retrieve detailed information about a specific Wifi.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `wifiBroadcastId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- _variantes por `type`: `IOT_OPTIMIZED`→`IntegrationIotOptimizedWifiBroadcastDetailDto`, `STANDARD`→`IntegrationStandardWifiBroadcastDetailDto` (ver openapi.json)_
- `basicDataRateKbpsByFrequencyGHz`: `object`
  - `5` **(obrigatório)**: `integer` (int32) enum: 6000, 9000, 12000, 24000 ex: `6000`
  - `2.4` **(obrigatório)**: `integer` (int32) enum: 1000, 2000, 5500, 6000, 9000, 11000, 12000, 24000 ex: `2000`
- `blackoutScheduleConfiguration`: `object`
  - `days` **(obrigatório)**: `array`
    - _array de_ `object`:
      - _variantes por `type`: `ALL_DAY`→`IntegrationWifiBlackoutScheduleConfigurationPerAllDayDto`, `TIME_RANGE`→`IntegrationWifiBlackoutScheduleConfigurationPerDayWithTimeRangeDto` (ver openapi.json)_
      - `day` **(obrigatório)**: `string` enum: SUN, MON, TUE, WED, THU, FRI, SAT
      - `type` **(obrigatório)**: `string`
- `broadcastingDeviceFilter`: Defines the custom scope of devices that will broadcast this WiFi network. If null, the WiFi network will be broadcast by all Access Point capable devices.
  - _variantes por `type`: `DEVICES`→`IntegrationWifiDevicesFilterDto`, `DEVICE_TAGS`→`IntegrationWifiDeviceTagsFilterDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `clientFilteringPolicy`: `object` - Client connection filtering policy. Allow/restrict access to the WiFi network based on client device MAC addresses.
  - `action` **(obrigatório)**: `string` enum: ALLOW, BLOCK
  - `macAddressFilter` **(obrigatório)**: `array`
    - _array de_ `string`:
      - `string`
- `clientIsolationEnabled` **(obrigatório)**: `boolean`
- `enabled` **(obrigatório)**: `boolean`
- `hideName` **(obrigatório)**: `boolean`
- `id` **(obrigatório)**: `string` (uuid)
- `mdnsProxyConfiguration`
  - _variantes por `mode`: `AUTO`→`IntegrationWifiMdnsProxyAutoConfigurationDto`, `CUSTOM`→`IntegrationWifiMdnsProxyCustomConfigurationDto` (ver openapi.json)_
  - `mode` **(obrigatório)**: `string`
- `metadata` **(obrigatório)**
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `multicastFilteringPolicy`
  - _variantes por `action`: `ALLOW`→`IntegrationWifiMulticastFilteringAllowPolicyDto`, `BLOCK`→`IntegrationWifiMulticastFilteringBlockPolicyDto` (ver openapi.json)_
  - `action` **(obrigatório)**: `string`
- `multicastToUnicastConversionEnabled` **(obrigatório)**: `boolean`
- `name` **(obrigatório)**: `string`
- `network`
  - _variantes por `type`: `NATIVE`→`IntegrationWifiNativeNetworkDto`, `SPECIFIC`→`IntegrationWifiSpecificNetworkDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `securityConfiguration` **(obrigatório)**: `object`
  - _variantes por `type`: `OPEN`→`IntegrationWifiOpenSecurityConfigurationDetailDto`, `WPA2_ENTERPRISE`→`IntegrationWifiWpa2EnterpriseSecurityConfigurationDetailDto`, `WPA2_PERSONAL`→`IntegrationWifiWpa2PersonalSecurityConfigurationDetailDto`, `WPA2_WPA3_ENTERPRISE`→`IntegrationWifiWpa2Wpa3EnterpriseSecurityConfigurationDetailDto`, `WPA2_WPA3_PERSONAL`→`IntegrationWifiWpa2Wpa3PersonalSecurityConfigurationDetailDto`, `WPA3_ENTERPRISE`→`IntegrationWifiWpa3EnterpriseSecurityConfigurationDetailDto`, `WPA3_PERSONAL`→`IntegrationWifiWpa3PersonalSecurityConfigurationDetailDto` (ver openapi.json)_
  - `radiusConfiguration`
  - `type` **(obrigatório)**: `string`
- `type` **(obrigatório)**: `string`
- `uapsdEnabled` **(obrigatório)**: `boolean` - Indicates whether Unscheduled Automatic Power Save Delivery (U-APSD) is enabled

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/wifi/broadcasts/{wifiBroadcastId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/wifi/broadcasts/{wifiBroadcastId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Update Wifi Broadcast

`PUT /v1/sites/{siteId}/wifi/broadcasts/{wifiBroadcastId}`  ·  operationId: `updateWifiBroadcast`

Update an existing Wifi Broadcast on the specified site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `wifiBroadcastId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- _variantes por `type`: `IOT_OPTIMIZED`→`IntegrationIotOptimizedWifiBroadcastCreateUpdateDto`, `STANDARD`→`IntegrationStandardWifiBroadcastCreateUpdateDto` (ver openapi.json)_
- `basicDataRateKbpsByFrequencyGHz`: `object`
  - `5` **(obrigatório)**: `integer` (int32) enum: 6000, 9000, 12000, 24000 ex: `6000`
  - `2.4` **(obrigatório)**: `integer` (int32) enum: 1000, 2000, 5500, 6000, 9000, 11000, 12000, 24000 ex: `2000`
- `blackoutScheduleConfiguration`: `object`
  - `days` **(obrigatório)**: `array`
    - _array de_ `object`:
      - _variantes por `type`: `ALL_DAY`→`IntegrationWifiBlackoutScheduleConfigurationPerAllDayDto`, `TIME_RANGE`→`IntegrationWifiBlackoutScheduleConfigurationPerDayWithTimeRangeDto` (ver openapi.json)_
      - `day` **(obrigatório)**: `string` enum: SUN, MON, TUE, WED, THU, FRI, SAT
      - `type` **(obrigatório)**: `string`
- `broadcastingDeviceFilter`: Defines the custom scope of devices that will broadcast this WiFi network. If null, the WiFi network will be broadcast by all Access Point capable devices.
  - _variantes por `type`: `DEVICES`→`IntegrationWifiDevicesFilterDto`, `DEVICE_TAGS`→`IntegrationWifiDeviceTagsFilterDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `clientFilteringPolicy`: `object` - Client connection filtering policy. Allow/restrict access to the WiFi network based on client device MAC addresses.
  - `action` **(obrigatório)**: `string` enum: ALLOW, BLOCK
  - `macAddressFilter` **(obrigatório)**: `array`
    - _array de_ `string`:
      - `string`
- `clientIsolationEnabled` **(obrigatório)**: `boolean`
- `enabled` **(obrigatório)**: `boolean`
- `hideName` **(obrigatório)**: `boolean`
- `mdnsProxyConfiguration`
  - _variantes por `mode`: `AUTO`→`IntegrationWifiMdnsProxyAutoConfigurationDto`, `CUSTOM`→`IntegrationWifiMdnsProxyCustomConfigurationDto` (ver openapi.json)_
  - `mode` **(obrigatório)**: `string`
- `multicastFilteringPolicy`
  - _variantes por `action`: `ALLOW`→`IntegrationWifiMulticastFilteringAllowPolicyDto`, `BLOCK`→`IntegrationWifiMulticastFilteringBlockPolicyDto` (ver openapi.json)_
  - `action` **(obrigatório)**: `string`
- `multicastToUnicastConversionEnabled` **(obrigatório)**: `boolean`
- `name` **(obrigatório)**: `string`
- `network`
  - _variantes por `type`: `NATIVE`→`IntegrationWifiNativeNetworkDto`, `SPECIFIC`→`IntegrationWifiSpecificNetworkDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `securityConfiguration` **(obrigatório)**: `object`
  - _variantes por `type`: `OPEN`→`IntegrationWifiOpenSecurityConfigurationDetailDto`, `WPA2_ENTERPRISE`→`IntegrationWifiWpa2EnterpriseSecurityConfigurationDetailDto`, `WPA2_PERSONAL`→`IntegrationWifiWpa2PersonalSecurityConfigurationDetailDto`, `WPA2_WPA3_ENTERPRISE`→`IntegrationWifiWpa2Wpa3EnterpriseSecurityConfigurationDetailDto`, `WPA2_WPA3_PERSONAL`→`IntegrationWifiWpa2Wpa3PersonalSecurityConfigurationDetailDto`, `WPA3_ENTERPRISE`→`IntegrationWifiWpa3EnterpriseSecurityConfigurationDetailDto`, `WPA3_PERSONAL`→`IntegrationWifiWpa3PersonalSecurityConfigurationDetailDto` (ver openapi.json)_
  - `radiusConfiguration`
  - `type` **(obrigatório)**: `string`
- `type` **(obrigatório)**: `string`
- `uapsdEnabled` **(obrigatório)**: `boolean` - Indicates whether Unscheduled Automatic Power Save Delivery (U-APSD) is enabled

**Resposta 200** - OK

- _variantes por `type`: `IOT_OPTIMIZED`→`IntegrationIotOptimizedWifiBroadcastDetailDto`, `STANDARD`→`IntegrationStandardWifiBroadcastDetailDto` (ver openapi.json)_
- `basicDataRateKbpsByFrequencyGHz`: `object`
  - `5` **(obrigatório)**: `integer` (int32) enum: 6000, 9000, 12000, 24000 ex: `6000`
  - `2.4` **(obrigatório)**: `integer` (int32) enum: 1000, 2000, 5500, 6000, 9000, 11000, 12000, 24000 ex: `2000`
- `blackoutScheduleConfiguration`: `object`
  - `days` **(obrigatório)**: `array`
    - _array de_ `object`:
      - _variantes por `type`: `ALL_DAY`→`IntegrationWifiBlackoutScheduleConfigurationPerAllDayDto`, `TIME_RANGE`→`IntegrationWifiBlackoutScheduleConfigurationPerDayWithTimeRangeDto` (ver openapi.json)_
      - `day` **(obrigatório)**: `string` enum: SUN, MON, TUE, WED, THU, FRI, SAT
      - `type` **(obrigatório)**: `string`
- `broadcastingDeviceFilter`: Defines the custom scope of devices that will broadcast this WiFi network. If null, the WiFi network will be broadcast by all Access Point capable devices.
  - _variantes por `type`: `DEVICES`→`IntegrationWifiDevicesFilterDto`, `DEVICE_TAGS`→`IntegrationWifiDeviceTagsFilterDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `clientFilteringPolicy`: `object` - Client connection filtering policy. Allow/restrict access to the WiFi network based on client device MAC addresses.
  - `action` **(obrigatório)**: `string` enum: ALLOW, BLOCK
  - `macAddressFilter` **(obrigatório)**: `array`
    - _array de_ `string`:
      - `string`
- `clientIsolationEnabled` **(obrigatório)**: `boolean`
- `enabled` **(obrigatório)**: `boolean`
- `hideName` **(obrigatório)**: `boolean`
- `id` **(obrigatório)**: `string` (uuid)
- `mdnsProxyConfiguration`
  - _variantes por `mode`: `AUTO`→`IntegrationWifiMdnsProxyAutoConfigurationDto`, `CUSTOM`→`IntegrationWifiMdnsProxyCustomConfigurationDto` (ver openapi.json)_
  - `mode` **(obrigatório)**: `string`
- `metadata` **(obrigatório)**
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `multicastFilteringPolicy`
  - _variantes por `action`: `ALLOW`→`IntegrationWifiMulticastFilteringAllowPolicyDto`, `BLOCK`→`IntegrationWifiMulticastFilteringBlockPolicyDto` (ver openapi.json)_
  - `action` **(obrigatório)**: `string`
- `multicastToUnicastConversionEnabled` **(obrigatório)**: `boolean`
- `name` **(obrigatório)**: `string`
- `network`
  - _variantes por `type`: `NATIVE`→`IntegrationWifiNativeNetworkDto`, `SPECIFIC`→`IntegrationWifiSpecificNetworkDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `securityConfiguration` **(obrigatório)**: `object`
  - _variantes por `type`: `OPEN`→`IntegrationWifiOpenSecurityConfigurationDetailDto`, `WPA2_ENTERPRISE`→`IntegrationWifiWpa2EnterpriseSecurityConfigurationDetailDto`, `WPA2_PERSONAL`→`IntegrationWifiWpa2PersonalSecurityConfigurationDetailDto`, `WPA2_WPA3_ENTERPRISE`→`IntegrationWifiWpa2Wpa3EnterpriseSecurityConfigurationDetailDto`, `WPA2_WPA3_PERSONAL`→`IntegrationWifiWpa2Wpa3PersonalSecurityConfigurationDetailDto`, `WPA3_ENTERPRISE`→`IntegrationWifiWpa3EnterpriseSecurityConfigurationDetailDto`, `WPA3_PERSONAL`→`IntegrationWifiWpa3PersonalSecurityConfigurationDetailDto` (ver openapi.json)_
  - `radiusConfiguration`
  - `type` **(obrigatório)**: `string`
- `type` **(obrigatório)**: `string`
- `uapsdEnabled` **(obrigatório)**: `boolean` - Indicates whether Unscheduled Automatic Power Save Delivery (U-APSD) is enabled

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PUT "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/wifi/broadcasts/{wifiBroadcastId}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PUT "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/wifi/broadcasts/{wifiBroadcastId}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Delete Wifi Broadcast

`DELETE /v1/sites/{siteId}/wifi/broadcasts/{wifiBroadcastId}`  ·  operationId: `deleteWifiBroadcast`

Delete an existing Wifi Broadcast from the specified site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `wifiBroadcastId` | path | sim | string (uuid) |  |
| `force` | query | não | boolean | (default False) |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X DELETE "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/wifi/broadcasts/{wifiBroadcastId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X DELETE "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/wifi/broadcasts/{wifiBroadcastId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Hotspot

Endpoints for managing guest access via Hotspot vouchers - create, list, or revoke vouchers
and track their usage and expiration.


### List Vouchers

`GET /v1/sites/{siteId}/hotspot/vouchers`  ·  operationId: `getVouchers`

Retrieve a paginated list of Hotspot vouchers.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`id`|`UUID`|`eq` `ne` `in` `notIn`|
|`createdAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
|`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
|`code`|`STRING`|`eq` `ne` `in` `notIn`|
|`authorizedGuestLimit`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
|`authorizedGuestCount`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le`|
|`activatedAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
|`expiresAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
|`expired`|`BOOLEAN`|`eq` `ne`|
|`timeLimitMinutes`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le`|
|`dataUsageLimitMBytes`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
|`rxRateLimitKbps`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
|`txRateLimitKbps`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 100) |
| `filter` | query | não | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `activatedAt`: `string` (date-time) - (Optional) timestamp when the voucher has been activated (authorization time of the first guest)
    - `authorizedGuestCount` **(obrigatório)**: `integer` (int64) ex: `0` - For how many guests the voucher has been used to authorize network access
    - `authorizedGuestLimit`: `integer` (int64) ex: `1` - (Optional) limit for how many different guests can use the same voucher to authorize network access
    - `code` **(obrigatório)**: `string` ex: `4861409510` - Secret code to active the voucher using the Hotspot portal
    - `createdAt` **(obrigatório)**: `string` (date-time)
    - `dataUsageLimitMBytes`: `integer` (int64) ex: `1024` - (Optional) data usage limit in megabytes
    - `expired` **(obrigatório)**: `boolean` - Whether the voucher has been expired and can no longer be used to authorize network access
    - `expiresAt`: `string` (date-time) - (Optional) timestamp when the voucher will become expired. All guests using the voucher will be unauthorized from network access
    - `id` **(obrigatório)**: `string` (uuid)
    - `name` **(obrigatório)**: `string` ex: `hotel-guest` - Voucher note, may contain duplicate values across multiple vouchers
    - `rxRateLimitKbps`: `integer` (int64) ex: `1000` - (Optional) download rate limit in kilobits per second
    - `timeLimitMinutes` **(obrigatório)**: `integer` (int64) ex: `1440` - How long (in minutes) the voucher will provide access to the network since authorization of the first guest. Subsequently connected guests, if allowed, will …
    - `txRateLimitKbps`: `integer` (int64) ex: `1000` - (Optional) upload rate limit in kilobits per second
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

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

Create one or more Hotspot vouchers.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- `authorizedGuestLimit`: `integer` (int64) ex: `1` - (Optional) limit for how many different guests can use the same voucher to authorize network access
- `count`: `integer` (int32) default=1 - Number of vouchers to generate
- `dataUsageLimitMBytes`: `integer` (int64) - (Optional) data usage limit in megabytes
- `name` **(obrigatório)**: `string` - Voucher note, duplicated across all generated vouchers
- `rxRateLimitKbps`: `integer` (int64) - (Optional) download rate limit in kilobits per second
- `timeLimitMinutes` **(obrigatório)**: `integer` (int64) - How long (in minutes) the voucher will provide access to the network since authorization of the first guest. Subsequently connected guests, if allowed, will …
- `txRateLimitKbps`: `integer` (int64) - (Optional) upload rate limit in kilobits per second

**Resposta 201** - Created

- `vouchers`: `array`
  - _array de_ `object`:
    - `activatedAt`: `string` (date-time) - (Optional) timestamp when the voucher has been activated (authorization time of the first guest)
    - `authorizedGuestCount` **(obrigatório)**: `integer` (int64) ex: `0` - For how many guests the voucher has been used to authorize network access
    - `authorizedGuestLimit`: `integer` (int64) ex: `1` - (Optional) limit for how many different guests can use the same voucher to authorize network access
    - `code` **(obrigatório)**: `string` ex: `4861409510` - Secret code to active the voucher using the Hotspot portal
    - `createdAt` **(obrigatório)**: `string` (date-time)
    - `dataUsageLimitMBytes`: `integer` (int64) ex: `1024` - (Optional) data usage limit in megabytes
    - `expired` **(obrigatório)**: `boolean` - Whether the voucher has been expired and can no longer be used to authorize network access
    - `expiresAt`: `string` (date-time) - (Optional) timestamp when the voucher will become expired. All guests using the voucher will be unauthorized from network access
    - `id` **(obrigatório)**: `string` (uuid)
    - `name` **(obrigatório)**: `string` ex: `hotel-guest` - Voucher note, may contain duplicate values across multiple vouchers
    - `rxRateLimitKbps`: `integer` (int64) ex: `1000` - (Optional) download rate limit in kilobits per second
    - `timeLimitMinutes` **(obrigatório)**: `integer` (int64) ex: `1440` - How long (in minutes) the voucher will provide access to the network since authorization of the first guest. Subsequently connected guests, if allowed, will …
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

Remove Hotspot vouchers based on the specified filter criteria.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`id`|`UUID`|`eq` `ne` `in` `notIn`|
|`createdAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
|`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
|`code`|`STRING`|`eq` `ne` `in` `notIn`|
|`authorizedGuestLimit`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
|`authorizedGuestCount`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le`|
|`activatedAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
|`expiresAt`|`TIMESTAMP`|`eq` `ne` `gt` `ge` `lt` `le`|
|`expired`|`BOOLEAN`|`eq` `ne`|
|`timeLimitMinutes`|`INTEGER`|`eq` `ne` `gt` `ge` `lt` `le`|
|`dataUsageLimitMBytes`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
|`rxRateLimitKbps`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
|`txRateLimitKbps`|`INTEGER`|`isNull` `isNotNull` `eq` `ne` `gt` `ge` `lt` `le`|
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

Retrieve details of a specific Hotspot voucher.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `voucherId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `activatedAt`: `string` (date-time) - (Optional) timestamp when the voucher has been activated (authorization time of the first guest)
- `authorizedGuestCount` **(obrigatório)**: `integer` (int64) ex: `0` - For how many guests the voucher has been used to authorize network access
- `authorizedGuestLimit`: `integer` (int64) ex: `1` - (Optional) limit for how many different guests can use the same voucher to authorize network access
- `code` **(obrigatório)**: `string` ex: `4861409510` - Secret code to active the voucher using the Hotspot portal
- `createdAt` **(obrigatório)**: `string` (date-time)
- `dataUsageLimitMBytes`: `integer` (int64) ex: `1024` - (Optional) data usage limit in megabytes
- `expired` **(obrigatório)**: `boolean` - Whether the voucher has been expired and can no longer be used to authorize network access
- `expiresAt`: `string` (date-time) - (Optional) timestamp when the voucher will become expired. All guests using the voucher will be unauthorized from network access
- `id` **(obrigatório)**: `string` (uuid)
- `name` **(obrigatório)**: `string` ex: `hotel-guest` - Voucher note, may contain duplicate values across multiple vouchers
- `rxRateLimitKbps`: `integer` (int64) ex: `1000` - (Optional) download rate limit in kilobits per second
- `timeLimitMinutes` **(obrigatório)**: `integer` (int64) ex: `1440` - How long (in minutes) the voucher will provide access to the network since authorization of the first guest. Subsequently connected guests, if allowed, will …
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

Remove a specific Hotspot voucher.

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

## Firewall

Endpoints for managing custom firewall zones and policies within a site.
Define or update network segmentation and security boundaries.


### List Firewall Policies

`GET /v1/sites/{siteId}/firewall/policies`  ·  operationId: `getFirewallPolicies`

Retrieve a list of all firewall policies on a site.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`id`|`UUID`|`eq` `ne` `in` `notIn`|
|`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
|`source.zoneId`|`UUID`|`eq` `ne` `in` `notIn`|
|`destination.zoneId`|`UUID`|`eq` `ne` `in` `notIn`|
|`metadata.origin`|`STRING`|`eq` `ne` `in` `notIn`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `action` **(obrigatório)**: Defines action for matched traffic.
      - _variantes por `type`: `ALLOW`→`IntegrationFirewallPolicyActionAllowDto`, `BLOCK`→`IntegrationFirewallPolicyActionBlockDto`, `REJECT`→`IntegrationFirewallPolicyActionRejectDto` (ver openapi.json)_
      - `type` **(obrigatório)**: `string`
    - `connectionStateFilter`: `array` - Match on firewall connection state. If null, matches all connection states.
      - _array de_ `string`:
        - `string` enum: NEW, INVALID, ESTABLISHED, RELATED
    - `description`: `string` ex: `A description for my firewall policy`
    - `destination` **(obrigatório)**: `object`
      - `trafficFilter`
        - _variantes por `type`: `APPLICATION`→`IntegrationFirewallPolicyDestinationApplicationFilterDto`, `APPLICATION_CATEGORY`→`IntegrationFirewallPolicyDestinationApplicationCategoryFilterDto`, `DOMAIN`→`IntegrationFirewallPolicyDestinationDomainFilterDto`, `IPV6_IID`→`IntegrationFirewallPolicyDestinationIpv6IidFilterDto`, `IP_ADDRESS`→`IntegrationFirewallPolicyDestinationIpAddressFilterDto`, `NETWORK`→`IntegrationFirewallPolicyDestinationNetworkFilterDto`, `PORT`→`IntegrationFirewallPolicyDestinationPortFilterDto`, `REGION`→`IntegrationFirewallPolicyDestinationRegionFilterDto`, `SITE_TO_SITE_VPN_TUNNEL`→`IntegrationFirewallPolicyDestinationSiteToSiteVpnTunnelFilterDto`, `VPN_SERVER`→`IntegrationFirewallPolicyDestinationVpnServerFilterDto` (ver openapi.json)_
        - `type` **(obrigatório)**: `string`
      - `zoneId` **(obrigatório)**: `string` (uuid) - ID of the firewall zone to which the matched traffic is destined.
    - `enabled` **(obrigatório)**: `boolean`
    - `id` **(obrigatório)**: `string` (uuid)
    - `index` **(obrigatório)**: `integer` (int32)
    - `ipProtocolScope` **(obrigatório)**: Defines rules for matching by IP version and protocol.
      - _variantes por `ipVersion`: `IPV4`→`IntegrationFirewallPolicyIpv4ProtocolScopeDto`, `IPV4_AND_IPV6`→`IntegrationFirewallPolicyIpv4AndIpv6ProtocolScopeDto`, `IPV6`→`IntegrationFirewallPolicyIpv6ProtocolScopeDto` (ver openapi.json)_
      - `ipVersion` **(obrigatório)**: `string`
    - `ipsecFilter`: `string` enum: MATCH_ENCRYPTED, MATCH_NOT_ENCRYPTED - Match on traffic encrypted, or not encrypted by IPsec. If null, matches all traffic.
    - `loggingEnabled` **(obrigatório)**: `boolean` - Generate syslog entries when traffic is matched. Such entries are sent to a remote syslog server.
    - `metadata` **(obrigatório)**
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
    - `name` **(obrigatório)**: `string` ex: `My firewall policy`
    - `schedule`: Defines date and time when the entity is active. If null, the entity is always active.
      - _variantes por `mode`: `CUSTOM`→`IntegrationFirewallScheduleCustomDto`, `EVERY_DAY`→`IntegrationFirewallScheduleEveryDayDto`, `EVERY_WEEK`→`IntegrationFirewallScheduleEveryWeekDto`, `ONE_TIME_ONLY`→`IntegrationFirewallScheduleOneTimeOnlyDto` (ver openapi.json)_
      - `mode` **(obrigatório)**: `string`
    - `source` **(obrigatório)**: `object`
      - `trafficFilter`
        - _variantes por `type`: `IPV6_IID`→`IntegrationFirewallPolicySourceIpv6IidFilterDto`, `IP_ADDRESS`→`IntegrationFirewallPolicySourceIpAddressFilterDto`, `MAC_ADDRESS`→`IntegrationFirewallPolicySourceMacAddressFilterDto`, `NETWORK`→`IntegrationFirewallPolicySourceNetworkFilterDto`, `PORT`→`IntegrationFirewallPolicySourcePortFilterDto`, `REGION`→`IntegrationFirewallPolicySourceRegionFilterDto`, `SITE_TO_SITE_VPN_TUNNEL`→`IntegrationFirewallPolicySourceSiteToSiteVpnTunnelFilterDto`, `VPN_SERVER`→`IntegrationFirewallPolicySourceVpnServerFilterDto` (ver openapi.json)_
        - `type` **(obrigatório)**: `string`
      - `zoneId` **(obrigatório)**: `string` (uuid) - ID of the firewall zone from which the matched traffic originates.
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/firewall/policies" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/firewall/policies" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Create Firewall Policy

`POST /v1/sites/{siteId}/firewall/policies`  ·  operationId: `createFirewallPolicy`

Create a new firewall policy on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- `action` **(obrigatório)**: Defines action for matched traffic.
  - _variantes por `type`: `ALLOW`→`IntegrationFirewallPolicyActionAllowDto`, `BLOCK`→`IntegrationFirewallPolicyActionBlockDto`, `REJECT`→`IntegrationFirewallPolicyActionRejectDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `connectionStateFilter`: `array` - Match on firewall connection state. If null, matches all connection states.
  - _array de_ `string`:
    - `string` enum: NEW, INVALID, ESTABLISHED, RELATED
- `description`: `string` ex: `A description for my firewall policy`
- `destination` **(obrigatório)**: `object`
  - `trafficFilter`
    - _variantes por `type`: `APPLICATION`→`IntegrationFirewallPolicyDestinationApplicationFilterDto`, `APPLICATION_CATEGORY`→`IntegrationFirewallPolicyDestinationApplicationCategoryFilterDto`, `DOMAIN`→`IntegrationFirewallPolicyDestinationDomainFilterDto`, `IPV6_IID`→`IntegrationFirewallPolicyDestinationIpv6IidFilterDto`, `IP_ADDRESS`→`IntegrationFirewallPolicyDestinationIpAddressFilterDto`, `NETWORK`→`IntegrationFirewallPolicyDestinationNetworkFilterDto`, `PORT`→`IntegrationFirewallPolicyDestinationPortFilterDto`, `REGION`→`IntegrationFirewallPolicyDestinationRegionFilterDto`, `SITE_TO_SITE_VPN_TUNNEL`→`IntegrationFirewallPolicyDestinationSiteToSiteVpnTunnelFilterDto`, `VPN_SERVER`→`IntegrationFirewallPolicyDestinationVpnServerFilterDto` (ver openapi.json)_
    - `type` **(obrigatório)**: `string`
  - `zoneId` **(obrigatório)**: `string` (uuid) - ID of the firewall zone to which the matched traffic is destined.
- `enabled` **(obrigatório)**: `boolean`
- `ipProtocolScope` **(obrigatório)**: Defines rules for matching by IP version and protocol.
  - _variantes por `ipVersion`: `IPV4`→`IntegrationFirewallPolicyIpv4ProtocolScopeDto`, `IPV4_AND_IPV6`→`IntegrationFirewallPolicyIpv4AndIpv6ProtocolScopeDto`, `IPV6`→`IntegrationFirewallPolicyIpv6ProtocolScopeDto` (ver openapi.json)_
  - `ipVersion` **(obrigatório)**: `string`
- `ipsecFilter`: `string` enum: MATCH_ENCRYPTED, MATCH_NOT_ENCRYPTED - Match on traffic encrypted, or not encrypted by IPsec. If null, matches all traffic.
- `loggingEnabled` **(obrigatório)**: `boolean` - Generate syslog entries when traffic is matched. Such entries are sent to a remote syslog server.
- `name` **(obrigatório)**: `string` ex: `My firewall policy`
- `schedule`: Defines date and time when the entity is active. If null, the entity is always active.
  - _variantes por `mode`: `CUSTOM`→`IntegrationFirewallScheduleCustomDto`, `EVERY_DAY`→`IntegrationFirewallScheduleEveryDayDto`, `EVERY_WEEK`→`IntegrationFirewallScheduleEveryWeekDto`, `ONE_TIME_ONLY`→`IntegrationFirewallScheduleOneTimeOnlyDto` (ver openapi.json)_
  - `mode` **(obrigatório)**: `string`
- `source` **(obrigatório)**: `object`
  - `trafficFilter`
    - _variantes por `type`: `IPV6_IID`→`IntegrationFirewallPolicySourceIpv6IidFilterDto`, `IP_ADDRESS`→`IntegrationFirewallPolicySourceIpAddressFilterDto`, `MAC_ADDRESS`→`IntegrationFirewallPolicySourceMacAddressFilterDto`, `NETWORK`→`IntegrationFirewallPolicySourceNetworkFilterDto`, `PORT`→`IntegrationFirewallPolicySourcePortFilterDto`, `REGION`→`IntegrationFirewallPolicySourceRegionFilterDto`, `SITE_TO_SITE_VPN_TUNNEL`→`IntegrationFirewallPolicySourceSiteToSiteVpnTunnelFilterDto`, `VPN_SERVER`→`IntegrationFirewallPolicySourceVpnServerFilterDto` (ver openapi.json)_
    - `type` **(obrigatório)**: `string`
  - `zoneId` **(obrigatório)**: `string` (uuid) - ID of the firewall zone from which the matched traffic originates.

**Resposta 201** - Created

- `action` **(obrigatório)**: Defines action for matched traffic.
  - _variantes por `type`: `ALLOW`→`IntegrationFirewallPolicyActionAllowDto`, `BLOCK`→`IntegrationFirewallPolicyActionBlockDto`, `REJECT`→`IntegrationFirewallPolicyActionRejectDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `connectionStateFilter`: `array` - Match on firewall connection state. If null, matches all connection states.
  - _array de_ `string`:
    - `string` enum: NEW, INVALID, ESTABLISHED, RELATED
- `description`: `string` ex: `A description for my firewall policy`
- `destination` **(obrigatório)**: `object`
  - `trafficFilter`
    - _variantes por `type`: `APPLICATION`→`IntegrationFirewallPolicyDestinationApplicationFilterDto`, `APPLICATION_CATEGORY`→`IntegrationFirewallPolicyDestinationApplicationCategoryFilterDto`, `DOMAIN`→`IntegrationFirewallPolicyDestinationDomainFilterDto`, `IPV6_IID`→`IntegrationFirewallPolicyDestinationIpv6IidFilterDto`, `IP_ADDRESS`→`IntegrationFirewallPolicyDestinationIpAddressFilterDto`, `NETWORK`→`IntegrationFirewallPolicyDestinationNetworkFilterDto`, `PORT`→`IntegrationFirewallPolicyDestinationPortFilterDto`, `REGION`→`IntegrationFirewallPolicyDestinationRegionFilterDto`, `SITE_TO_SITE_VPN_TUNNEL`→`IntegrationFirewallPolicyDestinationSiteToSiteVpnTunnelFilterDto`, `VPN_SERVER`→`IntegrationFirewallPolicyDestinationVpnServerFilterDto` (ver openapi.json)_
    - `type` **(obrigatório)**: `string`
  - `zoneId` **(obrigatório)**: `string` (uuid) - ID of the firewall zone to which the matched traffic is destined.
- `enabled` **(obrigatório)**: `boolean`
- `id` **(obrigatório)**: `string` (uuid)
- `index` **(obrigatório)**: `integer` (int32)
- `ipProtocolScope` **(obrigatório)**: Defines rules for matching by IP version and protocol.
  - _variantes por `ipVersion`: `IPV4`→`IntegrationFirewallPolicyIpv4ProtocolScopeDto`, `IPV4_AND_IPV6`→`IntegrationFirewallPolicyIpv4AndIpv6ProtocolScopeDto`, `IPV6`→`IntegrationFirewallPolicyIpv6ProtocolScopeDto` (ver openapi.json)_
  - `ipVersion` **(obrigatório)**: `string`
- `ipsecFilter`: `string` enum: MATCH_ENCRYPTED, MATCH_NOT_ENCRYPTED - Match on traffic encrypted, or not encrypted by IPsec. If null, matches all traffic.
- `loggingEnabled` **(obrigatório)**: `boolean` - Generate syslog entries when traffic is matched. Such entries are sent to a remote syslog server.
- `metadata` **(obrigatório)**
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `name` **(obrigatório)**: `string` ex: `My firewall policy`
- `schedule`: Defines date and time when the entity is active. If null, the entity is always active.
  - _variantes por `mode`: `CUSTOM`→`IntegrationFirewallScheduleCustomDto`, `EVERY_DAY`→`IntegrationFirewallScheduleEveryDayDto`, `EVERY_WEEK`→`IntegrationFirewallScheduleEveryWeekDto`, `ONE_TIME_ONLY`→`IntegrationFirewallScheduleOneTimeOnlyDto` (ver openapi.json)_
  - `mode` **(obrigatório)**: `string`
- `source` **(obrigatório)**: `object`
  - `trafficFilter`
    - _variantes por `type`: `IPV6_IID`→`IntegrationFirewallPolicySourceIpv6IidFilterDto`, `IP_ADDRESS`→`IntegrationFirewallPolicySourceIpAddressFilterDto`, `MAC_ADDRESS`→`IntegrationFirewallPolicySourceMacAddressFilterDto`, `NETWORK`→`IntegrationFirewallPolicySourceNetworkFilterDto`, `PORT`→`IntegrationFirewallPolicySourcePortFilterDto`, `REGION`→`IntegrationFirewallPolicySourceRegionFilterDto`, `SITE_TO_SITE_VPN_TUNNEL`→`IntegrationFirewallPolicySourceSiteToSiteVpnTunnelFilterDto`, `VPN_SERVER`→`IntegrationFirewallPolicySourceVpnServerFilterDto` (ver openapi.json)_
    - `type` **(obrigatório)**: `string`
  - `zoneId` **(obrigatório)**: `string` (uuid) - ID of the firewall zone from which the matched traffic originates.

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/firewall/policies" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/firewall/policies" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get User-Defined Firewall Policy Ordering

`GET /v1/sites/{siteId}/firewall/policies/ordering`  ·  operationId: `getFirewallPolicyOrdering`

Retrieve user-defined firewall policy ordering for a specific source/destination zone pair.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `sourceFirewallZoneId` | query | sim | string (uuid) |  |
| `destinationFirewallZoneId` | query | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `orderedFirewallPolicyIds` **(obrigatório)**: `object`
  - `afterSystemDefined` **(obrigatório)**: `array`
    - _array de_ `string`:
      - `string` (uuid)
  - `beforeSystemDefined` **(obrigatório)**: `array`
    - _array de_ `string`:
      - `string` (uuid)

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/firewall/policies/ordering" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/firewall/policies/ordering" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Reorder User-Defined Firewall Policies

`PUT /v1/sites/{siteId}/firewall/policies/ordering`  ·  operationId: `updateFirewallPolicyOrdering`

Reorder user-defined firewall policies for a specific source/destination zone pair.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `sourceFirewallZoneId` | query | sim | string (uuid) |  |
| `destinationFirewallZoneId` | query | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- `orderedFirewallPolicyIds` **(obrigatório)**: `object`
  - `afterSystemDefined` **(obrigatório)**: `array`
    - _array de_ `string`:
      - `string` (uuid)
  - `beforeSystemDefined` **(obrigatório)**: `array`
    - _array de_ `string`:
      - `string` (uuid)

**Resposta 200** - OK

- `orderedFirewallPolicyIds` **(obrigatório)**: `object`
  - `afterSystemDefined` **(obrigatório)**: `array`
    - _array de_ `string`:
      - `string` (uuid)
  - `beforeSystemDefined` **(obrigatório)**: `array`
    - _array de_ `string`:
      - `string` (uuid)

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PUT "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/firewall/policies/ordering" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PUT "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/firewall/policies/ordering" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get Firewall Policy

`GET /v1/sites/{siteId}/firewall/policies/{firewallPolicyId}`  ·  operationId: `getFirewallPolicy`

Retrieve specific firewall policy.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `firewallPolicyId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `action` **(obrigatório)**: Defines action for matched traffic.
  - _variantes por `type`: `ALLOW`→`IntegrationFirewallPolicyActionAllowDto`, `BLOCK`→`IntegrationFirewallPolicyActionBlockDto`, `REJECT`→`IntegrationFirewallPolicyActionRejectDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `connectionStateFilter`: `array` - Match on firewall connection state. If null, matches all connection states.
  - _array de_ `string`:
    - `string` enum: NEW, INVALID, ESTABLISHED, RELATED
- `description`: `string` ex: `A description for my firewall policy`
- `destination` **(obrigatório)**: `object`
  - `trafficFilter`
    - _variantes por `type`: `APPLICATION`→`IntegrationFirewallPolicyDestinationApplicationFilterDto`, `APPLICATION_CATEGORY`→`IntegrationFirewallPolicyDestinationApplicationCategoryFilterDto`, `DOMAIN`→`IntegrationFirewallPolicyDestinationDomainFilterDto`, `IPV6_IID`→`IntegrationFirewallPolicyDestinationIpv6IidFilterDto`, `IP_ADDRESS`→`IntegrationFirewallPolicyDestinationIpAddressFilterDto`, `NETWORK`→`IntegrationFirewallPolicyDestinationNetworkFilterDto`, `PORT`→`IntegrationFirewallPolicyDestinationPortFilterDto`, `REGION`→`IntegrationFirewallPolicyDestinationRegionFilterDto`, `SITE_TO_SITE_VPN_TUNNEL`→`IntegrationFirewallPolicyDestinationSiteToSiteVpnTunnelFilterDto`, `VPN_SERVER`→`IntegrationFirewallPolicyDestinationVpnServerFilterDto` (ver openapi.json)_
    - `type` **(obrigatório)**: `string`
  - `zoneId` **(obrigatório)**: `string` (uuid) - ID of the firewall zone to which the matched traffic is destined.
- `enabled` **(obrigatório)**: `boolean`
- `id` **(obrigatório)**: `string` (uuid)
- `index` **(obrigatório)**: `integer` (int32)
- `ipProtocolScope` **(obrigatório)**: Defines rules for matching by IP version and protocol.
  - _variantes por `ipVersion`: `IPV4`→`IntegrationFirewallPolicyIpv4ProtocolScopeDto`, `IPV4_AND_IPV6`→`IntegrationFirewallPolicyIpv4AndIpv6ProtocolScopeDto`, `IPV6`→`IntegrationFirewallPolicyIpv6ProtocolScopeDto` (ver openapi.json)_
  - `ipVersion` **(obrigatório)**: `string`
- `ipsecFilter`: `string` enum: MATCH_ENCRYPTED, MATCH_NOT_ENCRYPTED - Match on traffic encrypted, or not encrypted by IPsec. If null, matches all traffic.
- `loggingEnabled` **(obrigatório)**: `boolean` - Generate syslog entries when traffic is matched. Such entries are sent to a remote syslog server.
- `metadata` **(obrigatório)**
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `name` **(obrigatório)**: `string` ex: `My firewall policy`
- `schedule`: Defines date and time when the entity is active. If null, the entity is always active.
  - _variantes por `mode`: `CUSTOM`→`IntegrationFirewallScheduleCustomDto`, `EVERY_DAY`→`IntegrationFirewallScheduleEveryDayDto`, `EVERY_WEEK`→`IntegrationFirewallScheduleEveryWeekDto`, `ONE_TIME_ONLY`→`IntegrationFirewallScheduleOneTimeOnlyDto` (ver openapi.json)_
  - `mode` **(obrigatório)**: `string`
- `source` **(obrigatório)**: `object`
  - `trafficFilter`
    - _variantes por `type`: `IPV6_IID`→`IntegrationFirewallPolicySourceIpv6IidFilterDto`, `IP_ADDRESS`→`IntegrationFirewallPolicySourceIpAddressFilterDto`, `MAC_ADDRESS`→`IntegrationFirewallPolicySourceMacAddressFilterDto`, `NETWORK`→`IntegrationFirewallPolicySourceNetworkFilterDto`, `PORT`→`IntegrationFirewallPolicySourcePortFilterDto`, `REGION`→`IntegrationFirewallPolicySourceRegionFilterDto`, `SITE_TO_SITE_VPN_TUNNEL`→`IntegrationFirewallPolicySourceSiteToSiteVpnTunnelFilterDto`, `VPN_SERVER`→`IntegrationFirewallPolicySourceVpnServerFilterDto` (ver openapi.json)_
    - `type` **(obrigatório)**: `string`
  - `zoneId` **(obrigatório)**: `string` (uuid) - ID of the firewall zone from which the matched traffic originates.

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/firewall/policies/{firewallPolicyId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/firewall/policies/{firewallPolicyId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Update Firewall Policy

`PUT /v1/sites/{siteId}/firewall/policies/{firewallPolicyId}`  ·  operationId: `updateFirewallPolicy`

Update an existing firewall policy on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `firewallPolicyId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- `action` **(obrigatório)**: Defines action for matched traffic.
  - _variantes por `type`: `ALLOW`→`IntegrationFirewallPolicyActionAllowDto`, `BLOCK`→`IntegrationFirewallPolicyActionBlockDto`, `REJECT`→`IntegrationFirewallPolicyActionRejectDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `connectionStateFilter`: `array` - Match on firewall connection state. If null, matches all connection states.
  - _array de_ `string`:
    - `string` enum: NEW, INVALID, ESTABLISHED, RELATED
- `description`: `string` ex: `A description for my firewall policy`
- `destination` **(obrigatório)**: `object`
  - `trafficFilter`
    - _variantes por `type`: `APPLICATION`→`IntegrationFirewallPolicyDestinationApplicationFilterDto`, `APPLICATION_CATEGORY`→`IntegrationFirewallPolicyDestinationApplicationCategoryFilterDto`, `DOMAIN`→`IntegrationFirewallPolicyDestinationDomainFilterDto`, `IPV6_IID`→`IntegrationFirewallPolicyDestinationIpv6IidFilterDto`, `IP_ADDRESS`→`IntegrationFirewallPolicyDestinationIpAddressFilterDto`, `NETWORK`→`IntegrationFirewallPolicyDestinationNetworkFilterDto`, `PORT`→`IntegrationFirewallPolicyDestinationPortFilterDto`, `REGION`→`IntegrationFirewallPolicyDestinationRegionFilterDto`, `SITE_TO_SITE_VPN_TUNNEL`→`IntegrationFirewallPolicyDestinationSiteToSiteVpnTunnelFilterDto`, `VPN_SERVER`→`IntegrationFirewallPolicyDestinationVpnServerFilterDto` (ver openapi.json)_
    - `type` **(obrigatório)**: `string`
  - `zoneId` **(obrigatório)**: `string` (uuid) - ID of the firewall zone to which the matched traffic is destined.
- `enabled` **(obrigatório)**: `boolean`
- `ipProtocolScope` **(obrigatório)**: Defines rules for matching by IP version and protocol.
  - _variantes por `ipVersion`: `IPV4`→`IntegrationFirewallPolicyIpv4ProtocolScopeDto`, `IPV4_AND_IPV6`→`IntegrationFirewallPolicyIpv4AndIpv6ProtocolScopeDto`, `IPV6`→`IntegrationFirewallPolicyIpv6ProtocolScopeDto` (ver openapi.json)_
  - `ipVersion` **(obrigatório)**: `string`
- `ipsecFilter`: `string` enum: MATCH_ENCRYPTED, MATCH_NOT_ENCRYPTED - Match on traffic encrypted, or not encrypted by IPsec. If null, matches all traffic.
- `loggingEnabled` **(obrigatório)**: `boolean` - Generate syslog entries when traffic is matched. Such entries are sent to a remote syslog server.
- `name` **(obrigatório)**: `string` ex: `My firewall policy`
- `schedule`: Defines date and time when the entity is active. If null, the entity is always active.
  - _variantes por `mode`: `CUSTOM`→`IntegrationFirewallScheduleCustomDto`, `EVERY_DAY`→`IntegrationFirewallScheduleEveryDayDto`, `EVERY_WEEK`→`IntegrationFirewallScheduleEveryWeekDto`, `ONE_TIME_ONLY`→`IntegrationFirewallScheduleOneTimeOnlyDto` (ver openapi.json)_
  - `mode` **(obrigatório)**: `string`
- `source` **(obrigatório)**: `object`
  - `trafficFilter`
    - _variantes por `type`: `IPV6_IID`→`IntegrationFirewallPolicySourceIpv6IidFilterDto`, `IP_ADDRESS`→`IntegrationFirewallPolicySourceIpAddressFilterDto`, `MAC_ADDRESS`→`IntegrationFirewallPolicySourceMacAddressFilterDto`, `NETWORK`→`IntegrationFirewallPolicySourceNetworkFilterDto`, `PORT`→`IntegrationFirewallPolicySourcePortFilterDto`, `REGION`→`IntegrationFirewallPolicySourceRegionFilterDto`, `SITE_TO_SITE_VPN_TUNNEL`→`IntegrationFirewallPolicySourceSiteToSiteVpnTunnelFilterDto`, `VPN_SERVER`→`IntegrationFirewallPolicySourceVpnServerFilterDto` (ver openapi.json)_
    - `type` **(obrigatório)**: `string`
  - `zoneId` **(obrigatório)**: `string` (uuid) - ID of the firewall zone from which the matched traffic originates.

**Resposta 200** - OK

- `action` **(obrigatório)**: Defines action for matched traffic.
  - _variantes por `type`: `ALLOW`→`IntegrationFirewallPolicyActionAllowDto`, `BLOCK`→`IntegrationFirewallPolicyActionBlockDto`, `REJECT`→`IntegrationFirewallPolicyActionRejectDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `connectionStateFilter`: `array` - Match on firewall connection state. If null, matches all connection states.
  - _array de_ `string`:
    - `string` enum: NEW, INVALID, ESTABLISHED, RELATED
- `description`: `string` ex: `A description for my firewall policy`
- `destination` **(obrigatório)**: `object`
  - `trafficFilter`
    - _variantes por `type`: `APPLICATION`→`IntegrationFirewallPolicyDestinationApplicationFilterDto`, `APPLICATION_CATEGORY`→`IntegrationFirewallPolicyDestinationApplicationCategoryFilterDto`, `DOMAIN`→`IntegrationFirewallPolicyDestinationDomainFilterDto`, `IPV6_IID`→`IntegrationFirewallPolicyDestinationIpv6IidFilterDto`, `IP_ADDRESS`→`IntegrationFirewallPolicyDestinationIpAddressFilterDto`, `NETWORK`→`IntegrationFirewallPolicyDestinationNetworkFilterDto`, `PORT`→`IntegrationFirewallPolicyDestinationPortFilterDto`, `REGION`→`IntegrationFirewallPolicyDestinationRegionFilterDto`, `SITE_TO_SITE_VPN_TUNNEL`→`IntegrationFirewallPolicyDestinationSiteToSiteVpnTunnelFilterDto`, `VPN_SERVER`→`IntegrationFirewallPolicyDestinationVpnServerFilterDto` (ver openapi.json)_
    - `type` **(obrigatório)**: `string`
  - `zoneId` **(obrigatório)**: `string` (uuid) - ID of the firewall zone to which the matched traffic is destined.
- `enabled` **(obrigatório)**: `boolean`
- `id` **(obrigatório)**: `string` (uuid)
- `index` **(obrigatório)**: `integer` (int32)
- `ipProtocolScope` **(obrigatório)**: Defines rules for matching by IP version and protocol.
  - _variantes por `ipVersion`: `IPV4`→`IntegrationFirewallPolicyIpv4ProtocolScopeDto`, `IPV4_AND_IPV6`→`IntegrationFirewallPolicyIpv4AndIpv6ProtocolScopeDto`, `IPV6`→`IntegrationFirewallPolicyIpv6ProtocolScopeDto` (ver openapi.json)_
  - `ipVersion` **(obrigatório)**: `string`
- `ipsecFilter`: `string` enum: MATCH_ENCRYPTED, MATCH_NOT_ENCRYPTED - Match on traffic encrypted, or not encrypted by IPsec. If null, matches all traffic.
- `loggingEnabled` **(obrigatório)**: `boolean` - Generate syslog entries when traffic is matched. Such entries are sent to a remote syslog server.
- `metadata` **(obrigatório)**
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `name` **(obrigatório)**: `string` ex: `My firewall policy`
- `schedule`: Defines date and time when the entity is active. If null, the entity is always active.
  - _variantes por `mode`: `CUSTOM`→`IntegrationFirewallScheduleCustomDto`, `EVERY_DAY`→`IntegrationFirewallScheduleEveryDayDto`, `EVERY_WEEK`→`IntegrationFirewallScheduleEveryWeekDto`, `ONE_TIME_ONLY`→`IntegrationFirewallScheduleOneTimeOnlyDto` (ver openapi.json)_
  - `mode` **(obrigatório)**: `string`
- `source` **(obrigatório)**: `object`
  - `trafficFilter`
    - _variantes por `type`: `IPV6_IID`→`IntegrationFirewallPolicySourceIpv6IidFilterDto`, `IP_ADDRESS`→`IntegrationFirewallPolicySourceIpAddressFilterDto`, `MAC_ADDRESS`→`IntegrationFirewallPolicySourceMacAddressFilterDto`, `NETWORK`→`IntegrationFirewallPolicySourceNetworkFilterDto`, `PORT`→`IntegrationFirewallPolicySourcePortFilterDto`, `REGION`→`IntegrationFirewallPolicySourceRegionFilterDto`, `SITE_TO_SITE_VPN_TUNNEL`→`IntegrationFirewallPolicySourceSiteToSiteVpnTunnelFilterDto`, `VPN_SERVER`→`IntegrationFirewallPolicySourceVpnServerFilterDto` (ver openapi.json)_
    - `type` **(obrigatório)**: `string`
  - `zoneId` **(obrigatório)**: `string` (uuid) - ID of the firewall zone from which the matched traffic originates.

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PUT "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/firewall/policies/{firewallPolicyId}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PUT "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/firewall/policies/{firewallPolicyId}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Delete Firewall Policy

`DELETE /v1/sites/{siteId}/firewall/policies/{firewallPolicyId}`  ·  operationId: `deleteFirewallPolicy`

Delete an existing firewall policy on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `firewallPolicyId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X DELETE "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/firewall/policies/{firewallPolicyId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X DELETE "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/firewall/policies/{firewallPolicyId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Patch Firewall Policy

`PATCH /v1/sites/{siteId}/firewall/policies/{firewallPolicyId}`  ·  operationId: `patchFirewallPolicy`

Patch an existing firewall policy on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `firewallPolicyId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- `loggingEnabled`: `boolean`

**Resposta 200** - OK

- `action` **(obrigatório)**: Defines action for matched traffic.
  - _variantes por `type`: `ALLOW`→`IntegrationFirewallPolicyActionAllowDto`, `BLOCK`→`IntegrationFirewallPolicyActionBlockDto`, `REJECT`→`IntegrationFirewallPolicyActionRejectDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `connectionStateFilter`: `array` - Match on firewall connection state. If null, matches all connection states.
  - _array de_ `string`:
    - `string` enum: NEW, INVALID, ESTABLISHED, RELATED
- `description`: `string` ex: `A description for my firewall policy`
- `destination` **(obrigatório)**: `object`
  - `trafficFilter`
    - _variantes por `type`: `APPLICATION`→`IntegrationFirewallPolicyDestinationApplicationFilterDto`, `APPLICATION_CATEGORY`→`IntegrationFirewallPolicyDestinationApplicationCategoryFilterDto`, `DOMAIN`→`IntegrationFirewallPolicyDestinationDomainFilterDto`, `IPV6_IID`→`IntegrationFirewallPolicyDestinationIpv6IidFilterDto`, `IP_ADDRESS`→`IntegrationFirewallPolicyDestinationIpAddressFilterDto`, `NETWORK`→`IntegrationFirewallPolicyDestinationNetworkFilterDto`, `PORT`→`IntegrationFirewallPolicyDestinationPortFilterDto`, `REGION`→`IntegrationFirewallPolicyDestinationRegionFilterDto`, `SITE_TO_SITE_VPN_TUNNEL`→`IntegrationFirewallPolicyDestinationSiteToSiteVpnTunnelFilterDto`, `VPN_SERVER`→`IntegrationFirewallPolicyDestinationVpnServerFilterDto` (ver openapi.json)_
    - `type` **(obrigatório)**: `string`
  - `zoneId` **(obrigatório)**: `string` (uuid) - ID of the firewall zone to which the matched traffic is destined.
- `enabled` **(obrigatório)**: `boolean`
- `id` **(obrigatório)**: `string` (uuid)
- `index` **(obrigatório)**: `integer` (int32)
- `ipProtocolScope` **(obrigatório)**: Defines rules for matching by IP version and protocol.
  - _variantes por `ipVersion`: `IPV4`→`IntegrationFirewallPolicyIpv4ProtocolScopeDto`, `IPV4_AND_IPV6`→`IntegrationFirewallPolicyIpv4AndIpv6ProtocolScopeDto`, `IPV6`→`IntegrationFirewallPolicyIpv6ProtocolScopeDto` (ver openapi.json)_
  - `ipVersion` **(obrigatório)**: `string`
- `ipsecFilter`: `string` enum: MATCH_ENCRYPTED, MATCH_NOT_ENCRYPTED - Match on traffic encrypted, or not encrypted by IPsec. If null, matches all traffic.
- `loggingEnabled` **(obrigatório)**: `boolean` - Generate syslog entries when traffic is matched. Such entries are sent to a remote syslog server.
- `metadata` **(obrigatório)**
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `name` **(obrigatório)**: `string` ex: `My firewall policy`
- `schedule`: Defines date and time when the entity is active. If null, the entity is always active.
  - _variantes por `mode`: `CUSTOM`→`IntegrationFirewallScheduleCustomDto`, `EVERY_DAY`→`IntegrationFirewallScheduleEveryDayDto`, `EVERY_WEEK`→`IntegrationFirewallScheduleEveryWeekDto`, `ONE_TIME_ONLY`→`IntegrationFirewallScheduleOneTimeOnlyDto` (ver openapi.json)_
  - `mode` **(obrigatório)**: `string`
- `source` **(obrigatório)**: `object`
  - `trafficFilter`
    - _variantes por `type`: `IPV6_IID`→`IntegrationFirewallPolicySourceIpv6IidFilterDto`, `IP_ADDRESS`→`IntegrationFirewallPolicySourceIpAddressFilterDto`, `MAC_ADDRESS`→`IntegrationFirewallPolicySourceMacAddressFilterDto`, `NETWORK`→`IntegrationFirewallPolicySourceNetworkFilterDto`, `PORT`→`IntegrationFirewallPolicySourcePortFilterDto`, `REGION`→`IntegrationFirewallPolicySourceRegionFilterDto`, `SITE_TO_SITE_VPN_TUNNEL`→`IntegrationFirewallPolicySourceSiteToSiteVpnTunnelFilterDto`, `VPN_SERVER`→`IntegrationFirewallPolicySourceVpnServerFilterDto` (ver openapi.json)_
    - `type` **(obrigatório)**: `string`
  - `zoneId` **(obrigatório)**: `string` (uuid) - ID of the firewall zone from which the matched traffic originates.

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PATCH "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/firewall/policies/{firewallPolicyId}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PATCH "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/firewall/policies/{firewallPolicyId}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### List Firewall Zones

`GET /v1/sites/{siteId}/firewall/zones`  ·  operationId: `getFirewallZones`

Retrieve a list of all firewall zones on a site.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`id`|`UUID`|`eq` `ne` `in` `notIn`|
|`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
|`metadata.origin`|`STRING`|`eq` `ne` `in` `notIn`|
|`metadata.configurable`|`BOOLEAN`|`eq` `ne` `isNull` `isNotNull`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `id` **(obrigatório)**: `string` (uuid) ex: `ffcdb32c-6278-4364-8947-df4f77118df8`
    - `metadata` **(obrigatório)**: System-defined configurable zones support configuring only attached networks
      - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
    - `name` **(obrigatório)**: `string` ex: `Hotspot|My custom zone` - Name of a firewall zone
    - `networkIds` **(obrigatório)**: `array` - List of Network IDs
      - _array de_ `string`:
        - `string` (uuid) ex: `dfb21062-8ea0-4dca-b1d8-1eb3da00e58b`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/firewall/zones" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/firewall/zones" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Create Custom Firewall Zone

`POST /v1/sites/{siteId}/firewall/zones`  ·  operationId: `createFirewallZone`

Create a new custom firewall zone on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- `name` **(obrigatório)**: `string` ex: `Hotspot|My custom zone` - Name of a firewall zone
- `networkIds` **(obrigatório)**: `array` - List of Network IDs
  - _array de_ `string`:
    - `string` (uuid) ex: `dfb21062-8ea0-4dca-b1d8-1eb3da00e58b`

**Resposta 201** - Created

- `id` **(obrigatório)**: `string` (uuid) ex: `ffcdb32c-6278-4364-8947-df4f77118df8`
- `metadata` **(obrigatório)**: System-defined configurable zones support configuring only attached networks
  - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `name` **(obrigatório)**: `string` ex: `Hotspot|My custom zone` - Name of a firewall zone
- `networkIds` **(obrigatório)**: `array` - List of Network IDs
  - _array de_ `string`:
    - `string` (uuid) ex: `dfb21062-8ea0-4dca-b1d8-1eb3da00e58b`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/firewall/zones" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/firewall/zones" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get Firewall Zone

`GET /v1/sites/{siteId}/firewall/zones/{firewallZoneId}`  ·  operationId: `getFirewallZone`

Get a firewall zone on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `firewallZoneId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `id` **(obrigatório)**: `string` (uuid) ex: `ffcdb32c-6278-4364-8947-df4f77118df8`
- `metadata` **(obrigatório)**: System-defined configurable zones support configuring only attached networks
  - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `name` **(obrigatório)**: `string` ex: `Hotspot|My custom zone` - Name of a firewall zone
- `networkIds` **(obrigatório)**: `array` - List of Network IDs
  - _array de_ `string`:
    - `string` (uuid) ex: `dfb21062-8ea0-4dca-b1d8-1eb3da00e58b`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/firewall/zones/{firewallZoneId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/firewall/zones/{firewallZoneId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Update Firewall Zone

`PUT /v1/sites/{siteId}/firewall/zones/{firewallZoneId}`  ·  operationId: `updateFirewallZone`

Update a firewall zone on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `firewallZoneId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- `name` **(obrigatório)**: `string` ex: `Hotspot|My custom zone` - Name of a firewall zone
- `networkIds` **(obrigatório)**: `array` - List of Network IDs
  - _array de_ `string`:
    - `string` (uuid) ex: `dfb21062-8ea0-4dca-b1d8-1eb3da00e58b`

**Resposta 200** - OK

- `id` **(obrigatório)**: `string` (uuid) ex: `ffcdb32c-6278-4364-8947-df4f77118df8`
- `metadata` **(obrigatório)**: System-defined configurable zones support configuring only attached networks
  - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `name` **(obrigatório)**: `string` ex: `Hotspot|My custom zone` - Name of a firewall zone
- `networkIds` **(obrigatório)**: `array` - List of Network IDs
  - _array de_ `string`:
    - `string` (uuid) ex: `dfb21062-8ea0-4dca-b1d8-1eb3da00e58b`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PUT "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/firewall/zones/{firewallZoneId}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PUT "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/firewall/zones/{firewallZoneId}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Delete Custom Firewall Zone

`DELETE /v1/sites/{siteId}/firewall/zones/{firewallZoneId}`  ·  operationId: `deleteFirewallZone`

Delete a custom firewall zone from a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `firewallZoneId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X DELETE "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/firewall/zones/{firewallZoneId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X DELETE "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/firewall/zones/{firewallZoneId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Access Control (ACL Rules)

Endpoints for creating, listing, and managing ACL (Access Control List) rule
that enforce traffic filtering across devices and networks.


### List ACL Rules

`GET /v1/sites/{siteId}/acl-rules`  ·  operationId: `getAclRulePage`

$1e

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - _variantes por `type`: `IPV4`→`IntegrationIpAclRuleDto`, `MAC`→`IntegrationMacAclRuleDto` (ver openapi.json)_
    - `action` **(obrigatório)**: `string` enum: ALLOW, BLOCK ex: `ALLOW|BLOCK` - ACL rule action
    - `description`: `string` - ACL rule description
    - `destinationFilter`: Traffic destination filter
    - `enabled` **(obrigatório)**: `boolean` ex: `True`
    - `enforcingDeviceFilter`: IDs of the Switch-capable devices used to enforce the ACL rule. When null, the rule will be provisioned to all switches on the site.
      - _variantes por `type`: `DEVICES`→`IntegrationAclRuleDevicesFilterDto` (ver openapi.json)_
      - `type` **(obrigatório)**: `string`
    - `id` **(obrigatório)**: `string` (uuid)
    - `index` **(obrigatório)**: `integer` (int32) - ACL rule index. Lower index has higher priority
    - `metadata` **(obrigatório)**: Only user-defined rules can be deleted or modified
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
    - `name` **(obrigatório)**: `string` - ACL rule name
    - `sourceFilter`: Traffic source filter
    - `type` **(obrigatório)**: `string`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/acl-rules" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/acl-rules" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Create ACL Rule

`POST /v1/sites/{siteId}/acl-rules`  ·  operationId: `createAclRule`

Create a new user defined ACL rule on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- _variantes por `type`: `IPV4`→`IntegrationIpAclRuleCreateUpdateDto`, `MAC`→`IntegrationMacAclRuleCreateUpdateDto` (ver openapi.json)_
- `action` **(obrigatório)**: `string` enum: ALLOW, BLOCK ex: `ALLOW|BLOCK` - ACL rule action
- `description`: `string` - ACL rule description
- `destinationFilter`: Traffic destination filter
- `enabled` **(obrigatório)**: `boolean` ex: `True`
- `enforcingDeviceFilter`: IDs of the Switch-capable devices used to enforce the ACL rule. When null, the rule will be provisioned to all switches on the site.
  - _variantes por `type`: `DEVICES`→`IntegrationAclRuleDevicesFilterDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `index`: `integer` (int32) - ACL rule index. This property is deprecated and has no effect. Use the dedicated ACL rule reordering endpoint.
- `name` **(obrigatório)**: `string` - ACL rule name
- `sourceFilter`: Traffic source filter
- `type` **(obrigatório)**: `string`

**Resposta 201** - Created

- _variantes por `type`: `IPV4`→`IntegrationIpAclRuleDto`, `MAC`→`IntegrationMacAclRuleDto` (ver openapi.json)_
- `action` **(obrigatório)**: `string` enum: ALLOW, BLOCK ex: `ALLOW|BLOCK` - ACL rule action
- `description`: `string` - ACL rule description
- `destinationFilter`: Traffic destination filter
- `enabled` **(obrigatório)**: `boolean` ex: `True`
- `enforcingDeviceFilter`: IDs of the Switch-capable devices used to enforce the ACL rule. When null, the rule will be provisioned to all switches on the site.
  - _variantes por `type`: `DEVICES`→`IntegrationAclRuleDevicesFilterDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `id` **(obrigatório)**: `string` (uuid)
- `index` **(obrigatório)**: `integer` (int32) - ACL rule index. Lower index has higher priority
- `metadata` **(obrigatório)**: Only user-defined rules can be deleted or modified
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `name` **(obrigatório)**: `string` - ACL rule name
- `sourceFilter`: Traffic source filter
- `type` **(obrigatório)**: `string`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/acl-rules" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/acl-rules" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get User-Defined ACL Rule Ordering

`GET /v1/sites/{siteId}/acl-rules/ordering`  ·  operationId: `getAclRuleOrdering`

Retrieve user-defined ACL rule ordering on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `orderedAclRuleIds` **(obrigatório)**: `array`
  - _array de_ `string`:
    - `string` (uuid)

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/acl-rules/ordering" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/acl-rules/ordering" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Reorder User-Defined ACL Rules

`PUT /v1/sites/{siteId}/acl-rules/ordering`  ·  operationId: `updateAclRuleOrdering`

Reorder user-defined ACL rules on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- `orderedAclRuleIds` **(obrigatório)**: `array`
  - _array de_ `string`:
    - `string` (uuid)

**Resposta 200** - OK

- `orderedAclRuleIds` **(obrigatório)**: `array`
  - _array de_ `string`:
    - `string` (uuid)

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PUT "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/acl-rules/ordering" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PUT "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/acl-rules/ordering" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get ACL Rule

`GET /v1/sites/{siteId}/acl-rules/{aclRuleId}`  ·  operationId: `getAclRule`

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `aclRuleId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- _variantes por `type`: `IPV4`→`IntegrationIpAclRuleDto`, `MAC`→`IntegrationMacAclRuleDto` (ver openapi.json)_
- `action` **(obrigatório)**: `string` enum: ALLOW, BLOCK ex: `ALLOW|BLOCK` - ACL rule action
- `description`: `string` - ACL rule description
- `destinationFilter`: Traffic destination filter
- `enabled` **(obrigatório)**: `boolean` ex: `True`
- `enforcingDeviceFilter`: IDs of the Switch-capable devices used to enforce the ACL rule. When null, the rule will be provisioned to all switches on the site.
  - _variantes por `type`: `DEVICES`→`IntegrationAclRuleDevicesFilterDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `id` **(obrigatório)**: `string` (uuid)
- `index` **(obrigatório)**: `integer` (int32) - ACL rule index. Lower index has higher priority
- `metadata` **(obrigatório)**: Only user-defined rules can be deleted or modified
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `name` **(obrigatório)**: `string` - ACL rule name
- `sourceFilter`: Traffic source filter
- `type` **(obrigatório)**: `string`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/acl-rules/{aclRuleId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/acl-rules/{aclRuleId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Update ACL Rule

`PUT /v1/sites/{siteId}/acl-rules/{aclRuleId}`  ·  operationId: `updateAclRule`

Update an existing user defined ACL rule on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `aclRuleId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- _variantes por `type`: `IPV4`→`IntegrationIpAclRuleCreateUpdateDto`, `MAC`→`IntegrationMacAclRuleCreateUpdateDto` (ver openapi.json)_
- `action` **(obrigatório)**: `string` enum: ALLOW, BLOCK ex: `ALLOW|BLOCK` - ACL rule action
- `description`: `string` - ACL rule description
- `destinationFilter`: Traffic destination filter
- `enabled` **(obrigatório)**: `boolean` ex: `True`
- `enforcingDeviceFilter`: IDs of the Switch-capable devices used to enforce the ACL rule. When null, the rule will be provisioned to all switches on the site.
  - _variantes por `type`: `DEVICES`→`IntegrationAclRuleDevicesFilterDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `index`: `integer` (int32) - ACL rule index. This property is deprecated and has no effect. Use the dedicated ACL rule reordering endpoint.
- `name` **(obrigatório)**: `string` - ACL rule name
- `sourceFilter`: Traffic source filter
- `type` **(obrigatório)**: `string`

**Resposta 200** - OK

- _variantes por `type`: `IPV4`→`IntegrationIpAclRuleDto`, `MAC`→`IntegrationMacAclRuleDto` (ver openapi.json)_
- `action` **(obrigatório)**: `string` enum: ALLOW, BLOCK ex: `ALLOW|BLOCK` - ACL rule action
- `description`: `string` - ACL rule description
- `destinationFilter`: Traffic destination filter
- `enabled` **(obrigatório)**: `boolean` ex: `True`
- `enforcingDeviceFilter`: IDs of the Switch-capable devices used to enforce the ACL rule. When null, the rule will be provisioned to all switches on the site.
  - _variantes por `type`: `DEVICES`→`IntegrationAclRuleDevicesFilterDto` (ver openapi.json)_
  - `type` **(obrigatório)**: `string`
- `id` **(obrigatório)**: `string` (uuid)
- `index` **(obrigatório)**: `integer` (int32) - ACL rule index. Lower index has higher priority
- `metadata` **(obrigatório)**: Only user-defined rules can be deleted or modified
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `name` **(obrigatório)**: `string` - ACL rule name
- `sourceFilter`: Traffic source filter
- `type` **(obrigatório)**: `string`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PUT "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/acl-rules/{aclRuleId}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PUT "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/acl-rules/{aclRuleId}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Delete ACL Rule

`DELETE /v1/sites/{siteId}/acl-rules/{aclRuleId}`  ·  operationId: `deleteAclRule`

Delete an existing user defined ACL rule on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `aclRuleId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X DELETE "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/acl-rules/{aclRuleId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X DELETE "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/acl-rules/{aclRuleId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Switching

Endpoints for managing switching features like Switch Stacking and LAG.


### List LAGs

`GET /v1/sites/{siteId}/switching/lags`  ·  operationId: `getLagPage`

Retrieve a paginated list of all LAGs (Link Aggregation Groups) on a site.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`id`|`UUID`|`eq` `ne` `in` `notIn`|
|`type`|`STRING`|`eq` `ne` `in` `notIn`|
|`switchStackId`|`UUID`|`eq` `ne` `in` `notIn` `isNull` `isNotNull`|
|`mcLagDomainId`|`UUID`|`eq` `ne` `in` `notIn` `isNull` `isNotNull`|
|`members.deviceId`|`SET(UUID)`|`contains` `containsAny` `containsAll` `containsExactly`|
|`members.portIdxs`|`SET(INTEGER)`|`contains` `containsAny` `containsAll` `containsExactly`|
|`metadata.origin`|`STRING`|`eq` `ne` `in` `notIn`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - _variantes por `type`: `LOCAL`→`IntegrationLocalLagGlobalDto`, `MULTI_CHASSIS`→`IntegrationMcLagGlobalDto`, `SWITCH_STACK`→`IntegrationSwitchStackLagGlobalDto` (ver openapi.json)_
    - `id` **(obrigatório)**: `string` (uuid)
    - `members` **(obrigatório)**: `array`
      - _array de_ `object`:
        - `deviceId` **(obrigatório)**: `string` (uuid)
        - `portIdxs` **(obrigatório)**: `array`
          - _array de_ `integer`:
    - `metadata` **(obrigatório)**
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `DERIVED`→`IntegrationDerivedSiteToSiteTunnelMetadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
    - `type` **(obrigatório)**: `string`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/switching/lags" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/switching/lags" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get LAG Details

`GET /v1/sites/{siteId}/switching/lags/{lagId}`  ·  operationId: `getLag`

Retrieve LAG details.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `lagId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- _variantes por `type`: `LOCAL`→`IntegrationLocalLagGlobalDto`, `MULTI_CHASSIS`→`IntegrationMcLagGlobalDto`, `SWITCH_STACK`→`IntegrationSwitchStackLagGlobalDto` (ver openapi.json)_
- `id` **(obrigatório)**: `string` (uuid)
- `members` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `deviceId` **(obrigatório)**: `string` (uuid)
    - `portIdxs` **(obrigatório)**: `array`
      - _array de_ `integer`:
        - `integer` (int32)
- `metadata` **(obrigatório)**
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `DERIVED`→`IntegrationDerivedSiteToSiteTunnelMetadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `type` **(obrigatório)**: `string`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/switching/lags/{lagId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/switching/lags/{lagId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### List MC-LAG Domains

`GET /v1/sites/{siteId}/switching/mc-lag-domains`  ·  operationId: `getMcLagDomainPage`

Retrieve a paginated list of all MC-LAG Domains on a site.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`id`|`UUID`|`eq` `ne` `in` `notIn`|
|`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
|`peers.deviceId`|`SET(UUID)`|`contains` `containsAny` `containsAll` `containsExactly`|
|`metadata.origin`|`STRING`|`eq` `ne` `in` `notIn`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `id` **(obrigatório)**: `string` (uuid)
    - `lags` **(obrigatório)**: `array`
      - _array de_ `object`:
        - `id` **(obrigatório)**: `string` (uuid)
        - `members` **(obrigatório)**: `array`
          - _array de_ `object`:
        - `metadata` **(obrigatório)**
          - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `DERIVED`→`IntegrationDerivedSiteToSiteTunnelMetadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
    - `metadata` **(obrigatório)**
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `DERIVED`→`IntegrationDerivedSiteToSiteTunnelMetadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
    - `name` **(obrigatório)**: `string`
    - `peers` **(obrigatório)**: `array`
      - _array de_ `object`:
        - `deviceId` **(obrigatório)**: `string` (uuid)
        - `linkPortIdxs` **(obrigatório)**: `array`
          - _array de_ `integer`:
        - `role` **(obrigatório)**: `string` enum: TOP, BOTTOM
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/switching/mc-lag-domains" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/switching/mc-lag-domains" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get MC-LAG Domain

`GET /v1/sites/{siteId}/switching/mc-lag-domains/{mcLagDomainId}`  ·  operationId: `getMcLagDomain`

Retrieve MC-LAG Domain details.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `mcLagDomainId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `id` **(obrigatório)**: `string` (uuid)
- `lags` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `id` **(obrigatório)**: `string` (uuid)
    - `members` **(obrigatório)**: `array`
      - _array de_ `object`:
        - `deviceId` **(obrigatório)**: `string` (uuid)
        - `portIdxs` **(obrigatório)**: `array`
          - _array de_ `integer`:
    - `metadata` **(obrigatório)**
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `DERIVED`→`IntegrationDerivedSiteToSiteTunnelMetadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
- `metadata` **(obrigatório)**
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `DERIVED`→`IntegrationDerivedSiteToSiteTunnelMetadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `name` **(obrigatório)**: `string`
- `peers` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `deviceId` **(obrigatório)**: `string` (uuid)
    - `linkPortIdxs` **(obrigatório)**: `array`
      - _array de_ `integer`:
        - `integer` (int32)
    - `role` **(obrigatório)**: `string` enum: TOP, BOTTOM

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/switching/mc-lag-domains/{mcLagDomainId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/switching/mc-lag-domains/{mcLagDomainId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### List Switch Stacks

`GET /v1/sites/{siteId}/switching/switch-stacks`  ·  operationId: `getSwitchStackPage`

Retrieve a paginated list of all Switch Stacks on a site.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`id`|`UUID`|`eq` `ne` `in` `notIn`|
|`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
|`members.deviceId`|`SET(UUID)`|`contains` `containsAny` `containsAll` `containsExactly`|
|`metadata.origin`|`STRING`|`eq` `ne` `in` `notIn`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `id` **(obrigatório)**: `string` (uuid)
    - `lags` **(obrigatório)**: `array`
      - _array de_ `object`:
        - `id` **(obrigatório)**: `string` (uuid)
        - `members` **(obrigatório)**: `array`
          - _array de_ `object`:
        - `metadata` **(obrigatório)**
          - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
          - _variantes por `origin`: `DERIVED`→`IntegrationDerivedSiteToSiteTunnelMetadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
          - `origin` **(obrigatório)**: `string`
    - `members` **(obrigatório)**: `array`
      - _array de_ `object`:
        - `deviceId` **(obrigatório)**: `string` (uuid)
    - `metadata` **(obrigatório)**
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `DERIVED`→`IntegrationDerivedSiteToSiteTunnelMetadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
    - `name` **(obrigatório)**: `string`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/switching/switch-stacks" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/switching/switch-stacks" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get Switch Stack

`GET /v1/sites/{siteId}/switching/switch-stacks/{switchStackId}`  ·  operationId: `getSwitchStack`

Retrieve Switch Stack details.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `switchStackId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `id` **(obrigatório)**: `string` (uuid)
- `lags` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `id` **(obrigatório)**: `string` (uuid)
    - `members` **(obrigatório)**: `array`
      - _array de_ `object`:
        - `deviceId` **(obrigatório)**: `string` (uuid)
        - `portIdxs` **(obrigatório)**: `array`
          - _array de_ `integer`:
    - `metadata` **(obrigatório)**
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `DERIVED`→`IntegrationDerivedSiteToSiteTunnelMetadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
- `members` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `deviceId` **(obrigatório)**: `string` (uuid)
- `metadata` **(obrigatório)**
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `DERIVED`→`IntegrationDerivedSiteToSiteTunnelMetadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `name` **(obrigatório)**: `string`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/switching/switch-stacks/{switchStackId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/switching/switch-stacks/{switchStackId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## DNS Policies

Endpoints for managing DNS Policies within a site.


### List DNS Policies

`GET /v1/sites/{siteId}/dns/policies`  ·  operationId: `getDnsPolicyPage`

$1f

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - _variantes por `type`: `AAAA_RECORD`→`IntegrationDnsAaaaRecordDto`, `A_RECORD`→`IntegrationDnsARecordDto`, `CNAME_RECORD`→`IntegrationDnsCnameRecordDto`, `FORWARD_DOMAIN`→`IntegrationDnsForwardDomainPolicyDto`, `MX_RECORD`→`IntegrationDnsMxRecordDto`, `SRV_RECORD`→`IntegrationDnsSrvRecordDto`, `TXT_RECORD`→`IntegrationDnsTxtRecordDto` (ver openapi.json)_
    - `domain`: `string`
    - `enabled` **(obrigatório)**: `boolean`
    - `id` **(obrigatório)**: `string` (uuid)
    - `metadata` **(obrigatório)**
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
      - _variantes por `origin`: `DERIVED`→`IntegrationDerivedSiteToSiteTunnelMetadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
    - `type` **(obrigatório)**: `string`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/dns/policies" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/dns/policies" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Create DNS Policy

`POST /v1/sites/{siteId}/dns/policies`  ·  operationId: `createDnsPolicy`

Create a new DNS policy on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- _variantes por `type`: `AAAA_RECORD`→`IntegrationDnsAaaaRecordCreateUpdateDto`, `A_RECORD`→`IntegrationDnsARecordCreateUpdateDto`, `CNAME_RECORD`→`IntegrationDnsCnameRecordCreateUpdateDto`, `FORWARD_DOMAIN`→`IntegrationDnsForwardDomainPolicyCreateUpdateDto`, `MX_RECORD`→`IntegrationDnsMxRecordCreateUpdateDto`, `SRV_RECORD`→`IntegrationDnsSrvRecordCreateUpdateDto`, `TXT_RECORD`→`IntegrationDnsTxtRecordCreateUpdateDto` (ver openapi.json)_
- `enabled` **(obrigatório)**: `boolean`
- `type` **(obrigatório)**: `string`

**Resposta 201** - Created

- _variantes por `type`: `AAAA_RECORD`→`IntegrationDnsAaaaRecordDto`, `A_RECORD`→`IntegrationDnsARecordDto`, `CNAME_RECORD`→`IntegrationDnsCnameRecordDto`, `FORWARD_DOMAIN`→`IntegrationDnsForwardDomainPolicyDto`, `MX_RECORD`→`IntegrationDnsMxRecordDto`, `SRV_RECORD`→`IntegrationDnsSrvRecordDto`, `TXT_RECORD`→`IntegrationDnsTxtRecordDto` (ver openapi.json)_
- `domain`: `string`
- `enabled` **(obrigatório)**: `boolean`
- `id` **(obrigatório)**: `string` (uuid)
- `metadata` **(obrigatório)**
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `DERIVED`→`IntegrationDerivedSiteToSiteTunnelMetadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `type` **(obrigatório)**: `string`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/dns/policies" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/dns/policies" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get DNS Policy

`GET /v1/sites/{siteId}/dns/policies/{dnsPolicyId}`  ·  operationId: `getDnsPolicy`

Retrieve specific DNS policy.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `dnsPolicyId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- _variantes por `type`: `AAAA_RECORD`→`IntegrationDnsAaaaRecordDto`, `A_RECORD`→`IntegrationDnsARecordDto`, `CNAME_RECORD`→`IntegrationDnsCnameRecordDto`, `FORWARD_DOMAIN`→`IntegrationDnsForwardDomainPolicyDto`, `MX_RECORD`→`IntegrationDnsMxRecordDto`, `SRV_RECORD`→`IntegrationDnsSrvRecordDto`, `TXT_RECORD`→`IntegrationDnsTxtRecordDto` (ver openapi.json)_
- `domain`: `string`
- `enabled` **(obrigatório)**: `boolean`
- `id` **(obrigatório)**: `string` (uuid)
- `metadata` **(obrigatório)**
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `DERIVED`→`IntegrationDerivedSiteToSiteTunnelMetadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `type` **(obrigatório)**: `string`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/dns/policies/{dnsPolicyId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/dns/policies/{dnsPolicyId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Update DNS Policy

`PUT /v1/sites/{siteId}/dns/policies/{dnsPolicyId}`  ·  operationId: `updateDnsPolicy`

Update an existing DNS policy on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `dnsPolicyId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- _variantes por `type`: `AAAA_RECORD`→`IntegrationDnsAaaaRecordCreateUpdateDto`, `A_RECORD`→`IntegrationDnsARecordCreateUpdateDto`, `CNAME_RECORD`→`IntegrationDnsCnameRecordCreateUpdateDto`, `FORWARD_DOMAIN`→`IntegrationDnsForwardDomainPolicyCreateUpdateDto`, `MX_RECORD`→`IntegrationDnsMxRecordCreateUpdateDto`, `SRV_RECORD`→`IntegrationDnsSrvRecordCreateUpdateDto`, `TXT_RECORD`→`IntegrationDnsTxtRecordCreateUpdateDto` (ver openapi.json)_
- `enabled` **(obrigatório)**: `boolean`
- `type` **(obrigatório)**: `string`

**Resposta 200** - OK

- _variantes por `type`: `AAAA_RECORD`→`IntegrationDnsAaaaRecordDto`, `A_RECORD`→`IntegrationDnsARecordDto`, `CNAME_RECORD`→`IntegrationDnsCnameRecordDto`, `FORWARD_DOMAIN`→`IntegrationDnsForwardDomainPolicyDto`, `MX_RECORD`→`IntegrationDnsMxRecordDto`, `SRV_RECORD`→`IntegrationDnsSrvRecordDto`, `TXT_RECORD`→`IntegrationDnsTxtRecordDto` (ver openapi.json)_
- `domain`: `string`
- `enabled` **(obrigatório)**: `boolean`
- `id` **(obrigatório)**: `string` (uuid)
- `metadata` **(obrigatório)**
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
  - _variantes por `origin`: `DERIVED`→`IntegrationDerivedSiteToSiteTunnelMetadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
  - `origin` **(obrigatório)**: `string`
- `type` **(obrigatório)**: `string`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PUT "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/dns/policies/{dnsPolicyId}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PUT "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/dns/policies/{dnsPolicyId}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Delete DNS Policy

`DELETE /v1/sites/{siteId}/dns/policies/{dnsPolicyId}`  ·  operationId: `deleteDnsPolicy`

Delete an existing DNS policy on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `dnsPolicyId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X DELETE "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/dns/policies/{dnsPolicyId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X DELETE "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/dns/policies/{dnsPolicyId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Traffic Matching Lists

Endpoints for managing port and IP address lists used across firewall policy configurations.


### List Traffic Matching Lists

`GET /v1/sites/{siteId}/traffic-matching-lists`  ·  operationId: `getTrafficMatchingLists`

Retrieve all traffic matching lists on a site.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`id`|`UUID`|`eq` `ne` `in` `notIn`|
|`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - _variantes por `type`: `IPV4_ADDRESSES`→`IntegrationIpV4TrafficMatchingListDto`, `IPV6_ADDRESSES`→`IntegrationIpV6TrafficMatchingListDto`, `PORTS`→`IntegrationPortTrafficMatchingListDto` (ver openapi.json)_
    - `id` **(obrigatório)**: `string` (uuid) ex: `ffcdb32c-6278-4364-8947-df4f77118df8`
    - `name` **(obrigatório)**: `string` ex: `Allowed port list|Protected IP list`
    - `type` **(obrigatório)**: `string`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/traffic-matching-lists" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/traffic-matching-lists" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Create Traffic Matching List

`POST /v1/sites/{siteId}/traffic-matching-lists`  ·  operationId: `createTrafficMatchingList`

Create a new traffic matching list on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- _variantes por `type`: `IPV4_ADDRESSES`→`IntegrationIpV4TrafficMatchingListCreateUpdateDto`, `IPV6_ADDRESSES`→`IntegrationIpV6TrafficMatchingListCreateUpdateDto`, `PORTS`→`IntegrationPortTrafficMatchingListCreateUpdateDto` (ver openapi.json)_
- `name` **(obrigatório)**: `string` ex: `Allowed port list|Protected IP list`
- `type` **(obrigatório)**: `string`

**Resposta 201** - Created

- _variantes por `type`: `IPV4_ADDRESSES`→`IntegrationIpV4TrafficMatchingListDto`, `IPV6_ADDRESSES`→`IntegrationIpV6TrafficMatchingListDto`, `PORTS`→`IntegrationPortTrafficMatchingListDto` (ver openapi.json)_
- `id` **(obrigatório)**: `string` (uuid) ex: `ffcdb32c-6278-4364-8947-df4f77118df8`
- `name` **(obrigatório)**: `string` ex: `Allowed port list|Protected IP list`
- `type` **(obrigatório)**: `string`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/traffic-matching-lists" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/traffic-matching-lists" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get Traffic Matching List

`GET /v1/sites/{siteId}/traffic-matching-lists/{trafficMatchingListId}`  ·  operationId: `getTrafficMatchingList`

Get an exist traffic matching list on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `trafficMatchingListId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- _variantes por `type`: `IPV4_ADDRESSES`→`IntegrationIpV4TrafficMatchingListDto`, `IPV6_ADDRESSES`→`IntegrationIpV6TrafficMatchingListDto`, `PORTS`→`IntegrationPortTrafficMatchingListDto` (ver openapi.json)_
- `id` **(obrigatório)**: `string` (uuid) ex: `ffcdb32c-6278-4364-8947-df4f77118df8`
- `name` **(obrigatório)**: `string` ex: `Allowed port list|Protected IP list`
- `type` **(obrigatório)**: `string`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/traffic-matching-lists/{trafficMatchingListId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/traffic-matching-lists/{trafficMatchingListId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Update Traffic Matching List

`PUT /v1/sites/{siteId}/traffic-matching-lists/{trafficMatchingListId}`  ·  operationId: `updateTrafficMatchingList`

Update an exist traffic matching list on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `trafficMatchingListId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Corpo da requisição** (`application/json`)

- _variantes por `type`: `IPV4_ADDRESSES`→`IntegrationIpV4TrafficMatchingListCreateUpdateDto`, `IPV6_ADDRESSES`→`IntegrationIpV6TrafficMatchingListCreateUpdateDto`, `PORTS`→`IntegrationPortTrafficMatchingListCreateUpdateDto` (ver openapi.json)_
- `name` **(obrigatório)**: `string` ex: `Allowed port list|Protected IP list`
- `type` **(obrigatório)**: `string`

**Resposta 200** - OK

- _variantes por `type`: `IPV4_ADDRESSES`→`IntegrationIpV4TrafficMatchingListDto`, `IPV6_ADDRESSES`→`IntegrationIpV6TrafficMatchingListDto`, `PORTS`→`IntegrationPortTrafficMatchingListDto` (ver openapi.json)_
- `id` **(obrigatório)**: `string` (uuid) ex: `ffcdb32c-6278-4364-8947-df4f77118df8`
- `name` **(obrigatório)**: `string` ex: `Allowed port list|Protected IP list`
- `type` **(obrigatório)**: `string`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PUT "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/traffic-matching-lists/{trafficMatchingListId}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PUT "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/traffic-matching-lists/{trafficMatchingListId}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Delete Traffic Matching List

`DELETE /v1/sites/{siteId}/traffic-matching-lists/{trafficMatchingListId}`  ·  operationId: `deleteTrafficMatchingList`

Delete an exist traffic matching list on a site.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `trafficMatchingListId` | path | sim | string (uuid) |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X DELETE "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/traffic-matching-lists/{trafficMatchingListId}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X DELETE "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/traffic-matching-lists/{trafficMatchingListId}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Supporting Resources

Contains read-only reference endpoints used to retrieve supporting data
such as WAN interfaces, DPI categories, country codes, RADIUS profiles, and device tags.


### List Countries

`GET /v1/countries`  ·  operationId: `getCountries`

Returns ISO-standard country codes and names,
used for region-based configuration or regulatory compliance.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`code`|`STRING`|`eq` `ne` `in` `notIn`|
|`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `code` **(obrigatório)**: `string` ex: `CK|FK|KY` - The country code in ISO 3166-1 alpha-2 format.
    - `name` **(obrigatório)**: `string` ex: `Cook Islands|Falkland Islands, Malvinas|Cayman Islands` - The country name.
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/countries" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/countries" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### List DPI Applications

`GET /v1/dpi/applications`  ·  operationId: `getDpiApplications`

Lists DPI-recognized applications grouped under categories. Useful for firewall or traffic analytics integration.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`id`|`INTEGER`|`eq` `ne` `in` `notIn`|
|`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `id` **(obrigatório)**: `integer` (int32) ex: `786435|720973`
    - `name` **(obrigatório)**: `string` ex: `Adobe Express|Zoom`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/dpi/applications" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/dpi/applications" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### List DPI Application Categories

`GET /v1/dpi/categories`  ·  operationId: `getDpiApplicationCategories`

Returns predefined Deep Packet Inspection (DPI) application categories used for traffic identification and filtering.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`id`|`INTEGER`|`eq` `ne` `in` `notIn`|
|`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `id` **(obrigatório)**: `integer` (int32) ex: `3|5`
    - `name` **(obrigatório)**: `string` ex: `Network protocols|Business tools`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/dpi/categories" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/dpi/categories" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### List Device Tags

`GET /v1/sites/{siteId}/device-tags`  ·  operationId: `getDeviceTagPage`

Returns all device tags defined within a site, which can be used for WiFi Broadcast assignments.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`id`|`UUID`|`eq` `ne` `in` `notIn`|
|`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
|`deviceIds`|`SET(UUID)`|`contains` `containsAny` `containsAll` `containsExactly`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não |  |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `deviceIds` **(obrigatório)**: `array`
      - _array de_ `string`:
        - `string` (uuid)
    - `id` **(obrigatório)**: `string` (uuid)
    - `metadata` **(obrigatório)**
      - _variantes por `origin`: `ORCHESTRATED`→`Orchestrated entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
    - `name` **(obrigatório)**: `string`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/device-tags" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/device-tags" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### List Radius Profiles

`GET /v1/sites/{siteId}/radius/profiles`  ·  operationId: `getRadiusProfileOverviewPage`

Returns available RADIUS authentication profiles, including configuration origin metadata.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`id`|`UUID`|`eq` `ne` `in` `notIn`|
|`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
|`metadata.origin`|`STRING`|`eq` `ne` `in` `notIn`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `id` **(obrigatório)**: `string` (uuid)
    - `metadata` **(obrigatório)**
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `SYSTEM_DEFINED`→`System defined entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
    - `name` **(obrigatório)**: `string`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/radius/profiles" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/radius/profiles" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### List VPN Servers

`GET /v1/sites/{siteId}/vpn/servers`  ·  operationId: `getVpnServerPage`

Retrieve a paginated list of all VPN servers on a site.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`type`|`STRING`|`eq` `ne` `in` `notIn`|
|`id`|`UUID`|`eq` `ne` `in` `notIn`|
|`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
|`enabled`|`BOOLEAN`|`eq` `ne`|
|`metadata.origin`|`STRING`|`eq` `ne` `in` `notIn`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - _variantes por `type`: `L2TP`→`IntegrationL2tpServerOverviewDto`, `OPENVPN`→`IntegrationOpenVpnServerOverviewDto`, `PPTP`→`IntegrationPptpServerOverviewDto`, `UID`→`IntegrationUidVpnServerOverviewDto`, `WIREGUARD`→`IntegrationWireguardServerOverviewDto` (ver openapi.json)_
    - `enabled` **(obrigatório)**: `boolean`
    - `id` **(obrigatório)**: `string` (uuid)
    - `metadata` **(obrigatório)**
      - _variantes por `origin`: `DERIVED`→`Derived entity metadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
    - `name` **(obrigatório)**: `string`
    - `type` **(obrigatório)**: `string`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/vpn/servers" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/vpn/servers" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### List Site-To-Site VPN Tunnels

`GET /v1/sites/{siteId}/vpn/site-to-site-tunnels`  ·  operationId: `getSiteToSiteVpnTunnelPage`

Retrieve a paginated list of all site-to-site VPN tunnels on a site.

<details>
<summary>Filterable properties (click to expand)</summary>

|Name|Type|Allowed functions|
|-|-|-|
|`type`|`STRING`|`eq` `ne` `in` `notIn`|
|`id`|`UUID`|`eq` `ne` `in` `notIn`|
|`name`|`STRING`|`eq` `ne` `in` `notIn` `like`|
|`metadata.origin`|`STRING`|`eq` `ne` `in` `notIn`|
|`metadata.source`|`STRING`|`eq` `ne` `in` `notIn` `isNull` `isNotNull`|
</details>

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `filter` | query | não | string |  |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - _variantes por `type`: `IPSEC`→`IntegrationSiteToSiteIpsecTunnelOverviewDto`, `OPENVPN`→`IntegrationSiteToSiteOpenVpnTunnelOverviewDto`, `WIREGUARD`→`IntegrationSiteToSiteWireguardTunnelOverviewDto` (ver openapi.json)_
    - `id` **(obrigatório)**: `string` (uuid)
    - `metadata` **(obrigatório)**
      - _variantes por `origin`: `DERIVED`→`IntegrationDerivedSiteToSiteTunnelMetadata`, `USER_DEFINED`→`User defined entity metadata` (ver openapi.json)_
      - `origin` **(obrigatório)**: `string`
    - `name` **(obrigatório)**: `string`
    - `type` **(obrigatório)**: `string`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/vpn/site-to-site-tunnels" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/vpn/site-to-site-tunnels" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### List WAN Interfaces

`GET /v1/sites/{siteId}/wans`  ·  operationId: `getWansOverviewPage`

Returns available WAN interface definitions for a given site,
including identifiers and names. Useful for network and NAT configuration.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `offset` | query | não | integer (int32) | (default 0) |
| `limit` | query | não | integer (int32) | (default 25) |
| `siteId` | path | sim | string (uuid) |  |

**Resposta 200** - OK

- `count` **(obrigatório)**: `integer` (int32) ex: `10`
- `data` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `id` **(obrigatório)**: `string` (uuid)
    - `name` **(obrigatório)**: `string` ex: `Internet 1`
- `limit` **(obrigatório)**: `integer` (int32) ex: `25`
- `offset` **(obrigatório)**: `integer` (int64) ex: `0`
- `totalCount` **(obrigatório)**: `integer` (int64) ex: `1000`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/network/integration/v1/sites/{siteId}/wans" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/network/integration/v1/sites/{siteId}/wans" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>

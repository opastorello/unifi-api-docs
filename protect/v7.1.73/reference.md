# UniFi Protect API - v7.1.73 - Referência

> Espelho automático de [`developer.ui.com/protect/v7.1.73`](https://developer.ui.com/protect/v7.1.73).
> OpenAPI `3.1.0` · 73 operações em 54 paths · atualizado na origem em `2026-06-25T08:38:50.888Z`.

**OpenAPI completo (fonte da verdade):** [`openapi.json`](./openapi.json)

## Índice de endpoints

| Categoria | Método | Path | Operação |
|---|---|---|---|
| Information about application | `GET` | `/v1/meta/info` | Get application information |
| Viewer information & management | `GET` | `/v1/viewers/{id}` | Get viewer details |
| Viewer information & management | `PATCH` | `/v1/viewers/{id}` | Patch viewer settings |
| Viewer information & management | `GET` | `/v1/viewers` | Get all viewers |
| Live view management | `GET` | `/v1/liveviews/{id}` | Get live view details |
| Live view management | `PATCH` | `/v1/liveviews/{id}` | Patch live view configuration |
| Live view management | `GET` | `/v1/liveviews` | Get all live views |
| Live view management | `POST` | `/v1/liveviews` | Create live view |
| WebSocket updates | `GET` | `/v1/subscribe/devices` | Get update messages about devices |
| WebSocket updates | `GET` | `/v1/subscribe/events` | Get Protect event messages |
| Camera PTZ control & management | `POST` | `/v1/cameras/{id}/ptz/patrol/start/{slot}` | Start a camera PTZ patrol |
| Camera PTZ control & management | `POST` | `/v1/cameras/{id}/ptz/patrol/stop` | Stop active camera PTZ patrol |
| Camera PTZ control & management | `POST` | `/v1/cameras/{id}/ptz/goto/{slot}` | Move PTZ camera to preset |
| Alarm manager integration | `POST` | `/v1/alarm-manager/webhook/{id}` | Send a webhook to the alarm manager |
| Arm profile management | `GET` | `/v1/arm-profiles` | Get all arm profiles |
| Arm profile management | `POST` | `/v1/arm-profiles` | Create arm profile |
| Arm profile management | `PATCH` | `/v1/arm-profiles/settings` | Set current arm profile |
| Arm profile management | `DELETE` | `/v1/arm-profiles/{id}` | Delete arm profile |
| Arm profile management | `PATCH` | `/v1/arm-profiles/{id}` | Update arm profile |
| Arm profile management | `POST` | `/v1/arm-profiles/enable` | Enable arm alarm |
| Arm profile management | `POST` | `/v1/arm-profiles/disable` | Disable arm alarm |
| Light information & management | `GET` | `/v1/lights/{id}` | Get light details |
| Light information & management | `PATCH` | `/v1/lights/{id}` | Patch light settings |
| Light information & management | `GET` | `/v1/lights` | Get all lights |
| Camera information & management | `GET` | `/v1/cameras/{id}` | Get camera details |
| Camera information & management | `PATCH` | `/v1/cameras/{id}` | Patch camera settings |
| Camera information & management | `GET` | `/v1/cameras` | Get all cameras |
| Camera information & management | `GET` | `/v1/cameras/{id}/rtsps-stream` | Get RTSPS streams for camera |
| Camera information & management | `POST` | `/v1/cameras/{id}/rtsps-stream` | Create RTSPS streams for camera |
| Camera information & management | `DELETE` | `/v1/cameras/{id}/rtsps-stream` | Delete camera RTSPS stream |
| Camera information & management | `GET` | `/v1/cameras/{id}/snapshot` | Get camera snapshot |
| Camera information & management | `POST` | `/v1/cameras/{id}/disable-mic-permanently` | Permanently disable camera microphone |
| Camera information & management | `POST` | `/v1/cameras/{id}/talkback-session` | Create talkback session for camera |
| Sensor information & management | `GET` | `/v1/sensors/{id}` | Get sensor details |
| Sensor information & management | `PATCH` | `/v1/sensors/{id}` | Patch sensor settings |
| Sensor information & management | `GET` | `/v1/sensors` | Get all sensors |
| Siren information & management | `GET` | `/v1/sirens/{id}` | Get siren details |
| Siren information & management | `PATCH` | `/v1/sirens/{id}` | Patch siren settings |
| Siren information & management | `GET` | `/v1/sirens` | Get all sirens |
| Siren information & management | `POST` | `/v1/sirens/{id}/play` | Play siren |
| Siren information & management | `POST` | `/v1/sirens/{id}/stop` | Stop siren |
| Siren information & management | `POST` | `/v1/sirens/{id}/test-sound` | Test siren sound |
| Fob information & management | `GET` | `/v1/fobs/{id}` | Get fob details |
| Fob information & management | `PATCH` | `/v1/fobs/{id}` | Patch fob settings |
| Fob information & management | `GET` | `/v1/fobs` | Get all fobs |
| Relay information & management | `GET` | `/v1/relays/{id}` | Get relay details |
| Relay information & management | `PATCH` | `/v1/relays/{id}` | Patch relay settings |
| Relay information & management | `GET` | `/v1/relays` | Get all relays |
| Relay information & management | `POST` | `/v1/relays/{id}/outputs/{outputId}/activate` | Activate relay output |
| Speaker information & management | `GET` | `/v1/speakers/{id}` | Get speaker details |
| Speaker information & management | `PATCH` | `/v1/speakers/{id}` | Patch speaker settings |
| Speaker information & management | `GET` | `/v1/speakers` | Get all speakers |
| Speaker information & management | `POST` | `/v1/speakers/{id}/test-sound` | Test speaker sound |
| Bridge information & management | `GET` | `/v1/bridges/{id}` | Get bridge details |
| Bridge information & management | `PATCH` | `/v1/bridges/{id}` | Patch bridge settings |
| Bridge information & management | `GET` | `/v1/bridges` | Get all bridges |
| Link station information & management | `GET` | `/v1/link-stations/{id}` | Get link station details |
| Link station information & management | `PATCH` | `/v1/link-stations/{id}` | Patch link station settings |
| Link station information & management | `GET` | `/v1/link-stations` | Get all link stations |
| Alarm hub information & management | `GET` | `/v1/alarm-hubs/{id}` | Get alarm hub details |
| Alarm hub information & management | `PATCH` | `/v1/alarm-hubs/{id}` | Patch alarm hub settings |
| Alarm hub information & management | `GET` | `/v1/alarm-hubs` | Get all alarm hubs |
| Alarm hub information & management | `POST` | `/v1/alarm-hubs/{id}/outputs/{outputId}/trigger` | Trigger alarm hub output |
| NVR information & management | `GET` | `/v1/nvrs` | Get NVR details |
| Device asset file management | `GET` | `/v1/files/{fileType}` | Get device asset files |
| Device asset file management | `POST` | `/v1/files/{fileType}` | Upload device asset file |
| Chime information & management | `GET` | `/v1/chimes/{id}` | Get chime details |
| Chime information & management | `PATCH` | `/v1/chimes/{id}` | Patch chime settings |
| Chime information & management | `GET` | `/v1/chimes` | Get all chimes |
| Protect User information | `GET` | `/v1/users/{id}` | Get user details |
| Protect User information | `GET` | `/v1/users` | Get all users |
| UniFi Identity User information | `GET` | `/v1/ulp-users/{id}` | Get identity user details |
| UniFi Identity User information | `GET` | `/v1/ulp-users` | Get all identity users |


---

## Information about application


### Get application information

`GET /v1/meta/info`  ·  operationId: ``

Get generic information about the Protect application

**Resposta 200** - Success response

- `applicationVersion` **(obrigatório)**: `string` - Software version.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/meta/info" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/meta/info" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Viewer information & management


### Get viewer details

`GET /v1/viewers/{id}`  ·  operationId: ``

Get detailed information about a specific viewer

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of viewer |

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of viewer
- `modelKey` **(obrigatório)**: `string` - The model key of the viewer
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `liveview` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `streamLimit` **(obrigatório)**: `number` - Count of maximum supported parallel live streams.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/viewers/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/viewers/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Patch viewer settings

`PATCH /v1/viewers/{id}`  ·  operationId: ``

Patch the settings for a specific viewer

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of viewer |

**Corpo da requisição** (`application/json`)

- `name`: `string` - The name of the device.
- `liveview`
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of viewer
- `modelKey` **(obrigatório)**: `string` - The model key of the viewer
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `liveview` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `streamLimit` **(obrigatório)**: `number` - Count of maximum supported parallel live streams.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PATCH "https://$UNIFI_HOST/proxy/protect/integration/v1/viewers/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PATCH "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/viewers/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get all viewers

`GET /v1/viewers`  ·  operationId: ``

Get detailed information about all viewers

**Resposta 200** - Success response

- _array de_ `object`:
  - `id` **(obrigatório)**: `string` - The primary key of viewer
  - `modelKey` **(obrigatório)**: `string` - The model key of the viewer
  - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
  - `name` **(obrigatório)**
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`
  - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
  - `liveview` **(obrigatório)**
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`
  - `streamLimit` **(obrigatório)**: `number` - Count of maximum supported parallel live streams.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/viewers" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/viewers" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Live view management


### Get live view details

`GET /v1/liveviews/{id}`  ·  operationId: ``

Get detailed information about a specific live view

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of liveview |

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of liveview
- `modelKey` **(obrigatório)**: `string` - The model key of the liveview
- `name` **(obrigatório)**: `string` - The name of this live view.
- `isDefault` **(obrigatório)**: `boolean` - Whether this live view is the default one for all viewers.
- `isGlobal` **(obrigatório)**: `boolean` - Whether this live view is global and available system-wide to all users
- `owner` **(obrigatório)**: `string` - The primary key of user
- `layout` **(obrigatório)**: `number` - The number of slots this live view contains. Which as a consequence also affects the layout of the live view.
- `slots` **(obrigatório)**: `array` - List of cameras visible in each given slot. And cycling settings for each slot if it has multiple cameras listed.
  - _array de_ `object`:
    - `cameras` **(obrigatório)**: `array`
      - _array de_ `string`:
        - `string`
    - `cycleMode` **(obrigatório)**: `string` enum: motion, time - Whether to switch to next camera in slot based on motion events or a strict time interval
    - `cycleInterval` **(obrigatório)**: `number` - How long should each camera stream be shown for in seconds until we cycle to the next camera

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/liveviews/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/liveviews/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Patch live view configuration

`PATCH /v1/liveviews/{id}`  ·  operationId: ``

Patch the configuration about a specific live view

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of liveview |

**Corpo da requisição** (`application/json`)

- `id` **(obrigatório)**: `string` - The primary key of liveview
- `modelKey` **(obrigatório)**: `string` - The model key of the liveview
- `name` **(obrigatório)**: `string` - The name of this live view.
- `isDefault` **(obrigatório)**: `boolean` - Whether this live view is the default one for all viewers.
- `isGlobal` **(obrigatório)**: `boolean` - Whether this live view is global and available system-wide to all users
- `owner` **(obrigatório)**: `string` - The primary key of user
- `layout` **(obrigatório)**: `number` - The number of slots this live view contains. Which as a consequence also affects the layout of the live view.
- `slots` **(obrigatório)**: `array` - List of cameras visible in each given slot. And cycling settings for each slot if it has multiple cameras listed.
  - _array de_ `object`:
    - `cameras` **(obrigatório)**: `array`
      - _array de_ `string`:
        - `string`
    - `cycleMode` **(obrigatório)**: `string` enum: motion, time - Whether to switch to next camera in slot based on motion events or a strict time interval
    - `cycleInterval` **(obrigatório)**: `number` - How long should each camera stream be shown for in seconds until we cycle to the next camera

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of liveview
- `modelKey` **(obrigatório)**: `string` - The model key of the liveview
- `name` **(obrigatório)**: `string` - The name of this live view.
- `isDefault` **(obrigatório)**: `boolean` - Whether this live view is the default one for all viewers.
- `isGlobal` **(obrigatório)**: `boolean` - Whether this live view is global and available system-wide to all users
- `owner` **(obrigatório)**: `string` - The primary key of user
- `layout` **(obrigatório)**: `number` - The number of slots this live view contains. Which as a consequence also affects the layout of the live view.
- `slots` **(obrigatório)**: `array` - List of cameras visible in each given slot. And cycling settings for each slot if it has multiple cameras listed.
  - _array de_ `object`:
    - `cameras` **(obrigatório)**: `array`
      - _array de_ `string`:
        - `string`
    - `cycleMode` **(obrigatório)**: `string` enum: motion, time - Whether to switch to next camera in slot based on motion events or a strict time interval
    - `cycleInterval` **(obrigatório)**: `number` - How long should each camera stream be shown for in seconds until we cycle to the next camera

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PATCH "https://$UNIFI_HOST/proxy/protect/integration/v1/liveviews/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PATCH "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/liveviews/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get all live views

`GET /v1/liveviews`  ·  operationId: ``

Get detailed information about all live views

**Resposta 200** - Success response

- _array de_ `object`:
  - `id` **(obrigatório)**: `string` - The primary key of liveview
  - `modelKey` **(obrigatório)**: `string` - The model key of the liveview
  - `name` **(obrigatório)**: `string` - The name of this live view.
  - `isDefault` **(obrigatório)**: `boolean` - Whether this live view is the default one for all viewers.
  - `isGlobal` **(obrigatório)**: `boolean` - Whether this live view is global and available system-wide to all users
  - `owner` **(obrigatório)**: `string` - The primary key of user
  - `layout` **(obrigatório)**: `number` - The number of slots this live view contains. Which as a consequence also affects the layout of the live view.
  - `slots` **(obrigatório)**: `array` - List of cameras visible in each given slot. And cycling settings for each slot if it has multiple cameras listed.
    - _array de_ `object`:
      - `cameras` **(obrigatório)**: `array`
        - _array de_ `string`:
          - `string`
      - `cycleMode` **(obrigatório)**: `string` enum: motion, time - Whether to switch to next camera in slot based on motion events or a strict time interval
      - `cycleInterval` **(obrigatório)**: `number` - How long should each camera stream be shown for in seconds until we cycle to the next camera

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/liveviews" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/liveviews" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Create live view

`POST /v1/liveviews`  ·  operationId: ``

Create a new live view

**Corpo da requisição** (`application/json`)

- `id` **(obrigatório)**: `string` - The primary key of liveview
- `modelKey` **(obrigatório)**: `string` - The model key of the liveview
- `name` **(obrigatório)**: `string` - The name of this live view.
- `isDefault` **(obrigatório)**: `boolean` - Whether this live view is the default one for all viewers.
- `isGlobal` **(obrigatório)**: `boolean` - Whether this live view is global and available system-wide to all users
- `owner` **(obrigatório)**: `string` - The primary key of user
- `layout` **(obrigatório)**: `number` - The number of slots this live view contains. Which as a consequence also affects the layout of the live view.
- `slots` **(obrigatório)**: `array` - List of cameras visible in each given slot. And cycling settings for each slot if it has multiple cameras listed.
  - _array de_ `object`:
    - `cameras` **(obrigatório)**: `array`
      - _array de_ `string`:
        - `string`
    - `cycleMode` **(obrigatório)**: `string` enum: motion, time - Whether to switch to next camera in slot based on motion events or a strict time interval
    - `cycleInterval` **(obrigatório)**: `number` - How long should each camera stream be shown for in seconds until we cycle to the next camera

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of liveview
- `modelKey` **(obrigatório)**: `string` - The model key of the liveview
- `name` **(obrigatório)**: `string` - The name of this live view.
- `isDefault` **(obrigatório)**: `boolean` - Whether this live view is the default one for all viewers.
- `isGlobal` **(obrigatório)**: `boolean` - Whether this live view is global and available system-wide to all users
- `owner` **(obrigatório)**: `string` - The primary key of user
- `layout` **(obrigatório)**: `number` - The number of slots this live view contains. Which as a consequence also affects the layout of the live view.
- `slots` **(obrigatório)**: `array` - List of cameras visible in each given slot. And cycling settings for each slot if it has multiple cameras listed.
  - _array de_ `object`:
    - `cameras` **(obrigatório)**: `array`
      - _array de_ `string`:
        - `string`
    - `cycleMode` **(obrigatório)**: `string` enum: motion, time - Whether to switch to next camera in slot based on motion events or a strict time interval
    - `cycleInterval` **(obrigatório)**: `number` - How long should each camera stream be shown for in seconds until we cycle to the next camera

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/protect/integration/v1/liveviews" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/liveviews" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


---

## WebSocket updates


### Get update messages about devices

`GET /v1/subscribe/devices`  ·  operationId: ``

A WebSocket subscription which broadcasts all changes happening to Protect-managed hardware devices

**Resposta 200** - Success response

- _um de (variantes):_
  - **variante**:
    - _um de (type):_
      - **variante**:
        - `type` **(obrigatório)**: `string`
        - `item` **(obrigatório)**
          - _um de (modelKey):_
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of nvr
              - `modelKey` **(obrigatório)**: `string` - The model key of the nvr
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `doorbellSettings` **(obrigatório)**: `object`
                - `defaultMessageText`: `string` - Default text to display on the LCD screen.
                - `defaultMessageResetTimeoutMs`: `number` - Default timeout for resetting LCD screen to the default message.
                - `customMessages`: `array` - A list of custom doorbell messages.
                - `customImages`: `array` - A list of custom doorbell images for client preview.
              - `armMode` **(obrigatório)**: `object`
                - `status` **(obrigatório)**: `string` enum: arming, armed, breach, disabled
                - `armProfileId` **(obrigatório)**: `string|null`
                - `armedAt` **(obrigatório)**: `number|null`
                - `willBeArmedAt` **(obrigatório)**: `number|null`
                - `breachDetectedAt` **(obrigatório)**: `number|null`
                - `breachEventCount` **(obrigatório)**: `number`
                - `breachTriggerEventId` **(obrigatório)**: `string|null`
                - `breachEventId` **(obrigatório)**: `string|null`
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of camera
              - `modelKey` **(obrigatório)**: `string` - The model key of the camera
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `isMicEnabled` **(obrigatório)**: `boolean` - Whether or not the microphone on camera is enabled
              - `osdSettings` **(obrigatório)**: `object` - On Screen Display settings.
                - `isNameEnabled` **(obrigatório)**: `boolean` - Whether to show the name in the OSD.
                - `isDateEnabled` **(obrigatório)**: `boolean` - Whether to show the date in the OSD.
                - `isLogoEnabled` **(obrigatório)**: `boolean` - Whether to show the logo in the bottom right corner.
                - `isDebugEnabled` **(obrigatório)**: `boolean` - Whether debug info is enabled.
                - `overlayLocation` **(obrigatório)**: `string` enum: topLeft, topMiddle, topRight, bottomLeft, bottomMiddle, bottomRight - The location of the overlay on the screen.
              - `ledSettings` **(obrigatório)**: `object` - LED settings.
                - `isEnabled` **(obrigatório)**: `boolean` - Indicates whether the status LED is enabled.
                - `welcomeLed` **(obrigatório)**: `boolean` - Indicates whether the welcome LED is enabled.
                - `floodLed` **(obrigatório)**: `boolean` - Indicates whether the flood LED is enabled.
              - `lcdMessage` **(obrigatório)**: `object`
                - `type`: `string` enum: LEAVE_PACKAGE_AT_DOOR, DO_NOT_DISTURB, CUSTOM_MESSAGE, IMAGE
                - `resetAt`: `number|null` - UNIX timestamp when doorbell message should be removed (if not set then `nvr.doorbellSettings.defaultMessageResetTimeoutMs` is used, if set to `null` then in…
                - `text`: `string`
              - `micVolume` **(obrigatório)**: `number` - Mic volume: a number from 0-100.
              - `activePatrolSlot` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `number`
                  - **variante**:
                    - `null`
              - `videoMode` **(obrigatório)**: `string` enum: default, highFps, sport, slowShutter, lprReflex, lprNoneReflex - Current video mode of the camera
              - `hdrType` **(obrigatório)**: `string` enum: auto, on, off - High Dynamic Range (HDR) mode setting.
              - `featureFlags` **(obrigatório)**: `object`
                - `supportFullHdSnapshot` **(obrigatório)**: `boolean` - Whether camera support full HD or higher resolution snapshot
                - `hasHdr` **(obrigatório)**: `boolean` - Whether the camera supports High Dynamic Range mode
                - `smartDetectTypes` **(obrigatório)**: `array` - What smart detection object types do the camera support.
                - `smartDetectAudioTypes` **(obrigatório)**: `array` - What smart detection audio types do the camera support.
                - `videoModes` **(obrigatório)**: `array` - A list of supported video modes by the camera
                - `hasMic` **(obrigatório)**: `boolean` - Whether the camera has a microphone
                - `hasLedStatus` **(obrigatório)**: `boolean` - Whether the camera has LED status
                - `hasSpeaker` **(obrigatório)**: `boolean` - Whether the camera has a speaker to support talkback
              - `smartDetectSettings` **(obrigatório)**: `object` - Smart detection settings for the camera.
                - `objectTypes` **(obrigatório)**: `array`
                - `audioTypes` **(obrigatório)**: `array`
              - `hasPackageCamera` **(obrigatório)**: `boolean` - Whether the camera has a package camera.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of chime
              - `modelKey` **(obrigatório)**: `string` - The model key of the chime
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `cameraIds` **(obrigatório)**: `array` - The list of (doorbell-only) cameras which this chime is paired to.
                - _array de_ `string`:
              - `ringSettings` **(obrigatório)**: `array` - List of custom ringtone settings for (doorbell-only) cameras paired to this chime.
                - _array de_ `object`:
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of light
              - `modelKey` **(obrigatório)**: `string` - The model key of the light
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `lightModeSettings` **(obrigatório)**: `object` - Settings for when and how your light gets activated
                - `mode`: When will floodlight turn on.
                - `enableAt`: At what time is the lighting mode relevant and acted upon (this has no effect when mode is off).
              - `lightDeviceSettings` **(obrigatório)**: `object` - Hardware settings for light device.
                - `isIndicatorEnabled`: `boolean` - Turn on/off floodlight status LED indicator.
                - `pirDuration`: `number` - How long the light stays on after a motion event in milliseconds.
                - `pirSensitivity`: `number` - How sensitive is the PIR to motion (0-100)%.
                - `ledLevel`: `number` - Brightness level of the main LED (1-6).
              - `isDark` **(obrigatório)**: `boolean` - Whether the light is currently sensing that it's in a dark scene.
              - `isLightOn` **(obrigatório)**: `boolean` - Whether the light has its main LED currently enabled.
              - `isLightForceEnabled` **(obrigatório)**: `boolean` - Whether the light has its main LED currently force-enabled.
              - `lastMotion` **(obrigatório)**: `number|null` - Unix timestamp of the last time the PIR motion-detection was triggered.
              - `isPirMotionDetected` **(obrigatório)**: `boolean` - Whether the light PIR is currently detecting motion
              - `camera` **(obrigatório)**: Which camera is configured to be paired to this light.
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of viewer
              - `modelKey` **(obrigatório)**: `string` - The model key of the viewer
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `liveview` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `streamLimit` **(obrigatório)**: `number` - Count of maximum supported parallel live streams.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of speaker
              - `modelKey` **(obrigatório)**: `string` - The model key of the speaker
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `volume` **(obrigatório)**: `integer` - Speaker volume: a number from 0-100.
              - `micVolume` **(obrigatório)**: `integer` - Mic volume: a number from 0-100.
              - `isMicEnabled` **(obrigatório)**: `boolean` - Whether or not the microphone on the speaker is enabled.
              - `speakerState` **(obrigatório)**: `object` - Real-time state of Speaker
                - `status` **(obrigatório)**: `string` enum: idle, streaming, playing, tts_playing, uploading - Current status of the speaker
                - `mode` **(obrigatório)**: `string` enum: listen, talk - Current mode of the speaker
              - `featureFlags` **(obrigatório)**: `object` - Feature flags of the speaker
                - `hasMic` **(obrigatório)**: `boolean` - Whether the device has a microphone.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of bridge
              - `modelKey` **(obrigatório)**: `string` - The model key of the bridge
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `platform` **(obrigatório)**: `string|null` - The bridge platform
              - `clients` **(obrigatório)**: `array` - Array of IoT devices mac that bridge is reserving for
                - _array de_ `string`:
              - `maxClients` **(obrigatório)**: `number` - The max acceptable client number of a V2 bridge. V1 bridge does not support this feature.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of sensor
              - `modelKey` **(obrigatório)**: `string` - The model key of the sensor
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `mountType` **(obrigatório)**: `string` enum: door, window, garage, leak, none - Mounting type of the sensor.
              - `batteryStatus` **(obrigatório)**: `object` - [DEPRECATED] Use wirelessConnectionState.batteryStatus instead. Battery status.
                - `percentage`: `number|null` - Battery charge level from 0 to 100 (%).
                - `isLow`: `boolean` - Low battery charge level flag.
              - `stats` **(obrigatório)**: `object` - Sensor statistics.
                - `light`: `object` - Ambient light value (Lux).
                - `humidity`: `object` - Ambient light value (Lux).
                - `temperature`: `object` - Ambient light value (Lux).
              - `lightSettings` **(obrigatório)**: `object` - Ambient light sensor settings.
                - `isEnabled`: `boolean` - Enable ambient light sensor.
                - `margin`: `number` - Ambient light threshold detection hysteresis margin (Lux). Read-only value decided by sensor implementation.
                - `lowThreshold`: `number|null` - Ambient light interrupt threshold low level from 1 to 503192 (Lux).
                - `highThreshold`: `number|null` - Ambient light interrupt threshold high level from 1 to 503192 (Lux).
              - `humiditySettings` **(obrigatório)**: `object` - Relative humidity sensor settings.
                - `isEnabled`: `boolean` - Enable relative humidity sensor.
                - `margin`: `number` - Humidity threshold detection hysteresis margin (%). Read-only value decided by sensor implementation.
                - `lowThreshold`: `number|null` - Humidity low level threshold from 1 to 99 (%).
                - `highThreshold`: `number|null` - Humidity high level threshold from 1 to 99 (%).
              - `temperatureSettings` **(obrigatório)**: `object` - Temperature sensor settings.
                - `isEnabled`: `boolean` - Enable temperature sensor.
                - `margin`: `number` - Temperature threshold detection hysteresis margin (C). Read-only value decided by sensor implementation.
                - `lowThreshold`: `number|null` - Temperature low level threshold from -39 to 124 (C).
                - `highThreshold`: `number|null` - Temperature high level threshold from -39 to 124 (C).
              - `isOpened` **(obrigatório)**: `boolean|null` - Whether the door/window/garage is opened.
              - `openStatusChangedAt` **(obrigatório)**: `number|null` - Unix timestamp when the door/window/garage was last opened or closed, nullable.
              - `isMotionDetected` **(obrigatório)**: `boolean` - Whether sensor is currently detecting the motion.
              - `motionDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the last motion was detected.
              - `motionSettings` **(obrigatório)**: `object` - Motion sensor settings.
                - `isEnabled`: `boolean` - Enable motion sensor.
                - `sensitivity`: `number` - Motion sensitivity (0-100) used when system is not armed or when no armed override is set.
                - `sensitivityWhenArmed`: `number` - Motion sensitivity (0-100) used when the system is armed and `hasCustomSensitivityWhenArmed` is true on the sensor.
              - `glassBreakSettings` **(obrigatório)**: `object` - Glass break sensor settings.
                - `isEnabled`: `boolean` - Enable glass break sensor.
                - `sensitivity`: `number` - Glass break sensitivity (0-100) used when system is not armed or when no armed override is set.
                - `sensitivityWhenArmed`: `number` - Glass break sensitivity (0-100) used when the system is armed and `hasCustomSensitivityWhenArmed` is true on the sensor.
              - `scheduleMode` **(obrigatório)**: `string` enum: always, when_armed - When armed-mode detection runs: `always` or only `when_armed`. Applies to both glass break and motion together.
              - `armProfileIds` **(obrigatório)**: `array|null` - When `scheduleMode` is `when_armed`, restricts armed-mode detection to these arm profile ids. Empty or null = all profiles.
              - `hasCustomSensitivityWhenArmed` **(obrigatório)**: `boolean` - When true, glass break and motion both use their respective `sensitivityWhenArmed` value while the system is armed.
              - `alarmTriggeredAt` **(obrigatório)**: `number|null` - Unix timestamp when the smoke or carbon monoxide alarm was triggered, nullable.
              - `alarmSettings` **(obrigatório)**: `object` - Smoke and carbon monoxide alarm sensor settings.
                - `isEnabled`: `boolean` - Enable smoke and carbon monoxide alarm sensor.
              - `leakDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected a water leak, nullable.
              - `externalLeakDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected an external water leak, nullable.
              - `leakSettings` **(obrigatório)**: `object` - Leak sensor settings.
                - `isInternalEnabled`: `boolean` - Enable internal water leak detection.
                - `isExternalEnabled`: `boolean` - Enable external water leak detection.
              - `tamperingDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected tampering, nullable.
              - `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
                - `signalState` **(obrigatório)**: `object` - Signal state.
                - `batteryStatus` **(obrigatório)**: `object` - Battery status.
                - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of siren
              - `modelKey` **(obrigatório)**: `string` - The model key of the siren
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `volume` **(obrigatório)**: `integer` - Volume: a number from 1-100.
              - `ledSettings` **(obrigatório)**: `object` - Status LED settings.
                - `isEnabled` **(obrigatório)**: `boolean` - Enable status LED.
              - `sirenStatus` **(obrigatório)**: `object` - Status of the siren
                - `isActive` **(obrigatório)**: `boolean` - Whether the siren is active.
                - `activatedAt` **(obrigatório)**: `number|null` - Timestamp when the siren was activated.
                - `duration` **(obrigatório)**
              - `connectionType` **(obrigatório)**: `string` enum: ucp4, lora - The connection type of the siren.
              - `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
                - `signalState` **(obrigatório)**: `object` - Signal state.
                - `batteryStatus` **(obrigatório)**: `object` - Battery status.
                - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of fob
              - `modelKey` **(obrigatório)**: `string` - The model key of the fob
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `awayState` **(obrigatório)**: `string` enum: ONLINE, RECENTLY_SEEN, NO_RECENT_HEARTBEAT, DEVICE_LOST - Fob presence/away state.
              - `buttonLabels` **(obrigatório)**: `string` enum: securityActions, positionHint - Label style applied when this fob is rendered in button selection lists.
              - `featureFlags` **(obrigatório)**: `object` - Feature flags for the fob.
                - `buttons` **(obrigatório)**: `array` - Available button types on the fob.
              - `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
                - `signalState` **(obrigatório)**: `object` - Signal state.
                - `batteryStatus` **(obrigatório)**: `object` - Battery status.
                - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of relay
              - `modelKey` **(obrigatório)**: `string` - The model key of the relay
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `ledSettings` **(obrigatório)**: `object` - Status LED settings.
                - `isEnabled` **(obrigatório)**: `boolean` - Enable status LED.
              - `outputs` **(obrigatório)**: `array`
                - _array de_ `object`:
              - `inputs` **(obrigatório)**: `array`
                - _array de_ `object`:
              - `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
                - `signalState` **(obrigatório)**: `object` - Signal state.
                - `batteryStatus` **(obrigatório)**: `object` - Battery status.
                - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of device
              - `modelKey` **(obrigatório)**: `string` - The model key of the aiprocessor
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of device
              - `modelKey` **(obrigatório)**: `string` - The model key of the aiport
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of linkStation
              - `modelKey` **(obrigatório)**: `string` - The model key of the linkstation
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `isAlarmHub` **(obrigatório)**: `boolean` - Whether the linkstation is an alarm hub.
              - `ledSettings` **(obrigatório)**: `object` - Status LED settings.
                - `isEnabled` **(obrigatório)**: `boolean` - Whether the status LED is enabled.
              - `lastEvent` **(obrigatório)**: `number|null` - Timestamp when any last event was detected.
              - `alarmHub`: `object` - Alarm hub status and configuration. Only present when isAlarmHub is true.
                - `armed` **(obrigatório)**: `string` enum: on, off
                - `battery`: `object`
                - `buckboost` **(obrigatório)**: `string` enum: on, off
                - `connector`: `object`
                - `cover`: `object`
                - `currentMeterChannelStatus` **(obrigatório)**: `object`
                - `currentMeterStatus` **(obrigatório)**: `object`
                - `inputPower`: `object`
                - `poeout`: `object`
                - `powerMeter` **(obrigatório)**: `object`
                - `output` **(obrigatório)**: `object`
                - `input` **(obrigatório)**: `object`
                - `inputTerminalStatus`: `object`
                - `outputTerminalStatus`: `object`
                - `emergencyTerminalStatus`: `object|null`
                - `auxiliaryPowerTerminalStatus`: `object`
      - **variante**:
        - `type` **(obrigatório)**: `string`
        - `item` **(obrigatório)**
          - _um de (modelKey):_
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of nvr
              - `modelKey` **(obrigatório)**: `string` - The model key of the nvr
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `doorbellSettings`: `object`
                - `defaultMessageText`: `string` - Default text to display on the LCD screen.
                - `defaultMessageResetTimeoutMs`: `number` - Default timeout for resetting LCD screen to the default message.
                - `customMessages`: `array` - A list of custom doorbell messages.
                - `customImages`: `array` - A list of custom doorbell images for client preview.
              - `armMode`: `object`
                - `status` **(obrigatório)**: `string` enum: arming, armed, breach, disabled
                - `armProfileId` **(obrigatório)**: `string|null`
                - `armedAt` **(obrigatório)**: `number|null`
                - `willBeArmedAt` **(obrigatório)**: `number|null`
                - `breachDetectedAt` **(obrigatório)**: `number|null`
                - `breachEventCount` **(obrigatório)**: `number`
                - `breachTriggerEventId` **(obrigatório)**: `string|null`
                - `breachEventId` **(obrigatório)**: `string|null`
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of camera
              - `modelKey` **(obrigatório)**: `string` - The model key of the camera
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `isMicEnabled`: `boolean` - Whether or not the microphone on camera is enabled
              - `osdSettings`: `object` - On Screen Display settings.
                - `isNameEnabled` **(obrigatório)**: `boolean` - Whether to show the name in the OSD.
                - `isDateEnabled` **(obrigatório)**: `boolean` - Whether to show the date in the OSD.
                - `isLogoEnabled` **(obrigatório)**: `boolean` - Whether to show the logo in the bottom right corner.
                - `isDebugEnabled` **(obrigatório)**: `boolean` - Whether debug info is enabled.
                - `overlayLocation` **(obrigatório)**: `string` enum: topLeft, topMiddle, topRight, bottomLeft, bottomMiddle, bottomRight - The location of the overlay on the screen.
              - `ledSettings`: `object` - LED settings.
                - `isEnabled` **(obrigatório)**: `boolean` - Indicates whether the status LED is enabled.
                - `welcomeLed` **(obrigatório)**: `boolean` - Indicates whether the welcome LED is enabled.
                - `floodLed` **(obrigatório)**: `boolean` - Indicates whether the flood LED is enabled.
              - `lcdMessage`: `object`
                - `type`: `string` enum: LEAVE_PACKAGE_AT_DOOR, DO_NOT_DISTURB, CUSTOM_MESSAGE, IMAGE
                - `resetAt`: `number|null` - UNIX timestamp when doorbell message should be removed (if not set then `nvr.doorbellSettings.defaultMessageResetTimeoutMs` is used, if set to `null` then in…
                - `text`: `string`
              - `micVolume`: `number` - Mic volume: a number from 0-100.
              - `activePatrolSlot`
                - _um de (variantes):_
                  - **variante**:
                    - `number`
                  - **variante**:
                    - `null`
              - `videoMode`: `string` enum: default, highFps, sport, slowShutter, lprReflex, lprNoneReflex - Current video mode of the camera
              - `hdrType`: `string` enum: auto, on, off - High Dynamic Range (HDR) mode setting.
              - `featureFlags`: `object`
                - `supportFullHdSnapshot` **(obrigatório)**: `boolean` - Whether camera support full HD or higher resolution snapshot
                - `hasHdr` **(obrigatório)**: `boolean` - Whether the camera supports High Dynamic Range mode
                - `smartDetectTypes` **(obrigatório)**: `array` - What smart detection object types do the camera support.
                - `smartDetectAudioTypes` **(obrigatório)**: `array` - What smart detection audio types do the camera support.
                - `videoModes` **(obrigatório)**: `array` - A list of supported video modes by the camera
                - `hasMic` **(obrigatório)**: `boolean` - Whether the camera has a microphone
                - `hasLedStatus` **(obrigatório)**: `boolean` - Whether the camera has LED status
                - `hasSpeaker` **(obrigatório)**: `boolean` - Whether the camera has a speaker to support talkback
              - `smartDetectSettings`: `object` - Smart detection settings for the camera.
                - `objectTypes` **(obrigatório)**: `array`
                - `audioTypes` **(obrigatório)**: `array`
              - `hasPackageCamera`: `boolean` - Whether the camera has a package camera.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of chime
              - `modelKey` **(obrigatório)**: `string` - The model key of the chime
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `cameraIds`: `array` - The list of (doorbell-only) cameras which this chime is paired to.
                - _array de_ `string`:
              - `ringSettings`: `array` - List of custom ringtone settings for (doorbell-only) cameras paired to this chime.
                - _array de_ `object`:
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of light
              - `modelKey` **(obrigatório)**: `string` - The model key of the light
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `lightModeSettings`: `object` - Settings for when and how your light gets activated
                - `mode`: When will floodlight turn on.
                - `enableAt`: At what time is the lighting mode relevant and acted upon (this has no effect when mode is off).
              - `lightDeviceSettings`: `object` - Hardware settings for light device.
                - `isIndicatorEnabled`: `boolean` - Turn on/off floodlight status LED indicator.
                - `pirDuration`: `number` - How long the light stays on after a motion event in milliseconds.
                - `pirSensitivity`: `number` - How sensitive is the PIR to motion (0-100)%.
                - `ledLevel`: `number` - Brightness level of the main LED (1-6).
              - `isDark`: `boolean` - Whether the light is currently sensing that it's in a dark scene.
              - `isLightOn`: `boolean` - Whether the light has its main LED currently enabled.
              - `isLightForceEnabled`: `boolean` - Whether the light has its main LED currently force-enabled.
              - `lastMotion`: `number|null` - Unix timestamp of the last time the PIR motion-detection was triggered.
              - `isPirMotionDetected`: `boolean` - Whether the light PIR is currently detecting motion
              - `camera`: Which camera is configured to be paired to this light.
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of viewer
              - `modelKey` **(obrigatório)**: `string` - The model key of the viewer
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `liveview`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `streamLimit`: `number` - Count of maximum supported parallel live streams.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of speaker
              - `modelKey` **(obrigatório)**: `string` - The model key of the speaker
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `volume`: `integer` - Speaker volume: a number from 0-100.
              - `micVolume`: `integer` - Mic volume: a number from 0-100.
              - `isMicEnabled`: `boolean` - Whether or not the microphone on the speaker is enabled.
              - `speakerState`: `object` - Real-time state of Speaker
                - `status` **(obrigatório)**: `string` enum: idle, streaming, playing, tts_playing, uploading - Current status of the speaker
                - `mode` **(obrigatório)**: `string` enum: listen, talk - Current mode of the speaker
              - `featureFlags`: `object` - Feature flags of the speaker
                - `hasMic` **(obrigatório)**: `boolean` - Whether the device has a microphone.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of bridge
              - `modelKey` **(obrigatório)**: `string` - The model key of the bridge
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `platform`: `string|null` - The bridge platform
              - `clients`: `array` - Array of IoT devices mac that bridge is reserving for
                - _array de_ `string`:
              - `maxClients`: `number` - The max acceptable client number of a V2 bridge. V1 bridge does not support this feature.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of sensor
              - `modelKey` **(obrigatório)**: `string` - The model key of the sensor
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `mountType`: `string` enum: door, window, garage, leak, none - Mounting type of the sensor.
              - `batteryStatus`: `object` - [DEPRECATED] Use wirelessConnectionState.batteryStatus instead. Battery status.
                - `percentage`: `number|null` - Battery charge level from 0 to 100 (%).
                - `isLow`: `boolean` - Low battery charge level flag.
              - `stats`: `object` - Sensor statistics.
                - `light`: `object` - Ambient light value (Lux).
                - `humidity`: `object` - Ambient light value (Lux).
                - `temperature`: `object` - Ambient light value (Lux).
              - `lightSettings`: `object` - Ambient light sensor settings.
                - `isEnabled`: `boolean` - Enable ambient light sensor.
                - `margin`: `number` - Ambient light threshold detection hysteresis margin (Lux). Read-only value decided by sensor implementation.
                - `lowThreshold`: `number|null` - Ambient light interrupt threshold low level from 1 to 503192 (Lux).
                - `highThreshold`: `number|null` - Ambient light interrupt threshold high level from 1 to 503192 (Lux).
              - `humiditySettings`: `object` - Relative humidity sensor settings.
                - `isEnabled`: `boolean` - Enable relative humidity sensor.
                - `margin`: `number` - Humidity threshold detection hysteresis margin (%). Read-only value decided by sensor implementation.
                - `lowThreshold`: `number|null` - Humidity low level threshold from 1 to 99 (%).
                - `highThreshold`: `number|null` - Humidity high level threshold from 1 to 99 (%).
              - `temperatureSettings`: `object` - Temperature sensor settings.
                - `isEnabled`: `boolean` - Enable temperature sensor.
                - `margin`: `number` - Temperature threshold detection hysteresis margin (C). Read-only value decided by sensor implementation.
                - `lowThreshold`: `number|null` - Temperature low level threshold from -39 to 124 (C).
                - `highThreshold`: `number|null` - Temperature high level threshold from -39 to 124 (C).
              - `isOpened`: `boolean|null` - Whether the door/window/garage is opened.
              - `openStatusChangedAt`: `number|null` - Unix timestamp when the door/window/garage was last opened or closed, nullable.
              - `isMotionDetected`: `boolean` - Whether sensor is currently detecting the motion.
              - `motionDetectedAt`: `number|null` - Unix timestamp when the last motion was detected.
              - `motionSettings`: `object` - Motion sensor settings.
                - `isEnabled`: `boolean` - Enable motion sensor.
                - `sensitivity`: `number` - Motion sensitivity (0-100) used when system is not armed or when no armed override is set.
                - `sensitivityWhenArmed`: `number` - Motion sensitivity (0-100) used when the system is armed and `hasCustomSensitivityWhenArmed` is true on the sensor.
              - `glassBreakSettings`: `object` - Glass break sensor settings.
                - `isEnabled`: `boolean` - Enable glass break sensor.
                - `sensitivity`: `number` - Glass break sensitivity (0-100) used when system is not armed or when no armed override is set.
                - `sensitivityWhenArmed`: `number` - Glass break sensitivity (0-100) used when the system is armed and `hasCustomSensitivityWhenArmed` is true on the sensor.
              - `scheduleMode`: `string` enum: always, when_armed - When armed-mode detection runs: `always` or only `when_armed`. Applies to both glass break and motion together.
              - `armProfileIds`: `array|null` - When `scheduleMode` is `when_armed`, restricts armed-mode detection to these arm profile ids. Empty or null = all profiles.
              - `hasCustomSensitivityWhenArmed`: `boolean` - When true, glass break and motion both use their respective `sensitivityWhenArmed` value while the system is armed.
              - `alarmTriggeredAt`: `number|null` - Unix timestamp when the smoke or carbon monoxide alarm was triggered, nullable.
              - `alarmSettings`: `object` - Smoke and carbon monoxide alarm sensor settings.
                - `isEnabled`: `boolean` - Enable smoke and carbon monoxide alarm sensor.
              - `leakDetectedAt`: `number|null` - Unix timestamp when the sensor detected a water leak, nullable.
              - `externalLeakDetectedAt`: `number|null` - Unix timestamp when the sensor detected an external water leak, nullable.
              - `leakSettings`: `object` - Leak sensor settings.
                - `isInternalEnabled`: `boolean` - Enable internal water leak detection.
                - `isExternalEnabled`: `boolean` - Enable external water leak detection.
              - `tamperingDetectedAt`: `number|null` - Unix timestamp when the sensor detected tampering, nullable.
              - `wirelessConnectionState`: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
                - `signalState` **(obrigatório)**: `object` - Signal state.
                - `batteryStatus` **(obrigatório)**: `object` - Battery status.
                - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of siren
              - `modelKey` **(obrigatório)**: `string` - The model key of the siren
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `volume`: `integer` - Volume: a number from 1-100.
              - `ledSettings`: `object` - Status LED settings.
                - `isEnabled` **(obrigatório)**: `boolean` - Enable status LED.
              - `sirenStatus`: `object` - Status of the siren
                - `isActive` **(obrigatório)**: `boolean` - Whether the siren is active.
                - `activatedAt` **(obrigatório)**: `number|null` - Timestamp when the siren was activated.
                - `duration` **(obrigatório)**
              - `connectionType`: `string` enum: ucp4, lora - The connection type of the siren.
              - `wirelessConnectionState`: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
                - `signalState` **(obrigatório)**: `object` - Signal state.
                - `batteryStatus` **(obrigatório)**: `object` - Battery status.
                - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of fob
              - `modelKey` **(obrigatório)**: `string` - The model key of the fob
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `awayState`: `string` enum: ONLINE, RECENTLY_SEEN, NO_RECENT_HEARTBEAT, DEVICE_LOST - Fob presence/away state.
              - `buttonLabels`: `string` enum: securityActions, positionHint - Label style applied when this fob is rendered in button selection lists.
              - `featureFlags`: `object` - Feature flags for the fob.
                - `buttons` **(obrigatório)**: `array` - Available button types on the fob.
              - `wirelessConnectionState`: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
                - `signalState` **(obrigatório)**: `object` - Signal state.
                - `batteryStatus` **(obrigatório)**: `object` - Battery status.
                - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of relay
              - `modelKey` **(obrigatório)**: `string` - The model key of the relay
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `ledSettings`: `object` - Status LED settings.
                - `isEnabled` **(obrigatório)**: `boolean` - Enable status LED.
              - `outputs`: `array`
                - _array de_ `object`:
              - `inputs`: `array`
                - _array de_ `object`:
              - `wirelessConnectionState`: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
                - `signalState` **(obrigatório)**: `object` - Signal state.
                - `batteryStatus` **(obrigatório)**: `object` - Battery status.
                - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of device
              - `modelKey` **(obrigatório)**: `string` - The model key of the aiprocessor
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of device
              - `modelKey` **(obrigatório)**: `string` - The model key of the aiport
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of linkStation
              - `modelKey` **(obrigatório)**: `string` - The model key of the linkstation
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `isAlarmHub`: `boolean` - Whether the linkstation is an alarm hub.
              - `ledSettings`: `object` - Status LED settings.
                - `isEnabled` **(obrigatório)**: `boolean` - Whether the status LED is enabled.
              - `lastEvent`: `number|null` - Timestamp when any last event was detected.
              - `alarmHub`: `object` - Alarm hub status and configuration. Only present when isAlarmHub is true.
                - `armed` **(obrigatório)**: `string` enum: on, off
                - `battery`: `object`
                - `buckboost` **(obrigatório)**: `string` enum: on, off
                - `connector`: `object`
                - `cover`: `object`
                - `currentMeterChannelStatus` **(obrigatório)**: `object`
                - `currentMeterStatus` **(obrigatório)**: `object`
                - `inputPower`: `object`
                - `poeout`: `object`
                - `powerMeter` **(obrigatório)**: `object`
                - `output` **(obrigatório)**: `object`
                - `input` **(obrigatório)**: `object`
                - `inputTerminalStatus`: `object`
                - `outputTerminalStatus`: `object`
                - `emergencyTerminalStatus`: `object|null`
                - `auxiliaryPowerTerminalStatus`: `object`
      - **variante**:
        - `type` **(obrigatório)**: `string`
        - `item` **(obrigatório)**
          - _um de (modelKey):_
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of nvr
              - `modelKey` **(obrigatório)**: `string` - The model key of the nvr
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of camera
              - `modelKey` **(obrigatório)**: `string` - The model key of the camera
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of chime
              - `modelKey` **(obrigatório)**: `string` - The model key of the chime
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of light
              - `modelKey` **(obrigatório)**: `string` - The model key of the light
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of viewer
              - `modelKey` **(obrigatório)**: `string` - The model key of the viewer
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of speaker
              - `modelKey` **(obrigatório)**: `string` - The model key of the speaker
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of bridge
              - `modelKey` **(obrigatório)**: `string` - The model key of the bridge
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of sensor
              - `modelKey` **(obrigatório)**: `string` - The model key of the sensor
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of siren
              - `modelKey` **(obrigatório)**: `string` - The model key of the siren
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of fob
              - `modelKey` **(obrigatório)**: `string` - The model key of the fob
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of relay
              - `modelKey` **(obrigatório)**: `string` - The model key of the relay
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of device
              - `modelKey` **(obrigatório)**: `string` - The model key of the aiprocessor
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of device
              - `modelKey` **(obrigatório)**: `string` - The model key of the aiport
            - **variante**:
              - `id` **(obrigatório)**: `string` - The primary key of linkStation
              - `modelKey` **(obrigatório)**: `string` - The model key of the linkstation
  - **variante**:
    - _um de (type):_
      - **variante**:
        - `type` **(obrigatório)**: `string`
        - `item` **(obrigatório)**
          - _um de (variantes):_
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the nvr
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `doorbellSettings` **(obrigatório)**: `object`
                - `defaultMessageText`: `string` - Default text to display on the LCD screen.
                - `defaultMessageResetTimeoutMs`: `number` - Default timeout for resetting LCD screen to the default message.
                - `customMessages`: `array` - A list of custom doorbell messages.
                - `customImages`: `array` - A list of custom doorbell images for client preview.
              - `armMode` **(obrigatório)**: `object`
                - `status` **(obrigatório)**: `string` enum: arming, armed, breach, disabled
                - `armProfileId` **(obrigatório)**: `string|null`
                - `armedAt` **(obrigatório)**: `number|null`
                - `willBeArmedAt` **(obrigatório)**: `number|null`
                - `breachDetectedAt` **(obrigatório)**: `number|null`
                - `breachEventCount` **(obrigatório)**: `number`
                - `breachTriggerEventId` **(obrigatório)**: `string|null`
                - `breachEventId` **(obrigatório)**: `string|null`
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the camera
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `isMicEnabled` **(obrigatório)**: `boolean` - Whether or not the microphone on camera is enabled
              - `osdSettings` **(obrigatório)**: `object` - On Screen Display settings.
                - `isNameEnabled` **(obrigatório)**: `boolean` - Whether to show the name in the OSD.
                - `isDateEnabled` **(obrigatório)**: `boolean` - Whether to show the date in the OSD.
                - `isLogoEnabled` **(obrigatório)**: `boolean` - Whether to show the logo in the bottom right corner.
                - `isDebugEnabled` **(obrigatório)**: `boolean` - Whether debug info is enabled.
                - `overlayLocation` **(obrigatório)**: `string` enum: topLeft, topMiddle, topRight, bottomLeft, bottomMiddle, bottomRight - The location of the overlay on the screen.
              - `ledSettings` **(obrigatório)**: `object` - LED settings.
                - `isEnabled` **(obrigatório)**: `boolean` - Indicates whether the status LED is enabled.
                - `welcomeLed` **(obrigatório)**: `boolean` - Indicates whether the welcome LED is enabled.
                - `floodLed` **(obrigatório)**: `boolean` - Indicates whether the flood LED is enabled.
              - `lcdMessage` **(obrigatório)**: `object`
                - `type`: `string` enum: LEAVE_PACKAGE_AT_DOOR, DO_NOT_DISTURB, CUSTOM_MESSAGE, IMAGE
                - `resetAt`: `number|null` - UNIX timestamp when doorbell message should be removed (if not set then `nvr.doorbellSettings.defaultMessageResetTimeoutMs` is used, if set to `null` then in…
                - `text`: `string`
              - `micVolume` **(obrigatório)**: `number` - Mic volume: a number from 0-100.
              - `activePatrolSlot` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `number`
                  - **variante**:
                    - `null`
              - `videoMode` **(obrigatório)**: `string` enum: default, highFps, sport, slowShutter, lprReflex, lprNoneReflex - Current video mode of the camera
              - `hdrType` **(obrigatório)**: `string` enum: auto, on, off - High Dynamic Range (HDR) mode setting.
              - `featureFlags` **(obrigatório)**: `object`
                - `supportFullHdSnapshot` **(obrigatório)**: `boolean` - Whether camera support full HD or higher resolution snapshot
                - `hasHdr` **(obrigatório)**: `boolean` - Whether the camera supports High Dynamic Range mode
                - `smartDetectTypes` **(obrigatório)**: `array` - What smart detection object types do the camera support.
                - `smartDetectAudioTypes` **(obrigatório)**: `array` - What smart detection audio types do the camera support.
                - `videoModes` **(obrigatório)**: `array` - A list of supported video modes by the camera
                - `hasMic` **(obrigatório)**: `boolean` - Whether the camera has a microphone
                - `hasLedStatus` **(obrigatório)**: `boolean` - Whether the camera has LED status
                - `hasSpeaker` **(obrigatório)**: `boolean` - Whether the camera has a speaker to support talkback
              - `smartDetectSettings` **(obrigatório)**: `object` - Smart detection settings for the camera.
                - `objectTypes` **(obrigatório)**: `array`
                - `audioTypes` **(obrigatório)**: `array`
              - `hasPackageCamera` **(obrigatório)**: `boolean` - Whether the camera has a package camera.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the chime
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `cameraIds` **(obrigatório)**: `array` - The list of (doorbell-only) cameras which this chime is paired to.
                - _array de_ `string`:
              - `ringSettings` **(obrigatório)**: `array` - List of custom ringtone settings for (doorbell-only) cameras paired to this chime.
                - _array de_ `object`:
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the light
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `lightModeSettings` **(obrigatório)**: `object` - Settings for when and how your light gets activated
                - `mode`: When will floodlight turn on.
                - `enableAt`: At what time is the lighting mode relevant and acted upon (this has no effect when mode is off).
              - `lightDeviceSettings` **(obrigatório)**: `object` - Hardware settings for light device.
                - `isIndicatorEnabled`: `boolean` - Turn on/off floodlight status LED indicator.
                - `pirDuration`: `number` - How long the light stays on after a motion event in milliseconds.
                - `pirSensitivity`: `number` - How sensitive is the PIR to motion (0-100)%.
                - `ledLevel`: `number` - Brightness level of the main LED (1-6).
              - `isDark` **(obrigatório)**: `boolean` - Whether the light is currently sensing that it's in a dark scene.
              - `isLightOn` **(obrigatório)**: `boolean` - Whether the light has its main LED currently enabled.
              - `isLightForceEnabled` **(obrigatório)**: `boolean` - Whether the light has its main LED currently force-enabled.
              - `lastMotion` **(obrigatório)**: `number|null` - Unix timestamp of the last time the PIR motion-detection was triggered.
              - `isPirMotionDetected` **(obrigatório)**: `boolean` - Whether the light PIR is currently detecting motion
              - `camera` **(obrigatório)**: Which camera is configured to be paired to this light.
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the viewer
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `liveview` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `streamLimit` **(obrigatório)**: `number` - Count of maximum supported parallel live streams.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the speaker
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `volume` **(obrigatório)**: `integer` - Speaker volume: a number from 0-100.
              - `micVolume` **(obrigatório)**: `integer` - Mic volume: a number from 0-100.
              - `isMicEnabled` **(obrigatório)**: `boolean` - Whether or not the microphone on the speaker is enabled.
              - `speakerState` **(obrigatório)**: `object` - Real-time state of Speaker
                - `status` **(obrigatório)**: `string` enum: idle, streaming, playing, tts_playing, uploading - Current status of the speaker
                - `mode` **(obrigatório)**: `string` enum: listen, talk - Current mode of the speaker
              - `featureFlags` **(obrigatório)**: `object` - Feature flags of the speaker
                - `hasMic` **(obrigatório)**: `boolean` - Whether the device has a microphone.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the bridge
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `platform` **(obrigatório)**: `string|null` - The bridge platform
              - `clients` **(obrigatório)**: `array` - Array of IoT devices mac that bridge is reserving for
                - _array de_ `string`:
              - `maxClients` **(obrigatório)**: `number` - The max acceptable client number of a V2 bridge. V1 bridge does not support this feature.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the sensor
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `mountType` **(obrigatório)**: `string` enum: door, window, garage, leak, none - Mounting type of the sensor.
              - `batteryStatus` **(obrigatório)**: `object` - [DEPRECATED] Use wirelessConnectionState.batteryStatus instead. Battery status.
                - `percentage`: `number|null` - Battery charge level from 0 to 100 (%).
                - `isLow`: `boolean` - Low battery charge level flag.
              - `stats` **(obrigatório)**: `object` - Sensor statistics.
                - `light`: `object` - Ambient light value (Lux).
                - `humidity`: `object` - Ambient light value (Lux).
                - `temperature`: `object` - Ambient light value (Lux).
              - `lightSettings` **(obrigatório)**: `object` - Ambient light sensor settings.
                - `isEnabled`: `boolean` - Enable ambient light sensor.
                - `margin`: `number` - Ambient light threshold detection hysteresis margin (Lux). Read-only value decided by sensor implementation.
                - `lowThreshold`: `number|null` - Ambient light interrupt threshold low level from 1 to 503192 (Lux).
                - `highThreshold`: `number|null` - Ambient light interrupt threshold high level from 1 to 503192 (Lux).
              - `humiditySettings` **(obrigatório)**: `object` - Relative humidity sensor settings.
                - `isEnabled`: `boolean` - Enable relative humidity sensor.
                - `margin`: `number` - Humidity threshold detection hysteresis margin (%). Read-only value decided by sensor implementation.
                - `lowThreshold`: `number|null` - Humidity low level threshold from 1 to 99 (%).
                - `highThreshold`: `number|null` - Humidity high level threshold from 1 to 99 (%).
              - `temperatureSettings` **(obrigatório)**: `object` - Temperature sensor settings.
                - `isEnabled`: `boolean` - Enable temperature sensor.
                - `margin`: `number` - Temperature threshold detection hysteresis margin (C). Read-only value decided by sensor implementation.
                - `lowThreshold`: `number|null` - Temperature low level threshold from -39 to 124 (C).
                - `highThreshold`: `number|null` - Temperature high level threshold from -39 to 124 (C).
              - `isOpened` **(obrigatório)**: `boolean|null` - Whether the door/window/garage is opened.
              - `openStatusChangedAt` **(obrigatório)**: `number|null` - Unix timestamp when the door/window/garage was last opened or closed, nullable.
              - `isMotionDetected` **(obrigatório)**: `boolean` - Whether sensor is currently detecting the motion.
              - `motionDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the last motion was detected.
              - `motionSettings` **(obrigatório)**: `object` - Motion sensor settings.
                - `isEnabled`: `boolean` - Enable motion sensor.
                - `sensitivity`: `number` - Motion sensitivity (0-100) used when system is not armed or when no armed override is set.
                - `sensitivityWhenArmed`: `number` - Motion sensitivity (0-100) used when the system is armed and `hasCustomSensitivityWhenArmed` is true on the sensor.
              - `glassBreakSettings` **(obrigatório)**: `object` - Glass break sensor settings.
                - `isEnabled`: `boolean` - Enable glass break sensor.
                - `sensitivity`: `number` - Glass break sensitivity (0-100) used when system is not armed or when no armed override is set.
                - `sensitivityWhenArmed`: `number` - Glass break sensitivity (0-100) used when the system is armed and `hasCustomSensitivityWhenArmed` is true on the sensor.
              - `scheduleMode` **(obrigatório)**: `string` enum: always, when_armed - When armed-mode detection runs: `always` or only `when_armed`. Applies to both glass break and motion together.
              - `armProfileIds` **(obrigatório)**: `array|null` - When `scheduleMode` is `when_armed`, restricts armed-mode detection to these arm profile ids. Empty or null = all profiles.
              - `hasCustomSensitivityWhenArmed` **(obrigatório)**: `boolean` - When true, glass break and motion both use their respective `sensitivityWhenArmed` value while the system is armed.
              - `alarmTriggeredAt` **(obrigatório)**: `number|null` - Unix timestamp when the smoke or carbon monoxide alarm was triggered, nullable.
              - `alarmSettings` **(obrigatório)**: `object` - Smoke and carbon monoxide alarm sensor settings.
                - `isEnabled`: `boolean` - Enable smoke and carbon monoxide alarm sensor.
              - `leakDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected a water leak, nullable.
              - `externalLeakDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected an external water leak, nullable.
              - `leakSettings` **(obrigatório)**: `object` - Leak sensor settings.
                - `isInternalEnabled`: `boolean` - Enable internal water leak detection.
                - `isExternalEnabled`: `boolean` - Enable external water leak detection.
              - `tamperingDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected tampering, nullable.
              - `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
                - `signalState` **(obrigatório)**: `object` - Signal state.
                - `batteryStatus` **(obrigatório)**: `object` - Battery status.
                - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the siren
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `volume` **(obrigatório)**: `integer` - Volume: a number from 1-100.
              - `ledSettings` **(obrigatório)**: `object` - Status LED settings.
                - `isEnabled` **(obrigatório)**: `boolean` - Enable status LED.
              - `sirenStatus` **(obrigatório)**: `object` - Status of the siren
                - `isActive` **(obrigatório)**: `boolean` - Whether the siren is active.
                - `activatedAt` **(obrigatório)**: `number|null` - Timestamp when the siren was activated.
                - `duration` **(obrigatório)**
              - `connectionType` **(obrigatório)**: `string` enum: ucp4, lora - The connection type of the siren.
              - `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
                - `signalState` **(obrigatório)**: `object` - Signal state.
                - `batteryStatus` **(obrigatório)**: `object` - Battery status.
                - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the fob
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `awayState` **(obrigatório)**: `string` enum: ONLINE, RECENTLY_SEEN, NO_RECENT_HEARTBEAT, DEVICE_LOST - Fob presence/away state.
              - `buttonLabels` **(obrigatório)**: `string` enum: securityActions, positionHint - Label style applied when this fob is rendered in button selection lists.
              - `featureFlags` **(obrigatório)**: `object` - Feature flags for the fob.
                - `buttons` **(obrigatório)**: `array` - Available button types on the fob.
              - `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
                - `signalState` **(obrigatório)**: `object` - Signal state.
                - `batteryStatus` **(obrigatório)**: `object` - Battery status.
                - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the relay
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `ledSettings` **(obrigatório)**: `object` - Status LED settings.
                - `isEnabled` **(obrigatório)**: `boolean` - Enable status LED.
              - `outputs` **(obrigatório)**: `array`
                - _array de_ `object`:
              - `inputs` **(obrigatório)**: `array`
                - _array de_ `object`:
              - `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
                - `signalState` **(obrigatório)**: `object` - Signal state.
                - `batteryStatus` **(obrigatório)**: `object` - Battery status.
                - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the aiprocessor
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the aiport
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the linkstation
              - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
              - `isAlarmHub` **(obrigatório)**: `boolean` - Whether the linkstation is an alarm hub.
              - `ledSettings` **(obrigatório)**: `object` - Status LED settings.
                - `isEnabled` **(obrigatório)**: `boolean` - Whether the status LED is enabled.
              - `lastEvent` **(obrigatório)**: `number|null` - Timestamp when any last event was detected.
              - `alarmHub`: `object` - Alarm hub status and configuration. Only present when isAlarmHub is true.
                - `armed` **(obrigatório)**: `string` enum: on, off
                - `battery`: `object`
                - `buckboost` **(obrigatório)**: `string` enum: on, off
                - `connector`: `object`
                - `cover`: `object`
                - `currentMeterChannelStatus` **(obrigatório)**: `object`
                - `currentMeterStatus` **(obrigatório)**: `object`
                - `inputPower`: `object`
                - `poeout`: `object`
                - `powerMeter` **(obrigatório)**: `object`
                - `output` **(obrigatório)**: `object`
                - `input` **(obrigatório)**: `object`
                - `inputTerminalStatus`: `object`
                - `outputTerminalStatus`: `object`
                - `emergencyTerminalStatus`: `object|null`
                - `auxiliaryPowerTerminalStatus`: `object`
      - **variante**:
        - `type` **(obrigatório)**: `string`
        - `item` **(obrigatório)**
          - _um de (variantes):_
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the nvr
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `doorbellSettings`: `object`
                - `defaultMessageText`: `string` - Default text to display on the LCD screen.
                - `defaultMessageResetTimeoutMs`: `number` - Default timeout for resetting LCD screen to the default message.
                - `customMessages`: `array` - A list of custom doorbell messages.
                - `customImages`: `array` - A list of custom doorbell images for client preview.
              - `armMode`: `object`
                - `status` **(obrigatório)**: `string` enum: arming, armed, breach, disabled
                - `armProfileId` **(obrigatório)**: `string|null`
                - `armedAt` **(obrigatório)**: `number|null`
                - `willBeArmedAt` **(obrigatório)**: `number|null`
                - `breachDetectedAt` **(obrigatório)**: `number|null`
                - `breachEventCount` **(obrigatório)**: `number`
                - `breachTriggerEventId` **(obrigatório)**: `string|null`
                - `breachEventId` **(obrigatório)**: `string|null`
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the camera
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `isMicEnabled`: `boolean` - Whether or not the microphone on camera is enabled
              - `osdSettings`: `object` - On Screen Display settings.
                - `isNameEnabled` **(obrigatório)**: `boolean` - Whether to show the name in the OSD.
                - `isDateEnabled` **(obrigatório)**: `boolean` - Whether to show the date in the OSD.
                - `isLogoEnabled` **(obrigatório)**: `boolean` - Whether to show the logo in the bottom right corner.
                - `isDebugEnabled` **(obrigatório)**: `boolean` - Whether debug info is enabled.
                - `overlayLocation` **(obrigatório)**: `string` enum: topLeft, topMiddle, topRight, bottomLeft, bottomMiddle, bottomRight - The location of the overlay on the screen.
              - `ledSettings`: `object` - LED settings.
                - `isEnabled` **(obrigatório)**: `boolean` - Indicates whether the status LED is enabled.
                - `welcomeLed` **(obrigatório)**: `boolean` - Indicates whether the welcome LED is enabled.
                - `floodLed` **(obrigatório)**: `boolean` - Indicates whether the flood LED is enabled.
              - `lcdMessage`: `object`
                - `type`: `string` enum: LEAVE_PACKAGE_AT_DOOR, DO_NOT_DISTURB, CUSTOM_MESSAGE, IMAGE
                - `resetAt`: `number|null` - UNIX timestamp when doorbell message should be removed (if not set then `nvr.doorbellSettings.defaultMessageResetTimeoutMs` is used, if set to `null` then in…
                - `text`: `string`
              - `micVolume`: `number` - Mic volume: a number from 0-100.
              - `activePatrolSlot`
                - _um de (variantes):_
                  - **variante**:
                    - `number`
                  - **variante**:
                    - `null`
              - `videoMode`: `string` enum: default, highFps, sport, slowShutter, lprReflex, lprNoneReflex - Current video mode of the camera
              - `hdrType`: `string` enum: auto, on, off - High Dynamic Range (HDR) mode setting.
              - `featureFlags`: `object`
                - `supportFullHdSnapshot` **(obrigatório)**: `boolean` - Whether camera support full HD or higher resolution snapshot
                - `hasHdr` **(obrigatório)**: `boolean` - Whether the camera supports High Dynamic Range mode
                - `smartDetectTypes` **(obrigatório)**: `array` - What smart detection object types do the camera support.
                - `smartDetectAudioTypes` **(obrigatório)**: `array` - What smart detection audio types do the camera support.
                - `videoModes` **(obrigatório)**: `array` - A list of supported video modes by the camera
                - `hasMic` **(obrigatório)**: `boolean` - Whether the camera has a microphone
                - `hasLedStatus` **(obrigatório)**: `boolean` - Whether the camera has LED status
                - `hasSpeaker` **(obrigatório)**: `boolean` - Whether the camera has a speaker to support talkback
              - `smartDetectSettings`: `object` - Smart detection settings for the camera.
                - `objectTypes` **(obrigatório)**: `array`
                - `audioTypes` **(obrigatório)**: `array`
              - `hasPackageCamera`: `boolean` - Whether the camera has a package camera.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the chime
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `cameraIds`: `array` - The list of (doorbell-only) cameras which this chime is paired to.
                - _array de_ `string`:
              - `ringSettings`: `array` - List of custom ringtone settings for (doorbell-only) cameras paired to this chime.
                - _array de_ `object`:
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the light
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `lightModeSettings`: `object` - Settings for when and how your light gets activated
                - `mode`: When will floodlight turn on.
                - `enableAt`: At what time is the lighting mode relevant and acted upon (this has no effect when mode is off).
              - `lightDeviceSettings`: `object` - Hardware settings for light device.
                - `isIndicatorEnabled`: `boolean` - Turn on/off floodlight status LED indicator.
                - `pirDuration`: `number` - How long the light stays on after a motion event in milliseconds.
                - `pirSensitivity`: `number` - How sensitive is the PIR to motion (0-100)%.
                - `ledLevel`: `number` - Brightness level of the main LED (1-6).
              - `isDark`: `boolean` - Whether the light is currently sensing that it's in a dark scene.
              - `isLightOn`: `boolean` - Whether the light has its main LED currently enabled.
              - `isLightForceEnabled`: `boolean` - Whether the light has its main LED currently force-enabled.
              - `lastMotion`: `number|null` - Unix timestamp of the last time the PIR motion-detection was triggered.
              - `isPirMotionDetected`: `boolean` - Whether the light PIR is currently detecting motion
              - `camera`: Which camera is configured to be paired to this light.
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the viewer
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `liveview`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `streamLimit`: `number` - Count of maximum supported parallel live streams.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the speaker
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `volume`: `integer` - Speaker volume: a number from 0-100.
              - `micVolume`: `integer` - Mic volume: a number from 0-100.
              - `isMicEnabled`: `boolean` - Whether or not the microphone on the speaker is enabled.
              - `speakerState`: `object` - Real-time state of Speaker
                - `status` **(obrigatório)**: `string` enum: idle, streaming, playing, tts_playing, uploading - Current status of the speaker
                - `mode` **(obrigatório)**: `string` enum: listen, talk - Current mode of the speaker
              - `featureFlags`: `object` - Feature flags of the speaker
                - `hasMic` **(obrigatório)**: `boolean` - Whether the device has a microphone.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the bridge
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `platform`: `string|null` - The bridge platform
              - `clients`: `array` - Array of IoT devices mac that bridge is reserving for
                - _array de_ `string`:
              - `maxClients`: `number` - The max acceptable client number of a V2 bridge. V1 bridge does not support this feature.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the sensor
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `mountType`: `string` enum: door, window, garage, leak, none - Mounting type of the sensor.
              - `batteryStatus`: `object` - [DEPRECATED] Use wirelessConnectionState.batteryStatus instead. Battery status.
                - `percentage`: `number|null` - Battery charge level from 0 to 100 (%).
                - `isLow`: `boolean` - Low battery charge level flag.
              - `stats`: `object` - Sensor statistics.
                - `light`: `object` - Ambient light value (Lux).
                - `humidity`: `object` - Ambient light value (Lux).
                - `temperature`: `object` - Ambient light value (Lux).
              - `lightSettings`: `object` - Ambient light sensor settings.
                - `isEnabled`: `boolean` - Enable ambient light sensor.
                - `margin`: `number` - Ambient light threshold detection hysteresis margin (Lux). Read-only value decided by sensor implementation.
                - `lowThreshold`: `number|null` - Ambient light interrupt threshold low level from 1 to 503192 (Lux).
                - `highThreshold`: `number|null` - Ambient light interrupt threshold high level from 1 to 503192 (Lux).
              - `humiditySettings`: `object` - Relative humidity sensor settings.
                - `isEnabled`: `boolean` - Enable relative humidity sensor.
                - `margin`: `number` - Humidity threshold detection hysteresis margin (%). Read-only value decided by sensor implementation.
                - `lowThreshold`: `number|null` - Humidity low level threshold from 1 to 99 (%).
                - `highThreshold`: `number|null` - Humidity high level threshold from 1 to 99 (%).
              - `temperatureSettings`: `object` - Temperature sensor settings.
                - `isEnabled`: `boolean` - Enable temperature sensor.
                - `margin`: `number` - Temperature threshold detection hysteresis margin (C). Read-only value decided by sensor implementation.
                - `lowThreshold`: `number|null` - Temperature low level threshold from -39 to 124 (C).
                - `highThreshold`: `number|null` - Temperature high level threshold from -39 to 124 (C).
              - `isOpened`: `boolean|null` - Whether the door/window/garage is opened.
              - `openStatusChangedAt`: `number|null` - Unix timestamp when the door/window/garage was last opened or closed, nullable.
              - `isMotionDetected`: `boolean` - Whether sensor is currently detecting the motion.
              - `motionDetectedAt`: `number|null` - Unix timestamp when the last motion was detected.
              - `motionSettings`: `object` - Motion sensor settings.
                - `isEnabled`: `boolean` - Enable motion sensor.
                - `sensitivity`: `number` - Motion sensitivity (0-100) used when system is not armed or when no armed override is set.
                - `sensitivityWhenArmed`: `number` - Motion sensitivity (0-100) used when the system is armed and `hasCustomSensitivityWhenArmed` is true on the sensor.
              - `glassBreakSettings`: `object` - Glass break sensor settings.
                - `isEnabled`: `boolean` - Enable glass break sensor.
                - `sensitivity`: `number` - Glass break sensitivity (0-100) used when system is not armed or when no armed override is set.
                - `sensitivityWhenArmed`: `number` - Glass break sensitivity (0-100) used when the system is armed and `hasCustomSensitivityWhenArmed` is true on the sensor.
              - `scheduleMode`: `string` enum: always, when_armed - When armed-mode detection runs: `always` or only `when_armed`. Applies to both glass break and motion together.
              - `armProfileIds`: `array|null` - When `scheduleMode` is `when_armed`, restricts armed-mode detection to these arm profile ids. Empty or null = all profiles.
              - `hasCustomSensitivityWhenArmed`: `boolean` - When true, glass break and motion both use their respective `sensitivityWhenArmed` value while the system is armed.
              - `alarmTriggeredAt`: `number|null` - Unix timestamp when the smoke or carbon monoxide alarm was triggered, nullable.
              - `alarmSettings`: `object` - Smoke and carbon monoxide alarm sensor settings.
                - `isEnabled`: `boolean` - Enable smoke and carbon monoxide alarm sensor.
              - `leakDetectedAt`: `number|null` - Unix timestamp when the sensor detected a water leak, nullable.
              - `externalLeakDetectedAt`: `number|null` - Unix timestamp when the sensor detected an external water leak, nullable.
              - `leakSettings`: `object` - Leak sensor settings.
                - `isInternalEnabled`: `boolean` - Enable internal water leak detection.
                - `isExternalEnabled`: `boolean` - Enable external water leak detection.
              - `tamperingDetectedAt`: `number|null` - Unix timestamp when the sensor detected tampering, nullable.
              - `wirelessConnectionState`: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
                - `signalState` **(obrigatório)**: `object` - Signal state.
                - `batteryStatus` **(obrigatório)**: `object` - Battery status.
                - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the siren
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `volume`: `integer` - Volume: a number from 1-100.
              - `ledSettings`: `object` - Status LED settings.
                - `isEnabled` **(obrigatório)**: `boolean` - Enable status LED.
              - `sirenStatus`: `object` - Status of the siren
                - `isActive` **(obrigatório)**: `boolean` - Whether the siren is active.
                - `activatedAt` **(obrigatório)**: `number|null` - Timestamp when the siren was activated.
                - `duration` **(obrigatório)**
              - `connectionType`: `string` enum: ucp4, lora - The connection type of the siren.
              - `wirelessConnectionState`: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
                - `signalState` **(obrigatório)**: `object` - Signal state.
                - `batteryStatus` **(obrigatório)**: `object` - Battery status.
                - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the fob
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `awayState`: `string` enum: ONLINE, RECENTLY_SEEN, NO_RECENT_HEARTBEAT, DEVICE_LOST - Fob presence/away state.
              - `buttonLabels`: `string` enum: securityActions, positionHint - Label style applied when this fob is rendered in button selection lists.
              - `featureFlags`: `object` - Feature flags for the fob.
                - `buttons` **(obrigatório)**: `array` - Available button types on the fob.
              - `wirelessConnectionState`: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
                - `signalState` **(obrigatório)**: `object` - Signal state.
                - `batteryStatus` **(obrigatório)**: `object` - Battery status.
                - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the relay
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `ledSettings`: `object` - Status LED settings.
                - `isEnabled` **(obrigatório)**: `boolean` - Enable status LED.
              - `outputs`: `array`
                - _array de_ `object`:
              - `inputs`: `array`
                - _array de_ `object`:
              - `wirelessConnectionState`: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
                - `signalState` **(obrigatório)**: `object` - Signal state.
                - `batteryStatus` **(obrigatório)**: `object` - Battery status.
                - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the aiprocessor
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the aiport
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the linkstation
              - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
              - `name`
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - `null`
              - `mac`: `string` - The primary MAC address of the device.
              - `isAlarmHub`: `boolean` - Whether the linkstation is an alarm hub.
              - `ledSettings`: `object` - Status LED settings.
                - `isEnabled` **(obrigatório)**: `boolean` - Whether the status LED is enabled.
              - `lastEvent`: `number|null` - Timestamp when any last event was detected.
              - `alarmHub`: `object` - Alarm hub status and configuration. Only present when isAlarmHub is true.
                - `armed` **(obrigatório)**: `string` enum: on, off
                - `battery`: `object`
                - `buckboost` **(obrigatório)**: `string` enum: on, off
                - `connector`: `object`
                - `cover`: `object`
                - `currentMeterChannelStatus` **(obrigatório)**: `object`
                - `currentMeterStatus` **(obrigatório)**: `object`
                - `inputPower`: `object`
                - `poeout`: `object`
                - `powerMeter` **(obrigatório)**: `object`
                - `output` **(obrigatório)**: `object`
                - `input` **(obrigatório)**: `object`
                - `inputTerminalStatus`: `object`
                - `outputTerminalStatus`: `object`
                - `emergencyTerminalStatus`: `object|null`
                - `auxiliaryPowerTerminalStatus`: `object`
      - **variante**:
        - `type` **(obrigatório)**: `string`
        - `item` **(obrigatório)**
          - _um de (variantes):_
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the nvr
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the camera
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the chime
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the light
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the viewer
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the speaker
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the bridge
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the sensor
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the siren
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the fob
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the relay
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the aiprocessor
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the aiport
            - **variante**:
              - `id` **(obrigatório)**
                - _um de (variantes):_
                  - **variante**:
                    - `string`
                  - **variante**:
                    - _array de_ `string`:
              - `modelKey` **(obrigatório)**: `string` - The model key of the linkstation

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/subscribe/devices" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/subscribe/devices" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get Protect event messages

`GET /v1/subscribe/events`  ·  operationId: ``

A WebSocket subscription that broadcasts Protect events

**Resposta 200** - Success response

- _um de (type):_
  - **variante**:
    - `type` **(obrigatório)**: `string`
    - `item` **(obrigatório)**
      - _um de (type):_
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `sensorType` **(obrigatório)**: `object` - Name of the metric measured by the sensor
              - `text` **(obrigatório)**: `string` enum: temperature, light, humidity, aqi, vape, tvoc, pm1p0, pm2p5, pm4p0, pm10p0, co2, voc
            - `sensorValue` **(obrigatório)**: `object`
              - `text` **(obrigatório)**: `number` - Decimal value of the metric measured by the sensor
            - `status` **(obrigatório)**: `object`
              - `text` **(obrigatório)**: `string` enum: neutral, low, safe, high, unknown - What range does the measured metric fall into
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `sensorMountType` **(obrigatório)**: `object`
              - `text` **(obrigatório)**: `string` enum: door, window, garage, leak, none - Mounting type of the sensor.
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `sensorBatteryPercentage` **(obrigatório)**: `object` - Decimal value of the available sensor battery percentage
              - `number` **(obrigatório)**: `number`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `alarmType` **(obrigatório)**: `object` - A type of sensor alarm
              - `text` **(obrigatório)**: `string` enum: smoke, CO, glassBreak, sensorButtonPress, tamper, short, cut
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `sensorMountType` **(obrigatório)**: `object`
              - `text` **(obrigatório)**: `string` enum: door, window, garage, leak, none - Mounting type of the sensor.
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `sensorMountType` **(obrigatório)**: `object`
              - `text` **(obrigatório)**: `string` enum: door, window, garage, leak, none - Mounting type of the sensor.
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `source`: `string` enum: remote, local
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `button` **(obrigatório)**: `object` - The button that was pressed
              - `text` **(obrigatório)**: `string` enum: function, alarmHubButton, arm, disarm, night, panic, left, right, input1, input2
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `smartDetectTypes` **(obrigatório)**: `array|null`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `smartDetectTypes` **(obrigatório)**: `array|null`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `smartDetectTypes` **(obrigatório)**: `array|null`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `smartDetectTypes` **(obrigatório)**: `array|null`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `inputState` **(obrigatório)**: `object` - The state of the relay input circuit
              - `text` **(obrigatório)**: `string` enum: circuitClosed, circuitOpen
            - `inputChannel` **(obrigatório)**: `object` - The channel index of the relay input
              - `text` **(obrigatório)**: `string`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata`: `object`
            - `pin` **(obrigatório)**: `object` - The alarm hub input pin channel
              - `text` **(obrigatório)**: `string`
            - `status` **(obrigatório)**: `object` - The status of the alarm hub input
              - `text` **(obrigatório)**: `string`
            - `deviceId` **(obrigatório)**: `object` - The device ID of the alarm hub
              - `text` **(obrigatório)**: `string`
            - `deviceName` **(obrigatório)**: `object` - The configured name of the input
              - `text` **(obrigatório)**: `string`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata`: `object`
            - `pin` **(obrigatório)**: `object` - The alarm hub input pin channel
              - `text` **(obrigatório)**: `string`
            - `status` **(obrigatório)**: `object` - The status of the alarm hub input
              - `text` **(obrigatório)**: `string`
            - `deviceId` **(obrigatório)**: `object` - The device ID of the alarm hub
              - `text` **(obrigatório)**: `string`
            - `deviceName` **(obrigatório)**: `object` - The configured name of the input
              - `text` **(obrigatório)**: `string`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata`: `object`
            - `pin` **(obrigatório)**: `object` - The alarm hub input pin channel
              - `text` **(obrigatório)**: `string`
            - `status` **(obrigatório)**: `object` - The status of the alarm hub input
              - `text` **(obrigatório)**: `string`
            - `deviceId` **(obrigatório)**: `object` - The device ID of the alarm hub
              - `text` **(obrigatório)**: `string`
            - `deviceName` **(obrigatório)**: `object` - The configured name of the input
              - `text` **(obrigatório)**: `string`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata`: `object`
            - `pin` **(obrigatório)**: `object` - The alarm hub input pin channel
              - `text` **(obrigatório)**: `string`
            - `status` **(obrigatório)**: `object` - The status of the alarm hub input
              - `text` **(obrigatório)**: `string`
            - `alarmType` **(obrigatório)**: `object` - A type of sensor alarm
              - `text` **(obrigatório)**: `string` enum: smoke, CO, glassBreak, sensorButtonPress, tamper, short, cut
            - `deviceId` **(obrigatório)**: `object` - The device ID of the alarm hub
              - `text` **(obrigatório)**: `string`
            - `deviceName` **(obrigatório)**: `object` - The configured name of the input
              - `text` **(obrigatório)**: `string`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata`: `object`
            - `pin` **(obrigatório)**: `object` - The alarm hub input pin channel
              - `text` **(obrigatório)**: `string`
            - `status` **(obrigatório)**: `object` - The status of the alarm hub input
              - `text` **(obrigatório)**: `string`
            - `alarmType` **(obrigatório)**: `object` - A type of sensor alarm
              - `text` **(obrigatório)**: `string` enum: smoke, CO, glassBreak, sensorButtonPress, tamper, short, cut
            - `deviceId` **(obrigatório)**: `object` - The device ID of the alarm hub
              - `text` **(obrigatório)**: `string`
            - `deviceName` **(obrigatório)**: `object` - The configured name of the input
              - `text` **(obrigatório)**: `string`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata`: `object`
            - `pin` **(obrigatório)**: `object` - The alarm hub input pin channel
              - `text` **(obrigatório)**: `string`
            - `status` **(obrigatório)**: `object` - The status of the alarm hub input
              - `text` **(obrigatório)**: `string`
            - `button` **(obrigatório)**: `object` - The button that was pressed
              - `text` **(obrigatório)**: `string` enum: function, alarmHubButton, arm, disarm, night, panic, left, right, input1, input2
            - `alarmType` **(obrigatório)**: `object` - A type of sensor alarm
              - `text` **(obrigatório)**: `string` enum: smoke, CO, glassBreak, sensorButtonPress, tamper, short, cut
            - `deviceId` **(obrigatório)**: `object` - The device ID of the alarm hub
              - `text` **(obrigatório)**: `string`
            - `deviceName` **(obrigatório)**: `object` - The configured name of the input
              - `text` **(obrigatório)**: `string`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata`: `object`
            - `pin` **(obrigatório)**: `object` - The alarm hub input pin channel
              - `text` **(obrigatório)**: `string`
            - `status` **(obrigatório)**: `object` - The status of the alarm hub input
              - `text` **(obrigatório)**: `string`
            - `alarmType` **(obrigatório)**: `object` - A type of sensor alarm
              - `text` **(obrigatório)**: `string` enum: smoke, CO, glassBreak, sensorButtonPress, tamper, short, cut
            - `deviceId` **(obrigatório)**: `object` - The device ID of the alarm hub
              - `text` **(obrigatório)**: `string`
            - `deviceName` **(obrigatório)**: `object` - The configured name of the input
              - `text` **(obrigatório)**: `string`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `nfc` **(obrigatório)**: `object`
              - `ulpId` **(obrigatório)**: `string|null` - The unique id of the UniFi Identity user. Matches the id field of the corresponding UlpUser. Matches the ucoreUserId field of the corresponding Protect User.…
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `fingerprint` **(obrigatório)**: `object`
              - `ulpId` **(obrigatório)**: `string|null` - The unique id of the UniFi Identity user. Matches the id field of the corresponding UlpUser. Matches the ucoreUserId field of the corresponding Protect User.…
  - **variante**:
    - `type` **(obrigatório)**: `string`
    - `item` **(obrigatório)**
      - _um de (type):_
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `sensorType` **(obrigatório)**: `object` - Name of the metric measured by the sensor
              - `text` **(obrigatório)**: `string` enum: temperature, light, humidity, aqi, vape, tvoc, pm1p0, pm2p5, pm4p0, pm10p0, co2, voc
            - `sensorValue` **(obrigatório)**: `object`
              - `text` **(obrigatório)**: `number` - Decimal value of the metric measured by the sensor
            - `status` **(obrigatório)**: `object`
              - `text` **(obrigatório)**: `string` enum: neutral, low, safe, high, unknown - What range does the measured metric fall into
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `sensorMountType` **(obrigatório)**: `object`
              - `text` **(obrigatório)**: `string` enum: door, window, garage, leak, none - Mounting type of the sensor.
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `sensorBatteryPercentage` **(obrigatório)**: `object` - Decimal value of the available sensor battery percentage
              - `number` **(obrigatório)**: `number`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `alarmType` **(obrigatório)**: `object` - A type of sensor alarm
              - `text` **(obrigatório)**: `string` enum: smoke, CO, glassBreak, sensorButtonPress, tamper, short, cut
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `sensorMountType` **(obrigatório)**: `object`
              - `text` **(obrigatório)**: `string` enum: door, window, garage, leak, none - Mounting type of the sensor.
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `sensorMountType` **(obrigatório)**: `object`
              - `text` **(obrigatório)**: `string` enum: door, window, garage, leak, none - Mounting type of the sensor.
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `source`: `string` enum: remote, local
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `button` **(obrigatório)**: `object` - The button that was pressed
              - `text` **(obrigatório)**: `string` enum: function, alarmHubButton, arm, disarm, night, panic, left, right, input1, input2
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `smartDetectTypes` **(obrigatório)**: `array|null`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `smartDetectTypes` **(obrigatório)**: `array|null`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `smartDetectTypes` **(obrigatório)**: `array|null`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `smartDetectTypes` **(obrigatório)**: `array|null`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `inputState` **(obrigatório)**: `object` - The state of the relay input circuit
              - `text` **(obrigatório)**: `string` enum: circuitClosed, circuitOpen
            - `inputChannel` **(obrigatório)**: `object` - The channel index of the relay input
              - `text` **(obrigatório)**: `string`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata`: `object`
            - `pin` **(obrigatório)**: `object` - The alarm hub input pin channel
              - `text` **(obrigatório)**: `string`
            - `status` **(obrigatório)**: `object` - The status of the alarm hub input
              - `text` **(obrigatório)**: `string`
            - `deviceId` **(obrigatório)**: `object` - The device ID of the alarm hub
              - `text` **(obrigatório)**: `string`
            - `deviceName` **(obrigatório)**: `object` - The configured name of the input
              - `text` **(obrigatório)**: `string`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata`: `object`
            - `pin` **(obrigatório)**: `object` - The alarm hub input pin channel
              - `text` **(obrigatório)**: `string`
            - `status` **(obrigatório)**: `object` - The status of the alarm hub input
              - `text` **(obrigatório)**: `string`
            - `deviceId` **(obrigatório)**: `object` - The device ID of the alarm hub
              - `text` **(obrigatório)**: `string`
            - `deviceName` **(obrigatório)**: `object` - The configured name of the input
              - `text` **(obrigatório)**: `string`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata`: `object`
            - `pin` **(obrigatório)**: `object` - The alarm hub input pin channel
              - `text` **(obrigatório)**: `string`
            - `status` **(obrigatório)**: `object` - The status of the alarm hub input
              - `text` **(obrigatório)**: `string`
            - `deviceId` **(obrigatório)**: `object` - The device ID of the alarm hub
              - `text` **(obrigatório)**: `string`
            - `deviceName` **(obrigatório)**: `object` - The configured name of the input
              - `text` **(obrigatório)**: `string`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata`: `object`
            - `pin` **(obrigatório)**: `object` - The alarm hub input pin channel
              - `text` **(obrigatório)**: `string`
            - `status` **(obrigatório)**: `object` - The status of the alarm hub input
              - `text` **(obrigatório)**: `string`
            - `alarmType` **(obrigatório)**: `object` - A type of sensor alarm
              - `text` **(obrigatório)**: `string` enum: smoke, CO, glassBreak, sensorButtonPress, tamper, short, cut
            - `deviceId` **(obrigatório)**: `object` - The device ID of the alarm hub
              - `text` **(obrigatório)**: `string`
            - `deviceName` **(obrigatório)**: `object` - The configured name of the input
              - `text` **(obrigatório)**: `string`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata`: `object`
            - `pin` **(obrigatório)**: `object` - The alarm hub input pin channel
              - `text` **(obrigatório)**: `string`
            - `status` **(obrigatório)**: `object` - The status of the alarm hub input
              - `text` **(obrigatório)**: `string`
            - `alarmType` **(obrigatório)**: `object` - A type of sensor alarm
              - `text` **(obrigatório)**: `string` enum: smoke, CO, glassBreak, sensorButtonPress, tamper, short, cut
            - `deviceId` **(obrigatório)**: `object` - The device ID of the alarm hub
              - `text` **(obrigatório)**: `string`
            - `deviceName` **(obrigatório)**: `object` - The configured name of the input
              - `text` **(obrigatório)**: `string`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata`: `object`
            - `pin` **(obrigatório)**: `object` - The alarm hub input pin channel
              - `text` **(obrigatório)**: `string`
            - `status` **(obrigatório)**: `object` - The status of the alarm hub input
              - `text` **(obrigatório)**: `string`
            - `button` **(obrigatório)**: `object` - The button that was pressed
              - `text` **(obrigatório)**: `string` enum: function, alarmHubButton, arm, disarm, night, panic, left, right, input1, input2
            - `alarmType` **(obrigatório)**: `object` - A type of sensor alarm
              - `text` **(obrigatório)**: `string` enum: smoke, CO, glassBreak, sensorButtonPress, tamper, short, cut
            - `deviceId` **(obrigatório)**: `object` - The device ID of the alarm hub
              - `text` **(obrigatório)**: `string`
            - `deviceName` **(obrigatório)**: `object` - The configured name of the input
              - `text` **(obrigatório)**: `string`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata`: `object`
            - `pin` **(obrigatório)**: `object` - The alarm hub input pin channel
              - `text` **(obrigatório)**: `string`
            - `status` **(obrigatório)**: `object` - The status of the alarm hub input
              - `text` **(obrigatório)**: `string`
            - `alarmType` **(obrigatório)**: `object` - A type of sensor alarm
              - `text` **(obrigatório)**: `string` enum: smoke, CO, glassBreak, sensorButtonPress, tamper, short, cut
            - `deviceId` **(obrigatório)**: `object` - The device ID of the alarm hub
              - `text` **(obrigatório)**: `string`
            - `deviceName` **(obrigatório)**: `object` - The configured name of the input
              - `text` **(obrigatório)**: `string`
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `nfc` **(obrigatório)**: `object`
              - `ulpId` **(obrigatório)**: `string|null` - The unique id of the UniFi Identity user. Matches the id field of the corresponding UlpUser. Matches the ucoreUserId field of the corresponding Protect User.…
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of event
          - `modelKey` **(obrigatório)**: `string` - The model key of the event
          - `type` **(obrigatório)**: `string`
          - `start` **(obrigatório)**: `number` - Unix timestamp of the start time of the event.
          - `end`: `number|null` - Unix timestamp of the end time of the event.
          - `device` **(obrigatório)**: `string` - The primary key of device
          - `metadata` **(obrigatório)**: `object`
            - `fingerprint` **(obrigatório)**: `object`
              - `ulpId` **(obrigatório)**: `string|null` - The unique id of the UniFi Identity user. Matches the id field of the corresponding UlpUser. Matches the ucoreUserId field of the corresponding Protect User.…

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/subscribe/events" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/subscribe/events" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Camera PTZ control & management


### Start a camera PTZ patrol

`POST /v1/cameras/{id}/ptz/patrol/start/{slot}`  ·  operationId: ``

Start a camera PTZ patrol

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of camera |
| `slot` | path | sim | string | The slot number (0-4) of the patrol that is currently running, or null if no patrol is running |

**Resposta 204** - The camera PTZ patrol was started successfully.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/protect/integration/v1/cameras/{id}/ptz/patrol/start/{slot}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/cameras/{id}/ptz/patrol/start/{slot}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Stop active camera PTZ patrol

`POST /v1/cameras/{id}/ptz/patrol/stop`  ·  operationId: ``

Stop active camera PTZ patrol

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of camera |

**Resposta 204** - The camera PTZ patrol was stopped successfully.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/protect/integration/v1/cameras/{id}/ptz/patrol/stop" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/cameras/{id}/ptz/patrol/stop" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Move PTZ camera to preset

`POST /v1/cameras/{id}/ptz/goto/{slot}`  ·  operationId: ``

Adjust the PTZ camera position to a specified preset

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of camera |
| `slot` | path | sim | string | Which slot this preset belongs to (-1 home preset, >=0 other presets). |

**Resposta 204** - The PTZ camera was moved to the given preset successfully.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/protect/integration/v1/cameras/{id}/ptz/goto/{slot}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/cameras/{id}/ptz/goto/{slot}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Alarm manager integration


### Send a webhook to the alarm manager

`POST /v1/alarm-manager/webhook/{id}`  ·  operationId: ``

Send a webhook to the alarm manager to trigger configured alarms

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | User defined string used to trigger only specific alarms. Alarm should be configured with the same ID to be triggered. |

**Resposta 204** - Webhook was sent to alarm manager successfully

**Erros possíveis:** `400`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/protect/integration/v1/alarm-manager/webhook/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/alarm-manager/webhook/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Arm profile management


### Get all arm profiles

`GET /v1/arm-profiles`  ·  operationId: ``

Get a list of all arm profiles. Only available when using local alarm manager.

**Resposta 200** - Success response

- _array de_ `object`:
  - `id` **(obrigatório)**: `string` - The primary key of armProfile
  - `name` **(obrigatório)**: `string` - Name of the arm profile.
  - `automations` **(obrigatório)**: `array` - List of automation IDs associated with this arm profile.
    - _array de_ `string`:
      - `string`
  - `creator` **(obrigatório)**
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`
  - `schedules` **(obrigatório)**: `array` - List of arm schedules.
    - _array de_ `object`:
      - `start` **(obrigatório)**: `string` - Cron expression for the start time.
      - `end` **(obrigatório)**: `string` - Cron expression for the end time.
  - `recordEverything` **(obrigatório)**: `boolean` - Whether to record everything when this arm profile is active.
  - `activationDelay` **(obrigatório)**: Activation delay in milliseconds. Allowed values: 0 (none), 60000 (1 min), 300000 (5 min), 600000 (10 min).
    - _um de (variantes):_
      - **variante**:
        - `number`
      - **variante**:
        - `number`
      - **variante**:
        - `number`
      - **variante**:
        - `number`
  - `createdAt` **(obrigatório)**: `number` - Arm profile creation time.
  - `updatedAt` **(obrigatório)**: `number` - Arm profile update time.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/arm-profiles" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/arm-profiles" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Create arm profile

`POST /v1/arm-profiles`  ·  operationId: ``

Create a new arm profile. Only available when using local alarm manager.

**Corpo da requisição** (`application/json`)

- `name` **(obrigatório)**: `string` - Name of the arm profile.
- `automations` **(obrigatório)**: `array` - List of automation IDs associated with this arm profile.
  - _array de_ `string`:
    - `string`
- `schedules` **(obrigatório)**: `array` - List of arm schedules.
  - _array de_ `object`:
    - `start` **(obrigatório)**: `string` - Cron expression for the start time.
    - `end` **(obrigatório)**: `string` - Cron expression for the end time.
- `recordEverything` **(obrigatório)**: `boolean` - Whether to record everything when this arm profile is active.
- `activationDelay` **(obrigatório)**: Activation delay in milliseconds. Allowed values: 0 (none), 60000 (1 min), 300000 (5 min), 600000 (10 min).
  - _um de (variantes):_
    - **variante**:
      - `number`
    - **variante**:
      - `number`
    - **variante**:
      - `number`
    - **variante**:
      - `number`

**Resposta 201**

- `id` **(obrigatório)**: `string` - The primary key of armProfile
- `name` **(obrigatório)**: `string` - Name of the arm profile.
- `automations` **(obrigatório)**: `array` - List of automation IDs associated with this arm profile.
  - _array de_ `string`:
    - `string`
- `creator` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `schedules` **(obrigatório)**: `array` - List of arm schedules.
  - _array de_ `object`:
    - `start` **(obrigatório)**: `string` - Cron expression for the start time.
    - `end` **(obrigatório)**: `string` - Cron expression for the end time.
- `recordEverything` **(obrigatório)**: `boolean` - Whether to record everything when this arm profile is active.
- `activationDelay` **(obrigatório)**: Activation delay in milliseconds. Allowed values: 0 (none), 60000 (1 min), 300000 (5 min), 600000 (10 min).
  - _um de (variantes):_
    - **variante**:
      - `number`
    - **variante**:
      - `number`
    - **variante**:
      - `number`
    - **variante**:
      - `number`
- `createdAt` **(obrigatório)**: `number` - Arm profile creation time.
- `updatedAt` **(obrigatório)**: `number` - Arm profile update time.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/protect/integration/v1/arm-profiles" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/arm-profiles" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Set current arm profile

`PATCH /v1/arm-profiles/settings`  ·  operationId: ``

Set the current arm profile to be used when enabling the arm alarm. Only available when using local alarm manager.

**Corpo da requisição** (`application/json`)

- `armProfileId` **(obrigatório)**: `string` - The primary key of armProfile

**Resposta 204** - Arm profile settings updated successfully

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PATCH "https://$UNIFI_HOST/proxy/protect/integration/v1/arm-profiles/settings" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PATCH "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/arm-profiles/settings" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Delete arm profile

`DELETE /v1/arm-profiles/{id}`  ·  operationId: ``

Delete an arm profile by ID. Only available when using local alarm manager.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of armProfile |

**Resposta 204** - Arm profile deleted successfully

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X DELETE "https://$UNIFI_HOST/proxy/protect/integration/v1/arm-profiles/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X DELETE "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/arm-profiles/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Update arm profile

`PATCH /v1/arm-profiles/{id}`  ·  operationId: ``

Update an existing arm profile. Only available when using local alarm manager.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of armProfile |

**Corpo da requisição** (`application/json`)

- `name`: `string` - Name of the arm profile.
- `automations`: `array` - List of automation IDs associated with this arm profile.
  - _array de_ `string`:
    - `string`
- `schedules`: `array` - List of arm schedules.
  - _array de_ `object`:
    - `start` **(obrigatório)**: `string` - Cron expression for the start time.
    - `end` **(obrigatório)**: `string` - Cron expression for the end time.
- `recordEverything`: `boolean` - Whether to record everything when this arm profile is active.
- `activationDelay`: Activation delay in milliseconds. Allowed values: 0 (none), 60000 (1 min), 300000 (5 min), 600000 (10 min).
  - _um de (variantes):_
    - **variante**:
      - `number`
    - **variante**:
      - `number`
    - **variante**:
      - `number`
    - **variante**:
      - `number`

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of armProfile
- `name` **(obrigatório)**: `string` - Name of the arm profile.
- `automations` **(obrigatório)**: `array` - List of automation IDs associated with this arm profile.
  - _array de_ `string`:
    - `string`
- `creator` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `schedules` **(obrigatório)**: `array` - List of arm schedules.
  - _array de_ `object`:
    - `start` **(obrigatório)**: `string` - Cron expression for the start time.
    - `end` **(obrigatório)**: `string` - Cron expression for the end time.
- `recordEverything` **(obrigatório)**: `boolean` - Whether to record everything when this arm profile is active.
- `activationDelay` **(obrigatório)**: Activation delay in milliseconds. Allowed values: 0 (none), 60000 (1 min), 300000 (5 min), 600000 (10 min).
  - _um de (variantes):_
    - **variante**:
      - `number`
    - **variante**:
      - `number`
    - **variante**:
      - `number`
    - **variante**:
      - `number`
- `createdAt` **(obrigatório)**: `number` - Arm profile creation time.
- `updatedAt` **(obrigatório)**: `number` - Arm profile update time.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PATCH "https://$UNIFI_HOST/proxy/protect/integration/v1/arm-profiles/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PATCH "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/arm-profiles/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Enable arm alarm

`POST /v1/arm-profiles/enable`  ·  operationId: ``

Enable the arm alarm feature using the currently selected arm profile. Only available when using local alarm manager.

**Resposta 204** - Arm alarm enabled successfully

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/protect/integration/v1/arm-profiles/enable" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/arm-profiles/enable" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Disable arm alarm

`POST /v1/arm-profiles/disable`  ·  operationId: ``

Disable the arm alarm feature. Only available when using local alarm manager.

**Resposta 204** - Arm alarm disabled successfully

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/protect/integration/v1/arm-profiles/disable" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/arm-profiles/disable" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Light information & management


### Get light details

`GET /v1/lights/{id}`  ·  operationId: ``

Get detailed information about a specific light

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of light |

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of light
- `modelKey` **(obrigatório)**: `string` - The model key of the light
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `lightModeSettings` **(obrigatório)**: `object` - Settings for when and how your light gets activated
  - `mode`: When will floodlight turn on.
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `string`
      - **variante**:
        - `string`
  - `enableAt`: At what time is the lighting mode relevant and acted upon (this has no effect when mode is off).
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `string`
- `lightDeviceSettings` **(obrigatório)**: `object` - Hardware settings for light device.
  - `isIndicatorEnabled`: `boolean` - Turn on/off floodlight status LED indicator.
  - `pirDuration`: `number` - How long the light stays on after a motion event in milliseconds.
  - `pirSensitivity`: `number` - How sensitive is the PIR to motion (0-100)%.
  - `ledLevel`: `number` - Brightness level of the main LED (1-6).
- `isDark` **(obrigatório)**: `boolean` - Whether the light is currently sensing that it's in a dark scene.
- `isLightOn` **(obrigatório)**: `boolean` - Whether the light has its main LED currently enabled.
- `isLightForceEnabled` **(obrigatório)**: `boolean` - Whether the light has its main LED currently force-enabled.
- `lastMotion` **(obrigatório)**: `number|null` - Unix timestamp of the last time the PIR motion-detection was triggered.
- `isPirMotionDetected` **(obrigatório)**: `boolean` - Whether the light PIR is currently detecting motion
- `camera` **(obrigatório)**: Which camera is configured to be paired to this light.
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/lights/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/lights/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Patch light settings

`PATCH /v1/lights/{id}`  ·  operationId: ``

Patch the settings for a specific light

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of light |

**Corpo da requisição** (`application/json`)

- `name`: `string` - The name of the device.
- `isLightForceEnabled`: `boolean` - Whether the light has its main LED currently force-enabled.
- `lightModeSettings`: `object` - Settings for when and how your light gets activated
  - `mode`: When will floodlight turn on.
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `string`
      - **variante**:
        - `string`
  - `enableAt`: At what time is the lighting mode relevant and acted upon (this has no effect when mode is off).
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `string`
- `lightDeviceSettings`: `object` - Hardware settings for light device.
  - `isIndicatorEnabled`: `boolean` - Turn on/off floodlight status LED indicator.
  - `pirDuration`: `number` - How long the light stays on after a motion event in milliseconds.
  - `pirSensitivity`: `number` - How sensitive is the PIR to motion (0-100)%.
  - `ledLevel`: `number` - Brightness level of the main LED (1-6).

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of light
- `modelKey` **(obrigatório)**: `string` - The model key of the light
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `lightModeSettings` **(obrigatório)**: `object` - Settings for when and how your light gets activated
  - `mode`: When will floodlight turn on.
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `string`
      - **variante**:
        - `string`
  - `enableAt`: At what time is the lighting mode relevant and acted upon (this has no effect when mode is off).
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `string`
- `lightDeviceSettings` **(obrigatório)**: `object` - Hardware settings for light device.
  - `isIndicatorEnabled`: `boolean` - Turn on/off floodlight status LED indicator.
  - `pirDuration`: `number` - How long the light stays on after a motion event in milliseconds.
  - `pirSensitivity`: `number` - How sensitive is the PIR to motion (0-100)%.
  - `ledLevel`: `number` - Brightness level of the main LED (1-6).
- `isDark` **(obrigatório)**: `boolean` - Whether the light is currently sensing that it's in a dark scene.
- `isLightOn` **(obrigatório)**: `boolean` - Whether the light has its main LED currently enabled.
- `isLightForceEnabled` **(obrigatório)**: `boolean` - Whether the light has its main LED currently force-enabled.
- `lastMotion` **(obrigatório)**: `number|null` - Unix timestamp of the last time the PIR motion-detection was triggered.
- `isPirMotionDetected` **(obrigatório)**: `boolean` - Whether the light PIR is currently detecting motion
- `camera` **(obrigatório)**: Which camera is configured to be paired to this light.
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PATCH "https://$UNIFI_HOST/proxy/protect/integration/v1/lights/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PATCH "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/lights/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get all lights

`GET /v1/lights`  ·  operationId: ``

Get detailed information about all lights

**Resposta 200** - Success response

- _array de_ `object`:
  - `id` **(obrigatório)**: `string` - The primary key of light
  - `modelKey` **(obrigatório)**: `string` - The model key of the light
  - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
  - `name` **(obrigatório)**
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`
  - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
  - `lightModeSettings` **(obrigatório)**: `object` - Settings for when and how your light gets activated
    - `mode`: When will floodlight turn on.
      - _um de (variantes):_
        - **variante**:
          - `string`
        - **variante**:
          - `string`
        - **variante**:
          - `string`
    - `enableAt`: At what time is the lighting mode relevant and acted upon (this has no effect when mode is off).
      - _um de (variantes):_
        - **variante**:
          - `string`
        - **variante**:
          - `string`
  - `lightDeviceSettings` **(obrigatório)**: `object` - Hardware settings for light device.
    - `isIndicatorEnabled`: `boolean` - Turn on/off floodlight status LED indicator.
    - `pirDuration`: `number` - How long the light stays on after a motion event in milliseconds.
    - `pirSensitivity`: `number` - How sensitive is the PIR to motion (0-100)%.
    - `ledLevel`: `number` - Brightness level of the main LED (1-6).
  - `isDark` **(obrigatório)**: `boolean` - Whether the light is currently sensing that it's in a dark scene.
  - `isLightOn` **(obrigatório)**: `boolean` - Whether the light has its main LED currently enabled.
  - `isLightForceEnabled` **(obrigatório)**: `boolean` - Whether the light has its main LED currently force-enabled.
  - `lastMotion` **(obrigatório)**: `number|null` - Unix timestamp of the last time the PIR motion-detection was triggered.
  - `isPirMotionDetected` **(obrigatório)**: `boolean` - Whether the light PIR is currently detecting motion
  - `camera` **(obrigatório)**: Which camera is configured to be paired to this light.
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/lights" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/lights" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Camera information & management


### Get camera details

`GET /v1/cameras/{id}`  ·  operationId: ``

Get detailed information about a specific camera

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of camera |

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of camera
- `modelKey` **(obrigatório)**: `string` - The model key of the camera
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `isMicEnabled` **(obrigatório)**: `boolean` - Whether or not the microphone on camera is enabled
- `osdSettings` **(obrigatório)**: `object` - On Screen Display settings.
  - `isNameEnabled` **(obrigatório)**: `boolean` - Whether to show the name in the OSD.
  - `isDateEnabled` **(obrigatório)**: `boolean` - Whether to show the date in the OSD.
  - `isLogoEnabled` **(obrigatório)**: `boolean` - Whether to show the logo in the bottom right corner.
  - `isDebugEnabled` **(obrigatório)**: `boolean` - Whether debug info is enabled.
  - `overlayLocation` **(obrigatório)**: `string` enum: topLeft, topMiddle, topRight, bottomLeft, bottomMiddle, bottomRight - The location of the overlay on the screen.
- `ledSettings` **(obrigatório)**: `object` - LED settings.
  - `isEnabled` **(obrigatório)**: `boolean` - Indicates whether the status LED is enabled.
  - `welcomeLed` **(obrigatório)**: `boolean` - Indicates whether the welcome LED is enabled.
  - `floodLed` **(obrigatório)**: `boolean` - Indicates whether the flood LED is enabled.
- `lcdMessage` **(obrigatório)**: `object`
  - `type`: `string` enum: LEAVE_PACKAGE_AT_DOOR, DO_NOT_DISTURB, CUSTOM_MESSAGE, IMAGE
  - `resetAt`: `number|null` - UNIX timestamp when doorbell message should be removed (if not set then `nvr.doorbellSettings.defaultMessageResetTimeoutMs` is used, if set to `null` then in…
  - `text`: `string`
- `micVolume` **(obrigatório)**: `number` - Mic volume: a number from 0-100.
- `activePatrolSlot` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `number`
    - **variante**:
      - `null`
- `videoMode` **(obrigatório)**: `string` enum: default, highFps, sport, slowShutter, lprReflex, lprNoneReflex - Current video mode of the camera
- `hdrType` **(obrigatório)**: `string` enum: auto, on, off - High Dynamic Range (HDR) mode setting.
- `featureFlags` **(obrigatório)**: `object`
  - `supportFullHdSnapshot` **(obrigatório)**: `boolean` - Whether camera support full HD or higher resolution snapshot
  - `hasHdr` **(obrigatório)**: `boolean` - Whether the camera supports High Dynamic Range mode
  - `smartDetectTypes` **(obrigatório)**: `array` - What smart detection object types do the camera support.
    - _array de_ `string`:
      - `string` enum: person, vehicle, package, licensePlate, face, animal
  - `smartDetectAudioTypes` **(obrigatório)**: `array` - What smart detection audio types do the camera support.
    - _array de_ `string`:
      - `string` enum: alrmSmoke, alrmCmonx, alrmSiren, alrmBabyCry, alrmSpeak, alrmBark, alrmBurglar, alrmCarHorn, alrmGlassBreak
  - `videoModes` **(obrigatório)**: `array` - A list of supported video modes by the camera
    - _array de_ `string`:
      - `string` enum: default, highFps, homekit, sport, slowShutter, lprReflex, lprNoneReflex
  - `hasMic` **(obrigatório)**: `boolean` - Whether the camera has a microphone
  - `hasLedStatus` **(obrigatório)**: `boolean` - Whether the camera has LED status
  - `hasSpeaker` **(obrigatório)**: `boolean` - Whether the camera has a speaker to support talkback
- `smartDetectSettings` **(obrigatório)**: `object` - Smart detection settings for the camera.
  - `objectTypes` **(obrigatório)**: `array`
    - _array de_ `string`:
      - `string` enum: person, vehicle, package, licensePlate, face, animal
  - `audioTypes` **(obrigatório)**: `array`
    - _array de_ `string`:
      - `string` enum: alrmSmoke, alrmCmonx, alrmSiren, alrmBabyCry, alrmSpeak, alrmBark, alrmBurglar, alrmCarHorn, alrmGlassBreak
- `hasPackageCamera` **(obrigatório)**: `boolean` - Whether the camera has a package camera.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/cameras/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/cameras/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Patch camera settings

`PATCH /v1/cameras/{id}`  ·  operationId: ``

Patch the settings for a specific camera

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of camera |

**Corpo da requisição** (`application/json`)

- `name`: `string` - The name of the device.
- `osdSettings`: `object` - On Screen Display settings.
  - `isNameEnabled`: `boolean` - Whether to show the name in the OSD.
  - `isDateEnabled`: `boolean` - Whether to show the date in the OSD.
  - `isLogoEnabled`: `boolean` - Whether to show the logo in the bottom right corner.
  - `isDebugEnabled`: `boolean` - Whether debug info is enabled.
  - `overlayLocation`: `string` enum: topLeft, topMiddle, topRight, bottomLeft, bottomMiddle, bottomRight - The location of the overlay on the screen.
- `ledSettings`: `object` - LED settings.
  - `isEnabled`: `boolean` - Indicates whether the status LED is enabled.
  - `welcomeLed`: `boolean` - Indicates whether the welcome LED is enabled.
  - `floodLed`: `boolean` - Indicates whether the flood LED is enabled.
- `lcdMessage`: Message that's set on the LCD screen (for doorbells and/or other devices with LCD screens). To upload image assets for the LCD screen, use the `/files/{fileT…
  - _um de (variantes):_
    - **variante**:
      - `type` **(obrigatório)**: `string`
      - `resetAt`: `number|null` - UNIX timestamp when doorbell message should be removed (if not set then `nvr.doorbellSettings.defaultMessageResetTimeoutMs` is used, if set to `null` then in…
    - **variante**:
      - `type` **(obrigatório)**: `string`
      - `resetAt`: `number|null` - UNIX timestamp when doorbell message should be removed (if not set then `nvr.doorbellSettings.defaultMessageResetTimeoutMs` is used, if set to `null` then in…
    - **variante**:
      - `type` **(obrigatório)**: `string`
      - `resetAt`: `number|null` - UNIX timestamp when doorbell message should be removed (if not set then `nvr.doorbellSettings.defaultMessageResetTimeoutMs` is used, if set to `null` then in…
      - `text` **(obrigatório)**: `string` - The custom text message to show on the doorbell
    - **variante**:
      - `type` **(obrigatório)**: `string`
      - `resetAt`: `number|null` - UNIX timestamp when doorbell message should be removed (if not set then `nvr.doorbellSettings.defaultMessageResetTimeoutMs` is used, if set to `null` then in…
      - `text` **(obrigatório)**: `string` - The ID of the custom image to show on the doorbell
- `micVolume`
  - `number`
- `videoMode`: `string` enum: default, highFps, sport, slowShutter, lprReflex, lprNoneReflex - Current video mode of the camera
- `hdrType`: enum: auto, on, off - High Dynamic Range (HDR) mode setting.
  - `string` enum: auto, on, off
  - enum: auto, on, off
- `smartDetectSettings`: `object` - Smart detection settings for the camera.
  - `objectTypes`: `array`
    - _array de_ `string`:
      - `string` enum: person, vehicle, package, licensePlate, face, animal
  - `audioTypes`: `array`
    - _array de_ `string`:
      - `string` enum: alrmSmoke, alrmCmonx, alrmSiren, alrmBabyCry, alrmSpeak, alrmBark, alrmBurglar, alrmCarHorn, alrmGlassBreak

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of camera
- `modelKey` **(obrigatório)**: `string` - The model key of the camera
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `isMicEnabled` **(obrigatório)**: `boolean` - Whether or not the microphone on camera is enabled
- `osdSettings` **(obrigatório)**: `object` - On Screen Display settings.
  - `isNameEnabled` **(obrigatório)**: `boolean` - Whether to show the name in the OSD.
  - `isDateEnabled` **(obrigatório)**: `boolean` - Whether to show the date in the OSD.
  - `isLogoEnabled` **(obrigatório)**: `boolean` - Whether to show the logo in the bottom right corner.
  - `isDebugEnabled` **(obrigatório)**: `boolean` - Whether debug info is enabled.
  - `overlayLocation` **(obrigatório)**: `string` enum: topLeft, topMiddle, topRight, bottomLeft, bottomMiddle, bottomRight - The location of the overlay on the screen.
- `ledSettings` **(obrigatório)**: `object` - LED settings.
  - `isEnabled` **(obrigatório)**: `boolean` - Indicates whether the status LED is enabled.
  - `welcomeLed` **(obrigatório)**: `boolean` - Indicates whether the welcome LED is enabled.
  - `floodLed` **(obrigatório)**: `boolean` - Indicates whether the flood LED is enabled.
- `lcdMessage` **(obrigatório)**: `object`
  - `type`: `string` enum: LEAVE_PACKAGE_AT_DOOR, DO_NOT_DISTURB, CUSTOM_MESSAGE, IMAGE
  - `resetAt`: `number|null` - UNIX timestamp when doorbell message should be removed (if not set then `nvr.doorbellSettings.defaultMessageResetTimeoutMs` is used, if set to `null` then in…
  - `text`: `string`
- `micVolume` **(obrigatório)**: `number` - Mic volume: a number from 0-100.
- `activePatrolSlot` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `number`
    - **variante**:
      - `null`
- `videoMode` **(obrigatório)**: `string` enum: default, highFps, sport, slowShutter, lprReflex, lprNoneReflex - Current video mode of the camera
- `hdrType` **(obrigatório)**: `string` enum: auto, on, off - High Dynamic Range (HDR) mode setting.
- `featureFlags` **(obrigatório)**: `object`
  - `supportFullHdSnapshot` **(obrigatório)**: `boolean` - Whether camera support full HD or higher resolution snapshot
  - `hasHdr` **(obrigatório)**: `boolean` - Whether the camera supports High Dynamic Range mode
  - `smartDetectTypes` **(obrigatório)**: `array` - What smart detection object types do the camera support.
    - _array de_ `string`:
      - `string` enum: person, vehicle, package, licensePlate, face, animal
  - `smartDetectAudioTypes` **(obrigatório)**: `array` - What smart detection audio types do the camera support.
    - _array de_ `string`:
      - `string` enum: alrmSmoke, alrmCmonx, alrmSiren, alrmBabyCry, alrmSpeak, alrmBark, alrmBurglar, alrmCarHorn, alrmGlassBreak
  - `videoModes` **(obrigatório)**: `array` - A list of supported video modes by the camera
    - _array de_ `string`:
      - `string` enum: default, highFps, homekit, sport, slowShutter, lprReflex, lprNoneReflex
  - `hasMic` **(obrigatório)**: `boolean` - Whether the camera has a microphone
  - `hasLedStatus` **(obrigatório)**: `boolean` - Whether the camera has LED status
  - `hasSpeaker` **(obrigatório)**: `boolean` - Whether the camera has a speaker to support talkback
- `smartDetectSettings` **(obrigatório)**: `object` - Smart detection settings for the camera.
  - `objectTypes` **(obrigatório)**: `array`
    - _array de_ `string`:
      - `string` enum: person, vehicle, package, licensePlate, face, animal
  - `audioTypes` **(obrigatório)**: `array`
    - _array de_ `string`:
      - `string` enum: alrmSmoke, alrmCmonx, alrmSiren, alrmBabyCry, alrmSpeak, alrmBark, alrmBurglar, alrmCarHorn, alrmGlassBreak
- `hasPackageCamera` **(obrigatório)**: `boolean` - Whether the camera has a package camera.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PATCH "https://$UNIFI_HOST/proxy/protect/integration/v1/cameras/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PATCH "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/cameras/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get all cameras

`GET /v1/cameras`  ·  operationId: ``

Get detailed information about all cameras

**Resposta 200** - Success response

- _array de_ `object`:
  - `id` **(obrigatório)**: `string` - The primary key of camera
  - `modelKey` **(obrigatório)**: `string` - The model key of the camera
  - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
  - `name` **(obrigatório)**
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`
  - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
  - `isMicEnabled` **(obrigatório)**: `boolean` - Whether or not the microphone on camera is enabled
  - `osdSettings` **(obrigatório)**: `object` - On Screen Display settings.
    - `isNameEnabled` **(obrigatório)**: `boolean` - Whether to show the name in the OSD.
    - `isDateEnabled` **(obrigatório)**: `boolean` - Whether to show the date in the OSD.
    - `isLogoEnabled` **(obrigatório)**: `boolean` - Whether to show the logo in the bottom right corner.
    - `isDebugEnabled` **(obrigatório)**: `boolean` - Whether debug info is enabled.
    - `overlayLocation` **(obrigatório)**: `string` enum: topLeft, topMiddle, topRight, bottomLeft, bottomMiddle, bottomRight - The location of the overlay on the screen.
  - `ledSettings` **(obrigatório)**: `object` - LED settings.
    - `isEnabled` **(obrigatório)**: `boolean` - Indicates whether the status LED is enabled.
    - `welcomeLed` **(obrigatório)**: `boolean` - Indicates whether the welcome LED is enabled.
    - `floodLed` **(obrigatório)**: `boolean` - Indicates whether the flood LED is enabled.
  - `lcdMessage` **(obrigatório)**: `object`
    - `type`: `string` enum: LEAVE_PACKAGE_AT_DOOR, DO_NOT_DISTURB, CUSTOM_MESSAGE, IMAGE
    - `resetAt`: `number|null` - UNIX timestamp when doorbell message should be removed (if not set then `nvr.doorbellSettings.defaultMessageResetTimeoutMs` is used, if set to `null` then in…
    - `text`: `string`
  - `micVolume` **(obrigatório)**: `number` - Mic volume: a number from 0-100.
  - `activePatrolSlot` **(obrigatório)**
    - _um de (variantes):_
      - **variante**:
        - `number`
      - **variante**:
        - `null`
  - `videoMode` **(obrigatório)**: `string` enum: default, highFps, sport, slowShutter, lprReflex, lprNoneReflex - Current video mode of the camera
  - `hdrType` **(obrigatório)**: `string` enum: auto, on, off - High Dynamic Range (HDR) mode setting.
  - `featureFlags` **(obrigatório)**: `object`
    - `supportFullHdSnapshot` **(obrigatório)**: `boolean` - Whether camera support full HD or higher resolution snapshot
    - `hasHdr` **(obrigatório)**: `boolean` - Whether the camera supports High Dynamic Range mode
    - `smartDetectTypes` **(obrigatório)**: `array` - What smart detection object types do the camera support.
      - _array de_ `string`:
        - `string` enum: person, vehicle, package, licensePlate, face, animal
    - `smartDetectAudioTypes` **(obrigatório)**: `array` - What smart detection audio types do the camera support.
      - _array de_ `string`:
        - `string` enum: alrmSmoke, alrmCmonx, alrmSiren, alrmBabyCry, alrmSpeak, alrmBark, alrmBurglar, alrmCarHorn, alrmGlassBreak
    - `videoModes` **(obrigatório)**: `array` - A list of supported video modes by the camera
      - _array de_ `string`:
        - `string` enum: default, highFps, homekit, sport, slowShutter, lprReflex, lprNoneReflex
    - `hasMic` **(obrigatório)**: `boolean` - Whether the camera has a microphone
    - `hasLedStatus` **(obrigatório)**: `boolean` - Whether the camera has LED status
    - `hasSpeaker` **(obrigatório)**: `boolean` - Whether the camera has a speaker to support talkback
  - `smartDetectSettings` **(obrigatório)**: `object` - Smart detection settings for the camera.
    - `objectTypes` **(obrigatório)**: `array`
      - _array de_ `string`:
        - `string` enum: person, vehicle, package, licensePlate, face, animal
    - `audioTypes` **(obrigatório)**: `array`
      - _array de_ `string`:
        - `string` enum: alrmSmoke, alrmCmonx, alrmSiren, alrmBabyCry, alrmSpeak, alrmBark, alrmBurglar, alrmCarHorn, alrmGlassBreak
  - `hasPackageCamera` **(obrigatório)**: `boolean` - Whether the camera has a package camera.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/cameras" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/cameras" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get RTSPS streams for camera

`GET /v1/cameras/{id}/rtsps-stream`  ·  operationId: ``

Returns existing RTSPS stream URLs for camera

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of camera |

**Resposta 200** - Success response

- `high`: `string|null` (uri)
- `medium`: `string|null` (uri)
- `low`: `string|null` (uri)
- `package`: `string|null` (uri)

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/cameras/{id}/rtsps-stream" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/cameras/{id}/rtsps-stream" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Create RTSPS streams for camera

`POST /v1/cameras/{id}/rtsps-stream`  ·  operationId: ``

Returns RTSPS stream URLs for specified quality levels

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of camera |

**Corpo da requisição** (`application/json`)

- `qualities` **(obrigatório)**: `array` - Array of quality levels of RTSPS streams. All qualities (high, medium, low) are available for all cameras. The package quality is only available for cameras …
  - _array de_ `string`:
    - `string` enum: high, medium, low, package

**Resposta 200** - Success response

- `high`: `string` (uri)
- `medium`: `string` (uri)
- `low`: `string` (uri)
- `package`: `string` (uri)

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/protect/integration/v1/cameras/{id}/rtsps-stream" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/cameras/{id}/rtsps-stream" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Delete camera RTSPS stream

`DELETE /v1/cameras/{id}/rtsps-stream`  ·  operationId: ``

Remove the RTSPS stream for a specified camera

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of camera |
| `qualities` | query | sim |  | The array of quality levels for the RTSPS streams to be removed. All qualities (high, medium, low) are available for all cameras. The package quality is only available for cameras with hasPackageCamera: true. |

**Resposta 204** - RTSPS stream successfully removed

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X DELETE "https://$UNIFI_HOST/proxy/protect/integration/v1/cameras/{id}/rtsps-stream" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X DELETE "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/cameras/{id}/rtsps-stream" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get camera snapshot

`GET /v1/cameras/{id}/snapshot`  ·  operationId: ``

Get a snapshot image from a specific camera. Use channel=package for cameras with a package camera (hasPackageCamera: true).

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of camera |
| `channel` | query | não | string enum | Camera channel to capture snapshot from. Use "package" for cameras with a package camera (hasPackageCamera: true). |
| `highQuality` | query | não | string enum | Whether to force 1080P or higher resolution snapshot |

**Resposta 200** - Camera snapshot

**Erros possíveis:** `503`, `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/cameras/{id}/snapshot" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/cameras/{id}/snapshot" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Permanently disable camera microphone

`POST /v1/cameras/{id}/disable-mic-permanently`  ·  operationId: ``

Disable the microphone for a specific camera. This action cannot be undone unless the camera is reset.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of camera |

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of camera
- `modelKey` **(obrigatório)**: `string` - The model key of the camera
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `isMicEnabled` **(obrigatório)**: `boolean` - Whether or not the microphone on camera is enabled
- `osdSettings` **(obrigatório)**: `object` - On Screen Display settings.
  - `isNameEnabled` **(obrigatório)**: `boolean` - Whether to show the name in the OSD.
  - `isDateEnabled` **(obrigatório)**: `boolean` - Whether to show the date in the OSD.
  - `isLogoEnabled` **(obrigatório)**: `boolean` - Whether to show the logo in the bottom right corner.
  - `isDebugEnabled` **(obrigatório)**: `boolean` - Whether debug info is enabled.
  - `overlayLocation` **(obrigatório)**: `string` enum: topLeft, topMiddle, topRight, bottomLeft, bottomMiddle, bottomRight - The location of the overlay on the screen.
- `ledSettings` **(obrigatório)**: `object` - LED settings.
  - `isEnabled` **(obrigatório)**: `boolean` - Indicates whether the status LED is enabled.
  - `welcomeLed` **(obrigatório)**: `boolean` - Indicates whether the welcome LED is enabled.
  - `floodLed` **(obrigatório)**: `boolean` - Indicates whether the flood LED is enabled.
- `lcdMessage` **(obrigatório)**: `object`
  - `type`: `string` enum: LEAVE_PACKAGE_AT_DOOR, DO_NOT_DISTURB, CUSTOM_MESSAGE, IMAGE
  - `resetAt`: `number|null` - UNIX timestamp when doorbell message should be removed (if not set then `nvr.doorbellSettings.defaultMessageResetTimeoutMs` is used, if set to `null` then in…
  - `text`: `string`
- `micVolume` **(obrigatório)**: `number` - Mic volume: a number from 0-100.
- `activePatrolSlot` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `number`
    - **variante**:
      - `null`
- `videoMode` **(obrigatório)**: `string` enum: default, highFps, sport, slowShutter, lprReflex, lprNoneReflex - Current video mode of the camera
- `hdrType` **(obrigatório)**: `string` enum: auto, on, off - High Dynamic Range (HDR) mode setting.
- `featureFlags` **(obrigatório)**: `object`
  - `supportFullHdSnapshot` **(obrigatório)**: `boolean` - Whether camera support full HD or higher resolution snapshot
  - `hasHdr` **(obrigatório)**: `boolean` - Whether the camera supports High Dynamic Range mode
  - `smartDetectTypes` **(obrigatório)**: `array` - What smart detection object types do the camera support.
    - _array de_ `string`:
      - `string` enum: person, vehicle, package, licensePlate, face, animal
  - `smartDetectAudioTypes` **(obrigatório)**: `array` - What smart detection audio types do the camera support.
    - _array de_ `string`:
      - `string` enum: alrmSmoke, alrmCmonx, alrmSiren, alrmBabyCry, alrmSpeak, alrmBark, alrmBurglar, alrmCarHorn, alrmGlassBreak
  - `videoModes` **(obrigatório)**: `array` - A list of supported video modes by the camera
    - _array de_ `string`:
      - `string` enum: default, highFps, homekit, sport, slowShutter, lprReflex, lprNoneReflex
  - `hasMic` **(obrigatório)**: `boolean` - Whether the camera has a microphone
  - `hasLedStatus` **(obrigatório)**: `boolean` - Whether the camera has LED status
  - `hasSpeaker` **(obrigatório)**: `boolean` - Whether the camera has a speaker to support talkback
- `smartDetectSettings` **(obrigatório)**: `object` - Smart detection settings for the camera.
  - `objectTypes` **(obrigatório)**: `array`
    - _array de_ `string`:
      - `string` enum: person, vehicle, package, licensePlate, face, animal
  - `audioTypes` **(obrigatório)**: `array`
    - _array de_ `string`:
      - `string` enum: alrmSmoke, alrmCmonx, alrmSiren, alrmBabyCry, alrmSpeak, alrmBark, alrmBurglar, alrmCarHorn, alrmGlassBreak
- `hasPackageCamera` **(obrigatório)**: `boolean` - Whether the camera has a package camera.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/protect/integration/v1/cameras/{id}/disable-mic-permanently" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/cameras/{id}/disable-mic-permanently" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Create talkback session for camera

`POST /v1/cameras/{id}/talkback-session`  ·  operationId: ``

Returns the talkback stream URL and audio configuration for a specific camera

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of camera |

**Resposta 200** - Success response

- `url` **(obrigatório)**: `string` (uri) - Talkback stream URL
- `codec` **(obrigatório)**: `string` - Audio format to use.
- `samplingRate` **(obrigatório)**: `integer` - Sampling Rate.
- `bitsPerSample` **(obrigatório)**: `integer` - Bits per sample.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/protect/integration/v1/cameras/{id}/talkback-session" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/cameras/{id}/talkback-session" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Sensor information & management


### Get sensor details

`GET /v1/sensors/{id}`  ·  operationId: ``

Get detailed information about a specific sensor

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of sensor |

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of sensor
- `modelKey` **(obrigatório)**: `string` - The model key of the sensor
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `mountType` **(obrigatório)**: `string` enum: door, window, garage, leak, none - Mounting type of the sensor.
- `batteryStatus` **(obrigatório)**: `object` - [DEPRECATED] Use wirelessConnectionState.batteryStatus instead. Battery status.
  - `percentage`: `number|null` - Battery charge level from 0 to 100 (%).
  - `isLow`: `boolean` - Low battery charge level flag.
- `stats` **(obrigatório)**: `object` - Sensor statistics.
  - `light`: `object` - Ambient light value (Lux).
    - `value`
      - _um de (variantes):_
        - **variante**:
          - `number`
        - **variante**:
          - `null`
    - `status`: `string` enum: neutral, low, safe, high, unknown - What range does the measured metric fall into
  - `humidity`: `object` - Ambient light value (Lux).
    - `value`
      - _um de (variantes):_
        - **variante**:
          - `number`
        - **variante**:
          - `null`
    - `status`: `string` enum: neutral, low, safe, high, unknown - What range does the measured metric fall into
  - `temperature`: `object` - Ambient light value (Lux).
    - `value`
      - _um de (variantes):_
        - **variante**:
          - `number`
        - **variante**:
          - `null`
    - `status`: `string` enum: neutral, low, safe, high, unknown - What range does the measured metric fall into
- `lightSettings` **(obrigatório)**: `object` - Ambient light sensor settings.
  - `isEnabled`: `boolean` - Enable ambient light sensor.
  - `margin`: `number` - Ambient light threshold detection hysteresis margin (Lux). Read-only value decided by sensor implementation.
  - `lowThreshold`: `number|null` - Ambient light interrupt threshold low level from 1 to 503192 (Lux).
  - `highThreshold`: `number|null` - Ambient light interrupt threshold high level from 1 to 503192 (Lux).
- `humiditySettings` **(obrigatório)**: `object` - Relative humidity sensor settings.
  - `isEnabled`: `boolean` - Enable relative humidity sensor.
  - `margin`: `number` - Humidity threshold detection hysteresis margin (%). Read-only value decided by sensor implementation.
  - `lowThreshold`: `number|null` - Humidity low level threshold from 1 to 99 (%).
  - `highThreshold`: `number|null` - Humidity high level threshold from 1 to 99 (%).
- `temperatureSettings` **(obrigatório)**: `object` - Temperature sensor settings.
  - `isEnabled`: `boolean` - Enable temperature sensor.
  - `margin`: `number` - Temperature threshold detection hysteresis margin (C). Read-only value decided by sensor implementation.
  - `lowThreshold`: `number|null` - Temperature low level threshold from -39 to 124 (C).
  - `highThreshold`: `number|null` - Temperature high level threshold from -39 to 124 (C).
- `isOpened` **(obrigatório)**: `boolean|null` - Whether the door/window/garage is opened.
- `openStatusChangedAt` **(obrigatório)**: `number|null` - Unix timestamp when the door/window/garage was last opened or closed, nullable.
- `isMotionDetected` **(obrigatório)**: `boolean` - Whether sensor is currently detecting the motion.
- `motionDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the last motion was detected.
- `motionSettings` **(obrigatório)**: `object` - Motion sensor settings.
  - `isEnabled`: `boolean` - Enable motion sensor.
  - `sensitivity`: `number` - Motion sensitivity (0-100) used when system is not armed or when no armed override is set.
  - `sensitivityWhenArmed`: `number` - Motion sensitivity (0-100) used when the system is armed and `hasCustomSensitivityWhenArmed` is true on the sensor.
- `glassBreakSettings` **(obrigatório)**: `object` - Glass break sensor settings.
  - `isEnabled`: `boolean` - Enable glass break sensor.
  - `sensitivity`: `number` - Glass break sensitivity (0-100) used when system is not armed or when no armed override is set.
  - `sensitivityWhenArmed`: `number` - Glass break sensitivity (0-100) used when the system is armed and `hasCustomSensitivityWhenArmed` is true on the sensor.
- `scheduleMode` **(obrigatório)**: `string` enum: always, when_armed - When armed-mode detection runs: `always` or only `when_armed`. Applies to both glass break and motion together.
- `armProfileIds` **(obrigatório)**: `array|null` - When `scheduleMode` is `when_armed`, restricts armed-mode detection to these arm profile ids. Empty or null = all profiles.
- `hasCustomSensitivityWhenArmed` **(obrigatório)**: `boolean` - When true, glass break and motion both use their respective `sensitivityWhenArmed` value while the system is armed.
- `alarmTriggeredAt` **(obrigatório)**: `number|null` - Unix timestamp when the smoke or carbon monoxide alarm was triggered, nullable.
- `alarmSettings` **(obrigatório)**: `object` - Smoke and carbon monoxide alarm sensor settings.
  - `isEnabled`: `boolean` - Enable smoke and carbon monoxide alarm sensor.
- `leakDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected a water leak, nullable.
- `externalLeakDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected an external water leak, nullable.
- `leakSettings` **(obrigatório)**: `object` - Leak sensor settings.
  - `isInternalEnabled`: `boolean` - Enable internal water leak detection.
  - `isExternalEnabled`: `boolean` - Enable external water leak detection.
- `tamperingDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected tampering, nullable.
- `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
  - `signalState` **(obrigatório)**: `object` - Signal state.
    - `signalQuality` **(obrigatório)**: `number|null` - Percent representation of Bluetooth signal strength.
    - `signalStrength` **(obrigatório)**: `number|null` - dBm value of Bluetooth signal strength.
  - `batteryStatus` **(obrigatório)**: `object` - Battery status.
    - `percentage` **(obrigatório)**: `number|null` - Battery charge level from 0 to 100 (%).
    - `isLow` **(obrigatório)**: `boolean` - Low battery charge level flag.
  - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/sensors/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/sensors/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Patch sensor settings

`PATCH /v1/sensors/{id}`  ·  operationId: ``

Patch the settings for a specific sensor

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of sensor |

**Corpo da requisição** (`application/json`)

- `name`: `string` - The name of the device.
- `lightSettings`
  - `isEnabled`: `boolean` - Enable ambient light sensor.
  - `margin`: `number` - Ambient light threshold detection hysteresis margin (Lux). Read-only value decided by sensor implementation.
  - `lowThreshold`: `number|null` - Ambient light interrupt threshold low level from 1 to 503192 (Lux).
  - `highThreshold`: `number|null` - Ambient light interrupt threshold high level from 1 to 503192 (Lux).
- `humiditySettings`
  - `isEnabled`: `boolean` - Enable relative humidity sensor.
  - `margin`: `number` - Humidity threshold detection hysteresis margin (%). Read-only value decided by sensor implementation.
  - `lowThreshold`: `number|null` - Humidity low level threshold from 1 to 99 (%).
  - `highThreshold`: `number|null` - Humidity high level threshold from 1 to 99 (%).
- `temperatureSettings`
  - `isEnabled`: `boolean` - Enable temperature sensor.
  - `margin`: `number` - Temperature threshold detection hysteresis margin (C). Read-only value decided by sensor implementation.
  - `lowThreshold`: `number|null` - Temperature low level threshold from -39 to 124 (C).
  - `highThreshold`: `number|null` - Temperature high level threshold from -39 to 124 (C).
- `motionSettings`
  - `isEnabled`: `boolean` - Enable motion sensor.
  - `sensitivity`: `number` - Motion sensitivity (0-100) used when system is not armed or when no armed override is set.
  - `sensitivityWhenArmed`: `number` - Motion sensitivity (0-100) used when the system is armed and `hasCustomSensitivityWhenArmed` is true on the sensor.
- `glassBreakSettings`
  - `isEnabled`: `boolean` - Enable glass break sensor.
  - `sensitivity`: `number` - Glass break sensitivity (0-100) used when system is not armed or when no armed override is set.
  - `sensitivityWhenArmed`: `number` - Glass break sensitivity (0-100) used when the system is armed and `hasCustomSensitivityWhenArmed` is true on the sensor.
- `scheduleMode`: `string` enum: always, when_armed
- `armProfileIds`: `array|null`
- `hasCustomSensitivityWhenArmed`: `boolean`
- `alarmSettings`
  - `isEnabled`: `boolean` - Enable smoke and carbon monoxide alarm sensor.

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of sensor
- `modelKey` **(obrigatório)**: `string` - The model key of the sensor
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `mountType` **(obrigatório)**: `string` enum: door, window, garage, leak, none - Mounting type of the sensor.
- `batteryStatus` **(obrigatório)**: `object` - [DEPRECATED] Use wirelessConnectionState.batteryStatus instead. Battery status.
  - `percentage`: `number|null` - Battery charge level from 0 to 100 (%).
  - `isLow`: `boolean` - Low battery charge level flag.
- `stats` **(obrigatório)**: `object` - Sensor statistics.
  - `light`: `object` - Ambient light value (Lux).
    - `value`
      - _um de (variantes):_
        - **variante**:
          - `number`
        - **variante**:
          - `null`
    - `status`: `string` enum: neutral, low, safe, high, unknown - What range does the measured metric fall into
  - `humidity`: `object` - Ambient light value (Lux).
    - `value`
      - _um de (variantes):_
        - **variante**:
          - `number`
        - **variante**:
          - `null`
    - `status`: `string` enum: neutral, low, safe, high, unknown - What range does the measured metric fall into
  - `temperature`: `object` - Ambient light value (Lux).
    - `value`
      - _um de (variantes):_
        - **variante**:
          - `number`
        - **variante**:
          - `null`
    - `status`: `string` enum: neutral, low, safe, high, unknown - What range does the measured metric fall into
- `lightSettings` **(obrigatório)**: `object` - Ambient light sensor settings.
  - `isEnabled`: `boolean` - Enable ambient light sensor.
  - `margin`: `number` - Ambient light threshold detection hysteresis margin (Lux). Read-only value decided by sensor implementation.
  - `lowThreshold`: `number|null` - Ambient light interrupt threshold low level from 1 to 503192 (Lux).
  - `highThreshold`: `number|null` - Ambient light interrupt threshold high level from 1 to 503192 (Lux).
- `humiditySettings` **(obrigatório)**: `object` - Relative humidity sensor settings.
  - `isEnabled`: `boolean` - Enable relative humidity sensor.
  - `margin`: `number` - Humidity threshold detection hysteresis margin (%). Read-only value decided by sensor implementation.
  - `lowThreshold`: `number|null` - Humidity low level threshold from 1 to 99 (%).
  - `highThreshold`: `number|null` - Humidity high level threshold from 1 to 99 (%).
- `temperatureSettings` **(obrigatório)**: `object` - Temperature sensor settings.
  - `isEnabled`: `boolean` - Enable temperature sensor.
  - `margin`: `number` - Temperature threshold detection hysteresis margin (C). Read-only value decided by sensor implementation.
  - `lowThreshold`: `number|null` - Temperature low level threshold from -39 to 124 (C).
  - `highThreshold`: `number|null` - Temperature high level threshold from -39 to 124 (C).
- `isOpened` **(obrigatório)**: `boolean|null` - Whether the door/window/garage is opened.
- `openStatusChangedAt` **(obrigatório)**: `number|null` - Unix timestamp when the door/window/garage was last opened or closed, nullable.
- `isMotionDetected` **(obrigatório)**: `boolean` - Whether sensor is currently detecting the motion.
- `motionDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the last motion was detected.
- `motionSettings` **(obrigatório)**: `object` - Motion sensor settings.
  - `isEnabled`: `boolean` - Enable motion sensor.
  - `sensitivity`: `number` - Motion sensitivity (0-100) used when system is not armed or when no armed override is set.
  - `sensitivityWhenArmed`: `number` - Motion sensitivity (0-100) used when the system is armed and `hasCustomSensitivityWhenArmed` is true on the sensor.
- `glassBreakSettings` **(obrigatório)**: `object` - Glass break sensor settings.
  - `isEnabled`: `boolean` - Enable glass break sensor.
  - `sensitivity`: `number` - Glass break sensitivity (0-100) used when system is not armed or when no armed override is set.
  - `sensitivityWhenArmed`: `number` - Glass break sensitivity (0-100) used when the system is armed and `hasCustomSensitivityWhenArmed` is true on the sensor.
- `scheduleMode` **(obrigatório)**: `string` enum: always, when_armed - When armed-mode detection runs: `always` or only `when_armed`. Applies to both glass break and motion together.
- `armProfileIds` **(obrigatório)**: `array|null` - When `scheduleMode` is `when_armed`, restricts armed-mode detection to these arm profile ids. Empty or null = all profiles.
- `hasCustomSensitivityWhenArmed` **(obrigatório)**: `boolean` - When true, glass break and motion both use their respective `sensitivityWhenArmed` value while the system is armed.
- `alarmTriggeredAt` **(obrigatório)**: `number|null` - Unix timestamp when the smoke or carbon monoxide alarm was triggered, nullable.
- `alarmSettings` **(obrigatório)**: `object` - Smoke and carbon monoxide alarm sensor settings.
  - `isEnabled`: `boolean` - Enable smoke and carbon monoxide alarm sensor.
- `leakDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected a water leak, nullable.
- `externalLeakDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected an external water leak, nullable.
- `leakSettings` **(obrigatório)**: `object` - Leak sensor settings.
  - `isInternalEnabled`: `boolean` - Enable internal water leak detection.
  - `isExternalEnabled`: `boolean` - Enable external water leak detection.
- `tamperingDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected tampering, nullable.
- `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
  - `signalState` **(obrigatório)**: `object` - Signal state.
    - `signalQuality` **(obrigatório)**: `number|null` - Percent representation of Bluetooth signal strength.
    - `signalStrength` **(obrigatório)**: `number|null` - dBm value of Bluetooth signal strength.
  - `batteryStatus` **(obrigatório)**: `object` - Battery status.
    - `percentage` **(obrigatório)**: `number|null` - Battery charge level from 0 to 100 (%).
    - `isLow` **(obrigatório)**: `boolean` - Low battery charge level flag.
  - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`

**Erros possíveis:** `409`, `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PATCH "https://$UNIFI_HOST/proxy/protect/integration/v1/sensors/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PATCH "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/sensors/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get all sensors

`GET /v1/sensors`  ·  operationId: ``

Get detailed information about all sensors

**Resposta 200** - Success response

- _array de_ `object`:
  - `id` **(obrigatório)**: `string` - The primary key of sensor
  - `modelKey` **(obrigatório)**: `string` - The model key of the sensor
  - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
  - `name` **(obrigatório)**
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`
  - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
  - `mountType` **(obrigatório)**: `string` enum: door, window, garage, leak, none - Mounting type of the sensor.
  - `batteryStatus` **(obrigatório)**: `object` - [DEPRECATED] Use wirelessConnectionState.batteryStatus instead. Battery status.
    - `percentage`: `number|null` - Battery charge level from 0 to 100 (%).
    - `isLow`: `boolean` - Low battery charge level flag.
  - `stats` **(obrigatório)**: `object` - Sensor statistics.
    - `light`: `object` - Ambient light value (Lux).
      - `value`
        - _um de (variantes):_
          - **variante**:
            - `number`
          - **variante**:
            - `null`
      - `status`: `string` enum: neutral, low, safe, high, unknown - What range does the measured metric fall into
    - `humidity`: `object` - Ambient light value (Lux).
      - `value`
        - _um de (variantes):_
          - **variante**:
            - `number`
          - **variante**:
            - `null`
      - `status`: `string` enum: neutral, low, safe, high, unknown - What range does the measured metric fall into
    - `temperature`: `object` - Ambient light value (Lux).
      - `value`
        - _um de (variantes):_
          - **variante**:
            - `number`
          - **variante**:
            - `null`
      - `status`: `string` enum: neutral, low, safe, high, unknown - What range does the measured metric fall into
  - `lightSettings` **(obrigatório)**: `object` - Ambient light sensor settings.
    - `isEnabled`: `boolean` - Enable ambient light sensor.
    - `margin`: `number` - Ambient light threshold detection hysteresis margin (Lux). Read-only value decided by sensor implementation.
    - `lowThreshold`: `number|null` - Ambient light interrupt threshold low level from 1 to 503192 (Lux).
    - `highThreshold`: `number|null` - Ambient light interrupt threshold high level from 1 to 503192 (Lux).
  - `humiditySettings` **(obrigatório)**: `object` - Relative humidity sensor settings.
    - `isEnabled`: `boolean` - Enable relative humidity sensor.
    - `margin`: `number` - Humidity threshold detection hysteresis margin (%). Read-only value decided by sensor implementation.
    - `lowThreshold`: `number|null` - Humidity low level threshold from 1 to 99 (%).
    - `highThreshold`: `number|null` - Humidity high level threshold from 1 to 99 (%).
  - `temperatureSettings` **(obrigatório)**: `object` - Temperature sensor settings.
    - `isEnabled`: `boolean` - Enable temperature sensor.
    - `margin`: `number` - Temperature threshold detection hysteresis margin (C). Read-only value decided by sensor implementation.
    - `lowThreshold`: `number|null` - Temperature low level threshold from -39 to 124 (C).
    - `highThreshold`: `number|null` - Temperature high level threshold from -39 to 124 (C).
  - `isOpened` **(obrigatório)**: `boolean|null` - Whether the door/window/garage is opened.
  - `openStatusChangedAt` **(obrigatório)**: `number|null` - Unix timestamp when the door/window/garage was last opened or closed, nullable.
  - `isMotionDetected` **(obrigatório)**: `boolean` - Whether sensor is currently detecting the motion.
  - `motionDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the last motion was detected.
  - `motionSettings` **(obrigatório)**: `object` - Motion sensor settings.
    - `isEnabled`: `boolean` - Enable motion sensor.
    - `sensitivity`: `number` - Motion sensitivity (0-100) used when system is not armed or when no armed override is set.
    - `sensitivityWhenArmed`: `number` - Motion sensitivity (0-100) used when the system is armed and `hasCustomSensitivityWhenArmed` is true on the sensor.
  - `glassBreakSettings` **(obrigatório)**: `object` - Glass break sensor settings.
    - `isEnabled`: `boolean` - Enable glass break sensor.
    - `sensitivity`: `number` - Glass break sensitivity (0-100) used when system is not armed or when no armed override is set.
    - `sensitivityWhenArmed`: `number` - Glass break sensitivity (0-100) used when the system is armed and `hasCustomSensitivityWhenArmed` is true on the sensor.
  - `scheduleMode` **(obrigatório)**: `string` enum: always, when_armed - When armed-mode detection runs: `always` or only `when_armed`. Applies to both glass break and motion together.
  - `armProfileIds` **(obrigatório)**: `array|null` - When `scheduleMode` is `when_armed`, restricts armed-mode detection to these arm profile ids. Empty or null = all profiles.
  - `hasCustomSensitivityWhenArmed` **(obrigatório)**: `boolean` - When true, glass break and motion both use their respective `sensitivityWhenArmed` value while the system is armed.
  - `alarmTriggeredAt` **(obrigatório)**: `number|null` - Unix timestamp when the smoke or carbon monoxide alarm was triggered, nullable.
  - `alarmSettings` **(obrigatório)**: `object` - Smoke and carbon monoxide alarm sensor settings.
    - `isEnabled`: `boolean` - Enable smoke and carbon monoxide alarm sensor.
  - `leakDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected a water leak, nullable.
  - `externalLeakDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected an external water leak, nullable.
  - `leakSettings` **(obrigatório)**: `object` - Leak sensor settings.
    - `isInternalEnabled`: `boolean` - Enable internal water leak detection.
    - `isExternalEnabled`: `boolean` - Enable external water leak detection.
  - `tamperingDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected tampering, nullable.
  - `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
    - `signalState` **(obrigatório)**: `object` - Signal state.
      - `signalQuality` **(obrigatório)**: `number|null` - Percent representation of Bluetooth signal strength.
      - `signalStrength` **(obrigatório)**: `number|null` - dBm value of Bluetooth signal strength.
    - `batteryStatus` **(obrigatório)**: `object` - Battery status.
      - `percentage` **(obrigatório)**: `number|null` - Battery charge level from 0 to 100 (%).
      - `isLow` **(obrigatório)**: `boolean` - Low battery charge level flag.
    - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
      - _um de (variantes):_
        - **variante**:
          - `string`
        - **variante**:
          - `null`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/sensors" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/sensors" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Siren information & management


### Get siren details

`GET /v1/sirens/{id}`  ·  operationId: ``

Get detailed information about a specific siren

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of siren |

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of siren
- `modelKey` **(obrigatório)**: `string` - The model key of the siren
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `volume` **(obrigatório)**: `integer` - Volume: a number from 1-100.
- `ledSettings` **(obrigatório)**: `object` - Status LED settings.
  - `isEnabled` **(obrigatório)**: `boolean` - Enable status LED.
- `sirenStatus` **(obrigatório)**: `object` - Status of the siren
  - `isActive` **(obrigatório)**: `boolean` - Whether the siren is active.
  - `activatedAt` **(obrigatório)**: `number|null` - Timestamp when the siren was activated.
  - `duration` **(obrigatório)**
    - _um de (variantes):_
      - **variante**:
        - _um de (variantes):_
          - **variante**:
            - `number`
          - **variante**:
            - `number`
          - **variante**:
            - `number`
          - **variante**:
            - `number`
      - **variante**:
        - `null`
- `connectionType` **(obrigatório)**: `string` enum: ucp4, lora - The connection type of the siren.
- `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
  - `signalState` **(obrigatório)**: `object` - Signal state.
    - `signalQuality` **(obrigatório)**: `number|null` - Percent representation of Bluetooth signal strength.
    - `signalStrength` **(obrigatório)**: `number|null` - dBm value of Bluetooth signal strength.
  - `batteryStatus` **(obrigatório)**: `object` - Battery status.
    - `percentage` **(obrigatório)**: `number|null` - Battery charge level from 0 to 100 (%).
    - `isLow` **(obrigatório)**: `boolean` - Low battery charge level flag.
  - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/sirens/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/sirens/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Patch siren settings

`PATCH /v1/sirens/{id}`  ·  operationId: ``

Patch the settings for a specific siren

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of siren |

**Corpo da requisição** (`application/json`)

- `name`: `string` - The name of the device.
- `volume`: `integer` - Volume: a number from 1-100.
- `ledSettings`
  - `isEnabled` **(obrigatório)**: `boolean` - Enable status LED.

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of siren
- `modelKey` **(obrigatório)**: `string` - The model key of the siren
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `volume` **(obrigatório)**: `integer` - Volume: a number from 1-100.
- `ledSettings` **(obrigatório)**: `object` - Status LED settings.
  - `isEnabled` **(obrigatório)**: `boolean` - Enable status LED.
- `sirenStatus` **(obrigatório)**: `object` - Status of the siren
  - `isActive` **(obrigatório)**: `boolean` - Whether the siren is active.
  - `activatedAt` **(obrigatório)**: `number|null` - Timestamp when the siren was activated.
  - `duration` **(obrigatório)**
    - _um de (variantes):_
      - **variante**:
        - _um de (variantes):_
          - **variante**:
            - `number`
          - **variante**:
            - `number`
          - **variante**:
            - `number`
          - **variante**:
            - `number`
      - **variante**:
        - `null`
- `connectionType` **(obrigatório)**: `string` enum: ucp4, lora - The connection type of the siren.
- `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
  - `signalState` **(obrigatório)**: `object` - Signal state.
    - `signalQuality` **(obrigatório)**: `number|null` - Percent representation of Bluetooth signal strength.
    - `signalStrength` **(obrigatório)**: `number|null` - dBm value of Bluetooth signal strength.
  - `batteryStatus` **(obrigatório)**: `object` - Battery status.
    - `percentage` **(obrigatório)**: `number|null` - Battery charge level from 0 to 100 (%).
    - `isLow` **(obrigatório)**: `boolean` - Low battery charge level flag.
  - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PATCH "https://$UNIFI_HOST/proxy/protect/integration/v1/sirens/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PATCH "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/sirens/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get all sirens

`GET /v1/sirens`  ·  operationId: ``

Get detailed information about all sirens

**Resposta 200** - Success response

- _array de_ `object`:
  - `id` **(obrigatório)**: `string` - The primary key of siren
  - `modelKey` **(obrigatório)**: `string` - The model key of the siren
  - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
  - `name` **(obrigatório)**
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`
  - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
  - `volume` **(obrigatório)**: `integer` - Volume: a number from 1-100.
  - `ledSettings` **(obrigatório)**: `object` - Status LED settings.
    - `isEnabled` **(obrigatório)**: `boolean` - Enable status LED.
  - `sirenStatus` **(obrigatório)**: `object` - Status of the siren
    - `isActive` **(obrigatório)**: `boolean` - Whether the siren is active.
    - `activatedAt` **(obrigatório)**: `number|null` - Timestamp when the siren was activated.
    - `duration` **(obrigatório)**
      - _um de (variantes):_
        - **variante**:
          - _um de (variantes):_
            - **variante**:
              - `number`
            - **variante**:
              - `number`
            - **variante**:
              - `number`
            - **variante**:
              - `number`
        - **variante**:
          - `null`
  - `connectionType` **(obrigatório)**: `string` enum: ucp4, lora - The connection type of the siren.
  - `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
    - `signalState` **(obrigatório)**: `object` - Signal state.
      - `signalQuality` **(obrigatório)**: `number|null` - Percent representation of Bluetooth signal strength.
      - `signalStrength` **(obrigatório)**: `number|null` - dBm value of Bluetooth signal strength.
    - `batteryStatus` **(obrigatório)**: `object` - Battery status.
      - `percentage` **(obrigatório)**: `number|null` - Battery charge level from 0 to 100 (%).
      - `isLow` **(obrigatório)**: `boolean` - Low battery charge level flag.
    - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
      - _um de (variantes):_
        - **variante**:
          - `string`
        - **variante**:
          - `null`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/sirens" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/sirens" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Play siren

`POST /v1/sirens/{id}/play`  ·  operationId: ``

Activate the siren alarm for the specified duration. The siren status will be tracked and can be stopped early using the stop endpoint.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of siren |

**Corpo da requisição** (`application/json`)

- `duration`: Duration of the siren activation in seconds. Defaults to 5 seconds.
  - _um de (variantes):_
    - **variante**:
      - `number`
    - **variante**:
      - `number`
    - **variante**:
      - `number`
    - **variante**:
      - `number`

**Resposta 204** - The siren was activated successfully.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/protect/integration/v1/sirens/{id}/play" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/sirens/{id}/play" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Stop siren

`POST /v1/sirens/{id}/stop`  ·  operationId: ``

Stop an active siren.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of siren |

**Resposta 204** - The siren was stopped successfully.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/protect/integration/v1/sirens/{id}/stop" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/sirens/{id}/stop" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Test siren sound

`POST /v1/sirens/{id}/test-sound`  ·  operationId: ``

Test the siren sound for 5 seconds at the specified volume.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of siren |

**Corpo da requisição** (`application/json`)

- `volume`: `integer` - The volume for testing the siren sound. Defaults to the configured device volume.

**Resposta 204** - The siren sound test was initiated successfully.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/protect/integration/v1/sirens/{id}/test-sound" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/sirens/{id}/test-sound" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


---

## Fob information & management


### Get fob details

`GET /v1/fobs/{id}`  ·  operationId: ``

Get detailed information about a specific fob

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of fob |

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of fob
- `modelKey` **(obrigatório)**: `string` - The model key of the fob
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `awayState` **(obrigatório)**: `string` enum: ONLINE, RECENTLY_SEEN, NO_RECENT_HEARTBEAT, DEVICE_LOST - Fob presence/away state.
- `buttonLabels` **(obrigatório)**: `string` enum: securityActions, positionHint - Label style applied when this fob is rendered in button selection lists.
- `featureFlags` **(obrigatório)**: `object` - Feature flags for the fob.
  - `buttons` **(obrigatório)**: `array` - Available button types on the fob.
    - _array de_ `string`:
      - `string` enum: function, alarmHubButton, arm, disarm, night, panic, left, right, input1, input2
- `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
  - `signalState` **(obrigatório)**: `object` - Signal state.
    - `signalQuality` **(obrigatório)**: `number|null` - Percent representation of Bluetooth signal strength.
    - `signalStrength` **(obrigatório)**: `number|null` - dBm value of Bluetooth signal strength.
  - `batteryStatus` **(obrigatório)**: `object` - Battery status.
    - `percentage` **(obrigatório)**: `number|null` - Battery charge level from 0 to 100 (%).
    - `isLow` **(obrigatório)**: `boolean` - Low battery charge level flag.
  - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/fobs/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/fobs/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Patch fob settings

`PATCH /v1/fobs/{id}`  ·  operationId: ``

Patch the settings for a specific fob

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of fob |

**Corpo da requisição** (`application/json`)

- `name`: `string` - The name of the device.

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of fob
- `modelKey` **(obrigatório)**: `string` - The model key of the fob
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `awayState` **(obrigatório)**: `string` enum: ONLINE, RECENTLY_SEEN, NO_RECENT_HEARTBEAT, DEVICE_LOST - Fob presence/away state.
- `buttonLabels` **(obrigatório)**: `string` enum: securityActions, positionHint - Label style applied when this fob is rendered in button selection lists.
- `featureFlags` **(obrigatório)**: `object` - Feature flags for the fob.
  - `buttons` **(obrigatório)**: `array` - Available button types on the fob.
    - _array de_ `string`:
      - `string` enum: function, alarmHubButton, arm, disarm, night, panic, left, right, input1, input2
- `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
  - `signalState` **(obrigatório)**: `object` - Signal state.
    - `signalQuality` **(obrigatório)**: `number|null` - Percent representation of Bluetooth signal strength.
    - `signalStrength` **(obrigatório)**: `number|null` - dBm value of Bluetooth signal strength.
  - `batteryStatus` **(obrigatório)**: `object` - Battery status.
    - `percentage` **(obrigatório)**: `number|null` - Battery charge level from 0 to 100 (%).
    - `isLow` **(obrigatório)**: `boolean` - Low battery charge level flag.
  - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PATCH "https://$UNIFI_HOST/proxy/protect/integration/v1/fobs/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PATCH "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/fobs/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get all fobs

`GET /v1/fobs`  ·  operationId: ``

Get detailed information about all fobs

**Resposta 200** - Success response

- _array de_ `object`:
  - `id` **(obrigatório)**: `string` - The primary key of fob
  - `modelKey` **(obrigatório)**: `string` - The model key of the fob
  - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
  - `name` **(obrigatório)**
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`
  - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
  - `awayState` **(obrigatório)**: `string` enum: ONLINE, RECENTLY_SEEN, NO_RECENT_HEARTBEAT, DEVICE_LOST - Fob presence/away state.
  - `buttonLabels` **(obrigatório)**: `string` enum: securityActions, positionHint - Label style applied when this fob is rendered in button selection lists.
  - `featureFlags` **(obrigatório)**: `object` - Feature flags for the fob.
    - `buttons` **(obrigatório)**: `array` - Available button types on the fob.
      - _array de_ `string`:
        - `string` enum: function, alarmHubButton, arm, disarm, night, panic, left, right, input1, input2
  - `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
    - `signalState` **(obrigatório)**: `object` - Signal state.
      - `signalQuality` **(obrigatório)**: `number|null` - Percent representation of Bluetooth signal strength.
      - `signalStrength` **(obrigatório)**: `number|null` - dBm value of Bluetooth signal strength.
    - `batteryStatus` **(obrigatório)**: `object` - Battery status.
      - `percentage` **(obrigatório)**: `number|null` - Battery charge level from 0 to 100 (%).
      - `isLow` **(obrigatório)**: `boolean` - Low battery charge level flag.
    - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
      - _um de (variantes):_
        - **variante**:
          - `string`
        - **variante**:
          - `null`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/fobs" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/fobs" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Relay information & management


### Get relay details

`GET /v1/relays/{id}`  ·  operationId: ``

Get detailed information about a specific relay

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of relay |

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of relay
- `modelKey` **(obrigatório)**: `string` - The model key of the relay
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `ledSettings` **(obrigatório)**: `object` - Status LED settings.
  - `isEnabled` **(obrigatório)**: `boolean` - Enable status LED.
- `outputs` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `id` **(obrigatório)**: `number` - The channel index of the relay output.
    - `name` **(obrigatório)**: `string|null` - User-friendly name for this relay output.
    - `type` **(obrigatório)**: `string|null` enum: garageDoor, gate, valve, siren, custom - The type of device connected to this relay output.
    - `delay` **(obrigatório)**: `number|null` - Server-side delay in milliseconds before activation (0 = no delay, null = use default).
    - `pulseDuration` **(obrigatório)**: `number|null` - Auto-off duration in milliseconds (0 = permanent on until manually turned off, null = use default).
    - `state` **(obrigatório)**: `string|null` enum: on, off, offOtp - The current state of the relay output.
    - `rebootState` **(obrigatório)**: `string` enum: restore, on, off - The state the relay output should be set to after a reboot/power cycle.
- `inputs` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `id` **(obrigatório)**: `number` - The channel index of the relay input.
    - `name` **(obrigatório)**: `string|null` - User-friendly name for this relay input.
    - `state` **(obrigatório)**: `string|null` enum: on, off - The current state of the relay input.
    - `actionTrigger` **(obrigatório)**: `string|null` enum: switchedOn, switchedOff - The trigger event that activates the action.
    - `actionType` **(obrigatório)**: `string|null` enum: setOutputOn, setOutputOff, toggleOutput, followInput - The type of action to perform when triggered.
    - `actionOutputId` **(obrigatório)**: `number|null` - The index of the output to control when triggered.
- `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
  - `signalState` **(obrigatório)**: `object` - Signal state.
    - `signalQuality` **(obrigatório)**: `number|null` - Percent representation of Bluetooth signal strength.
    - `signalStrength` **(obrigatório)**: `number|null` - dBm value of Bluetooth signal strength.
  - `batteryStatus` **(obrigatório)**: `object` - Battery status.
    - `percentage` **(obrigatório)**: `number|null` - Battery charge level from 0 to 100 (%).
    - `isLow` **(obrigatório)**: `boolean` - Low battery charge level flag.
  - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/relays/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/relays/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Patch relay settings

`PATCH /v1/relays/{id}`  ·  operationId: ``

Patch the settings for a specific relay

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of relay |

**Corpo da requisição** (`application/json`)

- `name`: `string` - The name of the device.
- `ledSettings`: `object` - Status LED settings.
  - `isEnabled`: `boolean` - Enable status LED.

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of relay
- `modelKey` **(obrigatório)**: `string` - The model key of the relay
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `ledSettings` **(obrigatório)**: `object` - Status LED settings.
  - `isEnabled` **(obrigatório)**: `boolean` - Enable status LED.
- `outputs` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `id` **(obrigatório)**: `number` - The channel index of the relay output.
    - `name` **(obrigatório)**: `string|null` - User-friendly name for this relay output.
    - `type` **(obrigatório)**: `string|null` enum: garageDoor, gate, valve, siren, custom - The type of device connected to this relay output.
    - `delay` **(obrigatório)**: `number|null` - Server-side delay in milliseconds before activation (0 = no delay, null = use default).
    - `pulseDuration` **(obrigatório)**: `number|null` - Auto-off duration in milliseconds (0 = permanent on until manually turned off, null = use default).
    - `state` **(obrigatório)**: `string|null` enum: on, off, offOtp - The current state of the relay output.
    - `rebootState` **(obrigatório)**: `string` enum: restore, on, off - The state the relay output should be set to after a reboot/power cycle.
- `inputs` **(obrigatório)**: `array`
  - _array de_ `object`:
    - `id` **(obrigatório)**: `number` - The channel index of the relay input.
    - `name` **(obrigatório)**: `string|null` - User-friendly name for this relay input.
    - `state` **(obrigatório)**: `string|null` enum: on, off - The current state of the relay input.
    - `actionTrigger` **(obrigatório)**: `string|null` enum: switchedOn, switchedOff - The trigger event that activates the action.
    - `actionType` **(obrigatório)**: `string|null` enum: setOutputOn, setOutputOff, toggleOutput, followInput - The type of action to perform when triggered.
    - `actionOutputId` **(obrigatório)**: `number|null` - The index of the output to control when triggered.
- `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
  - `signalState` **(obrigatório)**: `object` - Signal state.
    - `signalQuality` **(obrigatório)**: `number|null` - Percent representation of Bluetooth signal strength.
    - `signalStrength` **(obrigatório)**: `number|null` - dBm value of Bluetooth signal strength.
  - `batteryStatus` **(obrigatório)**: `object` - Battery status.
    - `percentage` **(obrigatório)**: `number|null` - Battery charge level from 0 to 100 (%).
    - `isLow` **(obrigatório)**: `boolean` - Low battery charge level flag.
  - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PATCH "https://$UNIFI_HOST/proxy/protect/integration/v1/relays/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PATCH "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/relays/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get all relays

`GET /v1/relays`  ·  operationId: ``

Get detailed information about all relays

**Resposta 200** - Success response

- _array de_ `object`:
  - `id` **(obrigatório)**: `string` - The primary key of relay
  - `modelKey` **(obrigatório)**: `string` - The model key of the relay
  - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
  - `name` **(obrigatório)**
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`
  - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
  - `ledSettings` **(obrigatório)**: `object` - Status LED settings.
    - `isEnabled` **(obrigatório)**: `boolean` - Enable status LED.
  - `outputs` **(obrigatório)**: `array`
    - _array de_ `object`:
      - `id` **(obrigatório)**: `number` - The channel index of the relay output.
      - `name` **(obrigatório)**: `string|null` - User-friendly name for this relay output.
      - `type` **(obrigatório)**: `string|null` enum: garageDoor, gate, valve, siren, custom - The type of device connected to this relay output.
      - `delay` **(obrigatório)**: `number|null` - Server-side delay in milliseconds before activation (0 = no delay, null = use default).
      - `pulseDuration` **(obrigatório)**: `number|null` - Auto-off duration in milliseconds (0 = permanent on until manually turned off, null = use default).
      - `state` **(obrigatório)**: `string|null` enum: on, off, offOtp - The current state of the relay output.
      - `rebootState` **(obrigatório)**: `string` enum: restore, on, off - The state the relay output should be set to after a reboot/power cycle.
  - `inputs` **(obrigatório)**: `array`
    - _array de_ `object`:
      - `id` **(obrigatório)**: `number` - The channel index of the relay input.
      - `name` **(obrigatório)**: `string|null` - User-friendly name for this relay input.
      - `state` **(obrigatório)**: `string|null` enum: on, off - The current state of the relay input.
      - `actionTrigger` **(obrigatório)**: `string|null` enum: switchedOn, switchedOff - The trigger event that activates the action.
      - `actionType` **(obrigatório)**: `string|null` enum: setOutputOn, setOutputOff, toggleOutput, followInput - The type of action to perform when triggered.
      - `actionOutputId` **(obrigatório)**: `number|null` - The index of the output to control when triggered.
  - `wirelessConnectionState` **(obrigatório)**: `object` - Wireless connection state including signal quality, battery status, and bridge connection.
    - `signalState` **(obrigatório)**: `object` - Signal state.
      - `signalQuality` **(obrigatório)**: `number|null` - Percent representation of Bluetooth signal strength.
      - `signalStrength` **(obrigatório)**: `number|null` - dBm value of Bluetooth signal strength.
    - `batteryStatus` **(obrigatório)**: `object` - Battery status.
      - `percentage` **(obrigatório)**: `number|null` - Battery charge level from 0 to 100 (%).
      - `isLow` **(obrigatório)**: `boolean` - Low battery charge level flag.
    - `bridge` **(obrigatório)**: The ID of the bridge this device is connected through.
      - _um de (variantes):_
        - **variante**:
          - `string`
        - **variante**:
          - `null`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/relays" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/relays" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Activate relay output

`POST /v1/relays/{id}/outputs/{outputId}/activate`  ·  operationId: ``

Control a relay output state. Use "state" to set a specific state (on/off), or omit to toggle. When state is "on", you can optionally provide "pulseDuration" to auto-turn off after the specified milliseconds.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of relay |
| `outputId` | path | sim | integer | Output channel ID (0 or 1) |

**Corpo da requisição** (`application/json`)

- `state`: `string` enum: on, off - Desired output state. If omitted, toggles the current state.
- `pulseDuration`: `integer` - Auto-off duration in milliseconds (only applies when state is "on"). If greater than 0, the output auto-turns off after the specified duration.

**Resposta 204** - The relay output activation was initiated successfully.

**Erros possíveis:** `503`, `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/protect/integration/v1/relays/{id}/outputs/{outputId}/activate" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/relays/{id}/outputs/{outputId}/activate" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


---

## Speaker information & management


### Get speaker details

`GET /v1/speakers/{id}`  ·  operationId: ``

Get detailed information about a specific speaker

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of speaker |

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of speaker
- `modelKey` **(obrigatório)**: `string` - The model key of the speaker
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `volume` **(obrigatório)**: `integer` - Speaker volume: a number from 0-100.
- `micVolume` **(obrigatório)**: `integer` - Mic volume: a number from 0-100.
- `isMicEnabled` **(obrigatório)**: `boolean` - Whether or not the microphone on the speaker is enabled.
- `speakerState` **(obrigatório)**: `object` - Real-time state of Speaker
  - `status` **(obrigatório)**: `string` enum: idle, streaming, playing, tts_playing, uploading - Current status of the speaker
  - `mode` **(obrigatório)**: `string` enum: listen, talk - Current mode of the speaker
- `featureFlags` **(obrigatório)**: `object` - Feature flags of the speaker
  - `hasMic` **(obrigatório)**: `boolean` - Whether the device has a microphone.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/speakers/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/speakers/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Patch speaker settings

`PATCH /v1/speakers/{id}`  ·  operationId: ``

Patch the settings for a specific speaker

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of speaker |

**Corpo da requisição** (`application/json`)

- `name`: `string` - The name of the device.
- `volume`: `integer` - Speaker volume: a number from 0-100.
- `micVolume`: `integer` - Mic volume: a number from 0-100.
- `isMicEnabled`: `boolean` - Whether or not the microphone on the speaker is enabled.

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of speaker
- `modelKey` **(obrigatório)**: `string` - The model key of the speaker
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `volume` **(obrigatório)**: `integer` - Speaker volume: a number from 0-100.
- `micVolume` **(obrigatório)**: `integer` - Mic volume: a number from 0-100.
- `isMicEnabled` **(obrigatório)**: `boolean` - Whether or not the microphone on the speaker is enabled.
- `speakerState` **(obrigatório)**: `object` - Real-time state of Speaker
  - `status` **(obrigatório)**: `string` enum: idle, streaming, playing, tts_playing, uploading - Current status of the speaker
  - `mode` **(obrigatório)**: `string` enum: listen, talk - Current mode of the speaker
- `featureFlags` **(obrigatório)**: `object` - Feature flags of the speaker
  - `hasMic` **(obrigatório)**: `boolean` - Whether the device has a microphone.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PATCH "https://$UNIFI_HOST/proxy/protect/integration/v1/speakers/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PATCH "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/speakers/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get all speakers

`GET /v1/speakers`  ·  operationId: ``

Get detailed information about all speakers

**Resposta 200** - Success response

- _array de_ `object`:
  - `id` **(obrigatório)**: `string` - The primary key of speaker
  - `modelKey` **(obrigatório)**: `string` - The model key of the speaker
  - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
  - `name` **(obrigatório)**
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`
  - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
  - `volume` **(obrigatório)**: `integer` - Speaker volume: a number from 0-100.
  - `micVolume` **(obrigatório)**: `integer` - Mic volume: a number from 0-100.
  - `isMicEnabled` **(obrigatório)**: `boolean` - Whether or not the microphone on the speaker is enabled.
  - `speakerState` **(obrigatório)**: `object` - Real-time state of Speaker
    - `status` **(obrigatório)**: `string` enum: idle, streaming, playing, tts_playing, uploading - Current status of the speaker
    - `mode` **(obrigatório)**: `string` enum: listen, talk - Current mode of the speaker
  - `featureFlags` **(obrigatório)**: `object` - Feature flags of the speaker
    - `hasMic` **(obrigatório)**: `boolean` - Whether the device has a microphone.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/speakers" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/speakers" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Test speaker sound

`POST /v1/speakers/{id}/test-sound`  ·  operationId: ``

Test the speaker sound at the specified volume.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of speaker |

**Corpo da requisição** (`application/json`)

- `volume`: `integer` - The volume for testing the speaker sound. Defaults to the configured device volume.

**Resposta 204** - The speaker sound test was initiated successfully.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/protect/integration/v1/speakers/{id}/test-sound" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/speakers/{id}/test-sound" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


---

## Bridge information & management


### Get bridge details

`GET /v1/bridges/{id}`  ·  operationId: ``

Get detailed information about a specific bridge

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of bridge |

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of bridge
- `modelKey` **(obrigatório)**: `string` - The model key of the bridge
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `platform` **(obrigatório)**: `string|null` - The bridge platform
- `clients` **(obrigatório)**: `array` - Array of IoT devices mac that bridge is reserving for
  - _array de_ `string`:
    - `string`
- `maxClients` **(obrigatório)**: `number` - The max acceptable client number of a V2 bridge. V1 bridge does not support this feature.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/bridges/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/bridges/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Patch bridge settings

`PATCH /v1/bridges/{id}`  ·  operationId: ``

Patch the settings for a specific bridge

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of bridge |

**Corpo da requisição** (`application/json`)

- `name`: `string` - The name of the device.

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of bridge
- `modelKey` **(obrigatório)**: `string` - The model key of the bridge
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `platform` **(obrigatório)**: `string|null` - The bridge platform
- `clients` **(obrigatório)**: `array` - Array of IoT devices mac that bridge is reserving for
  - _array de_ `string`:
    - `string`
- `maxClients` **(obrigatório)**: `number` - The max acceptable client number of a V2 bridge. V1 bridge does not support this feature.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PATCH "https://$UNIFI_HOST/proxy/protect/integration/v1/bridges/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PATCH "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/bridges/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get all bridges

`GET /v1/bridges`  ·  operationId: ``

Get detailed information about all bridges

**Resposta 200** - Success response

- _array de_ `object`:
  - `id` **(obrigatório)**: `string` - The primary key of bridge
  - `modelKey` **(obrigatório)**: `string` - The model key of the bridge
  - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
  - `name` **(obrigatório)**
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`
  - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
  - `platform` **(obrigatório)**: `string|null` - The bridge platform
  - `clients` **(obrigatório)**: `array` - Array of IoT devices mac that bridge is reserving for
    - _array de_ `string`:
      - `string`
  - `maxClients` **(obrigatório)**: `number` - The max acceptable client number of a V2 bridge. V1 bridge does not support this feature.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/bridges" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/bridges" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Link station information & management


### Get link station details

`GET /v1/link-stations/{id}`  ·  operationId: ``

Get detailed information about a specific link station (non-alarm hub gateways)

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of linkStation |

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of linkStation
- `modelKey` **(obrigatório)**: `string` - The model key of the linkstation
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `isAlarmHub` **(obrigatório)**: `boolean` - Whether the linkstation is an alarm hub.
- `ledSettings` **(obrigatório)**: `object` - Status LED settings.
  - `isEnabled` **(obrigatório)**: `boolean` - Whether the status LED is enabled.
- `lastEvent` **(obrigatório)**: `number|null` - Timestamp when any last event was detected.
- `alarmHub`: `object` - Alarm hub status and configuration. Only present when isAlarmHub is true.
  - `armed` **(obrigatório)**: `string` enum: on, off
  - `battery`: `object`
    - `charging`: `string` enum: on, off
    - `connection`: `string` enum: connected, disconnected
    - `voltage`: `number`
    - `batteryStatus`: `string` enum: ok, low, critical
  - `buckboost` **(obrigatório)**: `string` enum: on, off
  - `connector`: `object`
    - `emergency`: `object`
      - `+` **(obrigatório)**: `string` enum: connected, disconnected
      - `-` **(obrigatório)**: `string` enum: connected, disconnected
    - `12v`: `object`
    - `relay`: `object`
    - `tb`: `object`
    - `battery`: `string` enum: connected, disconnected
    - `poeout`: `string` enum: connected, disconnected
  - `cover`: `object`
    - `distance`: `integer`
    - `status`: `string` enum: open, close
  - `currentMeterChannelStatus` **(obrigatório)**: `object`
  - `currentMeterStatus` **(obrigatório)**: `object`
  - `inputPower`: `object`
    - `bt`: `string` enum: low, high
    - `typ1`: `string` enum: low, high
    - `typ2`: `string` enum: low, high
  - `poeout`: `object`
    - `connection`: `string` enum: connected, disconnected
    - `powerSupply`: `string` enum: on, off
  - `powerMeter` **(obrigatório)**: `object`
  - `output` **(obrigatório)**: `object`
  - `input` **(obrigatório)**: `object`
  - `inputTerminalStatus`: `object`
  - `outputTerminalStatus`: `object`
  - `emergencyTerminalStatus`: `object|null`
    - `plusPinStatus` **(obrigatório)**: `string` enum: disabled, idle, not-connected, tamper, triggered, cut, short
    - `minusPinStatus` **(obrigatório)**: `string` enum: disabled, idle, not-connected, tamper, triggered, cut, short
    - `terminalStatus` **(obrigatório)**: `string` enum: disabled, idle, not-connected, tamper, triggered, cut, short, partially-connected
    - `idleSubState`: `string` enum: open, closed
  - `auxiliaryPowerTerminalStatus`: `object`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/link-stations/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/link-stations/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Patch link station settings

`PATCH /v1/link-stations/{id}`  ·  operationId: ``

Patch the settings for a specific link station

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of linkStation |

**Corpo da requisição** (`application/json`)

- `name`: `string` - The name of the device.

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of linkStation
- `modelKey` **(obrigatório)**: `string` - The model key of the linkstation
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `isAlarmHub` **(obrigatório)**: `boolean` - Whether the linkstation is an alarm hub.
- `ledSettings` **(obrigatório)**: `object` - Status LED settings.
  - `isEnabled` **(obrigatório)**: `boolean` - Whether the status LED is enabled.
- `lastEvent` **(obrigatório)**: `number|null` - Timestamp when any last event was detected.
- `alarmHub`: `object` - Alarm hub status and configuration. Only present when isAlarmHub is true.
  - `armed` **(obrigatório)**: `string` enum: on, off
  - `battery`: `object`
    - `charging`: `string` enum: on, off
    - `connection`: `string` enum: connected, disconnected
    - `voltage`: `number`
    - `batteryStatus`: `string` enum: ok, low, critical
  - `buckboost` **(obrigatório)**: `string` enum: on, off
  - `connector`: `object`
    - `emergency`: `object`
      - `+` **(obrigatório)**: `string` enum: connected, disconnected
      - `-` **(obrigatório)**: `string` enum: connected, disconnected
    - `12v`: `object`
    - `relay`: `object`
    - `tb`: `object`
    - `battery`: `string` enum: connected, disconnected
    - `poeout`: `string` enum: connected, disconnected
  - `cover`: `object`
    - `distance`: `integer`
    - `status`: `string` enum: open, close
  - `currentMeterChannelStatus` **(obrigatório)**: `object`
  - `currentMeterStatus` **(obrigatório)**: `object`
  - `inputPower`: `object`
    - `bt`: `string` enum: low, high
    - `typ1`: `string` enum: low, high
    - `typ2`: `string` enum: low, high
  - `poeout`: `object`
    - `connection`: `string` enum: connected, disconnected
    - `powerSupply`: `string` enum: on, off
  - `powerMeter` **(obrigatório)**: `object`
  - `output` **(obrigatório)**: `object`
  - `input` **(obrigatório)**: `object`
  - `inputTerminalStatus`: `object`
  - `outputTerminalStatus`: `object`
  - `emergencyTerminalStatus`: `object|null`
    - `plusPinStatus` **(obrigatório)**: `string` enum: disabled, idle, not-connected, tamper, triggered, cut, short
    - `minusPinStatus` **(obrigatório)**: `string` enum: disabled, idle, not-connected, tamper, triggered, cut, short
    - `terminalStatus` **(obrigatório)**: `string` enum: disabled, idle, not-connected, tamper, triggered, cut, short, partially-connected
    - `idleSubState`: `string` enum: open, closed
  - `auxiliaryPowerTerminalStatus`: `object`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PATCH "https://$UNIFI_HOST/proxy/protect/integration/v1/link-stations/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PATCH "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/link-stations/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get all link stations

`GET /v1/link-stations`  ·  operationId: ``

Get detailed information about all link stations (non-alarm hub gateways)

**Resposta 200** - Success response

- _array de_ `object`:
  - `id` **(obrigatório)**: `string` - The primary key of linkStation
  - `modelKey` **(obrigatório)**: `string` - The model key of the linkstation
  - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
  - `name` **(obrigatório)**
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`
  - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
  - `isAlarmHub` **(obrigatório)**: `boolean` - Whether the linkstation is an alarm hub.
  - `ledSettings` **(obrigatório)**: `object` - Status LED settings.
    - `isEnabled` **(obrigatório)**: `boolean` - Whether the status LED is enabled.
  - `lastEvent` **(obrigatório)**: `number|null` - Timestamp when any last event was detected.
  - `alarmHub`: `object` - Alarm hub status and configuration. Only present when isAlarmHub is true.
    - `armed` **(obrigatório)**: `string` enum: on, off
    - `battery`: `object`
      - `charging`: `string` enum: on, off
      - `connection`: `string` enum: connected, disconnected
      - `voltage`: `number`
      - `batteryStatus`: `string` enum: ok, low, critical
    - `buckboost` **(obrigatório)**: `string` enum: on, off
    - `connector`: `object`
      - `emergency`: `object`
        - `+` **(obrigatório)**: `string` enum: connected, disconnected
        - `-` **(obrigatório)**: `string` enum: connected, disconnected
      - `12v`: `object`
      - `relay`: `object`
      - `tb`: `object`
      - `battery`: `string` enum: connected, disconnected
      - `poeout`: `string` enum: connected, disconnected
    - `cover`: `object`
      - `distance`: `integer`
      - `status`: `string` enum: open, close
    - `currentMeterChannelStatus` **(obrigatório)**: `object`
    - `currentMeterStatus` **(obrigatório)**: `object`
    - `inputPower`: `object`
      - `bt`: `string` enum: low, high
      - `typ1`: `string` enum: low, high
      - `typ2`: `string` enum: low, high
    - `poeout`: `object`
      - `connection`: `string` enum: connected, disconnected
      - `powerSupply`: `string` enum: on, off
    - `powerMeter` **(obrigatório)**: `object`
    - `output` **(obrigatório)**: `object`
    - `input` **(obrigatório)**: `object`
    - `inputTerminalStatus`: `object`
    - `outputTerminalStatus`: `object`
    - `emergencyTerminalStatus`: `object|null`
      - `plusPinStatus` **(obrigatório)**: `string` enum: disabled, idle, not-connected, tamper, triggered, cut, short
      - `minusPinStatus` **(obrigatório)**: `string` enum: disabled, idle, not-connected, tamper, triggered, cut, short
      - `terminalStatus` **(obrigatório)**: `string` enum: disabled, idle, not-connected, tamper, triggered, cut, short, partially-connected
      - `idleSubState`: `string` enum: open, closed
    - `auxiliaryPowerTerminalStatus`: `object`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/link-stations" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/link-stations" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Alarm hub information & management


### Get alarm hub details

`GET /v1/alarm-hubs/{id}`  ·  operationId: ``

Get detailed information about a specific alarm hub

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of linkStation |

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of linkStation
- `modelKey` **(obrigatório)**: `string` - The model key of the linkstation
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `isAlarmHub` **(obrigatório)**: `boolean` - Whether the linkstation is an alarm hub.
- `ledSettings` **(obrigatório)**: `object` - Status LED settings.
  - `isEnabled` **(obrigatório)**: `boolean` - Whether the status LED is enabled.
- `lastEvent` **(obrigatório)**: `number|null` - Timestamp when any last event was detected.
- `alarmHub`: `object` - Alarm hub status and configuration. Only present when isAlarmHub is true.
  - `armed` **(obrigatório)**: `string` enum: on, off
  - `battery`: `object`
    - `charging`: `string` enum: on, off
    - `connection`: `string` enum: connected, disconnected
    - `voltage`: `number`
    - `batteryStatus`: `string` enum: ok, low, critical
  - `buckboost` **(obrigatório)**: `string` enum: on, off
  - `connector`: `object`
    - `emergency`: `object`
      - `+` **(obrigatório)**: `string` enum: connected, disconnected
      - `-` **(obrigatório)**: `string` enum: connected, disconnected
    - `12v`: `object`
    - `relay`: `object`
    - `tb`: `object`
    - `battery`: `string` enum: connected, disconnected
    - `poeout`: `string` enum: connected, disconnected
  - `cover`: `object`
    - `distance`: `integer`
    - `status`: `string` enum: open, close
  - `currentMeterChannelStatus` **(obrigatório)**: `object`
  - `currentMeterStatus` **(obrigatório)**: `object`
  - `inputPower`: `object`
    - `bt`: `string` enum: low, high
    - `typ1`: `string` enum: low, high
    - `typ2`: `string` enum: low, high
  - `poeout`: `object`
    - `connection`: `string` enum: connected, disconnected
    - `powerSupply`: `string` enum: on, off
  - `powerMeter` **(obrigatório)**: `object`
  - `output` **(obrigatório)**: `object`
  - `input` **(obrigatório)**: `object`
  - `inputTerminalStatus`: `object`
  - `outputTerminalStatus`: `object`
  - `emergencyTerminalStatus`: `object|null`
    - `plusPinStatus` **(obrigatório)**: `string` enum: disabled, idle, not-connected, tamper, triggered, cut, short
    - `minusPinStatus` **(obrigatório)**: `string` enum: disabled, idle, not-connected, tamper, triggered, cut, short
    - `terminalStatus` **(obrigatório)**: `string` enum: disabled, idle, not-connected, tamper, triggered, cut, short, partially-connected
    - `idleSubState`: `string` enum: open, closed
  - `auxiliaryPowerTerminalStatus`: `object`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/alarm-hubs/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/alarm-hubs/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Patch alarm hub settings

`PATCH /v1/alarm-hubs/{id}`  ·  operationId: ``

Patch the settings for a specific alarm hub

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of linkStation |

**Corpo da requisição** (`application/json`)

- `name`: `string` - The name of the device.

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of linkStation
- `modelKey` **(obrigatório)**: `string` - The model key of the linkstation
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `isAlarmHub` **(obrigatório)**: `boolean` - Whether the linkstation is an alarm hub.
- `ledSettings` **(obrigatório)**: `object` - Status LED settings.
  - `isEnabled` **(obrigatório)**: `boolean` - Whether the status LED is enabled.
- `lastEvent` **(obrigatório)**: `number|null` - Timestamp when any last event was detected.
- `alarmHub`: `object` - Alarm hub status and configuration. Only present when isAlarmHub is true.
  - `armed` **(obrigatório)**: `string` enum: on, off
  - `battery`: `object`
    - `charging`: `string` enum: on, off
    - `connection`: `string` enum: connected, disconnected
    - `voltage`: `number`
    - `batteryStatus`: `string` enum: ok, low, critical
  - `buckboost` **(obrigatório)**: `string` enum: on, off
  - `connector`: `object`
    - `emergency`: `object`
      - `+` **(obrigatório)**: `string` enum: connected, disconnected
      - `-` **(obrigatório)**: `string` enum: connected, disconnected
    - `12v`: `object`
    - `relay`: `object`
    - `tb`: `object`
    - `battery`: `string` enum: connected, disconnected
    - `poeout`: `string` enum: connected, disconnected
  - `cover`: `object`
    - `distance`: `integer`
    - `status`: `string` enum: open, close
  - `currentMeterChannelStatus` **(obrigatório)**: `object`
  - `currentMeterStatus` **(obrigatório)**: `object`
  - `inputPower`: `object`
    - `bt`: `string` enum: low, high
    - `typ1`: `string` enum: low, high
    - `typ2`: `string` enum: low, high
  - `poeout`: `object`
    - `connection`: `string` enum: connected, disconnected
    - `powerSupply`: `string` enum: on, off
  - `powerMeter` **(obrigatório)**: `object`
  - `output` **(obrigatório)**: `object`
  - `input` **(obrigatório)**: `object`
  - `inputTerminalStatus`: `object`
  - `outputTerminalStatus`: `object`
  - `emergencyTerminalStatus`: `object|null`
    - `plusPinStatus` **(obrigatório)**: `string` enum: disabled, idle, not-connected, tamper, triggered, cut, short
    - `minusPinStatus` **(obrigatório)**: `string` enum: disabled, idle, not-connected, tamper, triggered, cut, short
    - `terminalStatus` **(obrigatório)**: `string` enum: disabled, idle, not-connected, tamper, triggered, cut, short, partially-connected
    - `idleSubState`: `string` enum: open, closed
  - `auxiliaryPowerTerminalStatus`: `object`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PATCH "https://$UNIFI_HOST/proxy/protect/integration/v1/alarm-hubs/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PATCH "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/alarm-hubs/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get all alarm hubs

`GET /v1/alarm-hubs`  ·  operationId: ``

Get detailed information about all alarm hubs

**Resposta 200** - Success response

- _array de_ `object`:
  - `id` **(obrigatório)**: `string` - The primary key of linkStation
  - `modelKey` **(obrigatório)**: `string` - The model key of the linkstation
  - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
  - `name` **(obrigatório)**
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`
  - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
  - `isAlarmHub` **(obrigatório)**: `boolean` - Whether the linkstation is an alarm hub.
  - `ledSettings` **(obrigatório)**: `object` - Status LED settings.
    - `isEnabled` **(obrigatório)**: `boolean` - Whether the status LED is enabled.
  - `lastEvent` **(obrigatório)**: `number|null` - Timestamp when any last event was detected.
  - `alarmHub`: `object` - Alarm hub status and configuration. Only present when isAlarmHub is true.
    - `armed` **(obrigatório)**: `string` enum: on, off
    - `battery`: `object`
      - `charging`: `string` enum: on, off
      - `connection`: `string` enum: connected, disconnected
      - `voltage`: `number`
      - `batteryStatus`: `string` enum: ok, low, critical
    - `buckboost` **(obrigatório)**: `string` enum: on, off
    - `connector`: `object`
      - `emergency`: `object`
        - `+` **(obrigatório)**: `string` enum: connected, disconnected
        - `-` **(obrigatório)**: `string` enum: connected, disconnected
      - `12v`: `object`
      - `relay`: `object`
      - `tb`: `object`
      - `battery`: `string` enum: connected, disconnected
      - `poeout`: `string` enum: connected, disconnected
    - `cover`: `object`
      - `distance`: `integer`
      - `status`: `string` enum: open, close
    - `currentMeterChannelStatus` **(obrigatório)**: `object`
    - `currentMeterStatus` **(obrigatório)**: `object`
    - `inputPower`: `object`
      - `bt`: `string` enum: low, high
      - `typ1`: `string` enum: low, high
      - `typ2`: `string` enum: low, high
    - `poeout`: `object`
      - `connection`: `string` enum: connected, disconnected
      - `powerSupply`: `string` enum: on, off
    - `powerMeter` **(obrigatório)**: `object`
    - `output` **(obrigatório)**: `object`
    - `input` **(obrigatório)**: `object`
    - `inputTerminalStatus`: `object`
    - `outputTerminalStatus`: `object`
    - `emergencyTerminalStatus`: `object|null`
      - `plusPinStatus` **(obrigatório)**: `string` enum: disabled, idle, not-connected, tamper, triggered, cut, short
      - `minusPinStatus` **(obrigatório)**: `string` enum: disabled, idle, not-connected, tamper, triggered, cut, short
      - `terminalStatus` **(obrigatório)**: `string` enum: disabled, idle, not-connected, tamper, triggered, cut, short, partially-connected
      - `idleSubState`: `string` enum: open, closed
    - `auxiliaryPowerTerminalStatus`: `object`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/alarm-hubs" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/alarm-hubs" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Trigger alarm hub output

`POST /v1/alarm-hubs/{id}/outputs/{outputId}/trigger`  ·  operationId: ``

Trigger an alarm hub output channel. Can be used to turn on/off connected devices like sirens, lights, or other actuators.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of linkStation |
| `outputId` | path | sim | integer | Output channel ID (0 or 1) |

**Corpo da requisição** (`application/json`)

- `enable`: `boolean` - Set to true to turn on, false to turn off. If omitted, toggles the current state.
- `delay`: `integer` - Delay in milliseconds before the output activates
- `duration`: `integer` - Duration in milliseconds to keep the output active. 0 means indefinite until manually turned off.

**Resposta 204** - The output trigger was initiated successfully.

**Erros possíveis:** `503`, `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/protect/integration/v1/alarm-hubs/{id}/outputs/{outputId}/trigger" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/alarm-hubs/{id}/outputs/{outputId}/trigger" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


---

## NVR information & management


### Get NVR details

`GET /v1/nvrs`  ·  operationId: ``

Get detailed information about the NVR

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of nvr
- `modelKey` **(obrigatório)**: `string` - The model key of the nvr
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `doorbellSettings` **(obrigatório)**: `object`
  - `defaultMessageText`: `string` - Default text to display on the LCD screen.
  - `defaultMessageResetTimeoutMs`: `number` - Default timeout for resetting LCD screen to the default message.
  - `customMessages`: `array` - A list of custom doorbell messages.
    - _array de_ `string`:
      - `string`
  - `customImages`: `array` - A list of custom doorbell images for client preview.
    - _array de_ `object`:
      - `preview` **(obrigatório)**: `string`
      - `sprite` **(obrigatório)**: `string`
- `armMode` **(obrigatório)**: `object`
  - `status` **(obrigatório)**: `string` enum: arming, armed, breach, disabled
  - `armProfileId` **(obrigatório)**: `string|null`
  - `armedAt` **(obrigatório)**: `number|null`
  - `willBeArmedAt` **(obrigatório)**: `number|null`
  - `breachDetectedAt` **(obrigatório)**: `number|null`
  - `breachEventCount` **(obrigatório)**: `number`
  - `breachTriggerEventId` **(obrigatório)**: `string|null`
  - `breachEventId` **(obrigatório)**: `string|null`

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/nvrs" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/nvrs" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Device asset file management


### Get device asset files

`GET /v1/files/{fileType}`  ·  operationId: ``

Get a list of all device asset files

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `fileType` | path | sim | string enum | Device asset file type |

**Resposta 200** - Device asset list

- _array de_ `object`:
  - `name` **(obrigatório)**: `string` - Unique ID for the asset file
  - `type` **(obrigatório)**: `string` enum: animations - Device asset file type
  - `originalName`: `string` - Original filename of the uploaded file
  - `path` **(obrigatório)**: `string` - Path to the file on the filesystem

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/files/{fileType}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/files/{fileType}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Upload device asset file

`POST /v1/files/{fileType}`  ·  operationId: ``

Upload a new device asset file

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `fileType` | path | sim | string enum | Device asset file type |

**Resposta 200** - Processed and persisted device asset

- `name` **(obrigatório)**: `string` - Unique ID for the asset file
- `type` **(obrigatório)**: `string` enum: animations - Device asset file type
- `originalName`: `string` - Original filename of the uploaded file
- `path` **(obrigatório)**: `string` - Path to the file on the filesystem

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X POST "https://$UNIFI_HOST/proxy/protect/integration/v1/files/{fileType}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X POST "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/files/{fileType}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Chime information & management


### Get chime details

`GET /v1/chimes/{id}`  ·  operationId: ``

Get detailed information about a specific chime

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of chime |

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of chime
- `modelKey` **(obrigatório)**: `string` - The model key of the chime
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `cameraIds` **(obrigatório)**: `array` - The list of (doorbell-only) cameras which this chime is paired to.
  - _array de_ `string`:
    - `string`
- `ringSettings` **(obrigatório)**: `array` - List of custom ringtone settings for (doorbell-only) cameras paired to this chime.
  - _array de_ `object`:
    - `cameraId` **(obrigatório)**: `string` - Which paired (doorbell-only) camera do these settings refer to.
    - `repeatTimes` **(obrigatório)**: `number` - How many times should the ringtone be repeated
    - `ringtoneId` **(obrigatório)**: `string` - The ID of the ringtone that should be played when the (doorbell-only) camera is rung.
    - `volume` **(obrigatório)**: `number` - How loud should the ringtone be played. 0 being silent and 100 the loudest.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/chimes/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/chimes/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Patch chime settings

`PATCH /v1/chimes/{id}`  ·  operationId: ``

Patch the settings for a specific chime

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of chime |

**Corpo da requisição** (`application/json`)

- `name`: `string` - The name of the device.
- `cameraIds`: `array` - The list of (doorbell-only) cameras which this chime is paired to.
  - _array de_ `string`:
    - `string`
- `ringSettings`: `array` - List of custom ringtone settings for (doorbell-only) cameras paired to this chime.
  - _array de_ `obj`:
    - `cameraId` **(obrigatório)**: `string` - Which paired (doorbell-only) camera do these settings refer to.
    - `repeatTimes` **(obrigatório)**: `number` - How many times should the ringtone be repeated
    - `ringtoneId` **(obrigatório)**: `string` - The ID of the ringtone that should be played when the (doorbell-only) camera is rung.
    - `volume` **(obrigatório)**: `number` - How loud should the ringtone be played. 0 being silent and 100 the loudest.

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of chime
- `modelKey` **(obrigatório)**: `string` - The model key of the chime
- `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
- `name` **(obrigatório)**
  - _um de (variantes):_
    - **variante**:
      - `string`
    - **variante**:
      - `null`
- `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
- `cameraIds` **(obrigatório)**: `array` - The list of (doorbell-only) cameras which this chime is paired to.
  - _array de_ `string`:
    - `string`
- `ringSettings` **(obrigatório)**: `array` - List of custom ringtone settings for (doorbell-only) cameras paired to this chime.
  - _array de_ `object`:
    - `cameraId` **(obrigatório)**: `string` - Which paired (doorbell-only) camera do these settings refer to.
    - `repeatTimes` **(obrigatório)**: `number` - How many times should the ringtone be repeated
    - `ringtoneId` **(obrigatório)**: `string` - The ID of the ringtone that should be played when the (doorbell-only) camera is rung.
    - `volume` **(obrigatório)**: `number` - How loud should the ringtone be played. 0 being silent and 100 the loudest.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X PATCH "https://$UNIFI_HOST/proxy/protect/integration/v1/chimes/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
```bash
# Remoto (Cloud Connector)
curl -X PATCH "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/chimes/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get all chimes

`GET /v1/chimes`  ·  operationId: ``

Get detailed information about all chimes

**Resposta 200** - Success response

- _array de_ `object`:
  - `id` **(obrigatório)**: `string` - The primary key of chime
  - `modelKey` **(obrigatório)**: `string` - The model key of the chime
  - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
  - `name` **(obrigatório)**
    - _um de (variantes):_
      - **variante**:
        - `string`
      - **variante**:
        - `null`
  - `mac` **(obrigatório)**: `string` - The primary MAC address of the device.
  - `cameraIds` **(obrigatório)**: `array` - The list of (doorbell-only) cameras which this chime is paired to.
    - _array de_ `string`:
      - `string`
  - `ringSettings` **(obrigatório)**: `array` - List of custom ringtone settings for (doorbell-only) cameras paired to this chime.
    - _array de_ `object`:
      - `cameraId` **(obrigatório)**: `string` - Which paired (doorbell-only) camera do these settings refer to.
      - `repeatTimes` **(obrigatório)**: `number` - How many times should the ringtone be repeated
      - `ringtoneId` **(obrigatório)**: `string` - The ID of the ringtone that should be played when the (doorbell-only) camera is rung.
      - `volume` **(obrigatório)**: `number` - How loud should the ringtone be played. 0 being silent and 100 the loudest.

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/chimes" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/chimes" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Protect User information


### Get user details

`GET /v1/users/{id}`  ·  operationId: ``

Get detailed information about a specific Protect user.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of user |

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of user
- `name` **(obrigatório)**: `string` - The user name (first-name + last-name).
- `firstName` **(obrigatório)**: `string|null` - The user first-name.
- `lastName` **(obrigatório)**: `string|null` - The user last-name.
- `email` **(obrigatório)**: `string|null` - The user email.
- `ucoreUserId` **(obrigatório)**: `string|null` - The unique id of the UniFi Identity user. Matches the id field of the corresponding UlpUser.
- `modelKey` **(obrigatório)**: `string` - The model key of the user

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/users/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/users/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get all users

`GET /v1/users`  ·  operationId: ``

Get all Protect users. Users are filtered based on access permissions.

**Resposta 200** - Success response

- _array de_ `object`:
  - `id` **(obrigatório)**: `string` - The primary key of user
  - `name` **(obrigatório)**: `string` - The user name (first-name + last-name).
  - `firstName` **(obrigatório)**: `string|null` - The user first-name.
  - `lastName` **(obrigatório)**: `string|null` - The user last-name.
  - `email` **(obrigatório)**: `string|null` - The user email.
  - `ucoreUserId` **(obrigatório)**: `string|null` - The unique id of the UniFi Identity user. Matches the id field of the corresponding UlpUser.
  - `modelKey` **(obrigatório)**: `string` - The model key of the user

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/users" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/users" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## UniFi Identity User information


### Get identity user details

`GET /v1/ulp-users/{id}`  ·  operationId: ``

Get detailed information about a specific UniFi Identity user.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of ulpUser |

**Resposta 200** - Success response

- `id` **(obrigatório)**: `string` - The primary key of ulpUser
- `firstName` **(obrigatório)**: `string` - The first name of ulp user
- `lastName` **(obrigatório)**: `string` - The last name of ulp user
- `fullName` **(obrigatório)**: `string` - Fullname of ulp user
- `status` **(obrigatório)**: `string` enum: ACTIVE, DEACTIVATED - Active status of ulp user
- `modelKey` **(obrigatório)**: `string` - The model key of the ulpUser

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/ulp-users/{id}" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/ulp-users/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get all identity users

`GET /v1/ulp-users`  ·  operationId: ``

Get all UniFi Identity users with enrolled credentials (NFC cards, fingerprints).

**Resposta 200** - Success response

- _array de_ `object`:
  - `id` **(obrigatório)**: `string` - The primary key of ulpUser
  - `firstName` **(obrigatório)**: `string` - The first name of ulp user
  - `lastName` **(obrigatório)**: `string` - The last name of ulp user
  - `fullName` **(obrigatório)**: `string` - Fullname of ulp user
  - `status` **(obrigatório)**: `string` enum: ACTIVE, DEACTIVATED - Active status of ulp user
  - `modelKey` **(obrigatório)**: `string` - The model key of the ulpUser

**Erros possíveis:** `default`

<details><summary>Exemplo cURL</summary>

```bash
# Local
curl -X GET "https://$UNIFI_HOST/proxy/protect/integration/v1/ulp-users" \
     -H "X-API-KEY: $UNIFI_API_KEY"
```
```bash
# Remoto (Cloud Connector)
curl -X GET "https://api.ui.com/v1/connector/consoles/$CONSOLE_ID/protect/integration/v1/ulp-users" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>

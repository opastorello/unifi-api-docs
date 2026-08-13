# UniFi Protect API - v7.0.104 - Referência

> Espelho automático de [`developer.ui.com/protect/v7.0.104`](https://developer.ui.com/protect/v7.0.104).
> OpenAPI `3.1.0` · 35 operações em 25 paths · atualizado na origem em `2026-08-12T11:31:34.156Z`.

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
| NVR information & management | `GET` | `/v1/nvrs` | Get NVR details |
| Device asset file management | `GET` | `/v1/files/{fileType}` | Get device asset files |
| Device asset file management | `POST` | `/v1/files/{fileType}` | Upload device asset file |
| Chime information & management | `GET` | `/v1/chimes/{id}` | Get chime details |
| Chime information & management | `PATCH` | `/v1/chimes/{id}` | Patch chime settings |
| Chime information & management | `GET` | `/v1/chimes` | Get all chimes |


---

## Information about application


### Get application information

`GET /v1/meta/info`  ·  operationId: ``

Get generic information about the Protect application

**Resposta 200** - Success response

- `applicationVersion` **(obrigatório)**: `string` - Protect application version

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
- `mac` **(obrigatório)**: `string` - The MAC address of the device
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

- `name`: `string` - The name of the model
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
- `mac` **(obrigatório)**: `string` - The MAC address of the device
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
  - `mac` **(obrigatório)**: `string` - The MAC address of the device
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
            - `defaultMessageText`: `string`
            - `defaultMessageResetTimeoutMs`: `number`
            - `customMessages`: `array`
              - _array de_ `string`:
            - `customImages`: `array`
              - _array de_ `object`:
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
          - `mac` **(obrigatório)**: `string` - The MAC address of the device
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
            - `smartDetectAudioTypes` **(obrigatório)**: `array` - What smart detection audio types do the camera support.
              - _array de_ `string`:
            - `videoModes` **(obrigatório)**: `array` - A list of supported video modes by the camera
              - _array de_ `string`:
            - `hasMic` **(obrigatório)**: `boolean` - Whether the camera has a microphone
            - `hasLedStatus` **(obrigatório)**: `boolean` - Whether the camera has LED status
            - `hasSpeaker` **(obrigatório)**: `boolean` - Whether the camera has a speaker to support talkback
          - `smartDetectSettings` **(obrigatório)**: `object` - Smart detection settings for the camera.
            - `objectTypes` **(obrigatório)**: `array`
              - _array de_ `string`:
            - `audioTypes` **(obrigatório)**: `array`
              - _array de_ `string`:
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
          - `mac` **(obrigatório)**: `string` - The MAC address of the device
          - `cameraIds` **(obrigatório)**: `array` - The list of (doorbell-only) cameras which this chime is paired to.
            - _array de_ `string`:
              - `string`
          - `ringSettings` **(obrigatório)**: `array` - List of custom ringtone settings for (doorbell-only) cameras paired to this chime.
            - _array de_ `object`:
              - `cameraId` **(obrigatório)**: `string` - Which paired (doorbell-only) camera do these settings refer to.
              - `repeatTimes` **(obrigatório)**: `number` - How many times should the ringtone be repeated
              - `ringtoneId` **(obrigatório)**: `string` - The ID of the ringtone that should be played when the (doorbell-only) camera is rung.
              - `volume` **(obrigatório)**: `number` - How loud should the ringtone be played. 0 being silent and 100 the loudest.
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
          - `mac` **(obrigatório)**: `string` - The MAC address of the device
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
          - `mac` **(obrigatório)**: `string` - The MAC address of the device
          - `liveview` **(obrigatório)**
            - _um de (variantes):_
              - **variante**:
                - `string`
              - **variante**:
                - `null`
          - `streamLimit` **(obrigatório)**: `number` - Count of maximum supported parallel live streams.
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of device
          - `modelKey` **(obrigatório)**: `string` - The model key of the speaker
          - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
          - `name` **(obrigatório)**
            - _um de (variantes):_
              - **variante**:
                - `string`
              - **variante**:
                - `null`
          - `mac` **(obrigatório)**: `string` - The MAC address of the device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of device
          - `modelKey` **(obrigatório)**: `string` - The model key of the bridge
          - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
          - `name` **(obrigatório)**
            - _um de (variantes):_
              - **variante**:
                - `string`
              - **variante**:
                - `null`
          - `mac` **(obrigatório)**: `string` - The MAC address of the device
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
          - `mac` **(obrigatório)**: `string` - The MAC address of the device
          - `mountType` **(obrigatório)**: `string` enum: door, window, garage, leak, none - Mounting type of the sensor.
          - `batteryStatus` **(obrigatório)**: `object` - [DEPRECATED] Use wirelessConnectionState.batteryStatus instead. Battery status.
            - `percentage`: `number|null` - Battery charge level from 0 to 100 (%).
            - `isLow`: `boolean` - Low battery charge level flag.
          - `stats` **(obrigatório)**: `object` - Sensor statistics.
            - `light`: `object` - Ambient light value (Lux).
              - `value`
              - `status`: `string` enum: neutral, low, safe, high, unknown - What range does the measured metric fall into
            - `humidity`: `object` - Ambient light value (Lux).
              - `value`
              - `status`: `string` enum: neutral, low, safe, high, unknown - What range does the measured metric fall into
            - `temperature`: `object` - Ambient light value (Lux).
              - `value`
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
          - `isOpened` **(obrigatório)**: `boolean` - Whether the door/window/garage is opened.
          - `openStatusChangedAt` **(obrigatório)**: `number|null` - Unix timestamp when the door/window/garage was last opened or closed, nullable.
          - `isMotionDetected` **(obrigatório)**: `boolean` - Whether sensor is currently detecting the motion.
          - `motionDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the last motion was detected.
          - `motionSettings` **(obrigatório)**: `object` - Motion sensor settings.
            - `isEnabled`: `boolean` - Enable motion sensor.
            - `sensitivity`: `number` - Motion sensitivity (0-100).
          - `alarmTriggeredAt` **(obrigatório)**: `number|null` - Unix timestamp when the smoke or carbon monoxide alarm was triggered, nullable.
          - `alarmSettings` **(obrigatório)**: `object` - Smoke and carbon monoxide alarm sensor settings.
            - `isEnabled`: `boolean` - Enable smoke and carbon monoxide alarm sensor.
          - `leakDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected a water leak, nullable.
          - `externalLeakDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected an external water leak, nullable.
          - `leakSettings` **(obrigatório)**: `object` - Leak sensor settings.
            - `isInternalEnabled`: `boolean` - Enable internal water leak detection.
            - `isExternalEnabled`: `boolean` - Enable external water leak detection.
          - `tamperingDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected tampering, nullable.
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
          - `mac` **(obrigatório)**: `string` - The MAC address of the device
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
          - `mac` **(obrigatório)**: `string` - The MAC address of the device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of device
          - `modelKey` **(obrigatório)**: `string` - The model key of the linkstation
          - `state` **(obrigatório)**: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
          - `name` **(obrigatório)**
            - _um de (variantes):_
              - **variante**:
                - `string`
              - **variante**:
                - `null`
          - `mac` **(obrigatório)**: `string` - The MAC address of the device
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
            - `defaultMessageText`: `string`
            - `defaultMessageResetTimeoutMs`: `number`
            - `customMessages`: `array`
              - _array de_ `string`:
            - `customImages`: `array`
              - _array de_ `object`:
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
          - `mac`: `string` - The MAC address of the device
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
              - _array de_ `string`:
            - `smartDetectAudioTypes` **(obrigatório)**: `array` - What smart detection audio types do the camera support.
              - _array de_ `string`:
            - `videoModes` **(obrigatório)**: `array` - A list of supported video modes by the camera
              - _array de_ `string`:
            - `hasMic` **(obrigatório)**: `boolean` - Whether the camera has a microphone
            - `hasLedStatus` **(obrigatório)**: `boolean` - Whether the camera has LED status
            - `hasSpeaker` **(obrigatório)**: `boolean` - Whether the camera has a speaker to support talkback
          - `smartDetectSettings`: `object` - Smart detection settings for the camera.
            - `objectTypes` **(obrigatório)**: `array`
              - _array de_ `string`:
            - `audioTypes` **(obrigatório)**: `array`
              - _array de_ `string`:
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
          - `mac`: `string` - The MAC address of the device
          - `cameraIds`: `array` - The list of (doorbell-only) cameras which this chime is paired to.
            - _array de_ `string`:
              - `string`
          - `ringSettings`: `array` - List of custom ringtone settings for (doorbell-only) cameras paired to this chime.
            - _array de_ `object`:
              - `cameraId` **(obrigatório)**: `string` - Which paired (doorbell-only) camera do these settings refer to.
              - `repeatTimes` **(obrigatório)**: `number` - How many times should the ringtone be repeated
              - `ringtoneId` **(obrigatório)**: `string` - The ID of the ringtone that should be played when the (doorbell-only) camera is rung.
              - `volume` **(obrigatório)**: `number` - How loud should the ringtone be played. 0 being silent and 100 the loudest.
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
          - `mac`: `string` - The MAC address of the device
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
          - `mac`: `string` - The MAC address of the device
          - `liveview`
            - _um de (variantes):_
              - **variante**:
                - `string`
              - **variante**:
                - `null`
          - `streamLimit`: `number` - Count of maximum supported parallel live streams.
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of device
          - `modelKey` **(obrigatório)**: `string` - The model key of the speaker
          - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
          - `name`
            - _um de (variantes):_
              - **variante**:
                - `string`
              - **variante**:
                - `null`
          - `mac`: `string` - The MAC address of the device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of device
          - `modelKey` **(obrigatório)**: `string` - The model key of the bridge
          - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
          - `name`
            - _um de (variantes):_
              - **variante**:
                - `string`
              - **variante**:
                - `null`
          - `mac`: `string` - The MAC address of the device
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
          - `mac`: `string` - The MAC address of the device
          - `mountType`: `string` enum: door, window, garage, leak, none - Mounting type of the sensor.
          - `batteryStatus`: `object` - [DEPRECATED] Use wirelessConnectionState.batteryStatus instead. Battery status.
            - `percentage`: `number|null` - Battery charge level from 0 to 100 (%).
            - `isLow`: `boolean` - Low battery charge level flag.
          - `stats`: `object` - Sensor statistics.
            - `light`: `object` - Ambient light value (Lux).
              - `value`
              - `status`: `string` enum: neutral, low, safe, high, unknown - What range does the measured metric fall into
            - `humidity`: `object` - Ambient light value (Lux).
              - `value`
              - `status`: `string` enum: neutral, low, safe, high, unknown - What range does the measured metric fall into
            - `temperature`: `object` - Ambient light value (Lux).
              - `value`
              - `status`: `string` enum: neutral, low, safe, high, unknown - What range does the measured metric fall into
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
          - `isOpened`: `boolean` - Whether the door/window/garage is opened.
          - `openStatusChangedAt`: `number|null` - Unix timestamp when the door/window/garage was last opened or closed, nullable.
          - `isMotionDetected`: `boolean` - Whether sensor is currently detecting the motion.
          - `motionDetectedAt`: `number|null` - Unix timestamp when the last motion was detected.
          - `motionSettings`: `object` - Motion sensor settings.
            - `isEnabled`: `boolean` - Enable motion sensor.
            - `sensitivity`: `number` - Motion sensitivity (0-100).
          - `alarmTriggeredAt`: `number|null` - Unix timestamp when the smoke or carbon monoxide alarm was triggered, nullable.
          - `alarmSettings`: `object` - Smoke and carbon monoxide alarm sensor settings.
            - `isEnabled`: `boolean` - Enable smoke and carbon monoxide alarm sensor.
          - `leakDetectedAt`: `number|null` - Unix timestamp when the sensor detected a water leak, nullable.
          - `externalLeakDetectedAt`: `number|null` - Unix timestamp when the sensor detected an external water leak, nullable.
          - `leakSettings`: `object` - Leak sensor settings.
            - `isInternalEnabled`: `boolean` - Enable internal water leak detection.
            - `isExternalEnabled`: `boolean` - Enable external water leak detection.
          - `tamperingDetectedAt`: `number|null` - Unix timestamp when the sensor detected tampering, nullable.
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
          - `mac`: `string` - The MAC address of the device
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
          - `mac`: `string` - The MAC address of the device
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of device
          - `modelKey` **(obrigatório)**: `string` - The model key of the linkstation
          - `state`: `string` enum: CONNECTED, CONNECTING, DISCONNECTED - Connection state of the device.
          - `name`
            - _um de (variantes):_
              - **variante**:
                - `string`
              - **variante**:
                - `null`
          - `mac`: `string` - The MAC address of the device
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
          - `id` **(obrigatório)**: `string` - The primary key of device
          - `modelKey` **(obrigatório)**: `string` - The model key of the speaker
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of device
          - `modelKey` **(obrigatório)**: `string` - The model key of the bridge
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of sensor
          - `modelKey` **(obrigatório)**: `string` - The model key of the sensor
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of device
          - `modelKey` **(obrigatório)**: `string` - The model key of the aiprocessor
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of device
          - `modelKey` **(obrigatório)**: `string` - The model key of the aiport
        - **variante**:
          - `id` **(obrigatório)**: `string` - The primary key of device
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
              - `text` **(obrigatório)**: `string` enum: temperature, light, humidity, aqi, vape, tvoc, pm1p0, pm2p5, pm4p0, pm10p0, nox, co2
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
              - `text` **(obrigatório)**: `string` enum: temperature, light, humidity, aqi, vape, tvoc, pm1p0, pm2p5, pm4p0, pm10p0, nox, co2
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
| `slot` | path | sim | string | The slot number (0-4) of the preset to move the camera to |

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
- `mac` **(obrigatório)**: `string` - The MAC address of the device
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

- `name`: `string` - The name of the model
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
- `mac` **(obrigatório)**: `string` - The MAC address of the device
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
  - `mac` **(obrigatório)**: `string` - The MAC address of the device
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
- `mac` **(obrigatório)**: `string` - The MAC address of the device
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

- `name`: `string` - The name of the camera
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
- `mac` **(obrigatório)**: `string` - The MAC address of the device
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
  - `mac` **(obrigatório)**: `string` - The MAC address of the device
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

- `qualities` **(obrigatório)**: `array` - Array of quality levels of RTSPS streams
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
| `qualities` | query | sim |  | The array of quality levels for the RTSPS streams to be removed. |

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

Get a snapshot image from a specific camera

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `id` | path | sim | string | The primary key of camera |
| `highQuality` | query | não | string enum | Whether to force 1080P or higher resolution snapshot (default false) |

**Resposta 200** - Camera snapshot

**Erros possíveis:** `default`

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
- `mac` **(obrigatório)**: `string` - The MAC address of the device
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
- `mac` **(obrigatório)**: `string` - The MAC address of the device
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
- `isOpened` **(obrigatório)**: `boolean` - Whether the door/window/garage is opened.
- `openStatusChangedAt` **(obrigatório)**: `number|null` - Unix timestamp when the door/window/garage was last opened or closed, nullable.
- `isMotionDetected` **(obrigatório)**: `boolean` - Whether sensor is currently detecting the motion.
- `motionDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the last motion was detected.
- `motionSettings` **(obrigatório)**: `object` - Motion sensor settings.
  - `isEnabled`: `boolean` - Enable motion sensor.
  - `sensitivity`: `number` - Motion sensitivity (0-100).
- `alarmTriggeredAt` **(obrigatório)**: `number|null` - Unix timestamp when the smoke or carbon monoxide alarm was triggered, nullable.
- `alarmSettings` **(obrigatório)**: `object` - Smoke and carbon monoxide alarm sensor settings.
  - `isEnabled`: `boolean` - Enable smoke and carbon monoxide alarm sensor.
- `leakDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected a water leak, nullable.
- `externalLeakDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected an external water leak, nullable.
- `leakSettings` **(obrigatório)**: `object` - Leak sensor settings.
  - `isInternalEnabled`: `boolean` - Enable internal water leak detection.
  - `isExternalEnabled`: `boolean` - Enable external water leak detection.
- `tamperingDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected tampering, nullable.

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

- `name`: `string` - The name of the model
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
  - `sensitivity`: `number` - Motion sensitivity (0-100).
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
- `mac` **(obrigatório)**: `string` - The MAC address of the device
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
- `isOpened` **(obrigatório)**: `boolean` - Whether the door/window/garage is opened.
- `openStatusChangedAt` **(obrigatório)**: `number|null` - Unix timestamp when the door/window/garage was last opened or closed, nullable.
- `isMotionDetected` **(obrigatório)**: `boolean` - Whether sensor is currently detecting the motion.
- `motionDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the last motion was detected.
- `motionSettings` **(obrigatório)**: `object` - Motion sensor settings.
  - `isEnabled`: `boolean` - Enable motion sensor.
  - `sensitivity`: `number` - Motion sensitivity (0-100).
- `alarmTriggeredAt` **(obrigatório)**: `number|null` - Unix timestamp when the smoke or carbon monoxide alarm was triggered, nullable.
- `alarmSettings` **(obrigatório)**: `object` - Smoke and carbon monoxide alarm sensor settings.
  - `isEnabled`: `boolean` - Enable smoke and carbon monoxide alarm sensor.
- `leakDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected a water leak, nullable.
- `externalLeakDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected an external water leak, nullable.
- `leakSettings` **(obrigatório)**: `object` - Leak sensor settings.
  - `isInternalEnabled`: `boolean` - Enable internal water leak detection.
  - `isExternalEnabled`: `boolean` - Enable external water leak detection.
- `tamperingDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected tampering, nullable.

**Erros possíveis:** `default`

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
  - `mac` **(obrigatório)**: `string` - The MAC address of the device
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
  - `isOpened` **(obrigatório)**: `boolean` - Whether the door/window/garage is opened.
  - `openStatusChangedAt` **(obrigatório)**: `number|null` - Unix timestamp when the door/window/garage was last opened or closed, nullable.
  - `isMotionDetected` **(obrigatório)**: `boolean` - Whether sensor is currently detecting the motion.
  - `motionDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the last motion was detected.
  - `motionSettings` **(obrigatório)**: `object` - Motion sensor settings.
    - `isEnabled`: `boolean` - Enable motion sensor.
    - `sensitivity`: `number` - Motion sensitivity (0-100).
  - `alarmTriggeredAt` **(obrigatório)**: `number|null` - Unix timestamp when the smoke or carbon monoxide alarm was triggered, nullable.
  - `alarmSettings` **(obrigatório)**: `object` - Smoke and carbon monoxide alarm sensor settings.
    - `isEnabled`: `boolean` - Enable smoke and carbon monoxide alarm sensor.
  - `leakDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected a water leak, nullable.
  - `externalLeakDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected an external water leak, nullable.
  - `leakSettings` **(obrigatório)**: `object` - Leak sensor settings.
    - `isInternalEnabled`: `boolean` - Enable internal water leak detection.
    - `isExternalEnabled`: `boolean` - Enable external water leak detection.
  - `tamperingDetectedAt` **(obrigatório)**: `number|null` - Unix timestamp when the sensor detected tampering, nullable.

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
  - `defaultMessageText`: `string`
  - `defaultMessageResetTimeoutMs`: `number`
  - `customMessages`: `array`
    - _array de_ `string`:
      - `string`
  - `customImages`: `array`
    - _array de_ `object`:
      - `preview` **(obrigatório)**: `string`
      - `sprite` **(obrigatório)**: `string`

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
- `mac` **(obrigatório)**: `string` - The MAC address of the device
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

- `name`: `string` - The name of the chime
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
- `mac` **(obrigatório)**: `string` - The MAC address of the device
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
  - `mac` **(obrigatório)**: `string` - The MAC address of the device
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

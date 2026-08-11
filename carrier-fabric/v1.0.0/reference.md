# UniFi Carrier / ISP Fabric - Subscriber API - v1.0.0 - Referência

> Espelho automático de [`developer.ui.com/carrier-fabric/v1.0.0`](https://developer.ui.com/carrier-fabric/v1.0.0).
> OpenAPI `3.0.3` · 11 operações em 8 paths · atualizado na origem em `2026-08-06T02:10:23.136Z`.
> Autenticação: header `X-API-Key`.

**OpenAPI completo (fonte da verdade):** [`openapi.json`](./openapi.json)

## Índice de endpoints

| Categoria | Método | Path | Operação |
|---|---|---|---|
| Subscribers | `GET` | `/v1/carrier/subscribers` | List subscribers |
| Subscribers | `POST` | `/v1/carrier/subscribers` | Create a subscriber |
| Subscribers | `GET` | `/v1/carrier/subscribers/{id}` | Get a subscriber |
| Subscribers | `PATCH` | `/v1/carrier/subscribers/{id}` | Update a subscriber |
| Subscribers | `PUT` | `/v1/carrier/subscribers/{id}/host` | Attach or re-link the gateway host |
| Subscribers | `DELETE` | `/v1/carrier/subscribers/{id}/host` | Detach the gateway host |
| Subscribers | `PUT` | `/v1/carrier/subscribers/{id}/plan` | Assign a service plan |
| Service State | `POST` | `/v1/carrier/subscribers/{id}/suspend` | Suspend service |
| Service State | `POST` | `/v1/carrier/subscribers/{id}/resume` | Resume service |
| Service Plans | `GET` | `/v1/carrier/service-plans` | List service plans |
| Service Plans | `GET` | `/v1/carrier/service-plans/{id}` | Get a service plan |


---

## Subscribers

Create, read, update subscribers; attach the gateway host; assign a service plan.


### List subscribers

`GET https://api.ui.com/v1/carrier/subscribers`  ·  operationId: `listSubscribers`

Lists subscribers visible to the key (in-scope subscribers only). Cursor-paginated. Requires scope `read:subscribers`.

**Parâmetros**

| Parâmetro | Em | Obrig. | Tipo | Descrição |
|---|---|---|---|---|
| `limit` | query | não | integer | Page size - how many subscribers to return per page. Alias: pageSize. Must be an integer from 1 to 500. Anything else is rejected with 400 validation_failed naming whichever of the two spellings you sent and the bound it broke: a non-numeric value (abc, 1.5), a value below 1 (0, -1), or a value above 500. Nothing is silently rounded or clamped - if you ask for 1000 you get an error stating the maximum is 500, not a page of 500. Omit the parameter for the default of 50. (default 50) |
| `cursor` | query | não | string | Opaque keyset cursor from a prior response's meta.nextCursor. Alias: nextToken. A cursor is only valid for the same sort it was issued for. |
| `sort` | query | não | string enum | Sort field, optionally prefixed with "-" for descending. When omitted, results are newest-first. |
| `planId` | query | não | string (uuid) | Filter by assigned service plan. Must be a valid UUID - a malformed value is rejected with 400 validation_failed rather than silently matching nothing. A well-formed id that matches no plan returns 200 with an empty list. |
| `suspended` | query | não | boolean | Filter by suspension state. |

**Resposta 200** - OK

- `data`: `array`
  - _array de_ `object`:
    - `id`: `string` (uuid)
    - `orgId`: `string` (uuid)
    - `subscriberNumber`: `string` nullable ex: `SUB-10012` - The operator-supplied external reference.
    - `name`: `string` nullable
    - `email`: `string` nullable
    - `notes`: `string` nullable
    - `serviceAddress`: `string` - Omitted from the response entirely when not set (never returned as JSON null).
    - `planId`: `string` (uuid) nullable
    - `hostId`: `string` nullable
    - `state`: `string` enum: pending_assignment, provisioned, installed, suspended
    - `suspended`: `boolean`
    - `suspendReason`: `string` - Present only while suspended; omitted (not null) otherwise.
    - `suspendedAt`: `string` (date-time) - Omitted (not null) when the subscriber has never been suspended.
    - `metadata`: `object` - Omitted (not null) when no metadata is set.
    - `activatedAt`: `string` (date-time) - Omitted (not null) until the subscriber's first host attach.
    - `createdAt`: `string` (date-time)
    - `updatedAt`: `string` (date-time)
- `meta`: `object`
  - `nextCursor`: `string` nullable
  - `limit`: `integer`
  - `hasMore`: `boolean`
- `traceId`: `string`

**Erros possíveis:** `400`, `401`, `403`, `429`, `500`, `503`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X GET "https://api.ui.com/v1/carrier/subscribers" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Create a subscriber

`POST https://api.ui.com/v1/carrier/subscribers`  ·  operationId: `createSubscriber`

Creates a subscriber (identity, optional service address, and optionally a plan; attach a gateway host separately). Always returns `201` - there is no external-reference deduplication. `subscriberNumber` is the only required field. Requires scope `create:subscribers`.

**Corpo da requisição** (`application/json`)

- `subscriberNumber` **(obrigatório)**: `string` - The operator-supplied external reference. Required; 1-32 characters.
- `name`: `string` - Optional display name for the subscriber (e.g. the customer or account name shown in your CRM). The 128 limit is bytes of UTF-8, so multi-byte characters eac…
- `email`: `string` (email) - The 255 limit is bytes of UTF-8.
- `notes`: `string` - The 4096 limit is bytes of UTF-8, so multi-byte characters each count as more than one.
- `serviceAddress`: `string` nullable - Free-text service address. The 1024 limit is bytes of UTF-8, so multi-byte characters each count as more than one.
- `planId`: `string` (uuid) - Optionally assign a plan at create time.
- `metadata`: `object` - Free-form key/value metadata. The serialized JSON object must not exceed 8192 bytes (8 KiB); a larger object is rejected with 400.

**Resposta 201** - Created

- `data`: `object`
  - `id`: `string` (uuid)
  - `orgId`: `string` (uuid)
  - `subscriberNumber`: `string` nullable ex: `SUB-10012` - The operator-supplied external reference.
  - `name`: `string` nullable
  - `email`: `string` nullable
  - `notes`: `string` nullable
  - `serviceAddress`: `string` - Omitted from the response entirely when not set (never returned as JSON null).
  - `planId`: `string` (uuid) nullable
  - `hostId`: `string` nullable
  - `state`: `string` enum: pending_assignment, provisioned, installed, suspended
  - `suspended`: `boolean`
  - `suspendReason`: `string` - Present only while suspended; omitted (not null) otherwise.
  - `suspendedAt`: `string` (date-time) - Omitted (not null) when the subscriber has never been suspended.
  - `metadata`: `object` - Omitted (not null) when no metadata is set.
  - `activatedAt`: `string` (date-time) - Omitted (not null) until the subscriber's first host attach.
  - `createdAt`: `string` (date-time)
  - `updatedAt`: `string` (date-time)
- `traceId`: `string`

**Erros possíveis:** `400`, `401`, `403`, `404`, `429`, `500`, `503`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X POST "https://api.ui.com/v1/carrier/subscribers" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Get a subscriber

`GET https://api.ui.com/v1/carrier/subscribers/{id}`  ·  operationId: `getSubscriber`

Requires scope `read:subscribers`. Returns 404 for an unknown or out-of-scope subscriber, or 400 if `id` is not a valid UUID.

**Resposta 200** - OK

- `data`: `object`
  - `id`: `string` (uuid)
  - `orgId`: `string` (uuid)
  - `subscriberNumber`: `string` nullable ex: `SUB-10012` - The operator-supplied external reference.
  - `name`: `string` nullable
  - `email`: `string` nullable
  - `notes`: `string` nullable
  - `serviceAddress`: `string` - Omitted from the response entirely when not set (never returned as JSON null).
  - `planId`: `string` (uuid) nullable
  - `hostId`: `string` nullable
  - `state`: `string` enum: pending_assignment, provisioned, installed, suspended
  - `suspended`: `boolean`
  - `suspendReason`: `string` - Present only while suspended; omitted (not null) otherwise.
  - `suspendedAt`: `string` (date-time) - Omitted (not null) when the subscriber has never been suspended.
  - `metadata`: `object` - Omitted (not null) when no metadata is set.
  - `activatedAt`: `string` (date-time) - Omitted (not null) until the subscriber's first host attach.
  - `createdAt`: `string` (date-time)
  - `updatedAt`: `string` (date-time)
- `traceId`: `string`

**Erros possíveis:** `400`, `401`, `403`, `404`, `429`, `500`, `503`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X GET "https://api.ui.com/v1/carrier/subscribers/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Update a subscriber

`PATCH https://api.ui.com/v1/carrier/subscribers/{id}`  ·  operationId: `updateSubscriber`

Updates name / email / notes / service address / plan / subscriber number / metadata. An absent field is left unchanged; a JSON `null` clears `email`, `notes`, or `planId` (the nullable-clearable fields). Requires scope `update:subscribers`.

**Corpo da requisição** (`application/json`)

- `subscriberNumber`: `string` - The operator-supplied external reference. Absent leaves it unchanged. It cannot be cleared: JSON null, an empty string, or whitespace only is rejected with 4…
- `name`: `string` nullable - Optional display name. Absent leaves it unchanged; JSON null clears it; a value must be non-empty after trimming. The 128 limit is bytes of UTF-8, so multi-b…
- `email`: `string` (email) nullable - Absent leaves it unchanged; JSON null clears it. The 255 limit is bytes of UTF-8.
- `notes`: `string` nullable - Absent leaves it unchanged; JSON null clears it. The 4096 limit is bytes of UTF-8, so multi-byte characters each count as more than one.
- `serviceAddress`: `string` nullable - Free-text service address. Absent leaves it unchanged; JSON null clears it; a value replaces it verbatim. The 1024 limit is bytes of UTF-8, so multi-byte cha…
- `planId`: `string` (uuid) nullable - Absent leaves the assigned plan unchanged; JSON null clears it.
- `metadata`: `object` - Free-form key/value metadata. A supplied object REPLACES the whole document. Absent leaves it unchanged, and so does JSON null - send an empty object to empt…

**Resposta 200** - OK

- `data`: `object`
  - `id`: `string` (uuid)
  - `orgId`: `string` (uuid)
  - `subscriberNumber`: `string` nullable ex: `SUB-10012` - The operator-supplied external reference.
  - `name`: `string` nullable
  - `email`: `string` nullable
  - `notes`: `string` nullable
  - `serviceAddress`: `string` - Omitted from the response entirely when not set (never returned as JSON null).
  - `planId`: `string` (uuid) nullable
  - `hostId`: `string` nullable
  - `state`: `string` enum: pending_assignment, provisioned, installed, suspended
  - `suspended`: `boolean`
  - `suspendReason`: `string` - Present only while suspended; omitted (not null) otherwise.
  - `suspendedAt`: `string` (date-time) - Omitted (not null) when the subscriber has never been suspended.
  - `metadata`: `object` - Omitted (not null) when no metadata is set.
  - `activatedAt`: `string` (date-time) - Omitted (not null) until the subscriber's first host attach.
  - `createdAt`: `string` (date-time)
  - `updatedAt`: `string` (date-time)
- `traceId`: `string`

**Erros possíveis:** `400`, `401`, `403`, `404`, `429`, `500`, `503`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X PATCH "https://api.ui.com/v1/carrier/subscribers/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Attach or re-link the gateway host

`PUT https://api.ui.com/v1/carrier/subscribers/{id}/host`  ·  operationId: `attachSubscriberHost`

Attaches (or re-links) the subscriber's gateway host. A subscriber has at most one host; supplying a DIFFERENT host replaces the current one in place (RMA re-link).

**Not idempotent.** Re-sending the host this subscriber is already linked to is rejected with `409 gateway_already_attached` - nothing is written. A host linked to a *different* subscriber in the organization is `409 gateway_already_linked`. Read `GET /subscribers/{id}` (field `hostId`) if you need to know the current link before calling; `prevHostId` on a successful response is the host that was replaced (`null` on a fresh attach).

Because a repeat is an error rather than a no-op, do NOT blindly retry a request that timed out - re-read the subscriber first, or treat `409 gateway_already_attached` as "already applied".

Requires scope `update:subscribers`.

**Corpo da requisição** (`application/json`)

- `hostId` **(obrigatório)**: `string` - Gateway host identifier.

**Resposta 200** - OK

- `data`: `object`
  - `id`: `string` (uuid)
  - `orgId`: `string` (uuid)
  - `subscriberNumber`: `string` nullable ex: `SUB-10012` - The operator-supplied external reference.
  - `name`: `string` nullable
  - `email`: `string` nullable
  - `notes`: `string` nullable
  - `serviceAddress`: `string` - Omitted from the response entirely when not set (never returned as JSON null).
  - `planId`: `string` (uuid) nullable
  - `hostId`: `string` nullable
  - `state`: `string` enum: pending_assignment, provisioned, installed, suspended
  - `suspended`: `boolean`
  - `suspendReason`: `string` - Present only while suspended; omitted (not null) otherwise.
  - `suspendedAt`: `string` (date-time) - Omitted (not null) when the subscriber has never been suspended.
  - `metadata`: `object` - Omitted (not null) when no metadata is set.
  - `activatedAt`: `string` (date-time) - Omitted (not null) until the subscriber's first host attach.
  - `createdAt`: `string` (date-time)
  - `updatedAt`: `string` (date-time)
- `prevHostId`: `string` nullable
- `traceId`: `string`

**Erros possíveis:** `400`, `401`, `403`, `404`, `409`, `429`, `500`, `503`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X PUT "https://api.ui.com/v1/carrier/subscribers/{id}/host" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Detach the gateway host

`DELETE https://api.ui.com/v1/carrier/subscribers/{id}/host`  ·  operationId: `detachSubscriberHost`

Detaches the subscriber's gateway host.

**Not idempotent.** A subscriber with no linked host is rejected with `409 no_attached_host` - nothing is written. On success `prevHostId` is the host that was removed.

Because a repeat is an error rather than a no-op, do NOT blindly retry a request that timed out - re-read the subscriber first (`GET /subscribers/{id}`, field `hostId`), or treat `409 no_attached_host` as "already applied".

Requires scope `update:subscribers`.

**Resposta 200** - OK

- `data`: `object`
  - `id`: `string` (uuid)
  - `orgId`: `string` (uuid)
  - `subscriberNumber`: `string` nullable ex: `SUB-10012` - The operator-supplied external reference.
  - `name`: `string` nullable
  - `email`: `string` nullable
  - `notes`: `string` nullable
  - `serviceAddress`: `string` - Omitted from the response entirely when not set (never returned as JSON null).
  - `planId`: `string` (uuid) nullable
  - `hostId`: `string` nullable
  - `state`: `string` enum: pending_assignment, provisioned, installed, suspended
  - `suspended`: `boolean`
  - `suspendReason`: `string` - Present only while suspended; omitted (not null) otherwise.
  - `suspendedAt`: `string` (date-time) - Omitted (not null) when the subscriber has never been suspended.
  - `metadata`: `object` - Omitted (not null) when no metadata is set.
  - `activatedAt`: `string` (date-time) - Omitted (not null) until the subscriber's first host attach.
  - `createdAt`: `string` (date-time)
  - `updatedAt`: `string` (date-time)
- `prevHostId`: `string` nullable
- `traceId`: `string`

**Erros possíveis:** `400`, `401`, `403`, `404`, `409`, `429`, `500`, `503`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X DELETE "https://api.ui.com/v1/carrier/subscribers/{id}/host" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Assign a service plan

`PUT https://api.ui.com/v1/carrier/subscribers/{id}/plan`  ·  operationId: `assignSubscriberPlan`

Assigns the subscriber's service plan. Assigning an archived plan returns `400 service_plan_archived`; an unknown plan returns `404 service_plan_not_found`. Requires scope `assign:plans`.

**Corpo da requisição** (`application/json`)

- `planId` **(obrigatório)**: `string` (uuid)

**Resposta 200** - OK

- `data`: `object`
  - `id`: `string` (uuid)
  - `orgId`: `string` (uuid)
  - `subscriberNumber`: `string` nullable ex: `SUB-10012` - The operator-supplied external reference.
  - `name`: `string` nullable
  - `email`: `string` nullable
  - `notes`: `string` nullable
  - `serviceAddress`: `string` - Omitted from the response entirely when not set (never returned as JSON null).
  - `planId`: `string` (uuid) nullable
  - `hostId`: `string` nullable
  - `state`: `string` enum: pending_assignment, provisioned, installed, suspended
  - `suspended`: `boolean`
  - `suspendReason`: `string` - Present only while suspended; omitted (not null) otherwise.
  - `suspendedAt`: `string` (date-time) - Omitted (not null) when the subscriber has never been suspended.
  - `metadata`: `object` - Omitted (not null) when no metadata is set.
  - `activatedAt`: `string` (date-time) - Omitted (not null) until the subscriber's first host attach.
  - `createdAt`: `string` (date-time)
  - `updatedAt`: `string` (date-time)
- `traceId`: `string`

**Erros possíveis:** `400`, `401`, `403`, `404`, `429`, `500`, `503`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X PUT "https://api.ui.com/v1/carrier/subscribers/{id}/plan" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


---

## Service State

Suspend and resume a subscriber's service (subscriber-level, idempotent).


### Suspend service

`POST https://api.ui.com/v1/carrier/subscribers/{id}/suspend`  ·  operationId: `suspendSubscriber`

Suspends the subscriber's service (subscriber-level). Idempotent: suspending an already-suspended subscriber is a 200 no-op. Requires scope `suspend:service`.

**Corpo da requisição** (`application/json`)

- `reason`: `string`

**Resposta 200** - OK

- `data`: `object`
  - `id`: `string` (uuid)
  - `orgId`: `string` (uuid)
  - `subscriberNumber`: `string` nullable ex: `SUB-10012` - The operator-supplied external reference.
  - `name`: `string` nullable
  - `email`: `string` nullable
  - `notes`: `string` nullable
  - `serviceAddress`: `string` - Omitted from the response entirely when not set (never returned as JSON null).
  - `planId`: `string` (uuid) nullable
  - `hostId`: `string` nullable
  - `state`: `string` enum: pending_assignment, provisioned, installed, suspended
  - `suspended`: `boolean`
  - `suspendReason`: `string` - Present only while suspended; omitted (not null) otherwise.
  - `suspendedAt`: `string` (date-time) - Omitted (not null) when the subscriber has never been suspended.
  - `metadata`: `object` - Omitted (not null) when no metadata is set.
  - `activatedAt`: `string` (date-time) - Omitted (not null) until the subscriber's first host attach.
  - `createdAt`: `string` (date-time)
  - `updatedAt`: `string` (date-time)
- `traceId`: `string`

**Erros possíveis:** `400`, `401`, `403`, `404`, `429`, `500`, `503`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X POST "https://api.ui.com/v1/carrier/subscribers/{id}/suspend" \
     -H "X-API-Key: $UNIFI_SM_KEY" \
     -H "Content-Type: application/json" -d '{ ... }'
```
</details>


### Resume service

`POST https://api.ui.com/v1/carrier/subscribers/{id}/resume`  ·  operationId: `resumeSubscriber`

Resumes the subscriber's service. Idempotent: resuming a not-suspended subscriber is a 200 no-op. Requires scope `resume:service`. Returns 400 if `id` is not a valid UUID.

**Resposta 200** - OK

- `data`: `object`
  - `id`: `string` (uuid)
  - `orgId`: `string` (uuid)
  - `subscriberNumber`: `string` nullable ex: `SUB-10012` - The operator-supplied external reference.
  - `name`: `string` nullable
  - `email`: `string` nullable
  - `notes`: `string` nullable
  - `serviceAddress`: `string` - Omitted from the response entirely when not set (never returned as JSON null).
  - `planId`: `string` (uuid) nullable
  - `hostId`: `string` nullable
  - `state`: `string` enum: pending_assignment, provisioned, installed, suspended
  - `suspended`: `boolean`
  - `suspendReason`: `string` - Present only while suspended; omitted (not null) otherwise.
  - `suspendedAt`: `string` (date-time) - Omitted (not null) when the subscriber has never been suspended.
  - `metadata`: `object` - Omitted (not null) when no metadata is set.
  - `activatedAt`: `string` (date-time) - Omitted (not null) until the subscriber's first host attach.
  - `createdAt`: `string` (date-time)
  - `updatedAt`: `string` (date-time)
- `traceId`: `string`

**Erros possíveis:** `400`, `401`, `403`, `404`, `429`, `500`, `503`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X POST "https://api.ui.com/v1/carrier/subscribers/{id}/resume" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


---

## Service Plans

Read the org's service plans. Plans are authored in the console; there is no external write endpoint.


### List service plans

`GET https://api.ui.com/v1/carrier/service-plans`  ·  operationId: `listServicePlans`

Lists the org's service plans (read-only). Requires scope `read:plans`.

**Resposta 200** - OK

- `data`: `array`
  - _array de_ `object`:
    - `id`: `string` (uuid)
    - `orgId`: `string` (uuid)
    - `name`: `string`
    - `status`: `string` enum: active, archived
    - `downloadMbps`: `number` nullable
    - `uploadMbps`: `number` nullable
    - `metadata`: `object` - Omitted (not null) when no metadata is set.
    - `createdAt`: `string` (date-time)
    - `updatedAt`: `string` (date-time)
    - `archivedAt`: `string` (date-time) - Present when the plan is archived; omitted (not null) while active.
- `traceId`: `string`

**Erros possíveis:** `400`, `401`, `403`, `429`, `500`, `503`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X GET "https://api.ui.com/v1/carrier/service-plans" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>


### Get a service plan

`GET https://api.ui.com/v1/carrier/service-plans/{id}`  ·  operationId: `getServicePlan`

Requires scope `read:plans`. Returns 400 if `id` is not a valid UUID.

**Resposta 200** - OK

- `data`: `object`
  - `id`: `string` (uuid)
  - `orgId`: `string` (uuid)
  - `name`: `string`
  - `status`: `string` enum: active, archived
  - `downloadMbps`: `number` nullable
  - `uploadMbps`: `number` nullable
  - `metadata`: `object` - Omitted (not null) when no metadata is set.
  - `createdAt`: `string` (date-time)
  - `updatedAt`: `string` (date-time)
  - `archivedAt`: `string` (date-time) - Present when the plan is archived; omitted (not null) while active.
- `traceId`: `string`

**Erros possíveis:** `400`, `401`, `403`, `404`, `429`, `500`, `503`

<details><summary>Exemplo cURL</summary>

```bash
# Cloud
curl -X GET "https://api.ui.com/v1/carrier/service-plans/{id}" \
     -H "X-API-Key: $UNIFI_SM_KEY"
```
</details>

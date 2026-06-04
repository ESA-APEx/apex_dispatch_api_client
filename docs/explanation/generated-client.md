# Generated Client Architecture

The APEx Dispatch API client is generated from `schemas/openapi.json`. The
generated code follows a predictable structure so that integrations can stay
close to the OpenAPI contract.

## Package Layers

The package has four main layers:

- `client.py` stores HTTP configuration and creates cached `httpx` clients.
- `api/` contains one module per OpenAPI operation.
- `models/` contains request, response, enum, and schema classes.
- `types.py` contains shared helpers such as `Response`, `File`, and `UNSET`.

## Why Operations Are Modules

Operation names are long because they encode the OpenAPI operation and path.
For example:

```python
from apex_dispatch_api_client.api.unit_jobs import create_unit_job_unit_jobs_post
```

That module corresponds to:

```text
POST /unit_jobs
```

The naming is mechanical, but it keeps generated modules stable and traceable
to the schema.

## Parsed and Detailed Helpers

Each operation module separates "give me the useful object" from "give me the
HTTP response details":

- `sync` and `asyncio` return only the parsed response body.
- `sync_detailed` and `asyncio_detailed` return `Response`.

This keeps simple application code short while still allowing integrations to
inspect status codes, headers, and raw content when needed.

## Sync and Async Share Configuration

`Client` and `AuthenticatedClient` can create both a cached `httpx.Client` and
a cached `httpx.AsyncClient`. The same base URL, headers, cookies, SSL,
timeout, redirect, and `httpx_args` configuration is used for both.

Use a sync context manager for sync calls:

```python
with client:
    ...
```

Use an async context manager for async calls:

```python
async with client:
    ...
```

## Regeneration

The default `Taskfile.yaml` task downloads the OpenAPI schema, writes the
package version from the schema version, and regenerates the client into
`src/apex_dispatch_api_client`.

Generated files should be treated as schema-derived code. Prefer changes to
the schema or generator inputs when you need API-surface changes.

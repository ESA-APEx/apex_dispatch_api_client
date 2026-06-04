# Handle Errors

Generated endpoint modules parse documented error responses into typed error
models. Undocumented status codes return `None` by default or raise
`UnexpectedStatus` when configured.

## Parse Documented API Errors

```python
from apex_dispatch_api_client.api.unit_jobs import get_job_unit_jobs_job_id_get
from apex_dispatch_api_client.models.error_response import ErrorResponse

parsed = get_job_unit_jobs_job_id_get.sync(404, client=client)

if isinstance(parsed, ErrorResponse):
    print(parsed.error_code)
    print(parsed.message)
    print(parsed.request_id)
```

Common documented error models include:

- `ErrorResponse`
- `HTTPValidationError`

## Raise on Undocumented Status Codes

```python
from apex_dispatch_api_client import errors
from apex_dispatch_api_client.client import Client
from apex_dispatch_api_client.api.default import health_health_get

client = Client(
    base_url="https://dispatch-api.dev.apex.esa.int",
    raise_on_unexpected_status=True,
)

try:
    response = health_health_get.sync_detailed(client=client)
except errors.UnexpectedStatus as exc:
    print(exc.status_code)
    print(exc.content)
```

Use this mode when an unexpected server response should fail fast.

## Handle Timeouts

Endpoint helpers use `httpx` underneath and can raise
`httpx.TimeoutException`:

```python
import httpx

client = client.with_timeout(httpx.Timeout(10.0))
```

Catch `httpx.TimeoutException` around calls that depend on remote API
latency.

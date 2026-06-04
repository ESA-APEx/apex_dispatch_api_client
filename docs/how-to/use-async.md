# Use Async Calls

Every endpoint that supports synchronous calls also exposes asynchronous
helpers.

## Create an Async Client

```python
from apex_dispatch_api_client.client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://dispatch-api.dev.apex.esa.int",
    token="YOUR_ACCESS_TOKEN",
)
```

The same `AuthenticatedClient` object creates an `httpx.AsyncClient` when an
async operation needs it.

## Call an Async Endpoint

```python
import asyncio

from apex_dispatch_api_client.client import AuthenticatedClient
from apex_dispatch_api_client.api.upscale_tasks import (
    get_jobs_status_jobs_status_get,
)


async def main() -> None:
    async with AuthenticatedClient(
        base_url="https://dispatch-api.dev.apex.esa.int",
        token="YOUR_ACCESS_TOKEN",
    ) as client:
        status = await get_jobs_status_jobs_status_get.asyncio(client=client)
        print(status)


asyncio.run(main())
```

## Get Async HTTP Details

Use the detailed async helper when you need status code, headers, and raw
content:

```python
response = await get_jobs_status_jobs_status_get.asyncio_detailed(client=client)

print(response.status_code)
print(response.parsed)
```

The async detailed helper returns the same `Response` wrapper as the sync
detailed helper.

# Configure Clients

Use `Client` for public endpoints and `AuthenticatedClient` for secured
endpoints.

## Use a Public Client

```python
from apex_dispatch_api_client.client import Client

client = Client(base_url="https://dispatch-api.dev.apex.esa.int")
```

Public clients are suitable for endpoints such as `/health`.

## Use a Bearer Token

```python
from apex_dispatch_api_client.client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://dispatch-api.dev.apex.esa.int",
    token="YOUR_ACCESS_TOKEN",
)
```

`AuthenticatedClient` adds this header by default:

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Use a Custom Authentication Header

Set `prefix=""` when the header value must be the raw token:

```python
client = AuthenticatedClient(
    base_url="https://dispatch-api.dev.apex.esa.int",
    token="YOUR_API_KEY",
    prefix="",
    auth_header_name="X-Api-Key",
)
```

## Add Headers, Cookies, and Timeouts

```python
import httpx

client = AuthenticatedClient(
    base_url="https://dispatch-api.dev.apex.esa.int",
    token="YOUR_ACCESS_TOKEN",
    headers={"X-Request-Source": "notebook"},
    cookies={"session": "abc"},
    timeout=httpx.Timeout(30.0),
    follow_redirects=True,
)
```

You can derive a new client with additional settings:

```python
client = client.with_headers({"X-Trace-Id": "trace-123"})
client = client.with_timeout(httpx.Timeout(60.0))
```

These helpers also update the cached underlying `httpx.Client` or
`httpx.AsyncClient` when one has already been created.

## Pass Advanced httpx Options

Use `httpx_args` for constructor options supported by `httpx.Client` and
`httpx.AsyncClient`:

```python
client = AuthenticatedClient(
    base_url="https://dispatch-api.dev.apex.esa.int",
    token="YOUR_ACCESS_TOKEN",
    httpx_args={"trust_env": False},
)
```

## Use a Context Manager

```python
from apex_dispatch_api_client.api.default import health_health_get

with Client(base_url="https://dispatch-api.dev.apex.esa.int") as client:
    response = health_health_get.sync_detailed(client=client)
    print(response.status_code)
```

The context manager opens and closes the underlying `httpx.Client`.

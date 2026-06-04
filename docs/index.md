# APEx Dispatch API Client

This package is a Python client for the APEx Dispatch API. It wraps the
OpenAPI schema in typed Python models and operation modules built on top of
`httpx`.

## Documentation Structure

These docs follow the [Diataxis](https://diataxis.fr/) approach:

- Tutorials help you learn by completing a guided first task.
- How-to guides help you complete specific work.
- Reference pages describe the client, operations, and models.
- Explanation pages describe why the generated client behaves the way it does.

## Installation

Install the package from the repository root:

```bash
pip install .
```

For development, use the Hatch environments in `pyproject.toml`:

```bash
hatch run test:test
hatch run docs:build
```

## Minimal Client

Use `AuthenticatedClient` for secured APEx Dispatch endpoints:

```python
from apex_dispatch_api_client.client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://dispatch-api.dev.apex.esa.int",
    token="YOUR_ACCESS_TOKEN",
)
```

Use `Client` for public endpoints:

```python
from apex_dispatch_api_client.client import Client
from apex_dispatch_api_client.api.default import health_health_get

client = Client(base_url="https://dispatch-api.dev.apex.esa.int")
response = health_health_get.sync_detailed(client=client)

print(response.status_code)
```

## Where to Go Next

- Start with [Submit your first processing job](tutorials/first-processing-job.md).
- Use [Configure clients](how-to/configure-clients.md) when you need headers,
  cookies, timeouts, redirects, or custom `httpx` options.
- Keep [Operations](reference/operations.md) nearby while integrating endpoint
  modules.

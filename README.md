# APEx Dispatch API Client

Python client for the APEx Dispatch API.

The package is generated from the APEx Dispatch OpenAPI schema and provides
typed request and response models, synchronous and asynchronous endpoint
helpers, and `httpx`-based client configuration.

## Installation

Install the package from this repository:

```bash
pip install .
```

For local development, use the Hatch environments defined in
`pyproject.toml`:

```bash
hatch run test:test
hatch run docs:build
```

## Quick Start

```python
from apex_dispatch_api_client.client import AuthenticatedClient
from apex_dispatch_api_client.api.unit_jobs import create_unit_job_unit_jobs_post
from apex_dispatch_api_client.models.base_job_request import BaseJobRequest
from apex_dispatch_api_client.models.base_job_request_parameters import (
    BaseJobRequestParameters,
)
from apex_dispatch_api_client.models.output_format_enum import OutputFormatEnum
from apex_dispatch_api_client.models.process_type_enum import ProcessTypeEnum
from apex_dispatch_api_client.models.service_details import ServiceDetails

client = AuthenticatedClient(
    base_url="https://dispatch-api.dev.apex.esa.int",
    token="YOUR_ACCESS_TOKEN",
)

parameters = BaseJobRequestParameters()
parameters["bbox"] = [12.0, 41.0, 13.0, 42.0]
parameters["resolution"] = 10

request = BaseJobRequest(
    title="Vegetation index",
    label=ProcessTypeEnum.OGC_API_PROCESS,
    service=ServiceDetails(
        endpoint="https://processes.example.test",
        application="/processes/vegetation-index",
        namespace="apex",
    ),
    parameters=parameters,
    format_=OutputFormatEnum.GEOJSON,
)

job = create_unit_job_unit_jobs_post.sync(client=client, body=request)
print(job)
```

Use `sync_detailed` when you need the HTTP status code, headers, or raw
response content:

```python
response = create_unit_job_unit_jobs_post.sync_detailed(
    client=client,
    body=request,
)

print(response.status_code)
print(response.parsed)
```

Every generated operation module follows the same pattern:

- `sync(...)` returns the parsed response body.
- `sync_detailed(...)` returns `apex_dispatch_api_client.types.Response`.
- `asyncio(...)` is the asynchronous parsed-body helper.
- `asyncio_detailed(...)` is the asynchronous detailed helper.

## Client Types

Use `Client` for public endpoints such as `/health`.

Use `AuthenticatedClient` for secured endpoints. By default it sends
`Authorization: Bearer <token>`. You can customize the header for other API
gateway schemes:

```python
from apex_dispatch_api_client.client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://dispatch-api.dev.apex.esa.int",
    token="YOUR_API_KEY",
    prefix="",
    auth_header_name="X-Api-Key",
)
```

## Documentation

The MkDocs documentation is organized with the
[Diataxis](https://diataxis.fr/) framework:

- Tutorials for learning the client.
- How-to guides for common tasks.
- Reference pages for clients, operations, and models.
- Explanation pages for generated-client behavior and model serialization.

Build the documentation locally with:

```bash
hatch run docs:build
```

Serve it locally with:

```bash
hatch run docs:serve
```

## Regenerating the Client

The default Taskfile task downloads the APEx Dispatch OpenAPI schema and
regenerates the client:

```bash
task
```

The schema is stored in `schemas/openapi.json`, and generated Python code is
written to `src/apex_dispatch_api_client`.

## License

This project is licensed under the Apache License 2.0. See `LICENSE`.

# Submit Your First Processing Job

This tutorial walks through creating an authenticated client, building a
processing job request, and submitting it with the generated endpoint module.

## Before You Start

You need:

- Python 3.10 or newer.
- The `apex-dispatch-api-client` package installed.
- An APEx Dispatch API access token.
- A processing service endpoint and application path.

## Create a Python File

Create `first_job.py` with the imports you need:

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
```

## Configure the Client

```python
client = AuthenticatedClient(
    base_url="https://dispatch-api.dev.apex.esa.int",
    token="YOUR_ACCESS_TOKEN",
)
```

`AuthenticatedClient` sends the token as a bearer token by default.

## Describe the Service

```python
service = ServiceDetails(
    endpoint="https://processes.example.test",
    application="/processes/vegetation-index",
    namespace="apex",
)
```

For OGC API Processes, `endpoint` is the base platform API URL,
`application` is the service path, and `namespace` identifies the deployment
namespace.

## Build the Request Parameters

`BaseJobRequestParameters` is a flexible dict-like model. Add the parameters
expected by the service you are calling:

```python
parameters = BaseJobRequestParameters()
parameters["bbox"] = [12.0, 41.0, 13.0, 42.0]
parameters["resolution"] = 10
parameters["bands"] = ["B04", "B08"]
```

## Build the Job Request

```python
request = BaseJobRequest(
    title="Vegetation index",
    label=ProcessTypeEnum.OGC_API_PROCESS,
    service=service,
    parameters=parameters,
    format_=OutputFormatEnum.GEOJSON,
)
```

The Python attribute is named `format_` because `format` is a Python built-in.
The serialized request still uses the API field name `format`.

## Submit the Job

```python
created_job = create_unit_job_unit_jobs_post.sync(
    client=client,
    body=request,
)

print(created_job)
```

The plain `sync` helper returns the parsed response body. For this endpoint,
a successful response is parsed as `ProcessingJobSummary`.

## Get HTTP Details

Replace `sync` with `sync_detailed` when you want to inspect the HTTP response:

```python
response = create_unit_job_unit_jobs_post.sync_detailed(
    client=client,
    body=request,
)

print(response.status_code)
print(response.headers)
print(response.parsed)
```

You have now created a client, built a typed request, and submitted a
processing job through the generated APEx Dispatch API client.

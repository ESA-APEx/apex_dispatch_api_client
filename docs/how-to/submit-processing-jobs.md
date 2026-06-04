# Submit Processing Jobs

The client provides two processing-job creation endpoints:

- `create_unit_job_unit_jobs_post` posts to `/unit_jobs` and returns a job
  summary.
- `create_sync_job_sync_jobs_post` posts to `/sync_jobs` and returns the
  synchronous job result payload.

Both endpoints accept `BaseJobRequest`.

## Build a Base Job Request

```python
from apex_dispatch_api_client.models.base_job_request import BaseJobRequest
from apex_dispatch_api_client.models.base_job_request_parameters import (
    BaseJobRequestParameters,
)
from apex_dispatch_api_client.models.output_format_enum import OutputFormatEnum
from apex_dispatch_api_client.models.process_type_enum import ProcessTypeEnum
from apex_dispatch_api_client.models.service_details import ServiceDetails

parameters = BaseJobRequestParameters()
parameters["collection"] = "SENTINEL2_L2A"
parameters["bbox"] = [12.0, 41.0, 13.0, 42.0]

body = BaseJobRequest(
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
```

## Create a Unit Job

```python
from apex_dispatch_api_client.api.unit_jobs import create_unit_job_unit_jobs_post

job = create_unit_job_unit_jobs_post.sync(client=client, body=body)
print(job)
```

Use this endpoint when the processing job should be created and tracked by job
ID.

## Create a Synchronous Job

```python
from apex_dispatch_api_client.api.unit_jobs import create_sync_job_sync_jobs_post

result = create_sync_job_sync_jobs_post.sync(client=client, body=body)
print(result)
```

Use this endpoint when you want the API to return the processing result
directly.

## Request Service Parameters

Use `/params` before submitting a job when you need the parameter definitions
for a service:

```python
from apex_dispatch_api_client.api.unit_jobs import get_job_params_params_post
from apex_dispatch_api_client.models.param_request import ParamRequest

params = get_job_params_params_post.sync(
    client=client,
    body=ParamRequest(
        label=ProcessTypeEnum.OGC_API_PROCESS,
        service=body.service,
    ),
)

for param in params or []:
    print(param.name, param.type_, param.optional)
```

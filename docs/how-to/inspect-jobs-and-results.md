# Inspect Jobs and Results

Use the generated unit-job and status endpoint modules to check job state,
fetch results, and delete jobs.

## Get a Processing Job

```python
from apex_dispatch_api_client.api.unit_jobs import get_job_unit_jobs_job_id_get

job = get_job_unit_jobs_job_id_get.sync(42, client=client)
print(job)
```

A successful response is parsed as `ProcessingJob`.

## Get Job Results

```python
from apex_dispatch_api_client.api.unit_jobs import (
    get_job_results_unit_jobs_job_id_results_get,
)

results = get_job_results_unit_jobs_job_id_results_get.sync(42, client=client)
print(results)
```

The result endpoint returns a STAC `Collection`, `None`, or an error model,
depending on the API response.

## Check Combined Job Status

```python
from apex_dispatch_api_client.api.upscale_tasks import (
    get_jobs_status_jobs_status_get,
)
from apex_dispatch_api_client.models.jobs_filter import JobsFilter

status = get_jobs_status_jobs_status_get.sync(
    client=client,
    filter_=[JobsFilter.PROCESSING, JobsFilter.UPSCALING],
)

print(status)
```

The `filter_` argument accepts `JobsFilter.PROCESSING` and
`JobsFilter.UPSCALING`. The generated client serializes them as repeated
`filter` query parameters.

## Delete a Job

```python
from apex_dispatch_api_client.api.unit_jobs import delete_job_unit_jobs_job_id_delete

deleted = delete_job_unit_jobs_job_id_delete.sync(42, client=client)
print(deleted)
```

Use `sync_detailed` instead of `sync` when you need to distinguish response
status codes.

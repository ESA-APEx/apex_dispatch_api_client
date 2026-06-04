# Operations

Endpoint helpers live under `apex_dispatch_api_client.api`. Operation modules
are grouped by OpenAPI tag.

Each generated operation module exposes the same helper pattern:

| Helper | Return value |
| --- | --- |
| `sync(...)` | Parsed response body. |
| `sync_detailed(...)` | `Response[...]` with status, headers, content, and parsed body. |
| `asyncio(...)` | Awaitable parsed response body. |
| `asyncio_detailed(...)` | Awaitable `Response[...]`. |

The `health_health_get` module exposes only detailed helpers because the
successful response body is empty.

## Default

| Module | Method | Path | Client | Successful parsed response |
| --- | --- | --- | --- | --- |
| `default.health_health_get` | `GET` | `/health` | `Client` or `AuthenticatedClient` | `None` |

## Unit Jobs

| Module | Method | Path | Client | Body | Successful parsed response |
| --- | --- | --- | --- | --- | --- |
| `unit_jobs.create_unit_job_unit_jobs_post` | `POST` | `/unit_jobs` | `AuthenticatedClient` | `BaseJobRequest` | `ProcessingJobSummary` |
| `unit_jobs.create_sync_job_sync_jobs_post` | `POST` | `/sync_jobs` | `AuthenticatedClient` | `BaseJobRequest` | `Any` JSON payload |
| `unit_jobs.get_job_unit_jobs_job_id_get` | `GET` | `/unit_jobs/{job_id}` | `AuthenticatedClient` | None | `ProcessingJob` |
| `unit_jobs.get_job_results_unit_jobs_job_id_results_get` | `GET` | `/unit_jobs/{job_id}/results` | `AuthenticatedClient` | None | `Collection | None` |
| `unit_jobs.delete_job_unit_jobs_job_id_delete` | `DELETE` | `/unit_jobs/{job_id}` | `AuthenticatedClient` | None | `Any` JSON payload |
| `unit_jobs.get_job_params_params_post` | `POST` | `/params` | `AuthenticatedClient` | `ParamRequest` | `list[Parameter]` |

## Upscale Tasks

| Module | Method | Path | Client | Body or query | Successful parsed response |
| --- | --- | --- | --- | --- | --- |
| `upscale_tasks.create_upscale_task_upscale_tasks_post` | `POST` | `/upscale_tasks` | `AuthenticatedClient` | `UpscalingTaskRequest` | `UpscalingTaskSummary` |
| `upscale_tasks.get_upscale_task_upscale_tasks_task_id_get` | `GET` | `/upscale_tasks/{task_id}` | `AuthenticatedClient` | None | `UpscalingTask` |
| `upscale_tasks.get_jobs_status_jobs_status_get` | `GET` | `/jobs_status` | `AuthenticatedClient` | `filter_: list[JobsFilter]` | `JobsStatusResponse` |
| `upscale_tasks.split_in_tiles_tiles_post` | `POST` | `/tiles` | `Client` or `AuthenticatedClient` | `TileRequest` | `GeometryCollection` |

## Error Responses

Documented error responses are parsed into models such as `ErrorResponse` and
`HTTPValidationError`.

Undocumented status codes behave according to the client setting:

- `raise_on_unexpected_status=False`: parsed response is `None`.
- `raise_on_unexpected_status=True`: the helper raises `UnexpectedStatus`.

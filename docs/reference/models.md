# Models

Generated models live under `apex_dispatch_api_client.models`.

All generated model classes provide:

- `to_dict()` for API serialization.
- `from_dict(...)` for API parsing.
- `additional_properties` for extra API fields.
- Mapping-style access for extra fields with `model["field"]`.

## Request Models

| Model | Purpose |
| --- | --- |
| `BaseJobRequest` | Request body for `/unit_jobs` and `/sync_jobs`. |
| `BaseJobRequestParameters` | Flexible job parameter container. |
| `ParamRequest` | Request body for `/params`. |
| `ServiceDetails` | Processing service endpoint, application, and optional namespace. |
| `TileRequest` | Request body for `/tiles`. |
| `UpscalingTaskRequest` | Request body for `/upscale_tasks`. |
| `UpscalingTaskRequestParameters` | Flexible upscaling parameter container. |
| `ParameterDimension` | Parameter name and values used to create multiple upscaling jobs. |

## Response Models

| Model | Purpose |
| --- | --- |
| `ProcessingJob` | Full processing job. |
| `ProcessingJobSummary` | Summary returned after creating a processing job. |
| `UpscalingTask` | Full upscaling task. |
| `UpscalingTaskSummary` | Summary returned after creating an upscaling task. |
| `JobsStatusResponse` | Combined status response for processing and upscaling jobs. |
| `Collection` | STAC collection returned by job results. |
| `GeometryCollection` | GeoJSON geometry collection returned by tile splitting. |
| `Parameter` | Processing service parameter description. |
| `ErrorResponse` | API error body. |
| `HTTPValidationError` | Validation error body. |

## Common Enums

| Enum | Values |
| --- | --- |
| `ProcessTypeEnum` | `ogc_api_process`, `openeo` |
| `OutputFormatEnum` | `geojson`, `gtiff`, `json`, `netcdf` |
| `ProcessingStatusEnum` | `canceled`, `created`, `failed`, `finished`, `queued`, `running`, `unknown` |
| `JobsFilter` | `processing`, `upscaling` |
| `GridTypeEnum` | `20x20km`, `250x250km` |
| `ParamTypeEnum` | `array-string`, `boolean`, `bounding-box`, `datetime`, `date-interval`, `double`, `integer`, `polygon`, `string` |

## Flexible Parameter Containers

`BaseJobRequestParameters` and `UpscalingTaskRequestParameters` accept
service-specific fields:

```python
parameters = BaseJobRequestParameters()
parameters["collection"] = "SENTINEL2_L2A"
parameters["bbox"] = [12.0, 41.0, 13.0, 42.0]

payload = parameters.to_dict()
```

## Field Names Ending in `_`

Some model attributes end in `_` to avoid Python names such as `format` and
`type`:

| Python attribute | Serialized field |
| --- | --- |
| `format_` | `format` |
| `type_` | `type` |
| `license_` | `license` |

Use the Python attribute in code. `to_dict()` and `from_dict()` handle the API
field name.

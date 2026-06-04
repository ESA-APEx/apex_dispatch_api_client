# Data Models and Extra Fields

The generated models balance typed fields with the flexibility needed by
service-specific APEx Dispatch payloads.

## Typed Shells

Models such as `BaseJobRequest`, `ServiceDetails`, and `ProcessingJob` expose
known OpenAPI fields as Python attributes. Their `to_dict()` methods serialize
those attributes into API field names, and their `from_dict()` methods parse
API payloads back into model objects.

This gives application code a typed shape for stable API fields:

```python
request.title
request.service.endpoint
request.format_
```

## Flexible Parameter Payloads

Processing services can define their own parameter names and values. For that
reason, parameter containers such as `BaseJobRequestParameters` and
`UpscalingTaskRequestParameters` are intentionally dict-like:

```python
parameters = BaseJobRequestParameters()
parameters["resolution"] = 10
parameters["bbox"] = [12.0, 41.0, 13.0, 42.0]
```

When serialized, these values become the `parameters` object sent to the API.

## Additional Properties

Most generated models preserve fields that are present in API payloads but not
declared as explicit attributes. These values are stored in
`additional_properties`.

```python
service = ServiceDetails.from_dict(
    {
        "endpoint": "https://processes.example.test",
        "application": "/processes/vegetation-index",
        "deployment_id": "dep-123",
    }
)

print(service["deployment_id"])
print(service.additional_keys)
```

This behavior helps the client remain tolerant of compatible API additions.

## Unset and Explicit Null

Optional fields use `UNSET` to distinguish "not provided" from `None`.

For example, `ServiceDetails.namespace` can be omitted or explicitly set to
`None`. Omitted fields do not appear in `to_dict()` output. Explicit `None`
values are serialized as JSON `null`.

# Clients

The package exposes two client classes from `apex_dispatch_api_client.client`.

## `Client`

`Client` stores shared configuration for public API calls.

| Argument | Type | Description |
| --- | --- | --- |
| `base_url` | `str` | Base URL for the APEx Dispatch API. |
| `cookies` | `dict[str, str]` | Cookies sent with every request. |
| `headers` | `dict[str, str]` | Headers sent with every request. |
| `timeout` | `httpx.Timeout | None` | Request timeout configuration. |
| `verify_ssl` | `str | bool | ssl.SSLContext` | SSL certificate verification setting. |
| `follow_redirects` | `bool` | Redirect handling. Defaults to `False`. |
| `httpx_args` | `dict[str, Any]` | Extra constructor arguments passed to `httpx.Client` and `httpx.AsyncClient`. |
| `raise_on_unexpected_status` | `bool` | Raise `UnexpectedStatus` for undocumented status codes. Defaults to `False`. |

### Methods

| Method | Description |
| --- | --- |
| `with_headers(headers)` | Return an evolved client with merged headers. |
| `with_cookies(cookies)` | Return an evolved client with merged cookies. |
| `with_timeout(timeout)` | Return an evolved client with a new timeout. |
| `set_httpx_client(client)` | Set the underlying `httpx.Client`. |
| `get_httpx_client()` | Return the cached `httpx.Client`, creating it if needed. |
| `set_async_httpx_client(async_client)` | Set the underlying `httpx.AsyncClient`. |
| `get_async_httpx_client()` | Return the cached `httpx.AsyncClient`, creating it if needed. |

`Client` supports sync and async context managers.

## `AuthenticatedClient`

`AuthenticatedClient` has the same configuration as `Client` and adds
authentication fields.

| Argument | Type | Description |
| --- | --- | --- |
| `token` | `str` | Token used for authentication. |
| `prefix` | `str` | Authorization prefix. Defaults to `Bearer`. |
| `auth_header_name` | `str` | Authentication header name. Defaults to `Authorization`. |

By default, the client sends:

```text
Authorization: Bearer <token>
```

Set `prefix=""` to send the token without a prefix.

## Response Wrapper

Detailed endpoint helpers return `apex_dispatch_api_client.types.Response`.

| Attribute | Type | Description |
| --- | --- | --- |
| `status_code` | `http.HTTPStatus` | HTTP status code. |
| `content` | `bytes` | Raw response body. |
| `headers` | `MutableMapping[str, str]` | Response headers. |
| `parsed` | `T | None` | Parsed response model or raw JSON payload. |

## File Upload Type

`apex_dispatch_api_client.types.File` stores multipart upload values.

| Attribute | Type | Description |
| --- | --- | --- |
| `payload` | `BinaryIO` | File payload. |
| `file_name` | `str | None` | Optional filename. |
| `mime_type` | `str | None` | Optional MIME type. |

`File.to_tuple()` returns a tuple accepted by `httpx` multipart requests.

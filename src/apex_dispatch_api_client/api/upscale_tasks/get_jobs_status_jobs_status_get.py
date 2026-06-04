from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.jobs_filter import JobsFilter
from ...models.jobs_status_response import JobsStatusResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_: list[JobsFilter] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_filter_: list[str] | Unset = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = []
        for filter_item_data in filter_:
            filter_item = filter_item_data.value
            json_filter_.append(filter_item)

    params["filter"] = json_filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/jobs_status",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | JobsStatusResponse | None:
    if response.status_code == 200:
        response_200 = JobsStatusResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | HTTPValidationError | JobsStatusResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    filter_: list[JobsFilter] | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | JobsStatusResponse]:
    """Get a list of all upscaling tasks & processing jobs for the authenticated user

     Return combined list of upscaling tasks and processing jobs for the authenticated user.

    Args:
        filter_ (list[JobsFilter] | Unset): Filter jobs: upscaling, processing. Can be provided
            multiple times.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | JobsStatusResponse]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    filter_: list[JobsFilter] | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | JobsStatusResponse | None:
    """Get a list of all upscaling tasks & processing jobs for the authenticated user

     Return combined list of upscaling tasks and processing jobs for the authenticated user.

    Args:
        filter_ (list[JobsFilter] | Unset): Filter jobs: upscaling, processing. Can be provided
            multiple times.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | JobsStatusResponse
    """

    return sync_detailed(
        client=client,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    filter_: list[JobsFilter] | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | JobsStatusResponse]:
    """Get a list of all upscaling tasks & processing jobs for the authenticated user

     Return combined list of upscaling tasks and processing jobs for the authenticated user.

    Args:
        filter_ (list[JobsFilter] | Unset): Filter jobs: upscaling, processing. Can be provided
            multiple times.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | JobsStatusResponse]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    filter_: list[JobsFilter] | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | JobsStatusResponse | None:
    """Get a list of all upscaling tasks & processing jobs for the authenticated user

     Return combined list of upscaling tasks and processing jobs for the authenticated user.

    Args:
        filter_ (list[JobsFilter] | Unset): Filter jobs: upscaling, processing. Can be provided
            multiple times.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | JobsStatusResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
        )
    ).parsed

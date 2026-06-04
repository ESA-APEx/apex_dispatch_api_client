from http import HTTPStatus
import json

import httpx
import pytest

from apex_dispatch_api_client import errors
from apex_dispatch_api_client.api.default import health_health_get as health
from apex_dispatch_api_client.api.unit_jobs import (
    create_unit_job_unit_jobs_post as create_unit_job,
)
from apex_dispatch_api_client.api.unit_jobs import (
    get_job_unit_jobs_job_id_get as get_job,
)
from apex_dispatch_api_client.api.upscale_tasks import (
    get_jobs_status_jobs_status_get as get_jobs_status,
)
from apex_dispatch_api_client.client import AuthenticatedClient, Client
from apex_dispatch_api_client.models.base_job_request import BaseJobRequest
from apex_dispatch_api_client.models.base_job_request_parameters import (
    BaseJobRequestParameters,
)
from apex_dispatch_api_client.models.error_response import ErrorResponse
from apex_dispatch_api_client.models.jobs_filter import JobsFilter
from apex_dispatch_api_client.models.jobs_status_response import JobsStatusResponse
from apex_dispatch_api_client.models.output_format_enum import OutputFormatEnum
from apex_dispatch_api_client.models.process_type_enum import ProcessTypeEnum
from apex_dispatch_api_client.models.processing_job_summary import ProcessingJobSummary
from apex_dispatch_api_client.models.processing_status_enum import ProcessingStatusEnum
from apex_dispatch_api_client.models.service_details import ServiceDetails


BASE_URL = "https://dispatch.example.test"


def make_base_job_request() -> BaseJobRequest:
    parameters = BaseJobRequestParameters()
    parameters["resolution"] = 10
    parameters["bbox"] = [1.0, 2.0, 3.0, 4.0]

    service = ServiceDetails(
        endpoint="https://processes.example.test",
        application="/processes/vegetation-index",
        namespace="apex",
    )

    return BaseJobRequest(
        title="Vegetation index",
        label=ProcessTypeEnum.OGC_API_PROCESS,
        service=service,
        parameters=parameters,
        format_=OutputFormatEnum.GEOJSON,
    )


def make_processing_job_summary_payload() -> dict[str, object]:
    return {
        "id": 42,
        "title": "Vegetation index",
        "label": ProcessTypeEnum.OGC_API_PROCESS.value,
        "status": ProcessingStatusEnum.CREATED.value,
        "service": {
            "endpoint": "https://processes.example.test",
            "application": "/processes/vegetation-index",
            "namespace": "apex",
        },
        "parameters": {"resolution": 10},
    }


def make_auth_client(
    transport: httpx.MockTransport, **kwargs: object
) -> AuthenticatedClient:
    return AuthenticatedClient(
        base_url=BASE_URL,
        token="test-token",
        httpx_args={"transport": transport},
        **kwargs,
    )


def close_client(client: Client | AuthenticatedClient) -> None:
    if client._client is not None:
        client._client.close()


def test_health_sync_detailed_requests_health_endpoint() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "GET"
        assert request.url.path == "/health"
        return httpx.Response(200, content=b"ok")

    client = Client(
        base_url=BASE_URL,
        httpx_args={"transport": httpx.MockTransport(handler)},
    )

    try:
        response = health.sync_detailed(client=client)
    finally:
        close_client(client)

    assert response.status_code is HTTPStatus.OK
    assert response.content == b"ok"
    assert response.parsed is None


def test_create_unit_job_sends_json_body_and_parses_summary() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "POST"
        assert request.url.path == "/unit_jobs"
        assert request.headers["content-type"] == "application/json"

        body = json.loads(request.content)
        assert body == {
            "title": "Vegetation index",
            "label": "ogc_api_process",
            "service": {
                "endpoint": "https://processes.example.test",
                "application": "/processes/vegetation-index",
                "namespace": "apex",
            },
            "parameters": {"resolution": 10, "bbox": [1.0, 2.0, 3.0, 4.0]},
            "format": "geojson",
        }
        return httpx.Response(201, json=make_processing_job_summary_payload())

    client = make_auth_client(httpx.MockTransport(handler))

    try:
        response = create_unit_job.sync_detailed(
            client=client,
            body=make_base_job_request(),
        )
    finally:
        close_client(client)

    assert response.status_code is HTTPStatus.CREATED
    assert isinstance(response.parsed, ProcessingJobSummary)
    assert response.parsed.id == 42
    assert response.parsed.parameters["resolution"] == 10


def test_get_job_parses_error_response() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "GET"
        assert request.url.path == "/unit_jobs/404"
        return httpx.Response(
            404,
            json={
                "error_code": "job_not_found",
                "message": "Job was not found",
                "request_id": "req-123",
            },
        )

    client = make_auth_client(httpx.MockTransport(handler))

    try:
        parsed = get_job.sync(404, client=client)
    finally:
        close_client(client)

    assert isinstance(parsed, ErrorResponse)
    assert parsed.error_code == "job_not_found"
    assert parsed.request_id == "req-123"


def test_get_jobs_status_serializes_filter_query_and_parses_response() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "GET"
        assert request.url.path == "/jobs_status"
        assert request.url.params.get_list("filter") == ["processing", "upscaling"]
        return httpx.Response(
            200,
            json={
                "upscaling_tasks": [
                    {
                        "id": 7,
                        "title": "Upscale S2 scene",
                        "label": "openeo",
                        "status": "running",
                    }
                ],
                "processing_jobs": [make_processing_job_summary_payload()],
            },
        )

    client = make_auth_client(httpx.MockTransport(handler))

    try:
        parsed = get_jobs_status.sync(
            client=client,
            filter_=[JobsFilter.PROCESSING, JobsFilter.UPSCALING],
        )
    finally:
        close_client(client)

    assert isinstance(parsed, JobsStatusResponse)
    assert parsed.upscaling_tasks[0].id == 7
    assert parsed.processing_jobs[0].status is ProcessingStatusEnum.CREATED


def test_unexpected_status_raises_when_enabled() -> None:
    def handler(_: httpx.Request) -> httpx.Response:
        return httpx.Response(418, content=b"short and stout")

    client = Client(
        base_url=BASE_URL,
        raise_on_unexpected_status=True,
        httpx_args={"transport": httpx.MockTransport(handler)},
    )

    try:
        with pytest.raises(errors.UnexpectedStatus) as exc_info:
            health.sync_detailed(client=client)
    finally:
        close_client(client)

    assert exc_info.value.status_code == 418
    assert exc_info.value.content == b"short and stout"
    assert "Unexpected status code: 418" in str(exc_info.value)

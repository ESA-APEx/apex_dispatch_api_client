from datetime import datetime

from apex_dispatch_api_client.models.asset import Asset
from apex_dispatch_api_client.models.base_job_request import BaseJobRequest
from apex_dispatch_api_client.models.base_job_request_parameters import (
    BaseJobRequestParameters,
)
from apex_dispatch_api_client.models.output_format_enum import OutputFormatEnum
from apex_dispatch_api_client.models.process_type_enum import ProcessTypeEnum
from apex_dispatch_api_client.models.processing_job import ProcessingJob
from apex_dispatch_api_client.models.processing_job_parameters import (
    ProcessingJobParameters,
)
from apex_dispatch_api_client.models.processing_status_enum import ProcessingStatusEnum
from apex_dispatch_api_client.models.service_details import ServiceDetails


def test_service_details_omits_unset_namespace_and_preserves_extra_fields() -> None:
    service = ServiceDetails(
        endpoint="https://processes.example.test",
        application="/processes/vegetation-index",
    )

    assert service.to_dict() == {
        "endpoint": "https://processes.example.test",
        "application": "/processes/vegetation-index",
    }

    parsed = ServiceDetails.from_dict(
        {
            "endpoint": "https://processes.example.test",
            "application": "/processes/vegetation-index",
            "namespace": None,
            "deployment_id": "dep-123",
        }
    )

    assert parsed.namespace is None
    assert parsed["deployment_id"] == "dep-123"
    assert "deployment_id" in parsed
    assert parsed.additional_keys == ["deployment_id"]


def test_base_job_request_round_trips_nested_extra_properties() -> None:
    parameters = BaseJobRequestParameters()
    parameters["aoi"] = {"type": "Polygon"}
    parameters["bands"] = ["B04", "B08"]

    service = ServiceDetails(
        endpoint="https://processes.example.test",
        application="/processes/vegetation-index",
        namespace="apex",
    )
    service["deployment"] = {"id": "dep-123"}

    request = BaseJobRequest(
        title="Vegetation index",
        label=ProcessTypeEnum.OGC_API_PROCESS,
        service=service,
        parameters=parameters,
        format_=OutputFormatEnum.GEOJSON,
    )
    request["priority"] = "high"

    serialized = request.to_dict()
    parsed = BaseJobRequest.from_dict(serialized)

    assert serialized["format"] == "geojson"
    assert "format_" not in serialized
    assert parsed.label is ProcessTypeEnum.OGC_API_PROCESS
    assert parsed.format_ is OutputFormatEnum.GEOJSON
    assert parsed.parameters["bands"] == ["B04", "B08"]
    assert parsed.service["deployment"] == {"id": "dep-123"}
    assert parsed["priority"] == "high"


def test_processing_job_parses_datetimes_and_serializes_enums() -> None:
    payload = {
        "id": 42,
        "title": "Vegetation index",
        "label": "openeo",
        "status": "running",
        "service": {
            "endpoint": "https://openeo.example.test",
            "application": "https://example.test/process.json",
        },
        "parameters": {"collection": "SENTINEL2_L2A"},
        "created": "2026-06-04T10:30:00+00:00",
        "updated": "2026-06-04T10:35:00+00:00",
        "progress": 50,
    }

    job = ProcessingJob.from_dict(payload)
    serialized = job.to_dict()

    assert job.label is ProcessTypeEnum.OPENEO
    assert job.status is ProcessingStatusEnum.RUNNING
    assert isinstance(job.parameters, ProcessingJobParameters)
    assert isinstance(job.created, datetime)
    assert job.created.isoformat() == "2026-06-04T10:30:00+00:00"
    assert serialized["status"] == "running"
    assert serialized["updated"] == "2026-06-04T10:35:00+00:00"
    assert serialized["progress"] == 50


def test_asset_omits_unset_optional_fields_but_keeps_explicit_none() -> None:
    assert Asset(href="s3://bucket/data.tif").to_dict() == {
        "href": "s3://bucket/data.tif"
    }

    asset = Asset.from_dict(
        {
            "href": "s3://bucket/data.tif",
            "type": None,
            "roles": ["data"],
            "checksum": "sha256:abc",
        }
    )

    assert asset.type_ is None
    assert asset.roles == ["data"]
    assert asset["checksum"] == "sha256:abc"
    assert asset.to_dict()["type"] is None

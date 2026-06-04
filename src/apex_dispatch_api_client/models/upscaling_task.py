from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.process_type_enum import ProcessTypeEnum
from ..models.processing_status_enum import ProcessingStatusEnum

if TYPE_CHECKING:
    from ..models.processing_job_summary import ProcessingJobSummary
    from ..models.service_details import ServiceDetails


T = TypeVar("T", bound="UpscalingTask")


@_attrs_define
class UpscalingTask:
    """
    Attributes:
        id (int): Unique identifier of the upscaling task
        title (str): Title of the upscaling task
        label (ProcessTypeEnum):
        status (ProcessingStatusEnum):
        service (ServiceDetails):
        created (datetime.datetime): Creation time of the processing job
        updated (datetime.datetime): Timestamp representing the last time that the job details were updated
        jobs (list[ProcessingJobSummary]): List of processing jobs that were launched with the upscaling request
    """

    id: int
    title: str
    label: ProcessTypeEnum
    status: ProcessingStatusEnum
    service: ServiceDetails
    created: datetime.datetime
    updated: datetime.datetime
    jobs: list[ProcessingJobSummary]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        label = self.label.value

        status = self.status.value

        service = self.service.to_dict()

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        jobs = []
        for jobs_item_data in self.jobs:
            jobs_item = jobs_item_data.to_dict()
            jobs.append(jobs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "label": label,
                "status": status,
                "service": service,
                "created": created,
                "updated": updated,
                "jobs": jobs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.processing_job_summary import ProcessingJobSummary
        from ..models.service_details import ServiceDetails

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        label = ProcessTypeEnum(d.pop("label"))

        status = ProcessingStatusEnum(d.pop("status"))

        service = ServiceDetails.from_dict(d.pop("service"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        jobs = []
        _jobs = d.pop("jobs")
        for jobs_item_data in _jobs:
            jobs_item = ProcessingJobSummary.from_dict(jobs_item_data)

            jobs.append(jobs_item)

        upscaling_task = cls(
            id=id,
            title=title,
            label=label,
            status=status,
            service=service,
            created=created,
            updated=updated,
            jobs=jobs,
        )

        upscaling_task.additional_properties = d
        return upscaling_task

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

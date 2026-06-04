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
    from ..models.processing_job_parameters import ProcessingJobParameters
    from ..models.service_details import ServiceDetails


T = TypeVar("T", bound="ProcessingJob")


@_attrs_define
class ProcessingJob:
    """
    Attributes:
        id (int): Unique identifier of the processing job
        title (str): Title of the job
        label (ProcessTypeEnum):
        status (ProcessingStatusEnum):
        service (ServiceDetails):
        parameters (ProcessingJobParameters): JSON representing the parameters for the service execution
        created (datetime.datetime): Creation time of the processing job
        updated (datetime.datetime): Timestamp representing the last time that the job details were updated
    """

    id: int
    title: str
    label: ProcessTypeEnum
    status: ProcessingStatusEnum
    service: ServiceDetails
    parameters: ProcessingJobParameters
    created: datetime.datetime
    updated: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        label = self.label.value

        status = self.status.value

        service = self.service.to_dict()

        parameters = self.parameters.to_dict()

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "label": label,
                "status": status,
                "service": service,
                "parameters": parameters,
                "created": created,
                "updated": updated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.processing_job_parameters import ProcessingJobParameters
        from ..models.service_details import ServiceDetails

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        label = ProcessTypeEnum(d.pop("label"))

        status = ProcessingStatusEnum(d.pop("status"))

        service = ServiceDetails.from_dict(d.pop("service"))

        parameters = ProcessingJobParameters.from_dict(d.pop("parameters"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        processing_job = cls(
            id=id,
            title=title,
            label=label,
            status=status,
            service=service,
            parameters=parameters,
            created=created,
            updated=updated,
        )

        processing_job.additional_properties = d
        return processing_job

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

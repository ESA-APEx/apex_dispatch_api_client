from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.output_format_enum import OutputFormatEnum
from ..models.process_type_enum import ProcessTypeEnum

if TYPE_CHECKING:
    from ..models.base_job_request_parameters import BaseJobRequestParameters
    from ..models.service_details import ServiceDetails


T = TypeVar("T", bound="BaseJobRequest")


@_attrs_define
class BaseJobRequest:
    """
    Attributes:
        title (str): Title of the job to execute
        label (ProcessTypeEnum):
        service (ServiceDetails):
        parameters (BaseJobRequestParameters): JSON representing the parameters for the service execution
        format_ (OutputFormatEnum):
    """

    title: str
    label: ProcessTypeEnum
    service: ServiceDetails
    parameters: BaseJobRequestParameters
    format_: OutputFormatEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        label = self.label.value

        service = self.service.to_dict()

        parameters = self.parameters.to_dict()

        format_ = self.format_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "label": label,
                "service": service,
                "parameters": parameters,
                "format": format_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_job_request_parameters import BaseJobRequestParameters
        from ..models.service_details import ServiceDetails

        d = dict(src_dict)
        title = d.pop("title")

        label = ProcessTypeEnum(d.pop("label"))

        service = ServiceDetails.from_dict(d.pop("service"))

        parameters = BaseJobRequestParameters.from_dict(d.pop("parameters"))

        format_ = OutputFormatEnum(d.pop("format"))

        base_job_request = cls(
            title=title,
            label=label,
            service=service,
            parameters=parameters,
            format_=format_,
        )

        base_job_request.additional_properties = d
        return base_job_request

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

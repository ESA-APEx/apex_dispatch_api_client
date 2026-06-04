from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.output_format_enum import OutputFormatEnum
from ..models.process_type_enum import ProcessTypeEnum

if TYPE_CHECKING:
    from ..models.parameter_dimension import ParameterDimension
    from ..models.service_details import ServiceDetails
    from ..models.upscaling_task_request_parameters import (
        UpscalingTaskRequestParameters,
    )


T = TypeVar("T", bound="UpscalingTaskRequest")


@_attrs_define
class UpscalingTaskRequest:
    """
    Attributes:
        title (str): Title of the job to execute
        label (ProcessTypeEnum):
        service (ServiceDetails):
        parameters (UpscalingTaskRequestParameters): JSON representing the parameters for the service execution
        format_ (OutputFormatEnum):
        dimension (ParameterDimension):
    """

    title: str
    label: ProcessTypeEnum
    service: ServiceDetails
    parameters: UpscalingTaskRequestParameters
    format_: OutputFormatEnum
    dimension: ParameterDimension
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        label = self.label.value

        service = self.service.to_dict()

        parameters = self.parameters.to_dict()

        format_ = self.format_.value

        dimension = self.dimension.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "label": label,
                "service": service,
                "parameters": parameters,
                "format": format_,
                "dimension": dimension,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parameter_dimension import ParameterDimension
        from ..models.service_details import ServiceDetails
        from ..models.upscaling_task_request_parameters import (
            UpscalingTaskRequestParameters,
        )

        d = dict(src_dict)
        title = d.pop("title")

        label = ProcessTypeEnum(d.pop("label"))

        service = ServiceDetails.from_dict(d.pop("service"))

        parameters = UpscalingTaskRequestParameters.from_dict(d.pop("parameters"))

        format_ = OutputFormatEnum(d.pop("format"))

        dimension = ParameterDimension.from_dict(d.pop("dimension"))

        upscaling_task_request = cls(
            title=title,
            label=label,
            service=service,
            parameters=parameters,
            format_=format_,
            dimension=dimension,
        )

        upscaling_task_request.additional_properties = d
        return upscaling_task_request

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

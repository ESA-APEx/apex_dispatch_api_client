from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_type_enum import ProcessTypeEnum

if TYPE_CHECKING:
    from ..models.service_details import ServiceDetails


T = TypeVar("T", bound="ParamRequest")


@_attrs_define
class ParamRequest:
    """
    Attributes:
        label (ProcessTypeEnum):
        service (ServiceDetails):
    """

    label: ProcessTypeEnum
    service: ServiceDetails
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label.value

        service = self.service.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "service": service,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_details import ServiceDetails

        d = dict(src_dict)
        label = ProcessTypeEnum(d.pop("label"))

        service = ServiceDetails.from_dict(d.pop("service"))

        param_request = cls(
            label=label,
            service=service,
        )

        param_request.additional_properties = d
        return param_request

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

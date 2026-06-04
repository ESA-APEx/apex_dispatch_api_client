from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_type_enum import ProcessTypeEnum
from ..models.processing_status_enum import ProcessingStatusEnum

T = TypeVar("T", bound="UpscalingTaskSummary")


@_attrs_define
class UpscalingTaskSummary:
    """
    Attributes:
        id (int): Unique identifier of the upscaling task
        title (str): Title of the upscaling task
        label (ProcessTypeEnum):
        status (ProcessingStatusEnum):
    """

    id: int
    title: str
    label: ProcessTypeEnum
    status: ProcessingStatusEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        label = self.label.value

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "label": label,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        label = ProcessTypeEnum(d.pop("label"))

        status = ProcessingStatusEnum(d.pop("status"))

        upscaling_task_summary = cls(
            id=id,
            title=title,
            label=label,
            status=status,
        )

        upscaling_task_summary.additional_properties = d
        return upscaling_task_summary

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

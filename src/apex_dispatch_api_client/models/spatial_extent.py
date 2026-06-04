from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SpatialExtent")


@_attrs_define
class SpatialExtent:
    """https://github.com/radiantearth/stac-spec/blob/v1.0.0/collection-spec/collection-spec.md#spatial-extent-object

    Attributes:
        bbox (list[list[float | int]]):
    """

    bbox: list[list[float | int]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bbox = []
        for bbox_item_data in self.bbox:
            bbox_item: list[float | int]
            if isinstance(bbox_item_data, list):
                bbox_item = []
                for bbox_item_type_0_item_data in bbox_item_data:
                    bbox_item_type_0_item: float | int
                    bbox_item_type_0_item = bbox_item_type_0_item_data
                    bbox_item.append(bbox_item_type_0_item)

            bbox.append(bbox_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bbox": bbox,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bbox = []
        _bbox = d.pop("bbox")
        for bbox_item_data in _bbox:

            def _parse_bbox_item(data: object) -> list[float | int]:
                if not isinstance(data, list):
                    raise TypeError()
                bbox_item_type_0 = []
                _bbox_item_type_0 = data
                for bbox_item_type_0_item_data in _bbox_item_type_0:

                    def _parse_bbox_item_type_0_item(data: object) -> float | int:
                        return cast(float | int, data)

                    bbox_item_type_0_item = _parse_bbox_item_type_0_item(
                        bbox_item_type_0_item_data
                    )

                    bbox_item_type_0.append(bbox_item_type_0_item)

                return bbox_item_type_0

            bbox_item = _parse_bbox_item(bbox_item_data)

            bbox.append(bbox_item)

        spatial_extent = cls(
            bbox=bbox,
        )

        spatial_extent.additional_properties = d
        return spatial_extent

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

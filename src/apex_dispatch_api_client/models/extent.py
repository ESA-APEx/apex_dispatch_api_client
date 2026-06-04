from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.spatial_extent import SpatialExtent
    from ..models.time_interval import TimeInterval


T = TypeVar("T", bound="Extent")


@_attrs_define
class Extent:
    """https://github.com/radiantearth/stac-spec/blob/v1.0.0/collection-spec/collection-spec.md#extent-object

    Attributes:
        spatial (SpatialExtent): https://github.com/radiantearth/stac-spec/blob/v1.0.0/collection-spec/collection-
            spec.md#spatial-extent-object
        temporal (TimeInterval): https://github.com/radiantearth/stac-spec/blob/v1.0.0/collection-spec/collection-
            spec.md#temporal-extent-object
    """

    spatial: SpatialExtent
    temporal: TimeInterval
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spatial = self.spatial.to_dict()

        temporal = self.temporal.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spatial": spatial,
                "temporal": temporal,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spatial_extent import SpatialExtent
        from ..models.time_interval import TimeInterval

        d = dict(src_dict)
        spatial = SpatialExtent.from_dict(d.pop("spatial"))

        temporal = TimeInterval.from_dict(d.pop("temporal"))

        extent = cls(
            spatial=spatial,
            temporal=temporal,
        )

        extent.additional_properties = d
        return extent

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

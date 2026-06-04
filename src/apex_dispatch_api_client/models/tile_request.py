from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.grid_type_enum import GridTypeEnum

if TYPE_CHECKING:
    from ..models.polygon import Polygon


T = TypeVar("T", bound="TileRequest")


@_attrs_define
class TileRequest:
    """
    Attributes:
        aoi (Polygon): Polygon Model
        grid (GridTypeEnum):
    """

    aoi: Polygon
    grid: GridTypeEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aoi = self.aoi.to_dict()

        grid = self.grid.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aoi": aoi,
                "grid": grid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.polygon import Polygon

        d = dict(src_dict)
        aoi = Polygon.from_dict(d.pop("aoi"))

        grid = GridTypeEnum(d.pop("grid"))

        tile_request = cls(
            aoi=aoi,
            grid=grid,
        )

        tile_request.additional_properties = d
        return tile_request

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

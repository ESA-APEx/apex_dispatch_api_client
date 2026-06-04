from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="TimeInterval")


@_attrs_define
class TimeInterval:
    """https://github.com/radiantearth/stac-spec/blob/v1.0.0/collection-spec/collection-spec.md#temporal-extent-object

    Attributes:
        interval (list[list[datetime.datetime | None]]):
    """

    interval: list[list[datetime.datetime | None]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interval = []
        for interval_item_data in self.interval:
            interval_item = []
            for interval_item_item_data in interval_item_data:
                interval_item_item: None | str
                if isinstance(interval_item_item_data, datetime.datetime):
                    interval_item_item = interval_item_item_data.isoformat()
                else:
                    interval_item_item = interval_item_item_data
                interval_item.append(interval_item_item)

            interval.append(interval_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interval": interval,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interval = []
        _interval = d.pop("interval")
        for interval_item_data in _interval:
            interval_item = []
            _interval_item = interval_item_data
            for interval_item_item_data in _interval_item:

                def _parse_interval_item_item(data: object) -> datetime.datetime | None:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, str):
                            raise TypeError()
                        interval_item_item_type_0 = isoparse(data)

                        return interval_item_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(datetime.datetime | None, data)

                interval_item_item = _parse_interval_item_item(interval_item_item_data)

                interval_item.append(interval_item_item)

            interval.append(interval_item)

        time_interval = cls(
            interval=interval,
        )

        time_interval.additional_properties = d
        return time_interval

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

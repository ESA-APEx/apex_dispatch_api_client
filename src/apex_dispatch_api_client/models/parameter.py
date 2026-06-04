from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.param_type_enum import ParamTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Parameter")


@_attrs_define
class Parameter:
    """
    Attributes:
        name (str): Name of the parameter
        type_ (ParamTypeEnum):
        optional (bool): Indicates whether the parameter is optional
        description (str): Description of the parameter
        default (Any | Unset): Default value of the parameter, if any
        options (list[Any] | Unset): List of valid options for the parameter, if applicable
    """

    name: str
    type_: ParamTypeEnum
    optional: bool
    description: str
    default: Any | Unset = UNSET
    options: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        optional = self.optional

        description = self.description

        default = self.default

        options: list[Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "optional": optional,
                "description": description,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = ParamTypeEnum(d.pop("type"))

        optional = d.pop("optional")

        description = d.pop("description")

        default = d.pop("default", UNSET)

        options = cast(list[Any], d.pop("options", UNSET))

        parameter = cls(
            name=name,
            type_=type_,
            optional=optional,
            description=description,
            default=default,
            options=options,
        )

        parameter.additional_properties = d
        return parameter

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

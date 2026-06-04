from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceDetails")


@_attrs_define
class ServiceDetails:
    """
    Attributes:
        endpoint (str): URL to the endpoint where the service is hosted. For openEO, this is the openEO backend. For OGC
            API Processes, this field should include the base URL of the platform API
        application (str): Path to the application that needs to be executed. For openEO this is referring to the public
            URL of the UDP (JSON) to execute. For OGC API Processes, this field should include the URL path pointing to the
            hosted service.
        namespace (None | str | Unset): Namespace under the endpoint where the service is hosted.For openEO, this field
            is not set.For OGC API Processes, this field should include the namespace IDrepresenting the service deployment
    """

    endpoint: str
    application: str
    namespace: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint

        application = self.application

        namespace: None | str | Unset
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
                "application": application,
            }
        )
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        endpoint = d.pop("endpoint")

        application = d.pop("application")

        def _parse_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

        service_details = cls(
            endpoint=endpoint,
            application=application,
            namespace=namespace,
        )

        service_details.additional_properties = d
        return service_details

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

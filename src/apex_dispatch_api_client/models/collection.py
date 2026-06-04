from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    Literal,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection_assets_type_0 import CollectionAssetsType0
    from ..models.collection_summaries_type_0 import CollectionSummariesType0
    from ..models.extent import Extent
    from ..models.link import Link
    from ..models.provider import Provider


T = TypeVar("T", bound="Collection")


@_attrs_define
class Collection:
    """https://github.com/radiantearth/stac-spec/blob/v1.0.0/collection-spec/collection-spec.md

    Attributes:
        id (str):
        description (str):
        links (list[Link]):
        type_ (Literal['Collection']):
        license_ (str):
        extent (Extent): https://github.com/radiantearth/stac-spec/blob/v1.0.0/collection-spec/collection-
            spec.md#extent-object
        stac_version (str | Unset):  Default: '1.0.0'.
        stac_extensions (list[str] | None | Unset):
        title (None | str | Unset):
        assets (CollectionAssetsType0 | None | Unset):
        keywords (list[str] | None | Unset):
        providers (list[Provider] | None | Unset):
        summaries (CollectionSummariesType0 | None | Unset):
    """

    id: str
    description: str
    links: list[Link]
    type_: Literal["Collection"]
    license_: str
    extent: Extent
    stac_version: str | Unset = "1.0.0"
    stac_extensions: list[str] | None | Unset = UNSET
    title: None | str | Unset = UNSET
    assets: CollectionAssetsType0 | None | Unset = UNSET
    keywords: list[str] | None | Unset = UNSET
    providers: list[Provider] | None | Unset = UNSET
    summaries: CollectionSummariesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.collection_assets_type_0 import CollectionAssetsType0
        from ..models.collection_summaries_type_0 import CollectionSummariesType0

        id = self.id

        description = self.description

        links = []
        for componentsschemas_links_item_data in self.links:
            componentsschemas_links_item = componentsschemas_links_item_data.to_dict()
            links.append(componentsschemas_links_item)

        type_ = self.type_

        license_ = self.license_

        extent = self.extent.to_dict()

        stac_version = self.stac_version

        stac_extensions: list[str] | None | Unset
        if isinstance(self.stac_extensions, Unset):
            stac_extensions = UNSET
        elif isinstance(self.stac_extensions, list):
            stac_extensions = self.stac_extensions

        else:
            stac_extensions = self.stac_extensions

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        assets: dict[str, Any] | None | Unset
        if isinstance(self.assets, Unset):
            assets = UNSET
        elif isinstance(self.assets, CollectionAssetsType0):
            assets = self.assets.to_dict()
        else:
            assets = self.assets

        keywords: list[str] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, list):
            keywords = self.keywords

        else:
            keywords = self.keywords

        providers: list[dict[str, Any]] | None | Unset
        if isinstance(self.providers, Unset):
            providers = UNSET
        elif isinstance(self.providers, list):
            providers = []
            for providers_type_0_item_data in self.providers:
                providers_type_0_item = providers_type_0_item_data.to_dict()
                providers.append(providers_type_0_item)

        else:
            providers = self.providers

        summaries: dict[str, Any] | None | Unset
        if isinstance(self.summaries, Unset):
            summaries = UNSET
        elif isinstance(self.summaries, CollectionSummariesType0):
            summaries = self.summaries.to_dict()
        else:
            summaries = self.summaries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "description": description,
                "links": links,
                "type": type_,
                "license": license_,
                "extent": extent,
            }
        )
        if stac_version is not UNSET:
            field_dict["stac_version"] = stac_version
        if stac_extensions is not UNSET:
            field_dict["stac_extensions"] = stac_extensions
        if title is not UNSET:
            field_dict["title"] = title
        if assets is not UNSET:
            field_dict["assets"] = assets
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if providers is not UNSET:
            field_dict["providers"] = providers
        if summaries is not UNSET:
            field_dict["summaries"] = summaries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection_assets_type_0 import CollectionAssetsType0
        from ..models.collection_summaries_type_0 import CollectionSummariesType0
        from ..models.extent import Extent
        from ..models.link import Link
        from ..models.provider import Provider

        d = dict(src_dict)
        id = d.pop("id")

        description = d.pop("description")

        links = []
        _links = d.pop("links")
        for componentsschemas_links_item_data in _links:
            componentsschemas_links_item = Link.from_dict(
                componentsschemas_links_item_data
            )

            links.append(componentsschemas_links_item)

        type_ = cast(Literal["Collection"], d.pop("type"))
        if type_ != "Collection":
            raise ValueError(f"type must match const 'Collection', got '{type_}'")

        license_ = d.pop("license")

        extent = Extent.from_dict(d.pop("extent"))

        stac_version = d.pop("stac_version", UNSET)

        def _parse_stac_extensions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stac_extensions_type_0 = cast(list[str], data)

                return stac_extensions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        stac_extensions = _parse_stac_extensions(d.pop("stac_extensions", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_assets(data: object) -> CollectionAssetsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                assets_type_0 = CollectionAssetsType0.from_dict(data)

                return assets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CollectionAssetsType0 | None | Unset, data)

        assets = _parse_assets(d.pop("assets", UNSET))

        def _parse_keywords(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keywords_type_0 = cast(list[str], data)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_providers(data: object) -> list[Provider] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                providers_type_0 = []
                _providers_type_0 = data
                for providers_type_0_item_data in _providers_type_0:
                    providers_type_0_item = Provider.from_dict(
                        providers_type_0_item_data
                    )

                    providers_type_0.append(providers_type_0_item)

                return providers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Provider] | None | Unset, data)

        providers = _parse_providers(d.pop("providers", UNSET))

        def _parse_summaries(data: object) -> CollectionSummariesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                summaries_type_0 = CollectionSummariesType0.from_dict(data)

                return summaries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CollectionSummariesType0 | None | Unset, data)

        summaries = _parse_summaries(d.pop("summaries", UNSET))

        collection = cls(
            id=id,
            description=description,
            links=links,
            type_=type_,
            license_=license_,
            extent=extent,
            stac_version=stac_version,
            stac_extensions=stac_extensions,
            title=title,
            assets=assets,
            keywords=keywords,
            providers=providers,
            summaries=summaries,
        )

        collection.additional_properties = d
        return collection

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

from enum import Enum


class OutputFormatEnum(str, Enum):
    GEOJSON = "geojson"
    GTIFF = "gtiff"
    JSON = "json"
    NETCDF = "netcdf"

    def __str__(self) -> str:
        return str(self.value)

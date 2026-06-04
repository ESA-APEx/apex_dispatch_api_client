from enum import Enum


class ProcessTypeEnum(str, Enum):
    OGC_API_PROCESS = "ogc_api_process"
    OPENEO = "openeo"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class ParamTypeEnum(str, Enum):
    ARRAY_STRING = "array-string"
    BOOLEAN = "boolean"
    BOUNDING_BOX = "bounding-box"
    DATETIME = "datetime"
    DATE_INTERVAL = "date-interval"
    DOUBLE = "double"
    INTEGER = "integer"
    POLYGON = "polygon"
    STRING = "string"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class GridTypeEnum(str, Enum):
    VALUE_0 = "20x20km"
    VALUE_1 = "250x250km"

    def __str__(self) -> str:
        return str(self.value)

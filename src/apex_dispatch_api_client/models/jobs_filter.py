from enum import Enum


class JobsFilter(str, Enum):
    PROCESSING = "processing"
    UPSCALING = "upscaling"

    def __str__(self) -> str:
        return str(self.value)

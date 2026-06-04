from enum import Enum


class ProcessingStatusEnum(str, Enum):
    CANCELED = "canceled"
    CREATED = "created"
    FAILED = "failed"
    FINISHED = "finished"
    QUEUED = "queued"
    RUNNING = "running"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)

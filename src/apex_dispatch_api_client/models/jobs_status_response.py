from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.processing_job_summary import ProcessingJobSummary
    from ..models.upscaling_task_summary import UpscalingTaskSummary


T = TypeVar("T", bound="JobsStatusResponse")


@_attrs_define
class JobsStatusResponse:
    """
    Attributes:
        upscaling_tasks (list[UpscalingTaskSummary]): List of upscaling tasks that are available for the user
        processing_jobs (list[ProcessingJobSummary]): List of processing jobs that are available for the user
    """

    upscaling_tasks: list[UpscalingTaskSummary]
    processing_jobs: list[ProcessingJobSummary]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upscaling_tasks = []
        for upscaling_tasks_item_data in self.upscaling_tasks:
            upscaling_tasks_item = upscaling_tasks_item_data.to_dict()
            upscaling_tasks.append(upscaling_tasks_item)

        processing_jobs = []
        for processing_jobs_item_data in self.processing_jobs:
            processing_jobs_item = processing_jobs_item_data.to_dict()
            processing_jobs.append(processing_jobs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "upscaling_tasks": upscaling_tasks,
                "processing_jobs": processing_jobs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.processing_job_summary import ProcessingJobSummary
        from ..models.upscaling_task_summary import UpscalingTaskSummary

        d = dict(src_dict)
        upscaling_tasks = []
        _upscaling_tasks = d.pop("upscaling_tasks")
        for upscaling_tasks_item_data in _upscaling_tasks:
            upscaling_tasks_item = UpscalingTaskSummary.from_dict(
                upscaling_tasks_item_data
            )

            upscaling_tasks.append(upscaling_tasks_item)

        processing_jobs = []
        _processing_jobs = d.pop("processing_jobs")
        for processing_jobs_item_data in _processing_jobs:
            processing_jobs_item = ProcessingJobSummary.from_dict(
                processing_jobs_item_data
            )

            processing_jobs.append(processing_jobs_item)

        jobs_status_response = cls(
            upscaling_tasks=upscaling_tasks,
            processing_jobs=processing_jobs,
        )

        jobs_status_response.additional_properties = d
        return jobs_status_response

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

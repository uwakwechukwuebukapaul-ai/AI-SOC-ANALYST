"""
Sentinel DNA Runtime Metrics

Runtime observability and execution statistics.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
import time


@dataclass
class RuntimeMetrics:
    """
    Tracks runtime execution performance.
    """

    total_executions: int = 0

    successful_executions: int = 0

    failed_executions: int = 0

    total_execution_time: float = 0.0

    active_tasks: int = 0

    metadata: dict[str, Any] = field(
        default_factory=dict
    )


    def start_task(self) -> float:
        """
        Mark task start time.
        """

        self.active_tasks += 1

        return time.perf_counter()



    def record_success(
        self,
        duration: float | None = None,
    ) -> None:
        """
        Record successful execution.
        """

        self.total_executions += 1

        self.successful_executions += 1

        self.active_tasks = max(
            0,
            self.active_tasks - 1
        )


        if duration:

            self.total_execution_time += duration



    def record_failure(
        self,
        duration: float | None = None,
    ) -> None:
        """
        Record failed execution.
        """

        self.total_executions += 1

        self.failed_executions += 1

        self.active_tasks = max(
            0,
            self.active_tasks - 1
        )


        if duration:

            self.total_execution_time += duration



    @property
    def success_rate(self) -> float:
        """
        Successful execution percentage.
        """

        if self.total_executions == 0:

            return 0.0


        return (
            self.successful_executions
            /
            self.total_executions
        ) * 100



    @property
    def failure_rate(self) -> float:
        """
        Failure percentage.
        """

        if self.total_executions == 0:

            return 0.0


        return (
            self.failed_executions
            /
            self.total_executions
        ) * 100



    @property
    def average_execution_time(self) -> float:
        """
        Average task duration.
        """

        if self.total_executions == 0:

            return 0.0


        return (
            self.total_execution_time
            /
            self.total_executions
        )



    def to_dict(self) -> dict[str, Any]:
        """
        Export metrics.
        """

        return {
            "total_executions":
                self.total_executions,

            "successful_executions":
                self.successful_executions,

            "failed_executions":
                self.failed_executions,

            "success_rate":
                self.success_rate,

            "failure_rate":
                self.failure_rate,

            "average_execution_time":
                self.average_execution_time,

            "active_tasks":
                self.active_tasks,

            "metadata":
                self.metadata,
        }
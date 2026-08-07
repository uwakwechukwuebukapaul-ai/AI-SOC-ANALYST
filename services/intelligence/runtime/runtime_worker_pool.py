"""
Sentinel DNA Runtime Worker Pool

Enterprise execution worker manager.

Responsibilities:

- manage workers
- submit tasks
- execute runtime jobs
- track worker activity
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .task import Task

from .runtime_task_executor import (
    RuntimeTaskExecutor,
)


@dataclass
class RuntimeWorkerPool:
    """
    Runtime worker manager.
    """

    executor: RuntimeTaskExecutor = field(
        default_factory=RuntimeTaskExecutor
    )

    workers: int = 0

    completed: int = 0



    def start_workers(
        self,
        count: int,
    ) -> None:
        """
        Start worker instances.
        """

        self.workers = count



    def submit(
        self,
        task: Task,
    ) -> Any:
        """
        Submit task for execution.
        """

        if self.workers <= 0:
            return None


        result = self.executor.execute(
            task
        )


        if result is not None:
            self.completed += 1


        return result



    def stop_workers(self) -> None:
        """
        Stop all workers.
        """

        self.workers = 0



    def active_workers(self) -> int:
        """
        Return active workers.
        """

        return self.workers



    def clear(self) -> None:
        """
        Reset worker pool.
        """

        self.workers = 0

        self.completed = 0



    def status(self) -> dict[str, Any]:
        """
        Worker status.
        """

        return {
            "workers":
                self.workers,

            "completed":
                self.completed,

            "executor":
                self.executor.status(),
        }
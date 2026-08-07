"""
Sentinel DNA Runtime Scheduler Manager

Enterprise scheduling control layer.

Responsibilities:

- Task scheduling management
- Priority execution
- Queue inspection
- Scheduler lifecycle control
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .scheduler import Scheduler
from .task import Task


@dataclass
class RuntimeSchedulerManager:
    """
    Scheduler orchestration manager.
    """

    scheduler: Scheduler = field(
        default_factory=Scheduler
    )

    running: bool = False


    def start(self) -> None:
        """
        Enable scheduler.
        """

        self.running = True



    def stop(self) -> None:
        """
        Disable scheduler.
        """

        self.running = False



    def schedule(
        self,
        task: Task,
    ) -> None:
        """
        Add task to scheduler.
        """

        self.scheduler.schedule(
            task
        )



    def next_task(self) -> Task | None:
        """
        Retrieve next task.
        """

        if not self.running:
            return None

        return self.scheduler.next_task()



    def remove(
        self,
        task: Task,
    ) -> bool:
        """
        Remove scheduled task.
        """

        return self.scheduler.remove(
            task
        )



    def size(self) -> int:
        """
        Scheduler queue size.
        """

        return self.scheduler.size()



    def clear(self) -> None:
        """
        Clear scheduler.
        """

        self.scheduler.clear()



    def status(self) -> dict[str, Any]:
        """
        Scheduler status.
        """

        return {
            "running":
                self.running,

            "queue_size":
                self.scheduler.size(),
        }
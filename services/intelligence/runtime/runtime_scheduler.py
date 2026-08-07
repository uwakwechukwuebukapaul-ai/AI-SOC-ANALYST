"""
Sentinel DNA Runtime Scheduler

Enterprise task scheduling layer.

Responsibilities:

- register tasks
- prioritize execution
- dispatch queued tasks
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeScheduler:
    """
    Runtime task scheduler.
    """

    tasks: list[dict[str, Any]] = field(
        default_factory=list
    )


    executed: int = 0



    def schedule(
        self,
        task_id: str,
        priority: int = 0,
        payload: dict[str, Any] | None = None,
    ) -> None:
        """
        Add task to scheduler.
        """

        self.tasks.append(
            {
                "id":
                    task_id,

                "priority":
                    priority,

                "payload":
                    payload or {},
            }
        )


        self.tasks.sort(
            key=lambda item: item["priority"],
            reverse=True,
        )



    def next(
        self,
    ) -> dict[str, Any] | None:
        """
        Retrieve next task.
        """

        if not self.tasks:
            return None


        return self.tasks.pop(
            0
        )



    def complete(
        self,
    ) -> None:
        """
        Mark task completed.
        """

        self.executed += 1



    def pending(self) -> int:
        """
        Return queued tasks.
        """

        return len(
            self.tasks
        )



    def count(self) -> int:
        """
        Return executed tasks.
        """

        return self.executed



    def clear(self) -> None:
        """
        Reset scheduler.
        """

        self.tasks.clear()

        self.executed = 0



    def status(self) -> dict[str, Any]:
        """
        Scheduler status.
        """

        return {
            "pending":
                self.pending(),

            "executed":
                self.executed,
        }
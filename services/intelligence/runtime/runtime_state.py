"""
Sentinel DNA Runtime State Manager

Tracks runtime lifecycle and execution state.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class RuntimeState:
    """
    Runtime state container.
    """

    status: str = "initialized"

    workers: dict[str, str] = field(
        default_factory=dict
    )

    tasks: dict[str, str] = field(
        default_factory=dict
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


    def update_status(
        self,
        status: str,
    ) -> None:
        """
        Update runtime status.
        """

        self.status = status
        self._touch()



    def set_worker_state(
        self,
        worker_id: str,
        state: str,
    ) -> None:
        """
        Update worker state.
        """

        self.workers[worker_id] = state
        self._touch()



    def set_task_state(
        self,
        task_id: str,
        state: str,
    ) -> None:
        """
        Update task state.
        """

        self.tasks[task_id] = state
        self._touch()



    def get_worker_state(
        self,
        worker_id: str,
        default=None,
    ):

        return self.workers.get(
            worker_id,
            default,
        )



    def get_task_state(
        self,
        task_id: str,
        default=None,
    ):

        return self.tasks.get(
            task_id,
            default,
        )



    def _touch(self):

        self.updated_at = datetime.now(
            timezone.utc
        )



    def to_dict(self) -> dict[str, Any]:

        return {
            "status": self.status,
            "workers": self.workers,
            "tasks": self.tasks,
            "metadata": self.metadata,
            "updated_at":
                self.updated_at.isoformat(),
        }
"""
Sentinel DNA Runtime State

Central runtime state tracking layer.

Responsible for:

- Runtime lifecycle state
- Worker state tracking
- Execution counters
- Health state
- Runtime snapshots
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from datetime import datetime, timezone


@dataclass
class RuntimeState:
    """
    Enterprise runtime state manager.
    """

    status: str = "initialized"

    workers: dict[str, str] = field(
        default_factory=dict
    )

    executions: int = 0

    successful: int = 0

    failed: int = 0

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )


    def start(self) -> None:
        """
        Mark runtime active.
        """

        self.status = "running"



    def stop(self) -> None:
        """
        Mark runtime stopped.
        """

        self.status = "stopped"



    def register_worker(
        self,
        worker_id: str,
        state: str = "idle",
    ) -> None:
        """
        Register worker state.
        """

        self.workers[worker_id] = state



    def update_worker(
        self,
        worker_id: str,
        state: str,
    ) -> None:
        """
        Update worker state.
        """

        self.workers[worker_id] = state



    def record_success(self) -> None:
        """
        Record successful execution.
        """

        self.executions += 1
        self.successful += 1



    def record_failure(self) -> None:
        """
        Record failed execution.
        """

        self.executions += 1
        self.failed += 1



    def snapshot(self) -> dict[str, Any]:
        """
        Runtime state snapshot.
        """

        return {
            "status": self.status,
            "workers": self.workers,
            "executions": self.executions,
            "successful": self.successful,
            "failed": self.failed,
            "metadata": self.metadata,
        }



    def to_dict(self) -> dict[str, Any]:
        """
        Serialize runtime state.
        """

        return self.snapshot()
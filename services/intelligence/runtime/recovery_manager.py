"""
Sentinel DNA Runtime Recovery Manager

Handles runtime recovery,
failure tracking, and state restoration.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_store import RuntimeStore


@dataclass
class RecoveryManager:
    """
    Runtime failure recovery coordinator.
    """

    store: RuntimeStore = field(
        default_factory=RuntimeStore
    )

    failures: dict[str, dict[str, Any]] = field(
        default_factory=dict
    )

    recoveries: int = 0


    def record_failure(
        self,
        task_id: str,
        error: str,
    ) -> None:
        """
        Record failed execution.
        """

        self.failures[task_id] = {
            "error": error,
            "recovered": False,
        }



    def has_failure(
        self,
        task_id: str,
    ) -> bool:
        """
        Check failure existence.
        """

        return task_id in self.failures



    def create_checkpoint(
        self,
        name: str,
    ) -> dict:
        """
        Create recovery checkpoint.
        """

        return self.store.snapshot(
            name
        )



    def recover(
        self,
        checkpoint: str,
    ) -> dict:
        """
        Restore runtime state.
        """

        state = self.store.restore(
            checkpoint
        )

        self.recoveries += 1

        return state



    def mark_recovered(
        self,
        task_id: str,
    ) -> None:
        """
        Mark task recovery complete.
        """

        if task_id in self.failures:

            self.failures[task_id][
                "recovered"
            ] = True



    def clear_failure(
        self,
        task_id: str,
    ) -> None:
        """
        Remove failure record.
        """

        self.failures.pop(
            task_id,
            None,
        )



    def status(self) -> dict:
        """
        Runtime recovery status.
        """

        return {
            "failures":
                self.failures,

            "recoveries":
                self.recoveries,

            "active_failures":
                len(self.failures),
        }
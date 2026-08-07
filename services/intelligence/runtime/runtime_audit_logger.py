"""
Sentinel DNA Runtime Audit Logger

Enterprise audit tracking layer.

Responsibilities:

- record runtime actions
- maintain audit history
- provide compliance visibility
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any



@dataclass
class RuntimeAuditLogger:
    """
    Runtime audit recorder.
    """

    records: list[dict[str, Any]] = field(
        default_factory=list
    )



    def record(
        self,
        actor: str,
        action: str,
        details: dict[str, Any] | None = None,
    ) -> None:
        """
        Record runtime action.
        """

        self.records.append(
            {
                "actor":
                    actor,

                "action":
                    action,

                "details":
                    details or {},

                "timestamp":
                    datetime.now(
                        timezone.utc
                    ).isoformat(),
            }
        )



    def latest(
        self,
    ) -> dict[str, Any] | None:
        """
        Return latest audit record.
        """

        if not self.records:
            return None


        return self.records[-1]



    def count(self) -> int:
        """
        Return audit count.
        """

        return len(
            self.records
        )



    def clear(self) -> None:
        """
        Reset audit history.
        """

        self.records.clear()



    def status(self) -> dict[str, Any]:
        """
        Audit status.
        """

        return {
            "records":
                self.count(),
        }
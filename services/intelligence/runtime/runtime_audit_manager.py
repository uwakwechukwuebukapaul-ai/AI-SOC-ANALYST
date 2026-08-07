"""
Sentinel DNA Runtime Audit Manager
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class RuntimeAuditManager:
    """
    Runtime audit controller.
    """

    records: list[dict[str, Any]] = field(default_factory=list)

    def record(
        self,
        actor: str,
        component: str,
        action: str,
        details: dict[str, Any] | None = None,
    ) -> None:
        self.records.append(
            {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "actor": actor,
                "component": component,
                "action": action,
                "details": details or {},
            }
        )

    def by_actor(
        self,
        actor: str,
    ) -> list[dict[str, Any]]:
        return [
            record
            for record in self.records
            if record["actor"] == actor
        ]

    def by_component(
        self,
        component: str,
    ) -> list[dict[str, Any]]:
        return [
            record
            for record in self.records
            if record["component"] == component
        ]

    def latest(self) -> dict[str, Any] | None:
        if not self.records:
            return None
        return self.records[-1]

    def count(self) -> int:
        return len(self.records)

    def clear(self) -> None:
        self.records.clear()

    def status(self) -> dict[str, Any]:
        return {
            "count": self.count(),
            "latest": self.latest(),
        }
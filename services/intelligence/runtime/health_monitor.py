"""
Sentinel DNA Runtime Health Monitor

Runtime health tracking and diagnostics layer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class RuntimeHealthMonitor:
    """
    Tracks runtime availability and worker health.
    """

    healthy: bool = True

    last_heartbeat: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    failures: int = 0

    checks: int = 0

    metadata: dict[str, Any] = field(
        default_factory=dict
    )


    def heartbeat(self) -> None:
        """
        Update runtime heartbeat.
        """

        self.last_heartbeat = datetime.now(timezone.utc)


    def check(self) -> bool:
        """
        Perform health check.
        """

        self.checks += 1

        return self.healthy


    def mark_failure(self) -> None:
        """
        Record runtime failure.
        """

        self.failures += 1

        self.healthy = False


    def recover(self) -> None:
        """
        Recover runtime health.
        """

        self.healthy = True

        self.heartbeat()


    def status(self) -> dict[str, Any]:
        """
        Export health state.
        """

        return {
            "healthy": self.healthy,
            "failures": self.failures,
            "checks": self.checks,
            "last_heartbeat": (
                self.last_heartbeat.isoformat()
            ),
            "metadata": self.metadata,
        }
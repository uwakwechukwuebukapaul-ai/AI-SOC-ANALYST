"""
Sentinel DNA Runtime Health Monitor

Tracks runtime component health.

Responsibilities:

- register components
- update health status
- evaluate overall runtime health
- expose health metrics
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeHealthMonitor:
    """
    Runtime health tracking service.
    """

    components: dict[str, dict[str, Any]] = field(
        default_factory=dict
    )

    def register(
        self,
        name: str,
    ) -> None:
        """
        Register runtime component.
        """

        self.components[name] = {
            "status": "healthy",
        }

    def update(
        self,
        name: str,
        status: str,
    ) -> None:
        """
        Update component health.
        """

        if name not in self.components:
            self.register(name)

        self.components[name]["status"] = status

    def get(
        self,
        name: str,
    ) -> dict[str, Any] | None:
        """
        Retrieve component health.
        """

        return self.components.get(
            name
        )

    def healthy(self) -> bool:
        """
        Determine overall runtime health.
        """

        return all(
            component["status"] == "healthy"
            for component in self.components.values()
        )

    def check(self) -> dict[str, Any]:
        """
        Compatibility health check.

        Used by RuntimeControlPlane.
        """

        return {
            "healthy": self.healthy(),
            "components": dict(self.components),
            "count": self.count(),
        }

    def count(self) -> int:
        """
        Return component count.
        """

        return len(
            self.components
        )

    def clear(self) -> None:
        """
        Remove all health records.
        """

        self.components.clear()

    def status(self) -> dict[str, Any]:
        """
        Return health summary.
        """

        return self.check()
"""
Sentinel DNA Runtime Health Monitor

Enterprise runtime reliability layer.

Responsibilities:

- monitor component health
- record failures
- expose readiness status
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any



@dataclass
class RuntimeHealthMonitor:
    """
    Runtime health controller.
    """

    components: dict[str, str] = field(
        default_factory=dict
    )

    failures: list[dict[str, Any]] = field(
        default_factory=list
    )



    def register(
        self,
        name: str,
        status: str = "healthy",
    ) -> None:
        """
        Register component health.
        """

        self.components[name] = status



    def update(
        self,
        name: str,
        status: str,
    ) -> None:
        """
        Update component status.
        """

        self.components[name] = status



    def healthy(
        self,
        name: str,
    ) -> bool:
        """
        Check component health.
        """

        return (
            self.components.get(name)
            ==
            "healthy"
        )



    def record_failure(
        self,
        component: str,
        error: str,
    ) -> None:
        """
        Record runtime failure.
        """

        self.failures.append(
            {
                "component":
                    component,

                "error":
                    error,
            }
        )



    def ready(
        self,
    ) -> bool:
        """
        Check platform readiness.
        """

        return all(
            status == "healthy"
            for status in self.components.values()
        )



    def failure_count(self) -> int:
        """
        Return failure count.
        """

        return len(
            self.failures
        )



    def clear(self) -> None:
        """
        Reset health state.
        """

        self.components.clear()

        self.failures.clear()



    def status(self) -> dict[str, Any]:
        """
        Health status.
        """

        return {
            "components":
                self.components,

            "failures":
                self.failures,

            "ready":
                self.ready(),
        }
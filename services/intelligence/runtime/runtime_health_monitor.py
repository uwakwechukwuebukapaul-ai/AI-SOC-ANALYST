"""
Sentinel DNA Runtime Health Monitor

Enterprise runtime observability layer.

Responsibilities:

- monitor runtime health
- collect runtime metrics
- expose operational status
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_intelligence_runtime import (
    RuntimeIntelligenceRuntime,
)


@dataclass
class RuntimeHealthMonitor:
    """
    Runtime monitoring service.
    """

    runtime: RuntimeIntelligenceRuntime = field(
        default_factory=RuntimeIntelligenceRuntime
    )

    checks: int = 0


    def healthy(self) -> bool:
        """
        Check runtime health.
        """

        self.checks += 1

        return self.runtime.running



    def check(self) -> dict[str, Any]:
        """
        Return health snapshot.
        """

        self.checks += 1

        health = self.runtime.health()

        return {
            "healthy":
                self.runtime.running,

            "checks":
                self.checks,

            "runtime":
                health,
        }



    def metrics(self) -> dict[str, Any]:
        """
        Runtime metrics.
        """

        return {
            "health_checks":
                self.checks,

            "running":
                self.runtime.running,
        }



    def reset(self) -> None:
        """
        Reset monitoring counters.
        """

        self.checks = 0
"""
Sentinel DNA Runtime Metrics Collector

Enterprise runtime metrics layer.

Responsibilities:

- collect execution metrics
- track runtime events
- expose analytics data
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeMetricsCollector:
    """
    Runtime metrics collector.
    """

    executions: int = 0

    failures: int = 0

    events: list[dict[str, Any]] = field(
        default_factory=list
    )


    def record_execution(
        self,
        capability: str,
    ) -> None:
        """
        Record successful execution.
        """

        self.executions += 1

        self.events.append(
            {
                "type":
                    "execution",

                "capability":
                    capability,
            }
        )



    def record_failure(
        self,
        capability: str,
        error: str,
    ) -> None:
        """
        Record failed execution.
        """

        self.failures += 1

        self.events.append(
            {
                "type":
                    "failure",

                "capability":
                    capability,

                "error":
                    error,
            }
        )



    def total_events(self) -> int:
        """
        Return event count.
        """

        return len(
            self.events
        )



    def clear(self) -> None:
        """
        Reset metrics.
        """

        self.executions = 0

        self.failures = 0

        self.events.clear()



    def status(self) -> dict[str, Any]:
        """
        Metrics snapshot.
        """

        return {
            "executions":
                self.executions,

            "failures":
                self.failures,

            "events":
                self.total_events(),
        }
"""
Sentinel DNA Runtime Metrics Collector
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeMetricsCollector:
    """
    Collects runtime execution metrics.
    """

    metrics: dict[str, int] = field(default_factory=dict)

    # --------------------------------------------------
    # Enterprise Runtime API
    # --------------------------------------------------

    def record_execution(
        self,
        capability: str,
    ) -> None:
        self.increment(capability)

    def record_failure(
        self,
        capability: str,
    ) -> None:
        self.increment(f"{capability}:failed")

    @property
    def executions(self) -> int:
        return sum(
            value
            for key, value in self.metrics.items()
            if not key.endswith(":failed")
        )

    @property
    def failures(self) -> int:
        return sum(
            value
            for key, value in self.metrics.items()
            if key.endswith(":failed")
        )

    # --------------------------------------------------
    # Legacy Compatibility API
    # --------------------------------------------------

    def set(
        self,
        key: str,
        value: int,
    ) -> None:
        self.metrics[key] = value

    def increment(
        self,
        key: str,
        amount: int = 1,
    ) -> None:
        self.metrics[key] = (
            self.metrics.get(key, 0)
            + amount
        )

    def exists(
        self,
        key: str,
    ) -> bool:
        return key in self.metrics

    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        return self.metrics.get(
            key,
            default,
        )

    def remove(
        self,
        key: str,
    ) -> None:
        self.metrics.pop(
            key,
            None,
        )

    def clear(
        self,
    ) -> None:
        self.metrics.clear()

    def count(
        self,
    ) -> int:
        return len(self.metrics)

    def status(
        self,
    ) -> dict[str, Any]:
        return {
            "count": self.count(),
            "executions": self.executions,
            "failures": self.failures,
            "metrics": dict(self.metrics),
        }
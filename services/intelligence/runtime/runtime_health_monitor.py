"""
Sentinel DNA Runtime Health Monitor
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeState:
    """
    Runtime state tracker.
    """

    running: bool = False

    def start(self) -> None:
        self.running = True

    def stop(self) -> None:
        self.running = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "running": self.running,
        }


@dataclass
class RuntimeHealthMonitor:
    """
    Enterprise Runtime Health Monitor.
    """

    components: dict[str, bool] = field(default_factory=dict)

    # Backward-compatible runtime state
    runtime: RuntimeState = field(default_factory=RuntimeState)

    def register(
        self,
        component: str,
    ) -> None:
        """
        Register a component.
        """

        self.components[component] = True

    def unregister(
        self,
        component: str,
    ) -> None:
        """
        Remove a component.
        """

        self.components.pop(component, None)

    def set_health(
        self,
        component: str,
        healthy: bool,
    ) -> None:
        """
        Update component health.
        """

        self.components[component] = healthy

    def is_healthy(
        self,
        component: str,
    ) -> bool:
        """
        Check component health.
        """

        return self.components.get(component, False)

    def check(self) -> dict[str, Any]:
        """
        Legacy compatibility API.
        """

        healthy = all(self.components.values()) if self.components else True

        return {
            "healthy": healthy,
            "components": dict(self.components),
            "runtime": self.runtime.to_dict(),
        }

    def clear(self) -> None:
        """
        Clear all registered components.
        """

        self.components.clear()

    def count(self) -> int:
        """
        Number of monitored components.
        """

        return len(self.components)

    def status(self) -> dict[str, Any]:
        """
        Enterprise runtime status.
        """

        return {
            "count": self.count(),
            "healthy": all(self.components.values()) if self.components else True,
            "components": dict(self.components),
            "runtime": self.runtime.to_dict(),
        }
"""
Sentinel DNA Runtime State

Tracks runtime lifecycle, components,
metadata and execution health.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeState:
    """
    Runtime lifecycle state model.
    """

    status: str = "stopped"

    successful: int = 0

    failed: int = 0

    def start(self) -> None:
        """
        Start runtime.
        """

        self.status = "running"

    def stop(self) -> None:
        """
        Stop runtime.
        """

        self.status = "stopped"

    def record_success(self) -> None:
        """
        Record successful execution.
        """

        self.successful += 1

    def record_failure(self) -> None:
        """
        Record failed execution.
        """

        self.failed += 1

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize runtime state.
        """

        return {
            "status": self.status,
            "successful": self.successful,
            "failed": self.failed,
        }


class RuntimeStateManager:
    """
    Runtime state management service.

    Maintains:
    - lifecycle status
    - component health
    - metadata
    - snapshots
    """

    def __init__(self) -> None:
        self._status = "initialized"

        self._components: dict[str, str] = {}

        self._metadata: dict[str, Any] = {}

    def get_status(self) -> str:
        """
        Return current runtime status.
        """

        return self._status

    def set_status(
        self,
        status: str,
    ) -> None:
        """
        Update runtime status.
        """

        self._status = status

    def set_component(
        self,
        name: str,
        status: str,
    ) -> None:
        """
        Register component health.
        """

        self._components[name] = status

    def get_component(
        self,
        name: str,
    ) -> str | None:
        """
        Retrieve component health.
        """

        return self._components.get(name)

    def set_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store runtime metadata.
        """

        self._metadata[key] = value

    def get_metadata(
        self,
        key: str,
    ) -> Any:
        """
        Retrieve metadata.
        """

        return self._metadata.get(key)

    def snapshot(self) -> dict[str, Any]:
        """
        Return runtime snapshot.
        """

        return {
            "status": self._status,
            "components": self._components.copy(),
            "metadata": self._metadata.copy(),
        }

    def reset(self) -> None:
        """
        Reset runtime state.
        """

        self._status = "initialized"

        self._components.clear()

        self._metadata.clear()
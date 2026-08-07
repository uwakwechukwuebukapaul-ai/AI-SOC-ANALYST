"""
Base service adapter contract.

The runtime communicates with intelligence services through
this interface rather than depending directly on their
internal implementations.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class ServiceAdapter(ABC):
    """
    Stable contract for services consumed by the
    Investigation Runtime.
    """

    name: str = "unknown"
    capability: str = "unknown"

    @abstractmethod
    def execute(
        self,
        investigation: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Execute the service against an investigation.

        Implementations must return a serializable dictionary.
        """
        raise NotImplementedError

    def metadata(self) -> dict[str, str]:
        """Return service metadata exposed to the runtime."""

        return {
            "name": self.name,
            "capability": self.capability,
        }
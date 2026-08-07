"""
Sentinel DNA Runtime Capability Registry

Central registry for runtime capabilities.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeCapabilityRegistry:
    """
    Runtime capability registry.
    """

    capabilities: dict[str, dict[str, Any]] = field(
        default_factory=dict
    )

    def register(
        self,
        name: str,
        provider: str,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """
        Register a capability.
        """

        self.capabilities[name] = {
            "provider": provider,
            "metadata": metadata or {},
        }

    def get(
        self,
        name: str,
    ) -> dict[str, Any] | None:
        """
        Retrieve capability information.
        """

        return self.capabilities.get(name)

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check capability existence.
        """

        return name in self.capabilities

    def remove(
        self,
        name: str,
    ) -> None:
        """
        Remove capability.
        """

        self.capabilities.pop(name, None)

    def list_capabilities(
        self,
    ) -> list[str]:
        """
        Return registered capability names.
        """

        return sorted(self.capabilities.keys())

    def count(
        self,
    ) -> int:
        """
        Return capability count.
        """

        return len(self.capabilities)

    def clear(
        self,
    ) -> None:
        """
        Reset registry.
        """

        self.capabilities.clear()

    def status(
        self,
    ) -> dict[str, Any]:
        """
        Registry status.
        """

        return {
            "count": self.count(),
            "capabilities": self.list_capabilities(),
        }
"""
Sentinel DNA Runtime Registry Service

Application service for managing
runtime capabilities.

Responsibilities:

- capability discovery
- handler registration
- runtime metadata
- registry operations
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from .runtime_registry import RuntimeRegistry


@dataclass
class RuntimeRegistryService:
    """
    Enterprise registry service.
    """

    registry: RuntimeRegistry = field(
        default_factory=RuntimeRegistry
    )


    def register_capability(
        self,
        capability: str,
        handler: Callable,
    ) -> None:
        """
        Register execution capability.
        """

        self.registry.register_capability(
            capability,
            handler,
        )



    def register_agent(
        self,
        agent_name: str,
        metadata: dict[str, Any],
    ) -> None:
        """
        Register intelligence agent.
        """

        self.registry.register_agent(
            agent_name,
            metadata,
        )



    def register_handler(
        self,
        name: str,
        handler: Callable,
    ) -> None:
        """
        Register runtime handler.
        """

        self.registry.register_handler(
            name,
            handler,
        )



    def get_capability(
        self,
        capability: str,
    ):
        """
        Retrieve capability handler.
        """

        return self.registry.get_capability(
            capability
        )



    def clear(self) -> None:
        """
        Clear registry.
        """

        self.registry.clear()



    def status(self) -> dict[str, Any]:
        """
        Registry status.
        """

        return self.registry.to_dict()
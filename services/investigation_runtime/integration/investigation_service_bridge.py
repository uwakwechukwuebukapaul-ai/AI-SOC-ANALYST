"""
Investigation service bridge.

Connects Sentinel DNA intelligence services to the unified
Investigation Runtime through stable service adapters.
"""

from __future__ import annotations

from typing import Any, Callable

from ..adapters.intelligence_adapter import (
    IntelligenceServiceAdapter,
)
from ..adapters.service_adapter import ServiceAdapter
from .runtime_service_registry import RuntimeServiceRegistry


class InvestigationServiceBridge:
    """
    Integration boundary for investigation intelligence services.
    """

    def __init__(
        self,
        registry: RuntimeServiceRegistry | None = None,
    ) -> None:
        self.registry = (
            registry
            if registry is not None
            else RuntimeServiceRegistry()
        )

    def register_executor(
        self,
        *,
        name: str,
        capability: str,
        executor: Callable[
            [dict[str, Any]],
            dict[str, Any],
        ],
    ) -> ServiceAdapter:
        """
        Register a callable intelligence service.
        """

        adapter = IntelligenceServiceAdapter(
            name=name,
            capability=capability,
            executor=executor,
        )

        self.registry.register(adapter)

        return adapter

    def register_service(
        self,
        service: ServiceAdapter,
    ) -> None:
        """
        Register an existing service adapter.
        """

        self.registry.register(service)

    def available_services(self) -> list[str]:
        """
        Return names of available services.
        """

        return self.registry.names()

    def available_capabilities(self) -> dict[str, str]:
        """
        Return registered service capabilities.
        """

        return self.registry.capabilities()

    def execute(
        self,
        service_name: str,
        investigation: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Execute a service through the bridge.
        """

        return self.registry.execute(
            service_name,
            investigation,
        )
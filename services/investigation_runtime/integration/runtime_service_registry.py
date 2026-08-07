"""
Runtime service registry.

Maintains the intelligence services available to the
Investigation Runtime without coupling the runtime to
individual service implementations.
"""

from __future__ import annotations

from typing import Any

from ..adapters.service_adapter import ServiceAdapter


class RuntimeServiceRegistry:
    """
    Registry of services available to investigations.
    """

    def __init__(self) -> None:
        self._services: dict[str, ServiceAdapter] = {}

    def register(self, service: ServiceAdapter) -> None:
        """
        Register a service adapter.
        """

        if not isinstance(service, ServiceAdapter):
            raise TypeError(
                "Runtime service must implement ServiceAdapter."
            )

        if not service.name:
            raise ValueError("Service name is required.")

        if service.name in self._services:
            raise ValueError(
                f"Service '{service.name}' is already registered."
            )

        self._services[service.name] = service

    def unregister(self, name: str) -> ServiceAdapter | None:
        """
        Remove a registered service.
        """

        return self._services.pop(name, None)

    def get(self, name: str) -> ServiceAdapter:
        """
        Return a registered service.
        """

        try:
            return self._services[name]
        except KeyError as exc:
            raise KeyError(
                f"Runtime service '{name}' is not registered."
            ) from exc

    def has(self, name: str) -> bool:
        """
        Determine whether a service is registered.
        """

        return name in self._services

    def names(self) -> list[str]:
        """
        Return registered service names.
        """

        return list(self._services.keys())

    def capabilities(self) -> dict[str, str]:
        """
        Return service-to-capability mappings.
        """

        return {
            service.name: service.capability
            for service in self._services.values()
        }

    def metadata(self) -> list[dict[str, str]]:
        """
        Return metadata for all registered services.
        """

        return [
            service.metadata()
            for service in self._services.values()
        ]

    def execute(
        self,
        name: str,
        investigation: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Execute a registered service against an investigation.
        """

        service = self.get(name)

        return service.execute(investigation)
"""
Service registry for the Unified Investigation Runtime.

The registry deliberately uses dependency injection so intelligence
services remain independently testable and replaceable.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any


class ServiceRegistry:
    """
    Registry of investigation capabilities.

    Services can be registered as:
    - instances
    - classes
    - callables
    """

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}

    def register(
        self,
        name: str,
        service: Any,
        *,
        replace: bool = False,
    ) -> None:
        if not name or not name.strip():
            raise ValueError("Service name cannot be empty.")

        normalized_name = name.strip().lower()

        if (
            normalized_name in self._services
            and not replace
        ):
            raise ValueError(
                f"Service already registered: {normalized_name}"
            )

        self._services[normalized_name] = service

    def unregister(self, name: str) -> Any | None:
        return self._services.pop(
            name.strip().lower(),
            None,
        )

    def get(self, name: str) -> Any:
        normalized_name = name.strip().lower()

        if normalized_name not in self._services:
            raise KeyError(
                f"Investigation service not registered: "
                f"{normalized_name}"
            )

        return self._services[normalized_name]

    def resolve(self, name: str) -> Any:
        service = self.get(name)

        if isinstance(service, type):
            return service()

        if callable(service) and not hasattr(
            service,
            "execute",
        ):
            return service()

        return service

    def has(self, name: str) -> bool:
        return name.strip().lower() in self._services

    def names(self) -> list[str]:
        return sorted(self._services.keys())

    def clear(self) -> None:
        self._services.clear()

    def __contains__(self, name: str) -> bool:
        return self.has(name)

    def __len__(self) -> int:
        return len(self._services)
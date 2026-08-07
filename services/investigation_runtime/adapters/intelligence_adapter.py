"""
Generic adapter for Sentinel DNA intelligence services.
"""

from __future__ import annotations

from typing import Any, Callable

from .service_adapter import ServiceAdapter


class IntelligenceServiceAdapter(ServiceAdapter):
    """
    Adapts an existing intelligence engine into the
    Investigation Runtime service contract.

    The runtime does not need to know the internal API
    of the underlying intelligence engine.
    """

    def __init__(
        self,
        name: str,
        capability: str,
        executor: Callable[[dict[str, Any]], dict[str, Any]],
    ) -> None:
        if not name:
            raise ValueError("Service name is required.")

        if not capability:
            raise ValueError("Service capability is required.")

        if not callable(executor):
            raise TypeError("Executor must be callable.")

        self.name = name
        self.capability = capability
        self._executor = executor

    def execute(
        self,
        investigation: dict[str, Any],
    ) -> dict[str, Any]:
        if not isinstance(investigation, dict):
            raise TypeError("Investigation must be a dictionary.")

        result = self._executor(investigation)

        if not isinstance(result, dict):
            raise TypeError(
                f"{self.name} adapter must return a dictionary."
            )

        return result
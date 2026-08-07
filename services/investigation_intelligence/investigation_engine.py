"""
Public Investigation Intelligence Engine.
"""

from __future__ import annotations

from typing import Any

from .intelligence_coordinator import (
    IntelligenceCoordinator,
)


class InvestigationEngine:
    """
    High-level entry point for unified investigation
    intelligence.

    This engine intentionally remains independent from
    individual intelligence-service implementations.
    """

    def __init__(
        self,
        coordinator: IntelligenceCoordinator | None = None,
    ) -> None:
        self.coordinator = (
            coordinator
            or IntelligenceCoordinator()
        )

    def register_provider(
        self,
        name: str,
        provider,
    ) -> None:
        self.coordinator.register(
            name,
            provider,
        )

    def investigate(
        self,
        investigation: dict[str, Any],
    ) -> dict[str, Any]:
        if not isinstance(investigation, dict):
            raise TypeError(
                "Investigation must be a dictionary."
            )

        result = self.coordinator.analyze(
            investigation
        )

        return {
            "type": "investigation_intelligence",
            "status": "completed",
            "investigation": investigation,
            **result,
        }

    def providers(self) -> list[str]:
        return self.coordinator.providers()
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

    The engine supports both direct provider execution
    and analysis of intelligence results that were already
    executed by the Investigation Runtime.
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
        if not isinstance(
            investigation,
            dict,
        ):
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

    def analyze_results(
        self,
        investigation: dict[str, Any],
        intelligence: dict[
            str,
            dict[str, Any],
        ],
    ) -> dict[str, Any]:
        """
        Analyze intelligence results produced by the
        Investigation Runtime.
        """

        result = (
            self.coordinator.analyze_results(
                investigation,
                intelligence,
            )
        )

        return {
            "type": "investigation_intelligence",
            "status": "completed",
            "investigation": investigation,
            **result,
        }

    def providers(self) -> list[str]:
        return self.coordinator.providers()
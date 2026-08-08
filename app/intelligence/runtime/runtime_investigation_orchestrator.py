"""
Sentinel DNA Runtime Investigation Orchestrator

Canonical investigation coordination layer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_intelligence_router import (
    RuntimeIntelligenceRouter,
)
from .task import Task


@dataclass
class RuntimeInvestigationOrchestrator:
    """
    Investigation workflow runtime.

    Responsibilities:

    - create investigation tasks
    - route investigation capabilities
    - track successful investigation executions
    - expose runtime status
    """

    router: RuntimeIntelligenceRouter = field(
        default_factory=RuntimeIntelligenceRouter
    )

    investigations: int = 0

    failures: int = 0

    # ------------------------------------------------------------------
    # Agent Registration
    # ------------------------------------------------------------------

    def register_agent(
        self,
        agent: Any,
    ) -> None:
        """
        Register an investigation-capable runtime agent.
        """

        self.router.register_agent(agent)

    # ------------------------------------------------------------------
    # Investigation
    # ------------------------------------------------------------------

    def investigate(
        self,
        capability: str,
        evidence: dict[str, Any],
    ) -> Any:
        """
        Execute an investigation capability.
        """

        task = Task(
            capability=capability,
            payload=dict(
                evidence or {}
            ),
        )

        try:
            result = self.router.route(
                task
            )

            if result is not None:
                self.investigations += 1
            else:
                self.failures += 1

            return result

        except Exception:
            self.failures += 1
            raise

    # ------------------------------------------------------------------
    # Metrics
    # ------------------------------------------------------------------

    def count(self) -> int:
        """
        Return successful investigation count.
        """

        return self.investigations

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def clear(self) -> None:
        """
        Reset investigation runtime.
        """

        self.router.clear()

        self.investigations = 0

        self.failures = 0

    # ------------------------------------------------------------------
    # Status
    # ------------------------------------------------------------------

    def status(self) -> dict[str, Any]:
        """
        Return investigation runtime status.
        """

        return {
            "investigations": self.investigations,
            "failures": self.failures,
            "router": self.router.status(),
        }
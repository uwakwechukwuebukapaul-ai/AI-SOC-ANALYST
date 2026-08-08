"""
Sentinel DNA Runtime SOC Orchestrator

Enterprise AI SOC runtime control plane.

Responsibilities:

- coordinate SOC runtime services
- manage detection workflows
- manage threat intelligence workflows
- coordinate investigations
- coordinate response / SOAR actions
- coordinate autonomous agents
- expose unified runtime status
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_detection_orchestrator import (
    RuntimeDetectionOrchestrator,
)

from .runtime_threat_intelligence_orchestrator import (
    RuntimeThreatIntelligenceOrchestrator,
)

from .runtime_investigation_orchestrator import (
    RuntimeInvestigationOrchestrator,
)

from .runtime_response_orchestrator import (
    RuntimeResponseOrchestrator,
)

from .runtime_autonomous_agent_orchestrator import (
    RuntimeAutonomousAgentOrchestrator,
)


@dataclass
class RuntimeSOCOrchestrator:
    """
    Unified Sentinel DNA SOC runtime coordinator.

    This class acts as the runtime control plane between
    the application layer and individual intelligence
    execution domains.
    """

    detection: RuntimeDetectionOrchestrator = field(
        default_factory=RuntimeDetectionOrchestrator
    )

    intelligence: RuntimeThreatIntelligenceOrchestrator = field(
        default_factory=RuntimeThreatIntelligenceOrchestrator
    )

    investigation: RuntimeInvestigationOrchestrator = field(
        default_factory=RuntimeInvestigationOrchestrator
    )

    response: RuntimeResponseOrchestrator = field(
        default_factory=RuntimeResponseOrchestrator
    )

    autonomous: RuntimeAutonomousAgentOrchestrator = field(
        default_factory=RuntimeAutonomousAgentOrchestrator
    )

    operations: int = 0

    # ------------------------------------------------------------------
    # Detection
    # ------------------------------------------------------------------

    def analyze_event(
        self,
        event_type: str,
        event: dict[str, Any],
    ) -> Any:
        """
        Execute SOC detection analysis.
        """

        self.operations += 1

        return self.detection.evaluate(
            event_type,
            event,
        )

    # ------------------------------------------------------------------
    # Threat Intelligence
    # ------------------------------------------------------------------

    def enrich_threat(
        self,
        engine: str,
        artifact: dict[str, Any],
    ) -> Any:
        """
        Execute threat intelligence enrichment.
        """

        self.operations += 1

        return self.intelligence.analyze(
            engine,
            artifact,
        )

    # ------------------------------------------------------------------
    # Investigation
    # ------------------------------------------------------------------

    def investigate(
        self,
        capability: str,
        evidence: dict[str, Any],
    ) -> Any:
        """
        Start an investigation.
        """

        self.operations += 1

        return self.investigation.investigate(
            capability,
            evidence,
        )

    # ------------------------------------------------------------------
    # Response
    # ------------------------------------------------------------------

    def respond(
        self,
        action: str,
        context: dict[str, Any],
    ) -> Any:
        """
        Execute a response / SOAR action.
        """

        self.operations += 1

        return self.response.execute(
            action,
            context,
        )

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def clear(self) -> None:
        """
        Reset all SOC runtime state.
        """

        self.detection.clear()

        self.intelligence.clear()

        self.investigation.clear()

        self.response.clear()

        self.autonomous.clear()

        self.operations = 0

    # ------------------------------------------------------------------
    # Status
    # ------------------------------------------------------------------

    def status(self) -> dict[str, Any]:
        """
        Return complete SOC runtime status.
        """

        return {
            "operations": self.operations,
            "detection": self.detection.status(),
            "intelligence": self.intelligence.status(),
            "investigation": self.investigation.status(),
            "response": self.response.status(),
            "autonomous": self.autonomous.status(),
        }
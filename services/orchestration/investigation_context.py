"""
Shared investigation context.

The context is the single state container passed through the
Sentinel DNA investigation lifecycle.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any


class InvestigationContext:
    """Maintain state for one security investigation."""

    def __init__(
        self,
        *,
        case_id: str,
        alert: dict[str, Any],
    ) -> None:
        if not case_id:
            raise ValueError("case_id is required.")

        if not isinstance(alert, dict):
            raise TypeError("alert must be a dictionary.")

        self.case_id = case_id
        self.alert = deepcopy(alert)

        self.evidence: list[dict[str, Any]] = []
        self.iocs: list[dict[str, Any]] = []
        self.risk: dict[str, Any] = {}
        self.threat_intelligence: dict[str, Any] = {}
        self.detections: list[dict[str, Any]] = []
        self.hunt_results: list[dict[str, Any]] = []
        self.decisions: list[dict[str, Any]] = []
        self.recommendations: list[dict[str, Any]] = []
        self.response: dict[str, Any] = {}
        self.timeline: list[dict[str, Any]] = []

    def add_timeline_event(
        self,
        event: str,
        *,
        details: dict[str, Any] | None = None,
    ) -> None:
        """Add an event to the investigation timeline."""

        self.timeline.append(
            {
                "event": event,
                "details": deepcopy(details or {}),
            }
        )

    def snapshot(self) -> dict[str, Any]:
        """Return a safe copy of the complete investigation state."""

        return deepcopy(
            {
                "case_id": self.case_id,
                "alert": self.alert,
                "evidence": self.evidence,
                "iocs": self.iocs,
                "risk": self.risk,
                "threat_intelligence": self.threat_intelligence,
                "detections": self.detections,
                "hunt_results": self.hunt_results,
                "decisions": self.decisions,
                "recommendations": self.recommendations,
                "response": self.response,
                "timeline": self.timeline,
            }
        )
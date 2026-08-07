"""
Sentinel DNA
Enterprise Investigation Context

This module defines the InvestigationContext object that is shared
throughout the investigation lifecycle.

Author: Sentinel DNA
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


def utc_now() -> datetime:
    """
    Returns timezone-aware UTC datetime.

    Replaces deprecated datetime.now(timezone.utc).
    """
    return datetime.now(timezone.utc)


@dataclass
class InvestigationContext:
    """
    Shared context object passed through every investigation stage.
    """

    # ==============================
    # Core Case Information
    # ==============================

    case_id: Optional[int] = None

    investigation_id: Optional[str] = None

    source: str = "unknown"

    source_identifier: Optional[str] = None

    title: str = ""

    description: str = ""

    severity: str = "Low"

    priority: str = "Low"

    status: str = "NEW"

    analyst: Optional[str] = None


    # ==============================
    # Investigation Data
    # ==============================

    artifacts: List[Dict[str, Any]] = field(default_factory=list)

    iocs: List[Dict[str, Any]] = field(default_factory=list)

    evidence: List[Dict[str, Any]] = field(default_factory=list)

    mitre_techniques: List[Dict[str, Any]] = field(default_factory=list)

    threat_intelligence: List[Dict[str, Any]] = field(default_factory=list)

    recommendations: List[Dict[str, Any]] = field(default_factory=list)

    response_actions: List[Dict[str, Any]] = field(default_factory=list)

    timeline: List[Dict[str, Any]] = field(default_factory=list)

    notes: List[str] = field(default_factory=list)


    # ==============================
    # AI Intelligence Layer
    # ==============================

    ai_summary: str = ""

    executive_summary: str = ""

    attack_story: str = ""

    confidence: float = 0.0

    risk_score: int = 0


    # ==============================
    # Metadata
    # ==============================

    metadata: Dict[str, Any] = field(default_factory=dict)

    tags: List[str] = field(default_factory=list)


    created_at: datetime = field(default_factory=utc_now)

    updated_at: datetime = field(default_factory=utc_now)

    completed_at: Optional[datetime] = None


    # ==============================
    # Data Mutation Helpers
    # ==============================

    def add_artifact(self, artifact: Dict[str, Any]) -> None:
        self.artifacts.append(artifact)


    def add_ioc(self, ioc: Dict[str, Any]) -> None:
        self.iocs.append(ioc)


    def add_evidence(self, evidence: Dict[str, Any]) -> None:
        self.evidence.append(evidence)


    def add_mitre(self, technique: Dict[str, Any]) -> None:
        self.mitre_techniques.append(technique)


    def add_threat_intelligence(
        self,
        intel: Dict[str, Any]
    ) -> None:
        self.threat_intelligence.append(intel)


    def add_recommendation(
        self,
        recommendation: Dict[str, Any]
    ) -> None:
        self.recommendations.append(recommendation)


    def add_response_action(
        self,
        action: Dict[str, Any]
    ) -> None:
        self.response_actions.append(action)


    def add_timeline_event(
        self,
        stage: str,
        message: str,
    ) -> None:

        self.timeline.append(
            {
                "timestamp": utc_now().isoformat(),
                "stage": stage,
                "message": message,
            }
        )


    def add_note(self, note: str) -> None:
        self.notes.append(note)


    def update_timestamp(self) -> None:
        self.updated_at = utc_now()


    def mark_completed(self) -> None:

        self.completed_at = utc_now()

        self.status = "COMPLETED"

        self.update_timestamp()


    # ==============================
    # Serialization
    # ==============================

    def to_dict(self) -> Dict[str, Any]:

        return {

            "case_id": self.case_id,

            "investigation_id": self.investigation_id,

            "source": self.source,

            "source_identifier": self.source_identifier,

            "title": self.title,

            "description": self.description,

            "severity": self.severity,

            "priority": self.priority,

            "status": self.status,

            "analyst": self.analyst,


            "artifacts": self.artifacts,

            "iocs": self.iocs,

            "evidence": self.evidence,

            "mitre_techniques": self.mitre_techniques,

            "threat_intelligence": self.threat_intelligence,

            "recommendations": self.recommendations,

            "response_actions": self.response_actions,

            "timeline": self.timeline,

            "notes": self.notes,


            "ai_summary": self.ai_summary,

            "executive_summary": self.executive_summary,

            "attack_story": self.attack_story,

            "confidence": self.confidence,

            "risk_score": self.risk_score,


            "metadata": self.metadata,

            "tags": self.tags,


            "created_at": self.created_at.isoformat(),

            "updated_at": self.updated_at.isoformat(),

            "completed_at": (
                self.completed_at.isoformat()
                if self.completed_at
                else None
            ),
        }

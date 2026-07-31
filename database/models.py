"""
Sentinel DNA
Database Models
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class Incident:
    """
    Represents a security incident.
    """

    id: int | None = None

    timestamp: str = field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    threat: str = "Unknown"

    severity: str = "LOW"

    risk_score: int = 0

    mitre: str = "N/A"

    response_status: str = "INVESTIGATION REQUIRED"

    status: str = "OPEN"

    evidence: str = ""

    actions: list[str] = field(default_factory=list)

    analyst: str = ""

    notes: str = ""

    def validate(self) -> None:
        """
        Validate incident fields.
        """

        allowed = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}

        self.severity = self.severity.upper()

        if self.severity not in allowed:
            raise ValueError(
                f"Invalid severity: {self.severity}"
            )

        if self.risk_score < 0:
            raise ValueError(
                "Risk score cannot be negative."
            )

    def to_dict(self) -> dict[str, Any]:
        """
        Convert object to dictionary.
        """

        return {

            "id": self.id,

            "timestamp": self.timestamp,

            "threat": self.threat,

            "severity": self.severity,

            "risk_score": self.risk_score,

            "mitre": self.mitre,

            "response_status": self.response_status,

            "status": self.status,

            "evidence": self.evidence,

            "actions": self.actions,

            "analyst": self.analyst,

            "notes": self.notes,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        """
        Create Incident from dictionary.
        """

        return cls(

            id=data.get("id"),

            timestamp=data.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),

            threat=data.get("threat", "Unknown"),

            severity=data.get("severity", "LOW"),

            risk_score=int(data.get("risk_score", 0)),

            mitre=data.get("mitre", "N/A"),

            response_status=data.get(
                "response_status",
                "INVESTIGATION REQUIRED"
            ),

            status=data.get("status", "OPEN"),

            evidence=data.get("evidence", ""),

            actions=data.get("actions", []),

            analyst=data.get("analyst", ""),

            notes=data.get("notes", "")
        )
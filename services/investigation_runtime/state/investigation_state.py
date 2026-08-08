"""
Investigation state model.

Defines the lifecycle and runtime state of a Sentinel DNA
investigation without coupling the domain model to a
specific persistence technology.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class InvestigationStatus(str, Enum):
    """
    Lifecycle states supported by an investigation.
    """

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class InvestigationState:
    """
    Represents the current state of an investigation execution.

    The model intentionally stores generic dictionaries for
    investigation input, intelligence, findings, correlation,
    confidence, and errors so individual intelligence providers
    remain decoupled from the state layer.
    """

    investigation_id: str
    investigation: dict[str, Any]

    status: InvestigationStatus = (
        InvestigationStatus.PENDING
    )

    intelligence: dict[str, Any] = field(
        default_factory=dict
    )

    correlation: dict[str, Any] = field(
        default_factory=dict
    )

    confidence: dict[str, Any] = field(
        default_factory=dict
    )

    finding: dict[str, Any] = field(
        default_factory=dict
    )

    errors: list[dict[str, Any]] = field(
        default_factory=list
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc
        )
    )

    started_at: datetime | None = None

    completed_at: datetime | None = None

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc
        )
    )

    def __post_init__(self) -> None:
        if not self.investigation_id:
            raise ValueError(
                "Investigation ID is required."
            )

        if not isinstance(
            self.investigation,
            dict,
        ):
            raise TypeError(
                "Investigation must be a dictionary."
            )

        self.updated_at = datetime.now(
            timezone.utc
        )

    def start(self) -> None:
        """
        Transition the investigation into running state.
        """

        if self.status != InvestigationStatus.PENDING:
            raise ValueError(
                "Only pending investigations can start."
            )

        now = datetime.now(timezone.utc)

        self.status = InvestigationStatus.RUNNING
        self.started_at = now
        self.updated_at = now

    def complete(
        self,
        *,
        intelligence: dict[str, Any] | None = None,
        correlation: dict[str, Any] | None = None,
        confidence: dict[str, Any] | None = None,
        finding: dict[str, Any] | None = None,
    ) -> None:
        """
        Mark the investigation as successfully completed.
        """

        if self.status != InvestigationStatus.RUNNING:
            raise ValueError(
                "Only running investigations can complete."
            )

        if intelligence is not None:
            if not isinstance(intelligence, dict):
                raise TypeError(
                    "Intelligence must be a dictionary."
                )

            self.intelligence = intelligence

        if correlation is not None:
            if not isinstance(correlation, dict):
                raise TypeError(
                    "Correlation must be a dictionary."
                )

            self.correlation = correlation

        if confidence is not None:
            if not isinstance(confidence, dict):
                raise TypeError(
                    "Confidence must be a dictionary."
                )

            self.confidence = confidence

        if finding is not None:
            if not isinstance(finding, dict):
                raise TypeError(
                    "Finding must be a dictionary."
                )

            self.finding = finding

        now = datetime.now(timezone.utc)

        self.status = InvestigationStatus.COMPLETED
        self.completed_at = now
        self.updated_at = now

    def fail(
        self,
        error: str,
        *,
        service: str | None = None,
    ) -> None:
        """
        Mark the investigation as failed and preserve
        structured failure information.
        """

        if self.status not in {
            InvestigationStatus.PENDING,
            InvestigationStatus.RUNNING,
        }:
            raise ValueError(
                "Only pending or running investigations "
                "can fail."
            )

        if not error:
            raise ValueError(
                "Failure error is required."
            )

        failure = {
            "error": error,
            "service": service,
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
        }

        self.errors.append(failure)

        now = datetime.now(timezone.utc)

        self.status = InvestigationStatus.FAILED
        self.completed_at = now
        self.updated_at = now

    def cancel(self) -> None:
        """
        Cancel a pending or running investigation.
        """

        if self.status not in {
            InvestigationStatus.PENDING,
            InvestigationStatus.RUNNING,
        }:
            raise ValueError(
                "Only pending or running investigations "
                "can be cancelled."
            )

        now = datetime.now(timezone.utc)

        self.status = InvestigationStatus.CANCELLED
        self.completed_at = now
        self.updated_at = now

    def update(
        self,
        **values: Any,
    ) -> None:
        """
        Update supported investigation state fields.

        This method intentionally rejects unknown fields to
        prevent accidental corruption of the state model.
        """

        allowed = {
            "intelligence",
            "correlation",
            "confidence",
            "finding",
        }

        unknown = set(values) - allowed

        if unknown:
            raise ValueError(
                "Unsupported state fields: "
                + ", ".join(sorted(unknown))
            )

        for key, value in values.items():
            if not isinstance(value, dict):
                raise TypeError(
                    f"{key} must be a dictionary."
                )

            setattr(self, key, value)

        self.updated_at = datetime.now(
            timezone.utc
        )

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the state into a JSON-compatible dictionary.
        """

        return {
            "investigation_id": self.investigation_id,
            "investigation": self.investigation,
            "status": self.status.value,
            "intelligence": self.intelligence,
            "correlation": self.correlation,
            "confidence": self.confidence,
            "finding": self.finding,
            "errors": self.errors,
            "created_at": self.created_at.isoformat(),
            "started_at": (
                self.started_at.isoformat()
                if self.started_at
                else None
            ),
            "completed_at": (
                self.completed_at.isoformat()
                if self.completed_at
                else None
            ),
            "updated_at": self.updated_at.isoformat(),
        }
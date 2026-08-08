"""
Investigation runtime state model.

Tracks the lifecycle, execution results, errors, and
timestamps associated with a Sentinel DNA investigation.
"""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class InvestigationStatus(str, Enum):
    """Supported investigation lifecycle states."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class InvestigationState:
    """
    Mutable runtime state for a single investigation.

    The state model is intentionally independent from the
    execution and persistence layers.
    """

    def __init__(
        self,
        investigation_id: str,
        investigation: dict[str, Any] | None = None,
        status: InvestigationStatus = InvestigationStatus.PENDING,
        current_stage: str | None = None,
        completed_stages: list[str] | None = None,
        results: dict[str, Any] | None = None,
        errors: list[dict[str, Any]] | None = None,
        intelligence: dict[str, Any] | None = None,
        correlation: dict[str, Any] | None = None,
        confidence: dict[str, Any] | None = None,
        finding: dict[str, Any] | None = None,
        metadata: dict[str, Any] | None = None,
        created_at: datetime | None = None,
        started_at: datetime | None = None,
        completed_at: datetime | None = None,
        updated_at: datetime | None = None,
    ) -> None:
        if not investigation_id:
            raise ValueError(
                "Investigation ID is required."
            )

        if not isinstance(status, InvestigationStatus):
            try:
                status = InvestigationStatus(status)
            except (TypeError, ValueError) as exc:
                raise ValueError(
                    f"Invalid investigation status: {status}"
                ) from exc

        self.investigation_id = investigation_id
        self.investigation = deepcopy(
            investigation or {}
        )
        self.status = status

        self.current_stage = current_stage

        self.completed_stages = list(
            completed_stages or []
        )

        self.results = deepcopy(
            results or {}
        )

        self.errors = deepcopy(
            errors or []
        )

        self.intelligence = deepcopy(
            intelligence or {}
        )

        self.correlation = deepcopy(
            correlation or {}
        )

        self.confidence = deepcopy(
            confidence or {}
        )

        self.finding = deepcopy(
            finding or {}
        )

        self.metadata = deepcopy(
            metadata or {}
        )

        now = self._now()

        self.created_at = (
            created_at or now
        )

        self.started_at = started_at
        self.completed_at = completed_at

        self.updated_at = (
            updated_at or now
        )

    @staticmethod
    def _now() -> datetime:
        """Return the current timezone-aware UTC timestamp."""
        return datetime.now(timezone.utc)

    def _touch(self) -> None:
        """Update the modification timestamp."""
        self.updated_at = self._now()

    def start(
        self,
        stage: str | None = None,
    ) -> None:
        """
        Start or resume investigation execution.
        """
        self.status = InvestigationStatus.RUNNING
        self.current_stage = stage
        self.started_at = (
            self.started_at or self._now()
        )
        self.completed_at = None

        self._touch()

    def set_stage(
        self,
        stage: str,
    ) -> None:
        """Set the currently executing investigation stage."""
        if not stage:
            raise ValueError(
                "Stage is required."
            )

        self.current_stage = stage

        if self.status == InvestigationStatus.PENDING:
            self.status = InvestigationStatus.RUNNING

        if self.started_at is None:
            self.started_at = self._now()

        self._touch()

    def record_result(
        self,
        stage: str,
        result: dict[str, Any],
    ) -> None:
        """
        Record the result produced by an investigation stage.
        """
        if not stage:
            raise ValueError(
                "Stage is required."
            )

        if not isinstance(result, dict):
            raise TypeError(
                "Result must be a dictionary."
            )

        self.results[stage] = deepcopy(
            result
        )

        self._touch()

    def complete_stage(
        self,
        stage: str,
        result: dict[str, Any],
    ) -> None:
        """
        Record a successful stage and advance lifecycle state.
        """
        if not stage:
            raise ValueError(
                "Stage is required."
            )

        self.record_result(
            stage,
            result,
        )

        if stage not in self.completed_stages:
            self.completed_stages.append(stage)

        if self.current_stage == stage:
            self.current_stage = None

        self._touch()

    def record_error(
        self,
        stage: str,
        error: Exception,
    ) -> None:
        """
        Record a stage-level execution error.
        """
        if not stage:
            raise ValueError(
                "Stage is required."
            )

        if not isinstance(error, Exception):
            raise TypeError(
                "Error must be an Exception."
            )

        self.errors.append(
            {
                "stage": stage,
                "type": type(error).__name__,
                "message": str(error),
            }
        )

        self._touch()

    def complete(
        self,
        intelligence: dict[str, Any] | None = None,
        confidence: dict[str, Any] | None = None,
        finding: dict[str, Any] | None = None,
        correlation: dict[str, Any] | None = None,
    ) -> None:
        """
        Mark the investigation as successfully completed.
        """
        if intelligence is not None:
            if not isinstance(
                intelligence,
                dict,
            ):
                raise TypeError(
                    "Intelligence must be a dictionary."
                )

            self.intelligence = deepcopy(
                intelligence
            )

        if correlation is not None:
            if not isinstance(
                correlation,
                dict,
            ):
                raise TypeError(
                    "Correlation must be a dictionary."
                )

            self.correlation = deepcopy(
                correlation
            )

        if confidence is not None:
            if not isinstance(
                confidence,
                dict,
            ):
                raise TypeError(
                    "Confidence must be a dictionary."
                )

            self.confidence = deepcopy(
                confidence
            )

        if finding is not None:
            if not isinstance(
                finding,
                dict,
            ):
                raise TypeError(
                    "Finding must be a dictionary."
                )

            self.finding = deepcopy(
                finding
            )

        self.status = (
            InvestigationStatus.COMPLETED
        )

        self.current_stage = None
        self.completed_at = self._now()

        self._touch()

    def fail(
        self,
        error: str | None = None,
        service: str | None = None,
    ) -> None:
        """
        Mark the investigation as failed.

        A failure is represented by the FAILED lifecycle state.
        If a concrete error has already been recorded through
        record_error(), fail() does not create a duplicate
        generic error entry.
        """
        self.status = (
            InvestigationStatus.FAILED
        )

        self.current_stage = None
        self.completed_at = self._now()

        if error is not None:
            if not isinstance(error, str):
                raise TypeError(
                    "Error must be a string."
                )

            error_entry: dict[str, Any] = {
                "error": error,
            }

            if service:
                error_entry["service"] = service

            self.errors.append(
                error_entry
            )

        self._touch()

    def snapshot(self) -> dict[str, Any]:
        """
        Return a detached snapshot of the current state.
        """
        return deepcopy(
            self.to_dict()
        )

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize state into persistence-safe data.
        """
        return {
            "investigation_id": (
                self.investigation_id
            ),
            "investigation": deepcopy(
                self.investigation
            ),
            "status": self.status.value,
            "current_stage": (
                self.current_stage
            ),
            "completed_stages": list(
                self.completed_stages
            ),
            "results": deepcopy(
                self.results
            ),
            "errors": deepcopy(
                self.errors
            ),
            "intelligence": deepcopy(
                self.intelligence
            ),
            "correlation": deepcopy(
                self.correlation
            ),
            "confidence": deepcopy(
                self.confidence
            ),
            "finding": deepcopy(
                self.finding
            ),
            "metadata": deepcopy(
                self.metadata
            ),
            "created_at": (
                self.created_at.isoformat()
                if self.created_at
                else None
            ),
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
            "updated_at": (
                self.updated_at.isoformat()
                if self.updated_at
                else None
            ),
        }
"""
Structured results produced by the Unified Investigation Runtime.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass
class StageResult:
    """
    Result produced by one investigation stage.
    """

    stage: str
    status: str = "completed"
    data: dict[str, Any] = field(default_factory=dict)
    error: str | None = None
    started_at: datetime = field(default_factory=_utc_now)
    completed_at: datetime | None = None

    def complete(self) -> None:
        self.completed_at = _utc_now()

    @property
    def successful(self) -> bool:
        return self.status == "completed" and self.error is None


@dataclass
class InvestigationRuntimeResult:
    """
    Final structured result for a unified investigation.
    """

    investigation_id: str
    status: str = "completed"
    stages: list[StageResult] = field(default_factory=list)
    decision: str = "review"
    summary: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)
    started_at: datetime = field(default_factory=_utc_now)
    completed_at: datetime | None = None

    def add_stage(self, result: StageResult) -> None:
        self.stages.append(result)

    def complete(self) -> None:
        self.completed_at = _utc_now()

    @property
    def successful(self) -> bool:
        return self.status == "completed" and not any(
            stage.error for stage in self.stages
        )

    @property
    def failed_stages(self) -> list[StageResult]:
        return [
            stage
            for stage in self.stages
            if stage.error is not None
        ]

    def to_dict(self) -> dict[str, Any]:
        return {
            "investigation_id": self.investigation_id,
            "status": self.status,
            "decision": self.decision,
            "summary": self.summary,
            "metadata": self.metadata,
            "started_at": self.started_at.isoformat(),
            "completed_at": (
                self.completed_at.isoformat()
                if self.completed_at
                else None
            ),
            "stages": [
                {
                    "stage": stage.stage,
                    "status": stage.status,
                    "data": stage.data,
                    "error": stage.error,
                    "started_at": stage.started_at.isoformat(),
                    "completed_at": (
                        stage.completed_at.isoformat()
                        if stage.completed_at
                        else None
                    ),
                }
                for stage in self.stages
            ],
        }
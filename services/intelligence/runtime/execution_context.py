"""
Sentinel DNA Runtime Execution Context

Shared execution context passed between
runtime components during task execution.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
import uuid


@dataclass(slots=True)
class ExecutionContext:
    """
    Shared runtime context.
    """

    investigation_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    case_id: str | None = None

    alert_id: str | None = None

    correlation_id: str | None = None

    tenant_id: str | None = None

    evidence: list[Any] = field(default_factory=list)

    shared_data: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def add_evidence(self, item: Any) -> None:
        self.evidence.append(item)

    def set(self, key: str, value: Any) -> None:
        self.shared_data[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self.shared_data.get(key, default)

    def add_metadata(self, key: str, value: Any) -> None:
        self.metadata[key] = value

    def to_dict(self) -> dict[str, Any]:
        return {
            "investigation_id": self.investigation_id,
            "case_id": self.case_id,
            "alert_id": self.alert_id,
            "correlation_id": self.correlation_id,
            "tenant_id": self.tenant_id,
            "evidence": self.evidence,
            "shared_data": self.shared_data,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
        }
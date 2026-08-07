"""
Sentinel DNA Agent Context

Shared execution context passed to AI agents.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class AgentContext:
    """
    Execution context for AI agents.
    """

    investigation_id: str

    case_id: str

    alert: dict[str, Any] = field(
        default_factory=dict
    )

    evidence: list[dict[str, Any]] = field(
        default_factory=list
    )

    iocs: list[dict[str, Any]] = field(
        default_factory=list
    )

    timeline: list[dict[str, Any]] = field(
        default_factory=list
    )

    analyst: dict[str, Any] = field(
        default_factory=dict
    )

    configuration: dict[str, Any] = field(
        default_factory=dict
    )

    shared_data: dict[str, Any] = field(
        default_factory=dict
    )

    def set(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store shared runtime data.
        """

        self.shared_data[key] = value

    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve shared runtime data.
        """

        return self.shared_data.get(
            key,
            default,
        )

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the execution context.
        """

        return {
            "investigation_id": self.investigation_id,
            "case_id": self.case_id,
            "alert": self.alert,
            "evidence": self.evidence,
            "iocs": self.iocs,
            "timeline": self.timeline,
            "analyst": self.analyst,
            "configuration": self.configuration,
            "shared_data": self.shared_data,
        }
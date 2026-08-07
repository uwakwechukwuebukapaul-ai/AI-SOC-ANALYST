"""
Sentinel DNA Agent Result

Standardized execution result for AI agents.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class AgentExecutionStatus(str, Enum):
    """
    Agent execution status.
    """

    SUCCESS = "success"
    FAILED = "failed"
    PARTIAL = "partial"
    SKIPPED = "skipped"


@dataclass(slots=True)
class AgentResult:
    """
    Standard AI agent execution result.
    """

    agent_name: str

    status: AgentExecutionStatus

    confidence: float = 0.0

    findings: list[dict[str, Any]] = field(
        default_factory=list
    )

    recommendations: list[str] = field(
        default_factory=list
    )

    artifacts: dict[str, Any] = field(
        default_factory=dict
    )

    metrics: dict[str, Any] = field(
        default_factory=dict
    )

    errors: list[str] = field(
        default_factory=list
    )

    def successful(self) -> bool:
        """
        True when execution succeeded.
        """

        return self.status is AgentExecutionStatus.SUCCESS

    def add_finding(
        self,
        finding: dict[str, Any],
    ) -> None:
        """
        Add investigation finding.
        """

        self.findings.append(finding)

    def add_recommendation(
        self,
        recommendation: str,
    ) -> None:
        """
        Add recommendation.
        """

        self.recommendations.append(
            recommendation
        )

    def add_error(
        self,
        error: str,
    ) -> None:
        """
        Record execution error.
        """

        self.errors.append(error)

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the result.
        """

        return {
            "agent_name": self.agent_name,
            "status": self.status.value,
            "confidence": self.confidence,
            "findings": self.findings,
            "recommendations": self.recommendations,
            "artifacts": self.artifacts,
            "metrics": self.metrics,
            "errors": self.errors,
        }
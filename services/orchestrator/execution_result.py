"""
Sentinel DNA
Enterprise Investigation Execution Result

Standard output contract for all investigation agents.

Author: Sentinel DNA
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List


def utc_now() -> datetime:
    """
    Returns timezone-aware UTC datetime.
    """
    return datetime.now(timezone.utc)


@dataclass
class ExecutionResult:
    """
    Standard result object returned by every Sentinel DNA agent.

    Provides a unified structure for:
    - success/failure tracking
    - findings
    - agent metadata
    - execution timing
    """

    agent_name: str

    status: str = "SUCCESS"

    message: str = ""

    findings: List[Dict[str, Any]] = field(
        default_factory=list
    )

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    started_at: datetime = field(
        default_factory=utc_now
    )

    completed_at: datetime = field(
        default_factory=utc_now
    )


    def add_finding(
        self,
        finding: Dict[str, Any],
    ) -> None:
        """
        Add an investigation finding.
        """

        self.findings.append(finding)


    def fail(
        self,
        message: str,
    ) -> None:
        """
        Mark execution as failed.
        """

        self.status = "FAILED"

        self.message = message

        self.completed_at = utc_now()


    def succeed(
        self,
        message: str = "",
    ) -> None:
        """
        Mark execution as successful.
        """

        self.status = "SUCCESS"

        self.message = message

        self.completed_at = utc_now()


    def to_dict(self) -> Dict[str, Any]:
        """
        Serialize result for API/logging/storage.
        """

        return {
            "agent_name": self.agent_name,
            "status": self.status,
            "message": self.message,
            "findings": self.findings,
            "metadata": self.metadata,
            "started_at": self.started_at.isoformat(),
            "completed_at": self.completed_at.isoformat(),
        }
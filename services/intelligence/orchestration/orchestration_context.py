"""
Sentinel DNA Orchestration Context

Shared investigation state passed between orchestration
components and intelligence agents.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class OrchestrationContext:
    """
    Shared context for a Sentinel DNA investigation.

    The context carries investigation-level state.

    Runtime-specific state must not be stored here.
    """

    case_id: str

    alert: dict[str, Any] = field(
        default_factory=dict
    )

    evidence: list[Any] = field(
        default_factory=list
    )

    findings: list[Any] = field(
        default_factory=list
    )

    agent_results: dict[str, Any] = field(
        default_factory=dict
    )

    shared_data: dict[str, Any] = field(
        default_factory=dict
    )

    # ------------------------------------------------------------------
    # Result management
    # ------------------------------------------------------------------

    def add_result(
        self,
        agent_name: str,
        result: Any,
    ) -> None:
        """
        Store the result produced by an agent.
        """

        if not agent_name:
            raise ValueError(
                "Agent name is required."
            )

        self.agent_results[agent_name] = result

    # ------------------------------------------------------------------
    # Finding management
    # ------------------------------------------------------------------

    def add_finding(
        self,
        finding: Any,
    ) -> None:
        """
        Add an investigation finding.
        """

        self.findings.append(
            finding
        )

    # ------------------------------------------------------------------
    # Shared data
    # ------------------------------------------------------------------

    def set_shared(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store shared investigation data.
        """

        if not key or not key.strip():
            raise ValueError(
                "Shared-data key is required."
            )

        self.shared_data[key] = value

    def get_shared(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve shared investigation data.
        """

        return self.shared_data.get(
            key,
            default,
        )
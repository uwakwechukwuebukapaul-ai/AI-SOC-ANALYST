"""
Sentinel DNA Intelligence Execution Plan

Canonical workflow execution plan for intelligence operations.

The execution plan describes WHAT should execute.
The runtime framework determines HOW it executes.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ExecutionPlan:
    """
    Enterprise intelligence execution plan.

    An execution plan is intentionally declarative.

    It defines:

    - plan identity
    - participating agents
    - ordered capabilities
    - shared execution metadata
    - optional investigation correlation

    Runtime agents remain responsible for actual execution.
    """

    name: str

    agents: list[str] = field(
        default_factory=list
    )

    capabilities: list[str] = field(
        default_factory=list
    )

    correlation_id: str | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def __post_init__(self) -> None:
        """
        Validate and normalize the execution plan.
        """

        if not self.name or not self.name.strip():
            raise ValueError(
                "Execution plan name is required."
            )

        self.agents = [
            str(agent)
            for agent in self.agents
            if agent
        ]

        self.capabilities = [
            str(capability)
            for capability in self.capabilities
            if capability
        ]

    def add_agent(
        self,
        agent: str,
    ) -> None:
        """
        Add an agent to the execution plan.
        """

        if not agent or not agent.strip():
            raise ValueError(
                "Agent name is required."
            )

        if agent not in self.agents:
            self.agents.append(agent)

    def add_capability(
        self,
        capability: str,
    ) -> None:
        """
        Add a runtime capability to the execution plan.
        """

        if not capability or not capability.strip():
            raise ValueError(
                "Capability is required."
            )

        if capability not in self.capabilities:
            self.capabilities.append(
                capability
            )

    def contains_capability(
        self,
        capability: str,
    ) -> bool:
        """
        Determine whether the plan contains
        a capability.
        """

        return capability in self.capabilities

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the execution plan.
        """

        return {
            "name": self.name,
            "agents": list(self.agents),
            "capabilities": list(
                self.capabilities
            ),
            "correlation_id": self.correlation_id,
            "metadata": dict(self.metadata),
        }
"""
Sentinel DNA Agent Capability Model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class AgentCapability:
    """
    Describes a capability implemented by an AI agent.
    """

    name: str

    description: str

    category: str

    priority: int = 100

    required_inputs: list[str] = field(
        default_factory=list
    )

    produced_outputs: list[str] = field(
        default_factory=list
    )

    parallel_execution: bool = True

    enabled: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "priority": self.priority,
            "required_inputs": self.required_inputs,
            "produced_outputs": self.produced_outputs,
            "parallel_execution": self.parallel_execution,
            "enabled": self.enabled,
        }
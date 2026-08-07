"""
Sentinel DNA Agent Capability

Defines the strongly typed capability contract exposed by AI agents.

The model intentionally supports both the original runtime vocabulary
(inputs / outputs) and the newer orchestration vocabulary
(required_inputs / produced_outputs).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, init=False)
class AgentCapability:
    """
    Describes a capability exposed by a Sentinel DNA AI agent.

    The model supports:

    - capability discovery
    - execution planning
    - dependency resolution
    - parallel execution
    - runtime enable/disable controls
    - capability prioritization
    - backward-compatible inputs/outputs terminology
    """

    name: str
    description: str
    category: str

    required_inputs: list[str]
    produced_outputs: list[str]

    tags: list[str]

    priority: int
    enabled: bool
    parallel_execution: bool

    def __init__(
        self,
        name: str,
        description: str = "",
        category: str = "general",
        required_inputs: list[str] | None = None,
        produced_outputs: list[str] | None = None,
        tags: list[str] | None = None,
        priority: int = 100,
        enabled: bool = True,
        parallel_execution: bool = False,
        *,
        inputs: list[str] | None = None,
        outputs: list[str] | None = None,
    ) -> None:
        """
        Initialize an agent capability.

        Both vocabulary styles are supported:

        New:
            required_inputs
            produced_outputs

        Legacy:
            inputs
            outputs

        When both forms are supplied, the explicit modern fields take
        precedence.
        """

        if required_inputs is None:
            required_inputs = inputs

        if produced_outputs is None:
            produced_outputs = outputs

        self.name = name
        self.description = description
        self.category = category

        self.required_inputs = list(
            required_inputs or []
        )

        self.produced_outputs = list(
            produced_outputs or []
        )

        self.tags = list(tags or [])

        self.priority = priority
        self.enabled = enabled
        self.parallel_execution = parallel_execution

    @property
    def inputs(self) -> list[str]:
        """
        Backward-compatible alias for required_inputs.
        """

        return self.required_inputs

    @property
    def outputs(self) -> list[str]:
        """
        Backward-compatible alias for produced_outputs.
        """

        return self.produced_outputs

    def supports_input(
        self,
        input_name: str,
    ) -> bool:
        """
        Return True when this capability accepts
        the supplied input.
        """

        return input_name in self.required_inputs

    def produces_output(
        self,
        output_name: str,
    ) -> bool:
        """
        Return True when this capability produces
        the supplied output.
        """

        return output_name in self.produced_outputs

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the capability into a JSON-compatible dictionary.
        """

        return {
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "required_inputs": list(
                self.required_inputs
            ),
            "produced_outputs": list(
                self.produced_outputs
            ),
            "inputs": list(
                self.required_inputs
            ),
            "outputs": list(
                self.produced_outputs
            ),
            "tags": list(self.tags),
            "priority": self.priority,
            "enabled": self.enabled,
            "parallel_execution": (
                self.parallel_execution
            ),
        }

    def __repr__(self) -> str:
        return (
            "AgentCapability("
            f"name={self.name!r}, "
            f"category={self.category!r}, "
            f"priority={self.priority!r}, "
            f"enabled={self.enabled!r}, "
            "parallel_execution="
            f"{self.parallel_execution!r})"
        )
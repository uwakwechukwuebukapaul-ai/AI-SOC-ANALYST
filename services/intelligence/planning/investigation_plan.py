"""
Sentinel DNA Investigation Plan
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class InvestigationStep:
    """
    Represents one execution step.
    """

    agent_name: str
    capability: str
    parallel: bool = False


@dataclass(slots=True)
class InvestigationPlan:
    """
    Ordered execution plan.
    """

    steps: list[InvestigationStep] = field(default_factory=list)

    def add_step(self, step: InvestigationStep) -> None:
        self.steps.append(step)

    def __len__(self) -> int:
        return len(self.steps)
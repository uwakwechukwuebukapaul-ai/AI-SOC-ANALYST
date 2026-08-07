"""
Sentinel DNA Runtime Policy Engine

Enterprise runtime decision policy layer.

Responsibilities:

- create policies
- evaluate runtime actions
- return execution decisions
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class RuntimePolicyEngine:
    """
    Runtime policy evaluation engine.
    """

    policies: dict[str, Callable] = field(
        default_factory=dict
    )

    evaluations: int = 0


    def register(
        self,
        name: str,
        rule: Callable,
    ) -> None:
        """
        Register policy rule.
        """

        self.policies[name] = rule



    def evaluate(
        self,
        name: str,
        context: dict[str, Any],
    ) -> bool:
        """
        Evaluate policy.
        """

        self.evaluations += 1


        rule = self.policies.get(
            name
        )


        if rule is None:
            return False


        return bool(
            rule(context)
        )



    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check policy existence.
        """

        return name in self.policies



    def clear(self) -> None:
        """
        Reset policies.
        """

        self.policies.clear()

        self.evaluations = 0



    def status(self) -> dict[str, Any]:
        """
        Policy engine status.
        """

        return {
            "policies":
                list(
                    self.policies.keys()
                ),

            "evaluations":
                self.evaluations,
        }
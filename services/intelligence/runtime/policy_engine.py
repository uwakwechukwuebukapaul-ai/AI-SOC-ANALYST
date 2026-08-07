"""
Sentinel DNA Runtime Policy Engine

Controls runtime execution decisions
through configurable policies.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class PolicyEngine:
    """
    Runtime policy evaluation engine.
    """

    policies: dict[str, Callable] = field(
        default_factory=dict
    )


    def register_policy(
        self,
        name: str,
        policy: Callable,
    ) -> None:
        """
        Register policy rule.
        """

        self.policies[name] = policy



    def remove_policy(
        self,
        name: str,
    ) -> None:
        """
        Remove policy rule.
        """

        self.policies.pop(
            name,
            None,
        )



    def evaluate(
        self,
        context: dict[str, Any],
    ) -> bool:
        """
        Evaluate all policies.

        Returns:
            True if execution is allowed.
        """

        for policy in self.policies.values():

            if policy(context) is False:
                return False

        return True



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
        Remove all policies.
        """

        self.policies.clear()



    def size(self) -> int:
        """
        Return policy count.
        """

        return len(self.policies)



    def to_dict(self) -> dict:
        """
        Export policy state.
        """

        return {
            "policy_count": self.size(),
            "policies": list(
                self.policies.keys()
            ),
        }
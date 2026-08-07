"""
Sentinel DNA Runtime Security Orchestrator

Enterprise runtime security governance layer.

Responsibilities:

- manage permissions
- enforce execution policies
- control runtime access
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any



@dataclass
class RuntimeSecurityOrchestrator:
    """
    Runtime security controller.
    """

    policies: dict[str, bool] = field(
        default_factory=dict
    )

    permissions: dict[str, list[str]] = field(
        default_factory=dict
    )



    def add_policy(
        self,
        name: str,
        enabled: bool = True,
    ) -> None:
        """
        Register security policy.
        """

        self.policies[name] = enabled



    def grant(
        self,
        actor: str,
        capability: str,
    ) -> None:
        """
        Grant runtime capability.
        """

        if actor not in self.permissions:
            self.permissions[actor] = []


        self.permissions[actor].append(
            capability
        )



    def authorize(
        self,
        actor: str,
        capability: str,
    ) -> bool:
        """
        Check permission.
        """

        return capability in (
            self.permissions.get(
                actor,
                [],
            )
        )



    def policy_enabled(
        self,
        name: str,
    ) -> bool:
        """
        Check policy state.
        """

        return self.policies.get(
            name,
            False,
        )



    def clear(self) -> None:
        """
        Reset security state.
        """

        self.policies.clear()

        self.permissions.clear()



    def status(self) -> dict[str, Any]:
        """
        Security status.
        """

        return {
            "policies":
                self.policies,

            "actors":
                list(
                    self.permissions.keys()
                ),
        }
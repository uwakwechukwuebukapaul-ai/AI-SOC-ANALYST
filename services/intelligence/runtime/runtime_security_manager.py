"""
Sentinel DNA Runtime Security Manager

Enterprise runtime security governance layer.

Responsibilities:

- manage permissions
- authorize actions
- enforce runtime policies
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeSecurityManager:
    """
    Runtime security policy manager.
    """

    permissions: dict[str, set[str]] = field(
        default_factory=dict
    )

    policies: dict[str, bool] = field(
        default_factory=dict
    )


    def grant(
        self,
        actor: str,
        permission: str,
    ) -> None:
        """
        Grant permission.
        """

        if actor not in self.permissions:
            self.permissions[actor] = set()

        self.permissions[actor].add(
            permission
        )



    def revoke(
        self,
        actor: str,
        permission: str,
    ) -> None:
        """
        Remove permission.
        """

        if actor in self.permissions:
            self.permissions[actor].discard(
                permission
            )



    def allowed(
        self,
        actor: str,
        permission: str,
    ) -> bool:
        """
        Check permission.
        """

        return permission in self.permissions.get(
            actor,
            set(),
        )



    def set_policy(
        self,
        name: str,
        enabled: bool,
    ) -> None:
        """
        Configure security policy.
        """

        self.policies[name] = enabled



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

        self.permissions.clear()

        self.policies.clear()



    def status(self) -> dict[str, Any]:
        """
        Security status.
        """

        return {
            "permissions":
                {
                    key: list(value)
                    for key, value
                    in self.permissions.items()
                },

            "policies":
                self.policies,
        }
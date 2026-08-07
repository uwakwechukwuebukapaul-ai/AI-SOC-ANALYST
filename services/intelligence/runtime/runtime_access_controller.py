"""
Sentinel DNA Runtime Access Controller

Enterprise authorization gateway.

Responsibilities:

- validate actor permissions
- evaluate runtime policies
- authorize execution requests
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_security_manager import (
    RuntimeSecurityManager,
)

from .runtime_policy_engine import (
    RuntimePolicyEngine,
)


@dataclass
class RuntimeAccessController:
    """
    Runtime authorization controller.
    """

    security: RuntimeSecurityManager = field(
        default_factory=RuntimeSecurityManager
    )

    policies: RuntimePolicyEngine = field(
        default_factory=RuntimePolicyEngine
    )

    checks: int = 0


    def authorize(
        self,
        actor: str,
        permission: str,
        policy: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> bool:
        """
        Authorize runtime action.
        """

        self.checks += 1


        if not self.security.allowed(
            actor,
            permission,
        ):
            return False


        if policy:

            return self.policies.evaluate(
                policy,
                context or {},
            )


        return True



    def grant(
        self,
        actor: str,
        permission: str,
    ) -> None:
        """
        Grant access.
        """

        self.security.grant(
            actor,
            permission,
        )



    def register_policy(
        self,
        name: str,
        rule,
    ) -> None:
        """
        Register access policy.
        """

        self.policies.register(
            name,
            rule,
        )



    def clear(self) -> None:
        """
        Reset access state.
        """

        self.security.clear()

        self.policies.clear()

        self.checks = 0



    def status(self) -> dict[str, Any]:
        """
        Controller status.
        """

        return {
            "checks":
                self.checks,

            "security":
                self.security.status(),

            "policies":
                self.policies.status(),
        }
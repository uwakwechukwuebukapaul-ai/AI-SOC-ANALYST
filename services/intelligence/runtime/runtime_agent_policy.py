"""
Sentinel DNA Runtime Agent Policy Engine

Controls runtime agent permissions.

Responsibilities:

- register policies
- evaluate actions
- allow or deny execution
- expose policy status
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentPolicy:
    """
    Agent execution policy.
    """

    agent_id: str

    allowed_actions: list[str] = field(
        default_factory=list
    )

    denied_actions: list[str] = field(
        default_factory=list
    )


@dataclass
class RuntimeAgentPolicyEngine:
    """
    Runtime agent governance engine.
    """

    policies: dict[str, AgentPolicy] = field(
        default_factory=dict
    )


    def register(
        self,
        agent_id: str,
        allowed_actions: list[str] | None = None,
        denied_actions: list[str] | None = None,
    ) -> None:
        """
        Register agent policy.
        """

        self.policies[agent_id] = AgentPolicy(
            agent_id=agent_id,
            allowed_actions=(
                allowed_actions or []
            ),
            denied_actions=(
                denied_actions or []
            ),
        )


    def allow(
        self,
        agent_id: str,
        action: str,
    ) -> bool:
        """
        Add allowed action.
        """

        policy = self.policies.get(
            agent_id
        )

        if not policy:
            return False


        if action not in policy.allowed_actions:
            policy.allowed_actions.append(
                action
            )

        return True



    def deny(
        self,
        agent_id: str,
        action: str,
    ) -> bool:
        """
        Add denied action.
        """

        policy = self.policies.get(
            agent_id
        )

        if not policy:
            return False


        if action not in policy.denied_actions:
            policy.denied_actions.append(
                action
            )

        return True



    def evaluate(
        self,
        agent_id: str,
        action: str,
    ) -> bool:
        """
        Evaluate execution permission.
        """

        policy = self.policies.get(
            agent_id
        )

        if not policy:
            return False


        if action in policy.denied_actions:
            return False


        if action in policy.allowed_actions:
            return True


        return False



    def exists(
        self,
        agent_id: str,
    ) -> bool:
        """
        Check policy existence.
        """

        return agent_id in self.policies



    def remove(
        self,
        agent_id: str,
    ) -> bool:
        """
        Remove policy.
        """

        if agent_id not in self.policies:
            return False


        del self.policies[agent_id]

        return True



    def clear(
        self,
    ) -> None:
        """
        Clear policies.
        """

        self.policies.clear()



    def status(
        self,
    ) -> dict[str, Any]:
        """
        Policy engine status.
        """

        return {
            "policies": len(
                self.policies
            ),
            "agents": {
                key: vars(value)
                for key, value in self.policies.items()
            },
        }
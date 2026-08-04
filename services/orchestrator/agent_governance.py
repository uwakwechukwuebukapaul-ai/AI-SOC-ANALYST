"""
Sentinel DNA
Enterprise Agent Governance Layer

Responsible for:
- Agent permissions
- Action approval policies
- Autonomy levels
- Governance enforcement

Author: Sentinel DNA
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List, Any


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class AgentPolicy:
    """
    Defines governance policy for an agent.
    """

    agent_name: str

    permissions: List[str] = field(
        default_factory=list
    )

    autonomy_level: int = 1

    approval_required: bool = True

    status: str = "ACTIVE"

    created_at: str = field(
        default_factory=utc_now
    )


class AgentGovernance:
    """
    Enterprise governance controller.

    Controls:
    - agent permissions
    - autonomous action levels
    - approval requirements
    - policy enforcement
    """

    def __init__(self):

        self.policies: Dict[str, AgentPolicy] = {}


    def register_policy(
        self,
        agent_name: str,
        permissions: List[str],
        autonomy_level: int = 1,
        approval_required: bool = True,
    ) -> AgentPolicy:

        if agent_name in self.policies:
            raise ValueError(
                f"Policy already exists for {agent_name}"
            )

        policy = AgentPolicy(
            agent_name=agent_name,
            permissions=permissions,
            autonomy_level=autonomy_level,
            approval_required=approval_required,
        )

        self.policies[agent_name] = policy

        return policy


    def get_policy(
        self,
        agent_name: str
    ) -> AgentPolicy:

        if agent_name not in self.policies:

            raise ValueError(
                f"Unknown agent policy: {agent_name}"
            )

        return self.policies[agent_name]


    def has_permission(
        self,
        agent_name: str,
        permission: str
    ) -> bool:

        policy = self.get_policy(
            agent_name
        )

        return permission in policy.permissions


    def can_execute(
        self,
        agent_name: str,
        action: str,
    ) -> Dict[str, Any]:

        policy = self.get_policy(
            agent_name
        )

        allowed = (
            action in policy.permissions
        )

        return {

            "agent": agent_name,

            "action": action,

            "allowed": allowed,

            "approval_required": (
                policy.approval_required
            ),

            "autonomy_level": (
                policy.autonomy_level
            ),

        }


    def update_autonomy_level(
        self,
        agent_name: str,
        level: int
    ) -> AgentPolicy:

        policy = self.get_policy(
            agent_name
        )

        policy.autonomy_level = level

        return policy


    def disable_agent(
        self,
        agent_name: str
    ) -> AgentPolicy:

        policy = self.get_policy(
            agent_name
        )

        policy.status = "DISABLED"

        return policy


    def list_policies(
        self
    ) -> List[Dict[str, Any]]:

        return [

            {
                "agent_name": policy.agent_name,

                "permissions": policy.permissions,

                "autonomy_level": policy.autonomy_level,

                "approval_required": policy.approval_required,

                "status": policy.status,

            }

            for policy in self.policies.values()

        ]
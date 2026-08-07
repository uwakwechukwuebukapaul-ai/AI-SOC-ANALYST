"""
Sentinel DNA Runtime Agent Lifecycle Service

Enterprise agent lifecycle coordination layer.

Responsibilities:

- register agents
- start agents
- stop agents
- pause agents
- resume agents
- remove agents
- expose lifecycle status
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_agent_registry import (
    RuntimeAgentRegistry,
)

from .runtime_agent_health import (
    RuntimeAgentHealthManager,
)

from .runtime_agent_lifecycle import (
    RuntimeAgentLifecycleManager,
)


@dataclass
class RuntimeAgentLifecycleService:
    """
    Coordinates runtime agent lifecycle.
    """

    registry: RuntimeAgentRegistry = field(
        default_factory=RuntimeAgentRegistry
    )

    health: RuntimeAgentHealthManager = field(
        default_factory=RuntimeAgentHealthManager
    )

    lifecycle: RuntimeAgentLifecycleManager = field(
        default_factory=RuntimeAgentLifecycleManager
    )


    def register(
        self,
        agent: Any,
    ) -> None:
        """
        Register runtime agent.
        """

        agent_id = getattr(
            agent,
            "name",
            None,
        )

        if not agent_id:
            raise ValueError(
                "Agent requires name"
            )


        self.registry.register(
            agent
        )

        self.health.register(
            agent_id
        )

        self.lifecycle.register(
            agent_id
        )


    def start(
        self,
        agent_id: str,
    ) -> bool:
        """
        Start agent.
        """

        result = self.lifecycle.start(
            agent_id
        )

        if result:
            self.health.set_status(
                agent_id,
                "ACTIVE",
            )

        return result



    def pause(
        self,
        agent_id: str,
    ) -> bool:
        """
        Pause agent.
        """

        result = self.lifecycle.pause(
            agent_id
        )

        if result:
            self.health.set_status(
                agent_id,
                "PAUSED",
            )

        return result



    def resume(
        self,
        agent_id: str,
    ) -> bool:
        """
        Resume agent.
        """

        result = self.lifecycle.resume(
            agent_id
        )

        if result:
            self.health.set_status(
                agent_id,
                "ACTIVE",
            )

        return result



    def stop(
        self,
        agent_id: str,
    ) -> bool:
        """
        Stop agent.
        """

        result = self.lifecycle.stop(
            agent_id
        )

        if result:
            self.health.set_status(
                agent_id,
                "STOPPED",
            )

        return result



    def remove(
        self,
        agent_id: str,
    ) -> bool:
        """
        Remove agent.
        """

        lifecycle_removed = self.lifecycle.remove(
            agent_id
        )

        self.registry.remove(
            agent_id
        )

        self.health.agents.pop(
            agent_id,
            None,
        )

        return lifecycle_removed



    def status(
        self,
    ) -> dict[str, Any]:
        """
        Service status.
        """

        return {
            "registry": self.registry.status(),
            "health": self.health.status(),
            "lifecycle": self.lifecycle.status(),
        }



    def clear(
        self,
    ) -> None:
        """
        Clear all state.
        """

        self.registry.clear()

        self.health.clear()

        self.lifecycle.clear()
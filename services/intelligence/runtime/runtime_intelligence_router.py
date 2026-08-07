"""
Sentinel DNA Runtime Intelligence Router

Enterprise intelligence routing layer.

Supports:

- agent based routing
- capability based routing
- handler execution
- legacy pipeline compatibility
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from .task import Task

from .runtime_agent_orchestrator import (
    RuntimeAgentOrchestrator,
)


@dataclass
class RuntimeIntelligenceRouter:
    """
    Routes intelligence execution requests.
    """

    orchestrator: RuntimeAgentOrchestrator = field(
        default_factory=RuntimeAgentOrchestrator
    )

    handlers: dict[str, Callable] = field(
        default_factory=dict
    )

    routes: int = 0


    def register_agent(
        self,
        agent: Any,
    ) -> None:
        """
        Register runtime agent.
        """

        self.orchestrator.register_agent(
            agent
        )

        self.routes += 1



    def register(
        self,
        capability,
        handler=None,
    ) -> None:
        """
        Register capability route.

        Supports:

        register(agent)

        register(capability, handler)
        """

        if handler is None:

            self.register_agent(
                capability
            )

            return


        self.handlers[capability] = handler

        self.routes += 1



    def available(
        self,
        capability: str,
    ) -> bool:
        """
        Check capability availability.
        """

        if capability in self.handlers:
            return True


        return self.orchestrator.has_capability(
            capability
        )



    def route(
        self,
        capability_or_task,
        payload=None,
    ) -> Any:
        """
        Route intelligence execution.

        Supports:

        route(Task)

        route(
            capability,
            payload
        )
        """

        if isinstance(
            capability_or_task,
            Task,
        ):

            return self.orchestrator.execute(
                capability_or_task
            )


        capability = capability_or_task


        handler = self.handlers.get(
            capability
        )


        if handler:

            self.routes += 1

            return handler(
                payload
            )


        if self.orchestrator.has_capability(
            capability
        ):

            return self.orchestrator.submit(
                capability,
                payload or {},
            )


        return None



    def clear(
        self,
    ) -> None:
        """
        Clear routing state.
        """

        self.handlers.clear()

        self.orchestrator.clear()

        self.routes = 0



    def status(
        self,
    ) -> dict[str, Any]:
        """
        Router status.
        """

        return {
            "routes": self.routes,

            "handlers": list(
                self.handlers.keys()
            ),

            "agents":
                self.orchestrator.agent_count(),

            "orchestrator":
                self.orchestrator.status(),
        }
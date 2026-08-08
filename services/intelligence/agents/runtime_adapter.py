"""
Sentinel DNA Agent Runtime Adapter

Bridges Intelligence Agents with RuntimeTaskExecutor.
"""

from __future__ import annotations

from typing import Any

from services.intelligence.runtime.task import Task
from services.intelligence.agents.base_agent import BaseAgent


class AgentRuntimeAdapter:
    """
    Registers AI agents into the runtime execution layer.
    """

    def __init__(
        self,
        runtime_executor,
    ) -> None:

        self.runtime_executor = runtime_executor


    def register_agent(
        self,
        agent: BaseAgent,
    ) -> None:
        """
        Register agent capabilities with runtime.
        """

        for capability in agent.capabilities:

            capability_name = getattr(
                capability,
                "value",
                None,
            )

            if capability_name is None:

                capability_name = getattr(
                    capability,
                    "name",
                    None,
                )

            if capability_name is None:
                continue


            self.runtime_executor.register(
                capability_name,
                self._create_handler(agent),
            )


    def _create_handler(
        self,
        agent: BaseAgent,
    ):

        def handler(
            payload: dict[str, Any],
        ):

            context = payload.get(
                "context"
            )

            return agent.execute(
                context
            )

        return handler
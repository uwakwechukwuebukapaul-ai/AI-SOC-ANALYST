"""
Sentinel DNA Agent Dispatcher
"""

from __future__ import annotations

from services.intelligence.agents.agent_context import AgentContext
from services.intelligence.agents.agent_registry import AgentRegistry
from services.intelligence.agents.agent_result import (
    AgentExecutionStatus,
    AgentResult,
)


class AgentDispatcher:
    """
    Executes registered AI agents.
    """

    def __init__(
        self,
        registry: AgentRegistry,
    ) -> None:

        self._registry = registry

    def dispatch(
        self,
        agent_name: str,
        context: AgentContext,
    ) -> AgentResult:
        """
        Execute a registered agent.
        """

        agent = self._registry.get(agent_name)

        if agent is None:

            return AgentResult(
                agent_name=agent_name,
                status=AgentExecutionStatus.FAILED,
                errors=[
                    f"Agent '{agent_name}' not found."
                ],
            )

        if not agent.validate(context):

            return AgentResult(
                agent_name=agent.metadata.name,
                status=AgentExecutionStatus.FAILED,
                errors=[
                    "Context validation failed."
                ],
            )

        try:

            return agent.execute(context)

        except Exception as exc:

            return AgentResult(
                agent_name=agent.metadata.name,
                status=AgentExecutionStatus.FAILED,
                errors=[str(exc)],
            )
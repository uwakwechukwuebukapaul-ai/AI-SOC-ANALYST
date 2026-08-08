"""
Sentinel DNA Agent Pipeline

Executes investigation plans through registered agents.
"""

from typing import Any

from .orchestration_result import (
    OrchestrationResult,
)


class AgentPipeline:
    """
    Executes investigation agents from an orchestration plan.
    """

    def __init__(
        self,
        registry,
        runtime=None,
    ):
        self.registry = registry
        self.runtime = runtime


    def execute(
        self,
        plan,
        context,
    ) -> OrchestrationResult:
        """
        Execute all agents in an investigation plan.
        """

        result = OrchestrationResult(
            plan_name=getattr(
                plan,
                "name",
                "unknown",
            )
        )


        agents = getattr(
            plan,
            "agents",
            [],
        )


        if not agents:

            result.add_error(
                "No investigation agents defined"
            )

            return result


        for agent_name in agents:

            agent = self.registry.get(
                agent_name
            )


            if agent is None:

                result.add_error(
                    f"Agent not found: {agent_name}"
                )

                continue


            try:

                if self.runtime:

                    agent_result = self.runtime.execute(
                        agent_name,
                        context,
                    )

                else:

                    agent_result = agent.execute(
                        context
                    )


                result.add_agent_result(
                    agent_name,
                    agent_result,
                )


            except Exception as exc:

                result.add_error(
                    f"Agent execution failed: {agent_name}: {exc}"
                )


        return result
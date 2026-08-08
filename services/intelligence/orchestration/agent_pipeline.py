"""
Sentinel DNA Agent Pipeline

Canonical investigation execution adapter.

Architecture:

InvestigationCoordinator
        |
        v
AgentPipeline
        |
        v
Runtime Task
        |
        v
RuntimeTaskExecutor
        |
        v
Agent Capability Handler
        |
        v
BaseAgent.execute()

The pipeline translates orchestration plans into runtime execution.
"""


from __future__ import annotations

from typing import Any


from services.intelligence.orchestration.orchestration_result import (
    OrchestrationResult,
)

from services.intelligence.runtime.task import (
    Task,
)


class AgentPipeline:
    """
    Canonical investigation execution adapter.
    """


    def __init__(
        self,
        registry: Any,
        runtime: Any | None = None,
    ) -> None:

        self.registry = registry
        self.runtime = runtime



    # --------------------------------------------------------------
    # Execute investigation plan
    # --------------------------------------------------------------

    def execute(
        self,
        plan: Any,
        context: Any,
    ) -> OrchestrationResult:

        output = OrchestrationResult(
            plan_name=plan.name,
        )


        for agent_name in plan.agents:

            try:

                result = self._execute_agent(
                    agent_name,
                    context,
                )


                if result is None:

                    output.add_error(
                        f"Agent execution returned no result: {agent_name}"
                    )

                    continue


                output.add_agent_result(
                    agent_name,
                    result,
                )


            except Exception as error:

                output.add_error(
                    f"{agent_name}: {error}"
                )


        return output



    # --------------------------------------------------------------
    # Agent execution
    # --------------------------------------------------------------

    def _execute_agent(
        self,
        agent_name: str,
        context: Any,
    ) -> Any:


        agent = self._resolve_agent(
            agent_name
        )


        if agent is None:

            return None


        if self.runtime:

            return self._execute_runtime_agent(
                agent_name,
                agent,
                context,
            )


        return agent.execute(
            context
        )



    # --------------------------------------------------------------
    # Runtime execution
    # --------------------------------------------------------------

    def _execute_runtime_agent(
        self,
        agent_name: str,
        agent: Any,
        context: Any,
    ) -> Any:


        capability = self._resolve_capability(
            agent_name,
            agent,
        )


        task = Task(
            capability=capability,
            payload={
                "context": context
            },
            metadata={
                "agent_name": agent_name,
                "source": "agent_pipeline",
            },
        )


        execute = getattr(
            self.runtime,
            "execute",
            None,
        )


        if not callable(execute):

            raise RuntimeError(
                "Runtime executor unavailable"
            )


        result = execute(
            task
        )


        return result



    # --------------------------------------------------------------
    # Agent resolution
    # --------------------------------------------------------------

    def _resolve_agent(
        self,
        agent_name: str,
    ) -> Any | None:


        name = agent_name.strip()



        get = getattr(
            self.registry,
            "get",
            None,
        )


        if callable(get):

            agent = get(name)

            if agent:

                return agent



        list_agents = getattr(
            self.registry,
            "list_agents",
            None,
        )


        if callable(list_agents):

            for agent in list_agents():

                metadata = getattr(
                    agent,
                    "metadata",
                    None,
                )


                if metadata and metadata.name == name:

                    return agent



        return None



    # --------------------------------------------------------------
    # Capability mapping
    # --------------------------------------------------------------

    def _resolve_capability(
        self,
        agent_name: str,
        agent: Any,
    ) -> str:


        capabilities = getattr(
            agent,
            "capabilities",
            [],
        )


        if callable(capabilities):

            capabilities = capabilities()



        if capabilities:

            capability = capabilities[0]


            value = getattr(
                capability,
                "value",
                None,
            )


            if value:

                return value



            name = getattr(
                capability,
                "name",
                None,
            )


            if name:

                return name



        mapping = {

            "Investigation Agent":
                "investigation_execution",

            "IOC Enrichment Agent":
                "ioc_enrichment",

            "Threat Intelligence Agent":
                "threat_intelligence",

        }


        return mapping.get(
            agent_name,
            agent_name,
        )
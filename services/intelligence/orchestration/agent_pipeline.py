from services.intelligence.agents.agent_result import AgentResult
from services.intelligence.orchestration.orchestration_result import (
    OrchestrationResult,
)


class AgentPipeline:
    """
    Executes agents according to an investigation plan.
    """


    def __init__(self, registry):

        self.registry = registry



    def execute(
        self,
        plan,
        context
    ):

        output = OrchestrationResult(
            plan_name=plan.name
        )


        for agent_name in plan.agents:

            try:

                agent = self.registry.get(agent_name)

                if not agent:
                    output.add_error(
                        f"Agent not found: {agent_name}"
                    )
                    continue


                result = agent.execute(context)


                output.add_agent_result(
                    agent_name,
                    result
                )


            except Exception as error:

                output.add_error(
                    str(error)
                )


        return output
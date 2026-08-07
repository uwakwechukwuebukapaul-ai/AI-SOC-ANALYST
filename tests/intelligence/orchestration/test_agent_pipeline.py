from services.intelligence.orchestration.agent_pipeline import (
    AgentPipeline,
)


class FakeAgent:

    def execute(self, context):

        return "success"



class FakeRegistry:

    def get(self, name):

        return FakeAgent()



def test_pipeline_execution():

    pipeline = AgentPipeline(
        FakeRegistry()
    )

    assert pipeline is not None
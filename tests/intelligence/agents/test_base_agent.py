"""
Tests for BaseAgent.
"""

from services.intelligence.agents.base_agent import BaseAgent
from services.intelligence.agents.agent_metadata import AgentMetadata
from services.intelligence.agents.agent_capability import AgentCapability
from services.intelligence.agents.agent_context import AgentContext
from services.intelligence.agents.agent_result import (
    AgentResult,
    AgentExecutionStatus,
)


class FakeAgent(BaseAgent):

    @property
    def metadata(self) -> AgentMetadata:
        return AgentMetadata(
            name="Fake Agent",
            version="1.0",
            description="Testing agent",
        )

    @property
    def capabilities(self) -> list[AgentCapability]:
        return [
            AgentCapability(
                name="testing",
                description="Testing capability",
                category="testing",
            )
        ]

    def validate(
        self,
        context: AgentContext,
    ) -> bool:
        return True

    def execute(
        self,
        context: AgentContext,
    ) -> AgentResult:

        return AgentResult(
            agent_name=self.metadata.name,
            status=AgentExecutionStatus.SUCCESS,
            confidence=100.0,
        )

    def summarize(
        self,
        result: AgentResult,
    ) -> str:
        return "success"

    def cleanup(self) -> None:
        pass


def build_context():

    return AgentContext(
        investigation_id="INV-001",
        case_id="CASE-001",
    )


def test_metadata():

    agent = FakeAgent()

    assert agent.metadata.name == "Fake Agent"

    assert agent.metadata.version == "1.0"


def test_execute():

    agent = FakeAgent()

    result = agent.execute(build_context())

    assert result.successful()


def test_summary():

    agent = FakeAgent()

    result = agent.execute(build_context())

    assert agent.summarize(result) == "success"


def test_validation():

    agent = FakeAgent()

    assert agent.validate(build_context()) is True


def test_repr():

    agent = FakeAgent()

    assert "FakeAgent" in repr(agent)
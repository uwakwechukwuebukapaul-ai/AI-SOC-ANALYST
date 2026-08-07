"""
Tests for AgentDispatcher.
"""

from services.intelligence.agents.agent_capability import AgentCapability
from services.intelligence.agents.agent_context import AgentContext
from services.intelligence.agents.agent_dispatcher import AgentDispatcher
from services.intelligence.agents.agent_metadata import AgentMetadata
from services.intelligence.agents.agent_registry import AgentRegistry
from services.intelligence.agents.agent_result import (
    AgentExecutionStatus,
    AgentResult,
)
from services.intelligence.agents.base_agent import BaseAgent


class FakeAgent(BaseAgent):

    @property
    def metadata(self):
        return AgentMetadata(
            name="Fake Agent",
            version="1.0",
            description="Testing",
        )

    @property
    def capabilities(self):
        return [
            AgentCapability(
                name="testing",
                description="Testing",
                category="testing",
            )
        ]

    def validate(self, context):
        return True

    def execute(self, context):
        return AgentResult(
            agent_name=self.metadata.name,
            status=AgentExecutionStatus.SUCCESS,
            confidence=100,
        )

    def summarize(self, result):
        return "success"

    def cleanup(self):
        pass


def build_context():

    return AgentContext(
        investigation_id="INV-1",
        case_id="CASE-1",
    )


def test_dispatch():

    registry = AgentRegistry()

    registry.register(FakeAgent())

    dispatcher = AgentDispatcher(registry)

    result = dispatcher.dispatch(
        "Fake Agent",
        build_context(),
    )

    assert result.status == AgentExecutionStatus.SUCCESS


def test_missing_agent():

    dispatcher = AgentDispatcher(
        AgentRegistry()
    )

    result = dispatcher.dispatch(
        "Unknown",
        build_context(),
    )

    assert result.status == AgentExecutionStatus.FAILED


def test_registry_reference():

    registry = AgentRegistry()

    dispatcher = AgentDispatcher(registry)

    assert dispatcher._registry is registry
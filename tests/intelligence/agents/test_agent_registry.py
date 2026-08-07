"""
Tests for AgentRegistry.
"""

from services.intelligence.agents.agent_capability import AgentCapability
from services.intelligence.agents.agent_context import AgentContext
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
            description="Test",
        )

    @property
    def capabilities(self):
        return [
            AgentCapability(
                name="testing",
                description="Test capability",
                category="testing",
            )
        ]

    def validate(self, context: AgentContext):
        return True

    def execute(self, context: AgentContext):
        return AgentResult(
            agent_name=self.metadata.name,
            status=AgentExecutionStatus.SUCCESS,
        )

    def summarize(self, result):
        return "ok"

    def cleanup(self):
        pass


def test_register():

    registry = AgentRegistry()

    registry.register(FakeAgent())

    assert registry.count() == 1


def test_get():

    registry = AgentRegistry()

    registry.register(FakeAgent())

    assert registry.get("Fake Agent") is not None


def test_capability_lookup():

    registry = AgentRegistry()

    registry.register(FakeAgent())

    agents = registry.find_by_capability(
        "testing"
    )

    assert len(agents) == 1


def test_unregister():

    registry = AgentRegistry()

    registry.register(FakeAgent())

    registry.unregister("Fake Agent")

    assert registry.count() == 0


def test_clear():

    registry = AgentRegistry()

    registry.register(FakeAgent())

    registry.clear()

    assert registry.count() == 0
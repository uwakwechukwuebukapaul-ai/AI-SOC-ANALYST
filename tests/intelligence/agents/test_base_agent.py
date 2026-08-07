"""
Tests for BaseAgent.
"""

from services.intelligence.agents.base_agent import (
    BaseAgent,
)


class FakeAgent(BaseAgent):

    @property
    def name(self):
        return "Fake Agent"

    @property
    def version(self):
        return "1.0"

    @property
    def description(self):
        return "Testing"

    @property
    def capabilities(self):
        return ["testing"]

    def validate(self, context):

        return True

    def execute(self, context):

        return context

    def summarize(self, result):

        return "success"

    def cleanup(self):

        return None


def test_metadata():

    agent = FakeAgent()

    metadata = agent.metadata()

    assert metadata["name"] == "Fake Agent"

    assert metadata["version"] == "1.0"

    assert metadata["capabilities"] == [
        "testing"
    ]


def test_execute():

    agent = FakeAgent()

    assert (
        agent.execute("hello")
        ==
        "hello"
    )


def test_summary():

    agent = FakeAgent()

    assert (
        agent.summarize(None)
        ==
        "success"
    )


def test_validation():

    agent = FakeAgent()

    assert (
        agent.validate({})
        is True
    )


def test_repr():

    agent = FakeAgent()

    assert "FakeAgent" in repr(agent)
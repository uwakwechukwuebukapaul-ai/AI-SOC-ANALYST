import pytest

from services.orchestrator.agent_learning import (
    AgentLearningEngine
)


@pytest.fixture
def learning():
    return AgentLearningEngine()



def test_store_feedback(learning):

    result = learning.record_feedback(
        agent_name="threat_agent",
        task="phishing_detection",
        success=True,
        confidence=95
    )

    assert result["agent"] == "threat_agent"



def test_agent_performance(learning):

    learning.record_feedback(
        "ioc_agent",
        "ioc_lookup",
        True,
        90
    )

    learning.record_feedback(
        "ioc_agent",
        "ioc_lookup",
        False,
        50
    )

    result = learning.get_agent_performance(
        "ioc_agent"
    )

    assert result["executions"] == 2
    assert result["success_rate"] == 50



def test_agent_recommendation(learning):

    learning.record_feedback(
        "agent_a",
        "analysis",
        True,
        90
    )

    learning.record_feedback(
        "agent_b",
        "analysis",
        True,
        70
    )

    result = learning.recommend_agent(
        [
            "agent_a",
            "agent_b"
        ]
    )

    assert result["agent"] == "agent_a"



def test_empty_agent_performance(learning):

    result = learning.get_agent_performance(
        "unknown"
    )

    assert result["executions"] == 0



def test_learning_history(learning):

    learning.record_feedback(
        "agent",
        "task",
        True,
        80
    )

    history = learning.learning_history()

    assert len(history) == 1



def test_clear_learning(learning):

    learning.record_feedback(
        "agent",
        "task",
        True,
        80
    )

    learning.clear_learning()

    assert len(
        learning.learning_history()
    ) == 0
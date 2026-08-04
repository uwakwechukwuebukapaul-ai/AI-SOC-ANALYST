"""
Tests for Sentinel DNA Agent Memory
"""

from services.orchestrator.agent_memory import (
    AgentMemory,
)


def test_store_agent_memory():

    memory = AgentMemory()

    record = memory.remember(
        agent_name="threat_agent",
        success=True,
    )

    assert record.agent_name == "threat_agent"

    assert record.success is True



def test_agent_history_lookup():

    memory = AgentMemory()

    memory.remember(
        agent_name="ioc_agent",
        success=True,
    )

    history = memory.get_agent_history(
        "ioc_agent"
    )

    assert len(history) == 1



def test_success_rate():

    memory = AgentMemory()

    memory.remember(
        agent_name="risk_agent",
        success=True,
    )

    memory.remember(
        agent_name="risk_agent",
        success=False,
    )

    rate = memory.get_success_rate(
        "risk_agent"
    )

    assert rate == 0.5



def test_empty_agent_success_rate():

    memory = AgentMemory()

    assert (
        memory.get_success_rate(
            "unknown"
        )
        == 0.0
    )



def test_clear_memory():

    memory = AgentMemory()

    memory.remember(
        agent_name="summary_agent",
        success=True,
    )

    memory.clear()

    assert len(
        memory.get_all_records()
    ) == 0
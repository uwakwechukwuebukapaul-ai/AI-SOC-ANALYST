"""
Runtime Agent Orchestrator Tests
"""

from services.intelligence.runtime.runtime_agent_orchestrator import (
    RuntimeAgentOrchestrator,
)



def test_init():

    orchestrator = RuntimeAgentOrchestrator()

    assert (
        orchestrator.executions
        ==
        0
    )



def test_register_agent():

    orchestrator = RuntimeAgentOrchestrator()


    orchestrator.register_agent(
        "investigation_agent",
        [
            "investigate",
        ],
    )


    assert (
        orchestrator.agent_count()
        ==
        1
    )



def test_submit():

    orchestrator = RuntimeAgentOrchestrator()


    orchestrator.register_agent(
        "intel_agent",
        [
            "ioc_lookup",
        ],
    )


    result = orchestrator.submit(
        "ioc_lookup",
        {
            "ioc": "example.com"
        },
    )


    assert (
        result
        ==
        "intel_agent"
    )



def test_missing_agent():

    orchestrator = RuntimeAgentOrchestrator()


    result = orchestrator.submit(
        "unknown",
        {},
    )


    assert result is None



def test_clear():

    orchestrator = RuntimeAgentOrchestrator()


    orchestrator.register_agent(
        "agent",
        [],
    )


    orchestrator.clear()


    assert (
        orchestrator.agent_count()
        ==
        0
    )



def test_status():

    orchestrator = RuntimeAgentOrchestrator()


    result = orchestrator.status()


    assert "agents" in result

    assert "executions" in result
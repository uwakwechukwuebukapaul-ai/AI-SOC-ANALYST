"""
Runtime Investigation Orchestrator Tests
"""

from services.intelligence.runtime.runtime_investigation_orchestrator import (
    RuntimeInvestigationOrchestrator,
)

from services.intelligence.runtime.runtime_agent_runtime import (
    RuntimeAgentRuntime,
)



def create_agent():

    agent = RuntimeAgentRuntime(
        "investigation_agent"
    )


    agent.add_capability(
        "investigation"
    )


    agent.gateway.access.grant(
        "investigation_agent",
        "execute",
    )


    agent.gateway.execution.start()


    agent.gateway.execution.workers.executor.register(
        "investigation",
        lambda data: {
            "result":
                "complete"
        },
    )


    return agent



def test_init():

    orchestrator = RuntimeInvestigationOrchestrator()

    assert (
        orchestrator.count()
        ==
        0
    )



def test_register_agent():

    orchestrator = RuntimeInvestigationOrchestrator()


    orchestrator.register_agent(
        create_agent()
    )


    assert (
        orchestrator.router.available(
            "investigation"
        )
        is True
    )



def test_investigate():

    orchestrator = RuntimeInvestigationOrchestrator()


    orchestrator.register_agent(
        create_agent()
    )


    result = orchestrator.investigate(
        "investigation",
        {
            "ioc":
                "malicious-domain.com"
        },
    )


    assert (
        result["result"]
        ==
        "complete"
    )



def test_count():

    orchestrator = RuntimeInvestigationOrchestrator()


    orchestrator.register_agent(
        create_agent()
    )


    orchestrator.investigate(
        "investigation",
        {},
    )


    assert (
        orchestrator.count()
        ==
        1
    )



def test_clear():

    orchestrator = RuntimeInvestigationOrchestrator()


    orchestrator.clear()


    assert (
        orchestrator.count()
        ==
        0
    )



def test_status():

    orchestrator = RuntimeInvestigationOrchestrator()


    result = orchestrator.status()


    assert "investigations" in result

    assert "router" in result
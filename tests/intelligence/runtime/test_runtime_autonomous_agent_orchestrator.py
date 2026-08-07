"""
Runtime Autonomous Agent Orchestrator Tests
"""

from services.intelligence.runtime.runtime_autonomous_agent_orchestrator import (
    RuntimeAutonomousAgentOrchestrator,
)

from services.intelligence.runtime.runtime_agent_runtime import (
    RuntimeAgentRuntime,
)



def create_agent():

    agent = RuntimeAgentRuntime(
        "autonomous_agent"
    )

    agent.add_capability(
        "analysis"
    )

    return agent



def test_init():

    orchestrator = RuntimeAutonomousAgentOrchestrator()

    assert (
        orchestrator.objectives
        ==
        0
    )



def test_register_agent():

    orchestrator = RuntimeAutonomousAgentOrchestrator()


    orchestrator.register_agent(
        create_agent()
    )


    assert (
        orchestrator.agent_count()
        ==
        1
    )



def test_register_reasoner():

    orchestrator = RuntimeAutonomousAgentOrchestrator()


    orchestrator.register_reasoner(
        "investigator",
        lambda ctx: {
            "decision":
                "analyze"
        },
    )


    assert (
        orchestrator.reasoning.available(
            "investigator"
        )
        is True
    )



def test_execute_objective():

    orchestrator = RuntimeAutonomousAgentOrchestrator()


    orchestrator.register_reasoner(
        "risk",
        lambda ctx: {
            "risk":
                "high"
        },
    )


    result = orchestrator.execute_objective(
        "risk",
        {},
    )


    assert (
        result["risk"]
        ==
        "high"
    )



def test_clear():

    orchestrator = RuntimeAutonomousAgentOrchestrator()


    orchestrator.register_agent(
        create_agent()
    )


    orchestrator.clear()


    assert (
        orchestrator.agent_count()
        ==
        0
    )



def test_status():

    orchestrator = RuntimeAutonomousAgentOrchestrator()


    result = orchestrator.status()


    assert "agents" in result

    assert "reasoning" in result

    assert "objectives" in result
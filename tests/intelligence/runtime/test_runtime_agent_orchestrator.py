"""
Runtime Agent Orchestrator Tests
"""

from services.intelligence.runtime.runtime_agent_orchestrator import (
    RuntimeAgentOrchestrator,
)

from services.intelligence.runtime.runtime_agent_runtime import (
    RuntimeAgentRuntime,
)

from services.intelligence.runtime.task import (
    Task,
)



def create_agent():

    agent = RuntimeAgentRuntime(
        "analysis_agent"
    )

    agent.add_capability(
        "analysis"
    )

    return agent



def create_task():

    return Task(
        capability="analysis",
        payload={
            "test":
                True
        },
    )



def test_init():

    orchestrator = RuntimeAgentOrchestrator()

    assert (
        orchestrator.agent_count()
        ==
        0
    )



def test_register_agent():

    orchestrator = RuntimeAgentOrchestrator()


    orchestrator.register_agent(
        create_agent()
    )


    assert (
        orchestrator.agent_count()
        ==
        1
    )



def test_execute():

    orchestrator = RuntimeAgentOrchestrator()


    agent = create_agent()


    agent.gateway.access.grant(
        "analysis_agent",
        "execute",
    )


    agent.gateway.execution.start()


    agent.gateway.execution.workers.executor.register(
        "analysis",
        lambda data: {
            "done":
                True
        },
    )


    orchestrator.register_agent(
        agent
    )


    result = orchestrator.execute(
        create_task()
    )


    assert (
        result["done"]
        is True
    )



def test_clear():

    orchestrator = RuntimeAgentOrchestrator()


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

    orchestrator = RuntimeAgentOrchestrator()


    result = orchestrator.status()


    assert "agents" in result

    assert "executions" in result
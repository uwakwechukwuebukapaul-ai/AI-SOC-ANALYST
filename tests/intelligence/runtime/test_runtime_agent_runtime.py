"""
Runtime Agent Runtime Tests
"""

from services.intelligence.runtime.runtime_agent_runtime import (
    RuntimeAgentRuntime,
)

from services.intelligence.runtime.task import (
    Task,
)



def create_task():

    return Task(
        capability="analysis",
        payload={
            "test":
                True
        },
    )



def test_init():

    agent = RuntimeAgentRuntime(
        "analyst_agent"
    )


    assert (
        agent.name
        ==
        "analyst_agent"
    )



def test_capability():

    agent = RuntimeAgentRuntime(
        "agent"
    )


    agent.add_capability(
        "analysis"
    )


    assert (
        agent.can_execute(
            "analysis"
        )
        is True
    )



def test_execute():

    agent = RuntimeAgentRuntime(
        "agent"
    )


    agent.add_capability(
        "analysis"
    )


    agent.gateway.access.grant(
        "agent",
        "execute",
    )


    agent.gateway.execution.workers.executor.register(
        "analysis",
        lambda data: {
            "success":
                True
        },
    )


    agent.start()


    result = agent.execute(
        create_task()
    )


    assert (
        result["success"]
        is True
    )



def test_invalid_capability():

    agent = RuntimeAgentRuntime(
        "agent"
    )


    result = agent.execute(
        create_task()
    )


    assert result is None



def test_status():

    agent = RuntimeAgentRuntime(
        "agent"
    )


    result = agent.status()


    assert "name" in result

    assert "capabilities" in result

    assert "executions" in result
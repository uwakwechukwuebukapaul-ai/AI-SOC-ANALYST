"""
Runtime Agent Manager Tests
"""

from services.intelligence.runtime.runtime_agent_manager import (
    RuntimeAgentManager,
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

    manager = RuntimeAgentManager()

    assert (
        manager.count()
        ==
        0
    )



def test_register():

    manager = RuntimeAgentManager()

    manager.register(
        create_agent()
    )


    assert (
        manager.count()
        ==
        1
    )



def test_get():

    manager = RuntimeAgentManager()

    agent = create_agent()

    manager.register(
        agent
    )


    result = manager.get(
        "analysis_agent"
    )


    assert (
        result
        ==
        agent
    )



def test_find_capability():

    manager = RuntimeAgentManager()

    manager.register(
        create_agent()
    )


    result = manager.find_capability(
        "analysis"
    )


    assert (
        len(result)
        ==
        1
    )



def test_unregister():

    manager = RuntimeAgentManager()

    manager.register(
        create_agent()
    )


    manager.unregister(
        "analysis_agent"
    )


    assert (
        manager.count()
        ==
        0
    )



def test_status():

    manager = RuntimeAgentManager()


    result = manager.status()


    assert "agents" in result

    assert "count" in result
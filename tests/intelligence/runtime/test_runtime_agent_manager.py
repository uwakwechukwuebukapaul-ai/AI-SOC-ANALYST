"""
Runtime Agent Manager Tests
"""

from services.intelligence.runtime.runtime_agent_manager import (
    RuntimeAgentManager,
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
        "investigation_agent",
        [
            "investigate",
            "summarize",
        ],
    )


    assert (
        manager.exists(
            "investigation_agent"
        )
        is True
    )



def test_capability():

    manager = RuntimeAgentManager()


    manager.register(
        "threat_agent",
        [
            "ioc_lookup",
        ],
    )


    assert (
        manager.has_capability(
            "ioc_lookup"
        )
        is True
    )



def test_unregister():

    manager = RuntimeAgentManager()


    manager.register(
        "agent1",
        [],
    )


    manager.unregister(
        "agent1"
    )


    assert (
        manager.exists(
            "agent1"
        )
        is False
    )



def test_clear():

    manager = RuntimeAgentManager()


    manager.register(
        "agent1",
        [],
    )


    manager.clear()


    assert (
        manager.count()
        ==
        0
    )



def test_status():

    manager = RuntimeAgentManager()


    result = manager.status()


    assert "agents" in result

    assert "registered" in result
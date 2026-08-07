from services.intelligence.runtime.agent_manager import (
    AgentManager
)



def test_manager_init():

    manager = AgentManager()

    assert manager.agents == {}



def test_register_agent():

    manager = AgentManager()

    agent = manager.register(
        "investigator",
        "Investigation Agent",
        "incident_analysis",
    )

    assert agent.agent_id == "investigator"



def test_start_agent():

    manager = AgentManager()

    manager.register(
        "hunter",
        "Threat Hunter",
        "threat_hunting",
    )

    result = manager.start(
        "hunter"
    )

    assert result is True

    assert (
        manager.get("hunter").status
        ==
        "running"
    )



def test_pause_agent():

    manager = AgentManager()

    manager.register(
        "agent",
        "Agent",
        "analysis",
    )

    manager.pause(
        "agent"
    )

    assert (
        manager.get("agent").status
        ==
        "paused"
    )



def test_stop_agent():

    manager = AgentManager()

    manager.register(
        "agent",
        "Agent",
        "analysis",
    )

    manager.stop(
        "agent"
    )

    assert (
        manager.get("agent").status
        ==
        "stopped"
    )



def test_remove():

    manager = AgentManager()

    manager.register(
        "agent",
        "Agent",
        "analysis",
    )

    manager.remove(
        "agent"
    )

    assert "agent" not in manager.agents



def test_to_dict():

    manager = AgentManager()

    manager.register(
        "agent",
        "Agent",
        "analysis",
    )

    data = manager.to_dict()

    assert "agent" in data
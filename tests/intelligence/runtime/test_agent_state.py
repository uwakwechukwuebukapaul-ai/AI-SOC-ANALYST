from services.intelligence.runtime.agent_state import (
    AgentState,
    AgentStatus,
)


def test_default_state():

    state = AgentState(name="ThreatFusion")

    assert state.status == AgentStatus.IDLE
    assert state.current_task is None


def test_assign_task():

    state = AgentState(name="ThreatFusion")

    state.assign_task("TASK-1")

    assert state.current_task == "TASK-1"
    assert state.status == AgentStatus.RUNNING


def test_clear_task():

    state = AgentState(name="ThreatFusion")

    state.assign_task("TASK-1")
    state.clear_task()

    assert state.current_task is None
    assert state.status == AgentStatus.IDLE


def test_capabilities():

    state = AgentState(name="ThreatFusion")

    state.add_capability("ioc")

    assert "ioc" in state.capabilities


def test_to_dict():

    state = AgentState(name="ThreatFusion")

    data = state.to_dict()

    assert data["name"] == "ThreatFusion"
    assert "heartbeat" in data
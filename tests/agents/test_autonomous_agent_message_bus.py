from services.agents.autonomous_agent_message_bus import (
    AutonomousAgentMessageBus
)


def test_register_agent():

    bus = AutonomousAgentMessageBus()

    agent = bus.register_agent(
        "Detection Engine",
        ["threat_detection"]
    )

    assert agent["name"] == "Detection Engine"
    assert agent["status"] == "active"


def test_get_agent():

    bus = AutonomousAgentMessageBus()

    bus.register_agent(
        "SOC Brain",
        ["reasoning"]
    )

    agent = bus.get_agent("SOC Brain")

    assert agent["name"] == "SOC Brain"


def test_agent_subscription():

    bus = AutonomousAgentMessageBus()

    bus.register_agent(
        "Incident Response",
        ["containment"]
    )

    result = bus.subscribe(
        "Incident Response",
        "critical_alert"
    )

    assert result is True
    assert "critical_alert" in bus.subscriptions["Incident Response"]


def test_message_routing():

    bus = AutonomousAgentMessageBus()

    bus.register_agent(
        "SOAR Engine",
        ["automation"]
    )

    bus.subscribe(
        "SOAR Engine",
        "malware_detected"
    )

    message = bus.publish(
        "Detection Engine",
        "malware_detected",
        {
            "file": "malware.exe"
        }
    )

    assert "SOAR Engine" in message["recipients"]


def test_agent_health_monitoring():

    bus = AutonomousAgentMessageBus()

    bus.register_agent(
        "Threat Hunter",
        ["hunting"]
    )

    health = bus.get_agent_health()

    assert health["Threat Hunter"]["status"] == "active"


def test_clear_history():

    bus = AutonomousAgentMessageBus()

    bus.publish(
        "SOC Brain",
        "test_event",
        {}
    )

    result = bus.clear_history()

    assert result is True
    assert len(bus.messages) == 0
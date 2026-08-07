"""
SOAR integration validation.
"""

from services.soar import (
    ActionExecutor,
    AutomationEngine,
    PlaybookEngine,
    ResponseHistory,
)


def test_playbook_registration():
    engine = AutomationEngine()

    playbook = engine.register_playbook(
        name="contain-compromised-endpoint",
        trigger="high_risk_endpoint",
        actions=[
            "isolate_endpoint",
            "notify_analyst",
        ],
    )

    assert playbook["name"] == "contain-compromised-endpoint"
    assert len(playbook["actions"]) == 2


def test_playbook_validation():
    engine = PlaybookEngine()

    valid = engine.validate(
        {
            "name": "block-malicious-ip",
            "trigger": "malicious_ip_detected",
            "actions": ["block_ip"],
        }
    )

    invalid = engine.validate(
        {
            "name": "invalid-playbook",
            "trigger": "test",
            "actions": [],
        }
    )

    assert valid is True
    assert invalid is False


def test_action_execution_simulation():
    executor = ActionExecutor(simulation=True)

    executor.register_action(
        "isolate_endpoint",
        lambda payload: {
            "endpoint": payload["target"],
            "isolated": True,
        },
    )

    result = executor.execute(
        action="isolate_endpoint",
        target="WORKSTATION-01",
    )

    assert result["status"] == "simulated"
    assert result["simulation"] is True


def test_soar_playbook_execution():
    engine = AutomationEngine()

    engine.register_playbook(
        name="credential-attack-response",
        trigger="credential_attack",
        actions=[
            "disable_account",
            "notify_analyst",
        ],
    )

    result = engine.execute_playbook(
        "credential-attack-response",
        case_id="INC-20260807-001",
        target="user@example.com",
    )

    assert result["status"] == "completed"
    assert len(result["actions"]) == 2


def test_response_history():
    history = ResponseHistory()

    history.record(
        action="block_ip",
        status="simulated",
        case_id="INC-001",
        target="192.168.1.10",
    )

    history.record(
        action="notify_analyst",
        status="simulated",
        case_id="INC-001",
        target="analyst",
    )

    assert history.count() == 2
    assert len(history.for_case("INC-001")) == 2
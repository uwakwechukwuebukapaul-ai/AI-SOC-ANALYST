from services.response.autonomous_soar_response_engine import (
    AutonomousSOARResponseEngine
)


def test_create_response_action():

    engine = AutonomousSOARResponseEngine()

    response = engine.create_response_action(
        "malware",
        "isolate_endpoint"
    )

    assert response["incident_type"] == "malware"


def test_execute_playbook():

    engine = AutonomousSOARResponseEngine()

    result = engine.execute_playbook(
        "malware_containment"
    )

    assert (
        result["execution_status"]
        ==
        "completed"
    )

    assert (
        result["result"]
        ==
        "endpoint_isolated"
    )


def test_endpoint_isolation():

    engine = AutonomousSOARResponseEngine()

    result = engine.isolate_endpoint(
        "WORKSTATION-01"
    )

    assert result["status"] == "isolated"


def test_ioc_blocking():

    engine = AutonomousSOARResponseEngine()

    result = engine.block_ioc(
        "malicious-domain.com",
        "domain"
    )

    assert result["status"] == "success"


def test_approval_workflow():

    engine = AutonomousSOARResponseEngine()

    result = engine.approval_required(
        "automatic_containment",
        0.80
    )

    assert (
        result["approval_required"]
        is True
    )


def test_response_history():

    engine = AutonomousSOARResponseEngine()

    engine.create_response_action(
        "phishing",
        "quarantine_email"
    )

    history = engine.get_history()

    assert len(history) == 1
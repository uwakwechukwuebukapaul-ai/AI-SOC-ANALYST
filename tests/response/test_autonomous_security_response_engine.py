from services.response.autonomous_security_response_engine import (
    AutonomousSecurityResponseEngine
)


def test_register_playbook():

    engine = AutonomousSecurityResponseEngine()

    result = engine.register_playbook(
        "Malware Containment",
        [
            "isolate endpoint",
            "block hash",
            "collect forensic evidence"
        ]
    )

    assert result["name"] == "Malware Containment"
    assert len(result["actions"]) == 3


def test_analyze_incident():

    engine = AutonomousSecurityResponseEngine()

    result = engine.analyze_incident(
        {
            "id": "INC-001",
            "severity": "critical"
        }
    )

    assert result["priority"] == "immediate"
    assert result["recommended_action"] == "contain_and_investigate"


def test_execute_response():

    engine = AutonomousSecurityResponseEngine()

    result = engine.execute_response(
        "INC-001",
        "isolate_endpoint"
    )

    assert result["status"] == "executed"
    assert result["action"] == "isolate_endpoint"


def test_generate_response_plan():

    engine = AutonomousSecurityResponseEngine()

    result = engine.generate_response_plan(
        {
            "id": "INC-002",
            "severity": "high"
        }
    )

    assert result["incident_id"] == "INC-002"
    assert len(result["steps"]) == 5


def test_recommend_playbook():

    engine = AutonomousSecurityResponseEngine()

    engine.register_playbook(
        "Ransomware Response",
        [
            "isolate host",
            "disable account"
        ]
    )

    result = engine.recommend_playbook("ransomware")

    assert result is not None


def test_response_history():

    engine = AutonomousSecurityResponseEngine()

    engine.generate_response_plan(
        {
            "id": "INC-003",
            "severity": "medium"
        }
    )

    history = engine.get_history()

    assert len(history) == 2
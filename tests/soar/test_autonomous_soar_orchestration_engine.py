from services.soar.autonomous_soar_orchestration_engine import (
    AutonomousSOAROrchestrationEngine
)


def test_register_playbook():
    engine = AutonomousSOAROrchestrationEngine()

    result = engine.register_playbook(
        "malware_containment",
        ["isolate_host", "block_hash"]
    )

    assert result["status"] == "registered"


def test_analyze_incident():
    engine = AutonomousSOAROrchestrationEngine()

    result = engine.analyze_incident(
        "Malware infection detected"
    )

    assert result["severity"] == "high"


def test_execute_playbook():
    engine = AutonomousSOAROrchestrationEngine()

    result = engine.execute_playbook(
        "malware_containment",
        "INC-001"
    )

    assert result["status"] == "executed"


def test_generate_response_plan():
    engine = AutonomousSOAROrchestrationEngine()

    result = engine.generate_response_plan(
        "phishing"
    )

    assert len(result["steps"]) == 4


def test_recommend_playbook():
    engine = AutonomousSOAROrchestrationEngine()

    result = engine.recommend_playbook(
        "ransomware"
    )

    assert result["recommended_playbook"] == "automated_containment"


def test_response_history():
    engine = AutonomousSOAROrchestrationEngine()

    engine.register_playbook(
        "account_lockdown",
        ["disable_user"]
    )

    history = engine.get_history()

    assert len(history) == 1
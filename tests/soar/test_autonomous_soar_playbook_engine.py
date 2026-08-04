from services.soar.autonomous_soar_playbook_engine import (
    AutonomousSOARPlaybookEngine
)


def test_create_playbook():

    engine = AutonomousSOARPlaybookEngine()

    playbook = engine.create_playbook(
        "Ransomware Response",
        "ransomware_detected",
        [
            "isolate_host",
            "block_ioc"
        ]
    )

    assert playbook["name"] == "Ransomware Response"
    assert len(playbook["actions"]) == 2



def test_execute_playbook():

    engine = AutonomousSOARPlaybookEngine()

    playbook = engine.create_playbook(
        "Malware Response",
        "malware_detected",
        [
            "collect_evidence"
        ]
    )

    result = engine.execute_playbook(
        playbook["id"]
    )

    assert result["status"] == "completed"
    assert result["results"][0]["status"] == "success"



def test_response_recommendation():

    engine = AutonomousSOARPlaybookEngine()

    actions = engine.recommend_response(
        "critical"
    )

    assert "isolate_host" in actions
    assert "block_ioc" in actions



def test_invalid_playbook():

    engine = AutonomousSOARPlaybookEngine()

    result = engine.execute_playbook(
        "invalid"
    )

    assert result["status"] == "failed"



def test_execution_history():

    engine = AutonomousSOARPlaybookEngine()

    playbook = engine.create_playbook(
        "IOC Blocking",
        "ioc_detected",
        [
            "block_ioc"
        ]
    )

    engine.execute_playbook(
        playbook["id"]
    )

    history = engine.get_execution_history()

    assert len(history) == 1



def test_clear_history():

    engine = AutonomousSOARPlaybookEngine()

    engine.execution_history.append(
        {"test": True}
    )

    engine.clear_history()

    assert len(engine.execution_history) == 0
from services.attack.autonomous_attack_mapping_engine import (
    AutonomousAttackMappingEngine
)


def test_map_attack():
    engine = AutonomousAttackMappingEngine()

    result = engine.map_attack(
        "phishing attack with credential theft"
    )

    assert result["technique_count"] == 2


def test_detect_initial_access_tactic():
    engine = AutonomousAttackMappingEngine()

    tactic = engine.detect_tactic(
        "phishing email attack"
    )

    assert tactic == "Initial Access"


def test_attack_graph_generation():
    engine = AutonomousAttackMappingEngine()

    graph = engine.generate_attack_graph(
        "malware command execution"
    )

    assert len(graph["nodes"]) == 2


def test_unknown_behavior():
    engine = AutonomousAttackMappingEngine()

    result = engine.map_attack(
        "normal user activity"
    )

    assert result["technique_count"] == 0


def test_mapping_history():
    engine = AutonomousAttackMappingEngine()

    engine.map_attack("credential theft")

    assert len(engine.get_history()) == 1


def test_clear_history():
    engine = AutonomousAttackMappingEngine()

    engine.map_attack("malware")

    engine.clear_history()

    assert len(engine.get_history()) == 0
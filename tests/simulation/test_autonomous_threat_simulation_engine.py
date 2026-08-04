from services.simulation.autonomous_threat_simulation_engine import (
    AutonomousThreatSimulationEngine
)


def test_create_attack_scenario():

    engine = AutonomousThreatSimulationEngine()

    scenario = engine.create_attack_scenario(
        "Ransomware Simulation",
        "Test enterprise resilience"
    )

    assert scenario["status"] == "created"


def test_simulate_attack_path():

    engine = AutonomousThreatSimulationEngine()

    scenario = engine.create_attack_scenario(
        "APT Simulation",
        "Validate defenses"
    )

    result = engine.simulate_attack_path(
        scenario["id"],
        [
            "initial_access",
            "execution",
            "lateral_movement"
        ]
    )

    assert result["status"] == "completed"


def test_predict_attack_behavior():

    engine = AutonomousThreatSimulationEngine()

    result = engine.predict_attack_behavior(
        [
            "credential_access"
        ]
    )

    assert result["predicted_behavior"] == "lateral_movement"


def test_map_attack_techniques():

    engine = AutonomousThreatSimulationEngine()

    result = engine.map_attack_techniques(
        [
            "phishing",
            "execution"
        ]
    )

    assert len(result) == 2


def test_generate_defense_recommendation():

    engine = AutonomousThreatSimulationEngine()

    result = engine.generate_defense_recommendation(
        "critical"
    )

    assert "Isolate" in result["recommendation"]


def test_simulation_history():

    engine = AutonomousThreatSimulationEngine()

    engine.create_attack_scenario(
        "Test",
        "Testing"
    )

    history = engine.get_history()

    assert len(history) == 1
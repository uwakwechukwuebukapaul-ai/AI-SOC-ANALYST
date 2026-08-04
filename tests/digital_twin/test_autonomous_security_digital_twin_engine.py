from services.digital_twin.autonomous_security_digital_twin_engine import (
    AutonomousSecurityDigitalTwinEngine
)


def test_register_asset():
    engine = AutonomousSecurityDigitalTwinEngine()

    asset = engine.register_asset(
        "server-01",
        "database",
        "critical"
    )

    assert asset["asset_id"] == "server-01"


def test_create_attack_scenario():
    engine = AutonomousSecurityDigitalTwinEngine()

    scenario = engine.create_attack_scenario(
        "attack-001",
        "T1059",
        "high"
    )

    assert scenario["scenario_id"] == "attack-001"


def test_simulate_attack():
    engine = AutonomousSecurityDigitalTwinEngine()

    engine.register_asset(
        "server-01",
        "web_server",
        "high"
    )

    engine.create_attack_scenario(
        "scenario-01",
        "phishing",
        "critical"
    )

    result = engine.simulate_attack(
        "server-01",
        "scenario-01"
    )

    assert result["status"] == "completed"
    assert result["risk_score"] > 0


def test_security_posture_analysis():
    engine = AutonomousSecurityDigitalTwinEngine()

    engine.register_asset(
        "endpoint-01",
        "endpoint",
        "medium"
    )

    posture = engine.analyze_security_posture()

    assert posture["assets"] == 1


def test_generate_improvement_strategy():
    engine = AutonomousSecurityDigitalTwinEngine()

    strategy = engine.generate_improvement_strategy()

    assert strategy["confidence"] > 0


def test_digital_twin_history():
    engine = AutonomousSecurityDigitalTwinEngine()

    engine.register_asset(
        "asset-01",
        "server",
        "low"
    )

    history = engine.get_history()

    assert len(history) == 1
from services.evolution.autonomous_security_evolution_engine import (
    AutonomousSecurityEvolutionEngine
)


def test_create_evolution_cycle():

    engine = AutonomousSecurityEvolutionEngine()

    result = engine.create_evolution_cycle(
        "Improve threat detection"
    )

    assert result["status"] == "initialized"


def test_detection_improvement():

    engine = AutonomousSecurityEvolutionEngine()

    result = engine.improve_detection_strategy(
        "Rule based detection"
    )

    assert result["type"] == "detection_evolution"


def test_response_optimization():

    engine = AutonomousSecurityEvolutionEngine()

    result = engine.optimize_response_strategy(
        "Manual containment"
    )

    assert result["type"] == "response_evolution"


def test_agent_evolution():

    engine = AutonomousSecurityEvolutionEngine()

    result = engine.evolve_agent_capability(
        "Threat Hunter Agent"
    )

    assert result["type"] == "agent_evolution"


def test_evolution_confidence():

    engine = AutonomousSecurityEvolutionEngine()

    result = engine.improve_detection_strategy(
        "IOC detection"
    )

    confidence = engine.calculate_evolution_confidence(
        result
    )

    assert confidence["level"] == "high"


def test_evolution_history():

    engine = AutonomousSecurityEvolutionEngine()

    engine.create_evolution_cycle(
        "Optimize SOC workflow"
    )

    history = engine.get_evolution_history()

    assert len(history) == 1
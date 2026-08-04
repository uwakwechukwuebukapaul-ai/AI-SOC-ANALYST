from services.agents.autonomous_security_agent_evolution_engine import (
    AutonomousSecurityAgentEvolutionEngine,
)


def test_register_agent():

    engine = AutonomousSecurityAgentEvolutionEngine()

    agent = engine.register_agent(
        "agent-001",
        ["analysis", "response"],
    )

    assert agent["agent_id"] == "agent-001"
    assert agent["version"] == "1.0"


def test_analyze_agent_weakness():

    engine = AutonomousSecurityAgentEvolutionEngine()

    engine.register_agent("agent-001")

    result = engine.analyze_agent_weakness(
        "agent-001",
        40,
    )

    assert result["weakness"] == "decision_accuracy"


def test_generate_evolution_strategy():

    engine = AutonomousSecurityAgentEvolutionEngine()

    engine.register_agent("agent-001")

    strategy = engine.generate_evolution_strategy(
        "agent-001"
    )

    assert len(strategy["strategy"]) == 3


def test_evolve_agent():

    engine = AutonomousSecurityAgentEvolutionEngine()

    engine.register_agent("agent-001")

    result = engine.evolve_agent(
        "agent-001",
        "Improved threat reasoning",
    )

    assert result["new_version"] == "1.1"
    assert result["evolution_level"] == 1


def test_compare_agent_versions():

    engine = AutonomousSecurityAgentEvolutionEngine()

    engine.register_agent("agent-001")

    result = engine.compare_agent_versions(
        "agent-001"
    )

    assert result["current_version"] == "1.0"


def test_evolution_history():

    engine = AutonomousSecurityAgentEvolutionEngine()

    engine.register_agent("agent-001")

    engine.evolve_agent(
        "agent-001",
        "Improved detection",
    )

    history = engine.evolution_history_records()

    assert len(history) == 1
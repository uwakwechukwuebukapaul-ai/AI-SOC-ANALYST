from services.orchestrator.agent_decision_engine import (
    AgentDecisionEngine,
)


def test_register_decision_rule():

    engine = AgentDecisionEngine()

    rule = engine.register_decision_rule(
        "threat_analysis",
        "threat_agent",
        5,
    )

    assert rule["agent"] == "threat_agent"
    assert rule["priority"] == 5



def test_select_best_agent():

    engine = AgentDecisionEngine()

    engine.register_decision_rule(
        "ioc_lookup",
        "ioc_agent",
        4,
    )

    decision = engine.select_best_agent(
        "ioc_lookup"
    )

    assert decision["selected_agent"] == "ioc_agent"
    assert decision["reason"] == "Capability match"



def test_priority_calculation():

    engine = AgentDecisionEngine()

    priority = engine.calculate_priority(
        "critical"
    )

    assert priority == 5



def test_decision_history():

    engine = AgentDecisionEngine()

    engine.register_decision_rule(
        "classification",
        "classifier_agent",
    )

    engine.select_best_agent(
        "classification"
    )

    history = engine.get_decision_history()

    assert len(history) == 1



def test_clear_decisions():

    engine = AgentDecisionEngine()

    engine.register_decision_rule(
        "analysis",
        "analysis_agent",
    )

    engine.select_best_agent(
        "analysis"
    )

    engine.clear_decisions()

    assert engine.get_decision_history() == []



def test_unknown_capability_handling():

    engine = AgentDecisionEngine()

    result = engine.handle_unknown_capability(
        "unknown_skill"
    )

    assert result["status"] == "unavailable"
    assert result["agent"] is None
from services.meta_intelligence.autonomous_security_meta_intelligence_engine import (
    AutonomousSecurityMetaIntelligenceEngine
)


def test_register_intelligence_module():

    engine = AutonomousSecurityMetaIntelligenceEngine()

    result = engine.register_intelligence_module(
        "investigation_engine",
        {
            "status": "active",
            "capability": "case analysis"
        }
    )

    assert result["name"] == "investigation_engine"
    assert result["status"] == "active"



def test_analyze_system_state():

    engine = AutonomousSecurityMetaIntelligenceEngine()

    result = engine.analyze_system_state(
        {
            "threat_level": "critical",
            "system_health": "healthy"
        }
    )

    assert result["priority"] == "investigation"



def test_select_optimal_engine():

    engine = AutonomousSecurityMetaIntelligenceEngine()

    result = engine.select_optimal_engine(
        "optimize"
    )

    assert result["selected_engine"] == "optimization_engine"



def test_generate_autonomous_strategy():

    engine = AutonomousSecurityMetaIntelligenceEngine()

    result = engine.generate_autonomous_strategy(
        {
            "priority": "optimization"
        }
    )

    assert "strategy_id" in result
    assert len(result["actions"]) == 3



def test_meta_decision_confidence():

    engine = AutonomousSecurityMetaIntelligenceEngine()

    confidence = engine.calculate_meta_decision_confidence(
        {
            "validated": True,
            "multiple_sources": True
        }
    )

    assert confidence == 1.0



def test_meta_intelligence_history():

    engine = AutonomousSecurityMetaIntelligenceEngine()

    engine.register_intelligence_module(
        "prediction_engine",
        {}
    )

    history = engine.get_history()

    assert len(history) == 1
from services.meta_intelligence.autonomous_security_meta_intelligence_engine import (
    AutonomousSecurityMetaIntelligenceEngine
)



def test_register_intelligence_module():

    engine = AutonomousSecurityMetaIntelligenceEngine()

    result = engine.register_intelligence_module(
        "prediction_engine",
        [
            "prediction",
            "forecasting"
        ]
    )

    assert result["status"] == "active"



def test_analyze_system_state():

    engine = AutonomousSecurityMetaIntelligenceEngine()

    engine.register_intelligence_module(
        "response_engine",
        [
            "response"
        ]
    )

    result = engine.analyze_system_state()

    assert result["health"] == "optimal"



def test_select_optimal_engine():

    engine = AutonomousSecurityMetaIntelligenceEngine()

    engine.register_intelligence_module(
        "decision_engine",
        [
            "decision"
        ]
    )

    result = engine.select_optimal_engine(
        "decision"
    )

    assert result["selected_engine"] == "decision_engine"



def test_generate_autonomous_strategy():

    engine = AutonomousSecurityMetaIntelligenceEngine()

    result = engine.generate_autonomous_strategy(
        {
            "severity": "critical"
        }
    )

    assert (
        "activate_response_engine"
        in result["strategy"]["actions"]
    )



def test_meta_decision_confidence():

    engine = AutonomousSecurityMetaIntelligenceEngine()

    result = engine.calculate_meta_decision_confidence(
        0.9,
        0.8
    )

    assert result["classification"] == "high"



def test_meta_intelligence_history():

    engine = AutonomousSecurityMetaIntelligenceEngine()

    engine.register_intelligence_module(
        "test_engine",
        []
    )

    history = engine.get_history()

    assert len(history) > 0
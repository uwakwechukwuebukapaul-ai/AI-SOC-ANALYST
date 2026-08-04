from services.intelligence.autonomous_security_intelligence_core import (
    AutonomousSecurityIntelligenceCore
)


def test_register_component():

    core = AutonomousSecurityIntelligenceCore()

    result = core.register_component(
        "risk_engine",
        "Autonomous Risk Intelligence Engine"
    )

    assert result["component_id"] == "risk_engine"
    assert result["status"] == "active"



def test_analyze_security_event():

    core = AutonomousSecurityIntelligenceCore()

    result = core.analyze_security_event(
        {
            "event": "failed_login",
            "severity": "high"
        }
    )

    assert result["risk_score"] == 75
    assert result["risk_level"] == "HIGH"



def test_generate_decision():

    core = AutonomousSecurityIntelligenceCore()

    analysis = {
        "risk_score": 95,
        "risk_level": "CRITICAL"
    }

    decision = core.generate_decision(
        analysis
    )

    assert decision["recommended_action"] == "contain_threat"



def test_assign_agent():

    core = AutonomousSecurityIntelligenceCore()

    decision = {
        "recommended_action": "start_investigation"
    }

    result = core.assign_agent(
        decision
    )

    assert result["agent"] == "investigation_agent"



def test_execute_intelligence_cycle():

    core = AutonomousSecurityIntelligenceCore()

    result = core.execute_intelligence_cycle(
        {
            "event": "malware_detection",
            "severity": "critical"
        }
    )

    assert result["status"] == "completed"
    assert result["decision"]["risk_level"] == "CRITICAL"



def test_intelligence_history():

    core = AutonomousSecurityIntelligenceCore()

    core.execute_intelligence_cycle(
        {
            "event": "phishing",
            "severity": "medium"
        }
    )

    history = core.intelligence_history()

    assert len(history) == 1
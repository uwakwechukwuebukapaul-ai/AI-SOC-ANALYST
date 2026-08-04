from services.orchestrator.agent_reasoning import (
    AgentReasoningEngine,
)


def test_context_evaluation():

    engine = AgentReasoningEngine()

    result = engine.evaluate_context(
        {
            "risk_score": 80,
            "severity": "High",
            "iocs": [
                {
                    "type": "ip"
                }
            ]
        }
    )


    assert result["risk_level"] == "HIGH"

    assert result["requires_action"] is True



def test_generate_response_decision():

    engine = AgentReasoningEngine()


    decision = engine.generate_decision(
        {
            "risk_score": 95,
            "severity": "Critical",
            "iocs": []
        }
    )


    assert decision.action == "INITIATE_RESPONSE"

    assert decision.confidence > 0



def test_generate_analysis_decision():

    engine = AgentReasoningEngine()


    decision = engine.generate_decision(
        {
            "risk_score": 10,
            "severity": "Low",
        }
    )


    assert decision.action == "CONTINUE_ANALYSIS"



def test_confidence_calculation():

    engine = AgentReasoningEngine()


    score = engine.calculate_confidence(
        evidence_count=5,
        intelligence_count=3,
    )


    assert score > 0



def test_reasoning_history():

    engine = AgentReasoningEngine()


    engine.generate_decision(
        {
            "risk_score": 90,
            "severity": "High",
        }
    )


    history = engine.get_history()


    assert len(history) == 1



def test_clear_reasoning_history():

    engine = AgentReasoningEngine()


    engine.generate_decision(
        {
            "risk_score": 90
        }
    )


    engine.clear_history()


    assert len(engine.get_history()) == 0
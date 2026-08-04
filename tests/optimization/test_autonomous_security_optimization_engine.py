from services.optimization.autonomous_security_optimization_engine import (
    AutonomousSecurityOptimizationEngine
)


def test_analyze_evaluation_results():

    engine = AutonomousSecurityOptimizationEngine()

    result = engine.analyze_evaluation_results(
        {
            "score": 40,
            "weaknesses": [
                "slow investigation",
                "false positives"
            ]
        }
    )

    assert result["priority"] == "critical"
    assert len(result["weaknesses"]) == 2



def test_optimize_detection_rules():

    engine = AutonomousSecurityOptimizationEngine()

    result = engine.optimize_detection_rules({})

    assert result["component"] == "detection_engine"
    assert result["status"] == "optimized"



def test_optimize_response_playbook():

    engine = AutonomousSecurityOptimizationEngine()

    result = engine.optimize_response_playbook({})

    assert result["component"] == "soar_engine"
    assert result["status"] == "optimized"



def test_optimize_agent_behavior():

    engine = AutonomousSecurityOptimizationEngine()

    result = engine.optimize_agent_behavior({})

    assert result["component"] == "agent_system"
    assert result["status"] == "optimized"



def test_generate_improvement_plan():

    engine = AutonomousSecurityOptimizationEngine()

    result = engine.generate_improvement_plan(
        {
            "target": "SOC improvement"
        }
    )

    assert "plan_id" in result
    assert len(result["objectives"]) == 3



def test_optimization_history():

    engine = AutonomousSecurityOptimizationEngine()

    engine.optimize_detection_rules({})

    history = engine.get_optimization_history()

    assert len(history) == 1
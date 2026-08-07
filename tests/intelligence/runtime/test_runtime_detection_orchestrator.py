"""
Runtime Detection Orchestrator Tests
"""

from services.intelligence.runtime.runtime_detection_orchestrator import (
    RuntimeDetectionOrchestrator,
)



def test_init():

    orchestrator = RuntimeDetectionOrchestrator()

    assert (
        orchestrator.count()
        ==
        0
    )



def test_register_rule():

    orchestrator = RuntimeDetectionOrchestrator()


    orchestrator.register_rule(
        "malware_detection",
        lambda event: {
            "alert":
                True
        },
    )


    assert (
        orchestrator.exists(
            "malware_detection"
        )
        is True
    )



def test_evaluate_detection():

    orchestrator = RuntimeDetectionOrchestrator()


    orchestrator.register_rule(
        "phishing",
        lambda event: {
            "severity":
                "high"
        },
    )


    result = orchestrator.evaluate(
        "phishing",
        {
            "email":
                "test"
        },
    )


    assert (
        result["severity"]
        ==
        "high"
    )



def test_missing_rule():

    orchestrator = RuntimeDetectionOrchestrator()


    result = orchestrator.evaluate(
        "missing",
        {},
    )


    assert result is None



def test_clear():

    orchestrator = RuntimeDetectionOrchestrator()


    orchestrator.register_rule(
        "test",
        lambda x: True,
    )


    orchestrator.clear()


    assert (
        orchestrator.exists(
            "test"
        )
        is False
    )



def test_status():

    orchestrator = RuntimeDetectionOrchestrator()


    result = orchestrator.status()


    assert "rules" in result

    assert "detections" in result
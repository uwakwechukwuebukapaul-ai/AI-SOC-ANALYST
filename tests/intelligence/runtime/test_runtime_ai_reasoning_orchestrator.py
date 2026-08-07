"""
Runtime AI Reasoning Orchestrator Tests
"""

from services.intelligence.runtime.runtime_ai_reasoning_orchestrator import (
    RuntimeAIReasoningOrchestrator,
)



def test_init():

    orchestrator = RuntimeAIReasoningOrchestrator()

    assert (
        orchestrator.count()
        ==
        0
    )



def test_register_engine():

    orchestrator = RuntimeAIReasoningOrchestrator()


    orchestrator.register_engine(
        "risk_reasoner",
        lambda ctx: {
            "risk":
                "high"
        },
    )


    assert (
        orchestrator.available(
            "risk_reasoner"
        )
        is True
    )



def test_reason():

    orchestrator = RuntimeAIReasoningOrchestrator()


    orchestrator.register_engine(
        "classifier",
        lambda ctx: {
            "classification":
                "phishing"
        },
    )


    result = orchestrator.reason(
        "classifier",
        {
            "email":
                "suspicious"
        },
    )


    assert (
        result["classification"]
        ==
        "phishing"
    )



def test_missing_engine():

    orchestrator = RuntimeAIReasoningOrchestrator()


    result = orchestrator.reason(
        "missing",
        {},
    )


    assert result is None



def test_clear():

    orchestrator = RuntimeAIReasoningOrchestrator()


    orchestrator.register_engine(
        "test",
        lambda x: True,
    )


    orchestrator.clear()


    assert (
        orchestrator.available(
            "test"
        )
        is False
    )



def test_status():

    orchestrator = RuntimeAIReasoningOrchestrator()


    result = orchestrator.status()


    assert "engines" in result

    assert "decisions" in result
"""
Runtime Threat Intelligence Orchestrator Tests
"""

from services.intelligence.runtime.runtime_threat_intelligence_orchestrator import (
    RuntimeThreatIntelligenceOrchestrator,
)



def test_init():

    orchestrator = RuntimeThreatIntelligenceOrchestrator()

    assert (
        orchestrator.count()
        ==
        0
    )



def test_register_engine():

    orchestrator = RuntimeThreatIntelligenceOrchestrator()


    orchestrator.register_engine(
        "ioc_engine",
        lambda data: {
            "risk":
                "high"
        },
    )


    assert (
        orchestrator.available(
            "ioc_engine"
        )
        is True
    )



def test_analyze():

    orchestrator = RuntimeThreatIntelligenceOrchestrator()


    orchestrator.register_engine(
        "ioc_engine",
        lambda data: {
            "malicious":
                True
        },
    )


    result = orchestrator.analyze(
        "ioc_engine",
        {
            "ioc":
                "example.com"
        },
    )


    assert (
        result["malicious"]
        is True
    )



def test_missing_engine():

    orchestrator = RuntimeThreatIntelligenceOrchestrator()


    result = orchestrator.analyze(
        "missing",
        {},
    )


    assert result is None



def test_clear():

    orchestrator = RuntimeThreatIntelligenceOrchestrator()


    orchestrator.register_engine(
        "test",
        lambda data: True,
    )


    orchestrator.clear()


    assert (
        orchestrator.available(
            "test"
        )
        is False
    )



def test_status():

    orchestrator = RuntimeThreatIntelligenceOrchestrator()


    result = orchestrator.status()


    assert "engines" in result

    assert "operations" in result
"""
Runtime SOC Orchestrator Tests
"""

from services.intelligence.runtime.runtime_soc_orchestrator import (
    RuntimeSOCOrchestrator,
)



def test_init():

    orchestrator = RuntimeSOCOrchestrator()

    assert (
        orchestrator.operations
        ==
        0
    )



def test_detection_flow():

    orchestrator = RuntimeSOCOrchestrator()


    orchestrator.detection.register_rule(
        "malware",
        lambda event: {
            "alert":
                True
        },
    )


    result = orchestrator.analyze_event(
        "malware",
        {},
    )


    assert (
        result["alert"]
        is True
    )



def test_threat_intelligence_flow():

    orchestrator = RuntimeSOCOrchestrator()


    orchestrator.intelligence.register_engine(
        "ioc",
        lambda data: {
            "risk":
                "high"
        },
    )


    result = orchestrator.enrich_threat(
        "ioc",
        {},
    )


    assert (
        result["risk"]
        ==
        "high"
    )



def test_response_flow():

    orchestrator = RuntimeSOCOrchestrator()


    orchestrator.response.register_action(
        "block",
        lambda ctx: {
            "blocked":
                True
        },
    )


    result = orchestrator.respond(
        "block",
        {},
    )


    assert (
        result["blocked"]
        is True
    )



def test_clear():

    orchestrator = RuntimeSOCOrchestrator()


    orchestrator.operations = 5


    orchestrator.clear()


    assert (
        orchestrator.operations
        ==
        0
    )



def test_status():

    orchestrator = RuntimeSOCOrchestrator()


    result = orchestrator.status()


    assert "operations" in result

    assert "detection" in result

    assert "intelligence" in result

    assert "investigation" in result

    assert "response" in result
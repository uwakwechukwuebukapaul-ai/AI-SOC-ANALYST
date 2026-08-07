"""
Runtime Context Orchestrator Tests
"""

from services.intelligence.runtime.runtime_context_orchestrator import (
    RuntimeContextOrchestrator,
)



def test_init():

    manager = RuntimeContextOrchestrator()

    assert (
        manager.count()
        ==
        0
    )



def test_create_context():

    manager = RuntimeContextOrchestrator()


    manager.create(
        "case_001",
        {
            "case":
                "phishing"
        },
    )


    assert (
        manager.exists(
            "case_001"
        )
        is True
    )



def test_get_context():

    manager = RuntimeContextOrchestrator()


    manager.create(
        "case_001",
        {
            "risk":
                "high"
        },
    )


    result = manager.get(
        "case_001"
    )


    assert (
        result["risk"]
        ==
        "high"
    )



def test_update_context():

    manager = RuntimeContextOrchestrator()


    manager.create(
        "case_001",
        {},
    )


    manager.update(
        "case_001",
        "severity",
        "critical",
    )


    result = manager.get(
        "case_001"
    )


    assert (
        result["severity"]
        ==
        "critical"
    )



def test_clear():

    manager = RuntimeContextOrchestrator()


    manager.create(
        "test",
        {},
    )


    manager.clear()


    assert (
        manager.count()
        ==
        0
    )



def test_status():

    manager = RuntimeContextOrchestrator()


    result = manager.status()


    assert "contexts" in result
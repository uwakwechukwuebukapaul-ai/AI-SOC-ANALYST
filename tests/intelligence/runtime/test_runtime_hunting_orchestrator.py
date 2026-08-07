"""
Runtime Hunting Orchestrator Tests
"""

from services.intelligence.runtime.runtime_hunting_orchestrator import (
    RuntimeHuntingOrchestrator,
)



def test_init():

    orchestrator = RuntimeHuntingOrchestrator()

    assert (
        orchestrator.count()
        ==
        0
    )



def test_register_hunt():

    orchestrator = RuntimeHuntingOrchestrator()


    orchestrator.register_hunt(
        "suspicious_process",
        lambda data: {
            "found":
                True
        },
    )


    assert (
        orchestrator.exists(
            "suspicious_process"
        )
        is True
    )



def test_execute_hunt():

    orchestrator = RuntimeHuntingOrchestrator()


    orchestrator.register_hunt(
        "malware_hunt",
        lambda data: {
            "matches":
                5
        },
    )


    result = orchestrator.execute(
        "malware_hunt",
        {
            "host":
                "endpoint01"
        },
    )


    assert (
        result["matches"]
        ==
        5
    )



def test_missing_hunt():

    orchestrator = RuntimeHuntingOrchestrator()


    result = orchestrator.execute(
        "unknown",
        {},
    )


    assert result is None



def test_clear():

    orchestrator = RuntimeHuntingOrchestrator()


    orchestrator.register_hunt(
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

    orchestrator = RuntimeHuntingOrchestrator()


    result = orchestrator.status()


    assert "hunts" in result

    assert "executions" in result
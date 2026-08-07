"""
Runtime MITRE Orchestrator Tests
"""

from services.intelligence.runtime.runtime_mitre_orchestrator import (
    RuntimeMitreOrchestrator,
)



def test_init():

    orchestrator = RuntimeMitreOrchestrator()

    assert (
        orchestrator.count()
        ==
        0
    )



def test_register():

    orchestrator = RuntimeMitreOrchestrator()


    orchestrator.register_technique(
        "T1059",
        {
            "name":
                "Command and Scripting Interpreter"
        },
    )


    assert (
        orchestrator.exists(
            "T1059"
        )
        is True
    )



def test_map_behavior():

    orchestrator = RuntimeMitreOrchestrator()


    orchestrator.register_technique(
        "PowerShell",
        {
            "technique":
                "T1059.001"
        },
    )


    result = orchestrator.map_behavior(
        "PowerShell"
    )


    assert (
        result["technique"]
        ==
        "T1059.001"
    )



def test_missing_behavior():

    orchestrator = RuntimeMitreOrchestrator()


    result = orchestrator.map_behavior(
        "unknown"
    )


    assert result is None



def test_clear():

    orchestrator = RuntimeMitreOrchestrator()


    orchestrator.register_technique(
        "T1003",
        {},
    )


    orchestrator.clear()


    assert (
        orchestrator.exists(
            "T1003"
        )
        is False
    )



def test_status():

    orchestrator = RuntimeMitreOrchestrator()


    result = orchestrator.status()


    assert "techniques" in result

    assert "mappings" in result
"""
Runtime Event Orchestrator Tests
"""

from services.intelligence.runtime.runtime_event_orchestrator import (
    RuntimeEventOrchestrator,
)



def test_init():

    orchestrator = RuntimeEventOrchestrator()

    assert (
        orchestrator.executions
        ==
        0
    )



def test_register():

    orchestrator = RuntimeEventOrchestrator()


    orchestrator.register(
        "alert",
        lambda data: {
            "handled":
                True
        },
    )


    assert (
        orchestrator.processor.processor_count(
            "alert"
        )
        ==
        1
    )



def test_emit():

    orchestrator = RuntimeEventOrchestrator()


    result = []


    orchestrator.register(
        "alert",
        lambda data: result.append(data),
    )


    orchestrator.emit(
        "alert",
        {
            "severity":
                "high"
        },
    )


    assert (
        result[0]["severity"]
        ==
        "high"
    )



def test_execution_count():

    orchestrator = RuntimeEventOrchestrator()


    orchestrator.register(
        "event",
        lambda data: True,
    )


    orchestrator.emit(
        "event",
        {},
    )


    assert (
        orchestrator.executions
        ==
        1
    )



def test_clear():

    orchestrator = RuntimeEventOrchestrator()


    orchestrator.register(
        "event",
        lambda data: True,
    )


    orchestrator.emit(
        "event",
        {},
    )


    orchestrator.clear()


    assert (
        orchestrator.executions
        ==
        0
    )



def test_status():

    orchestrator = RuntimeEventOrchestrator()


    result = orchestrator.status()


    assert "executions" in result

    assert "events" in result

    assert "processor" in result
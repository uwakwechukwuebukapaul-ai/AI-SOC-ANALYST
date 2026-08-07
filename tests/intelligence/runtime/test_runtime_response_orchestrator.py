"""
Runtime Response Orchestrator Tests
"""

from services.intelligence.runtime.runtime_response_orchestrator import (
    RuntimeResponseOrchestrator,
)



def test_init():

    orchestrator = RuntimeResponseOrchestrator()

    assert (
        orchestrator.count()
        ==
        0
    )



def test_register_action():

    orchestrator = RuntimeResponseOrchestrator()


    orchestrator.register_action(
        "block_ip",
        lambda ctx: {
            "blocked":
                True
        },
    )


    assert (
        orchestrator.available(
            "block_ip"
        )
        is True
    )



def test_execute_action():

    orchestrator = RuntimeResponseOrchestrator()


    orchestrator.register_action(
        "disable_user",
        lambda ctx: {
            "disabled":
                True
        },
    )


    result = orchestrator.execute(
        "disable_user",
        {
            "user":
                "attacker"
        },
    )


    assert (
        result["disabled"]
        is True
    )



def test_missing_action():

    orchestrator = RuntimeResponseOrchestrator()


    result = orchestrator.execute(
        "missing",
        {},
    )


    assert result is None



def test_clear():

    orchestrator = RuntimeResponseOrchestrator()


    orchestrator.register_action(
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

    orchestrator = RuntimeResponseOrchestrator()


    result = orchestrator.status()


    assert "actions" in result

    assert "executions" in result
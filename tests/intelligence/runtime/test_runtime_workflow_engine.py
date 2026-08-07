"""
Runtime Workflow Engine Tests
"""

from services.intelligence.runtime.runtime_workflow_engine import (
    RuntimeWorkflowEngine,
)



def test_init():

    engine = RuntimeWorkflowEngine()

    assert (
        engine.count()
        ==
        0
    )



def test_register():

    engine = RuntimeWorkflowEngine()


    engine.register(
        "investigation",
        [
            lambda ctx: {
                "step":
                    1
            }
        ],
    )


    assert (
        engine.exists(
            "investigation"
        )
        is True
    )



def test_execute():

    engine = RuntimeWorkflowEngine()


    engine.register(
        "response",
        [
            lambda ctx: {
                "blocked":
                    True
            },

            lambda ctx: {
                "logged":
                    True
            },
        ],
    )


    result = engine.execute(
        "response",
        {},
    )


    assert (
        result[0]["blocked"]
        is True
    )

    assert (
        result[1]["logged"]
        is True
    )



def test_missing_workflow():

    engine = RuntimeWorkflowEngine()


    result = engine.execute(
        "missing",
        {},
    )


    assert result is None



def test_clear():

    engine = RuntimeWorkflowEngine()


    engine.register(
        "test",
        [],
    )


    engine.clear()


    assert (
        engine.exists(
            "test"
        )
        is False
    )



def test_status():

    engine = RuntimeWorkflowEngine()


    result = engine.status()


    assert "workflows" in result

    assert "executions" in result
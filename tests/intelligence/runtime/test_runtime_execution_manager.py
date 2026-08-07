"""
Runtime Execution Manager Tests
"""

from services.intelligence.runtime.runtime_execution_manager import (
    RuntimeExecutionManager,
)



def test_manager_init():

    manager = RuntimeExecutionManager()

    assert (
        manager.executions
        ==
        0
    )



def test_register():

    manager = RuntimeExecutionManager()


    manager.register(
        "analysis",
        lambda data: data,
    )


    assert (
        manager.pipeline.dispatcher.exists(
            "analysis"
        )
        is True
    )



def test_submit():

    manager = RuntimeExecutionManager()


    manager.submit(
        "test",
        {},
    )


    assert (
        manager.pending()
        ==
        1
    )



def test_execute():

    manager = RuntimeExecutionManager()


    manager.register(
        "test",
        lambda data: {
            "success":
                True
        },
    )


    manager.submit(
        "test",
        {},
    )


    result = manager.execute()


    assert (
        result["success"]
        is True
    )



def test_clear():

    manager = RuntimeExecutionManager()


    manager.submit(
        "task",
        {},
    )


    manager.clear()


    assert (
        manager.pending()
        ==
        0
    )



def test_status():

    manager = RuntimeExecutionManager()


    result = manager.status()


    assert "executions" in result

    assert "pending" in result
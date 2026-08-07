"""
Runtime Execution Manager Tests
"""

from services.intelligence.runtime.runtime_execution_manager import (
    RuntimeExecutionManager,
)

from services.intelligence.runtime.task import Task



def create_task():

    return Task(
        capability="analysis",
        payload={
            "event": "test"
        }
    )



def test_manager_init():

    manager = RuntimeExecutionManager()

    assert (
        manager.running
        is False
    )



def test_start():

    manager = RuntimeExecutionManager()

    manager.start()

    assert (
        manager.running
        is True
    )



def test_stop():

    manager = RuntimeExecutionManager()

    manager.start()

    manager.stop()

    assert (
        manager.running
        is False
    )



def test_submit():

    manager = RuntimeExecutionManager()

    manager.submit(
        create_task()
    )

    assert (
        manager.pipeline.size()
        ==
        1
    )



def test_execute():

    manager = RuntimeExecutionManager()


    manager.register_handler(
        "analysis",
        lambda task: "done"
    )


    result = manager.execute(
        create_task()
    )


    assert (
        result.success
        is True
    )



def test_status():

    manager = RuntimeExecutionManager()

    result = manager.status()

    assert "running" in result

    assert "executed_tasks" in result
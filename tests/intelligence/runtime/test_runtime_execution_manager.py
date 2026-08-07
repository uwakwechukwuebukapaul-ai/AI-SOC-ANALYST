"""
Runtime Execution Manager Tests
"""

from services.intelligence.runtime.runtime_execution_manager import (
    RuntimeExecutionManager,
)

from services.intelligence.runtime.task import (
    Task,
)



def create_task():

    return Task(
        capability="analysis",
        payload={
            "test":
                True
        },
    )



def test_init():

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



def test_submit():

    manager = RuntimeExecutionManager()


    manager.start()


    manager.workers.executor.register(
        "analysis",
        lambda data: {
            "done":
                True
        },
    )


    result = manager.submit(
        create_task()
    )


    assert (
        result["done"]
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



def test_clear():

    manager = RuntimeExecutionManager()


    manager.start()

    manager.clear()


    assert (
        manager.metrics.executions
        ==
        0
    )



def test_status():

    manager = RuntimeExecutionManager()


    result = manager.status()


    assert "running" in result

    assert "workers" in result

    assert "metrics" in result
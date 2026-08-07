"""
Runtime Scheduler Manager Tests
"""

from services.intelligence.runtime.runtime_scheduler_manager import (
    RuntimeSchedulerManager,
)

from services.intelligence.runtime.task import Task



def create_task():

    return Task(
        capability="test.capability",
        payload={
            "message": "test task"
        }
    )



def test_manager_init():

    manager = RuntimeSchedulerManager()

    assert (
        manager.running
        is False
    )



def test_start():

    manager = RuntimeSchedulerManager()

    manager.start()

    assert (
        manager.running
        is True
    )



def test_stop():

    manager = RuntimeSchedulerManager()

    manager.start()

    manager.stop()

    assert (
        manager.running
        is False
    )



def test_schedule():

    manager = RuntimeSchedulerManager()

    manager.start()

    task = create_task()

    manager.schedule(
        task
    )

    assert (
        manager.size()
        ==
        1
    )



def test_next_task():

    manager = RuntimeSchedulerManager()

    manager.start()

    task = create_task()

    manager.schedule(
        task
    )

    result = manager.next_task()

    assert result == task



def test_clear():

    manager = RuntimeSchedulerManager()

    manager.start()

    manager.schedule(
        create_task()
    )

    manager.clear()

    assert (
        manager.size()
        ==
        0
    )



def test_status():

    manager = RuntimeSchedulerManager()

    result = manager.status()

    assert "running" in result

    assert "queue_size" in result
"""
Scheduler Runtime Tests
"""


from services.intelligence.runtime.scheduler import (
    Scheduler,
)

from services.intelligence.runtime.task import (
    Task,
    TaskPriority,
)



def create_task(priority):

    return Task(
        capability="test",
        payload={},
        priority=priority,
    )



def test_scheduler_default():

    scheduler = Scheduler()

    assert scheduler.size() == 0



def test_schedule():

    scheduler = Scheduler()

    task = create_task(
        TaskPriority.NORMAL
    )

    scheduler.schedule(task)

    assert scheduler.size() == 1

    assert task.status.value == "queued"



def test_priority_order():

    scheduler = Scheduler()

    low = create_task(
        TaskPriority.LOW
    )

    high = create_task(
        TaskPriority.HIGH
    )


    scheduler.schedule(low)

    scheduler.schedule(high)


    result = scheduler.next_task()


    assert result == high



def test_next_task_empty():

    scheduler = Scheduler()

    assert scheduler.next_task() is None



def test_remove():

    scheduler = Scheduler()

    task = create_task(
        TaskPriority.NORMAL
    )

    scheduler.schedule(task)


    removed = scheduler.remove(
        task.task_id
    )


    assert removed is True

    assert scheduler.size() == 0



def test_clear():

    scheduler = Scheduler()

    scheduler.schedule(
        create_task(
            TaskPriority.NORMAL
        )
    )


    scheduler.clear()


    assert scheduler.size() == 0



def test_contains():

    scheduler = Scheduler()

    task = create_task(
        TaskPriority.NORMAL
    )


    scheduler.schedule(task)


    assert scheduler.contains(
        task.task_id
    )
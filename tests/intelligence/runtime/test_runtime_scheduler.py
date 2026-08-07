from services.intelligence.runtime.runtime_scheduler import (
    RuntimeScheduler,
)



def test_scheduler_init():

    scheduler = RuntimeScheduler()

    assert scheduler.size() == 0



def test_schedule():

    scheduler = RuntimeScheduler()


    scheduler.schedule(
        "task1",
        {},
    )


    assert scheduler.size() == 1



def test_priority():

    scheduler = RuntimeScheduler()


    scheduler.schedule(
        "low",
        {},
        priority=20,
    )


    scheduler.schedule(
        "high",
        {},
        priority=1,
    )


    task = scheduler.next_task()


    assert task.task_id == "high"



def test_complete():

    scheduler = RuntimeScheduler()


    scheduler.complete(
        "task1"
    )


    assert (
        "task1"
        in scheduler.completed
    )



def test_fail():

    scheduler = RuntimeScheduler()


    scheduler.fail(
        "task1"
    )


    assert (
        "task1"
        in scheduler.failed
    )



def test_status():

    scheduler = RuntimeScheduler()


    status = scheduler.status()


    assert "queued" in status
    assert "completed" in status
"""
Runtime Scheduler Tests
"""

from services.intelligence.runtime.runtime_scheduler import (
    RuntimeScheduler,
)



def test_init():

    scheduler = RuntimeScheduler()

    assert (
        scheduler.pending()
        ==
        0
    )



def test_schedule():

    scheduler = RuntimeScheduler()


    scheduler.schedule(
        "task01",
    )


    assert (
        scheduler.pending()
        ==
        1
    )



def test_priority_order():

    scheduler = RuntimeScheduler()


    scheduler.schedule(
        "low",
        priority=1,
    )


    scheduler.schedule(
        "high",
        priority=10,
    )


    result = scheduler.next()


    assert (
        result["id"]
        ==
        "high"
    )



def test_next_empty():

    scheduler = RuntimeScheduler()


    assert (
        scheduler.next()
        is None
    )



def test_complete():

    scheduler = RuntimeScheduler()


    scheduler.complete()


    assert (
        scheduler.count()
        ==
        1
    )



def test_clear():

    scheduler = RuntimeScheduler()


    scheduler.schedule(
        "test",
    )


    scheduler.clear()


    assert (
        scheduler.pending()
        ==
        0
    )



def test_status():

    scheduler = RuntimeScheduler()


    result = scheduler.status()


    assert "pending" in result

    assert "executed" in result
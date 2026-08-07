"""
Runtime Scheduler Orchestrator Tests
"""

from services.intelligence.runtime.runtime_scheduler_orchestrator import (
    RuntimeSchedulerOrchestrator,
)



def test_init():

    scheduler = RuntimeSchedulerOrchestrator()

    assert (
        scheduler.running
        is False
    )



def test_start():

    scheduler = RuntimeSchedulerOrchestrator()


    scheduler.start()


    assert (
        scheduler.running
        is True
    )



def test_schedule():

    scheduler = RuntimeSchedulerOrchestrator()


    scheduler.schedule(
        "investigation",
        5,
    )


    assert (
        scheduler.size()
        ==
        1
    )



def test_priority():

    scheduler = RuntimeSchedulerOrchestrator()


    scheduler.schedule(
        "low",
        1,
    )

    scheduler.schedule(
        "high",
        10,
    )


    result = scheduler.next_job()


    assert (
        result["name"]
        ==
        "high"
    )



def test_execute():

    scheduler = RuntimeSchedulerOrchestrator()


    scheduler.start()


    scheduler.schedule(
        "response",
        5,
    )


    result = scheduler.execute()


    assert (
        result["name"]
        ==
        "response"
    )



def test_clear():

    scheduler = RuntimeSchedulerOrchestrator()


    scheduler.schedule(
        "test",
    )


    scheduler.clear()


    assert (
        scheduler.size()
        ==
        0
    )



def test_status():

    scheduler = RuntimeSchedulerOrchestrator()


    result = scheduler.status()


    assert "running" in result

    assert "queue_size" in result

    assert "executions" in result
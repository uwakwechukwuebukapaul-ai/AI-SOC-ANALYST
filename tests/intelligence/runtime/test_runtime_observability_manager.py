"""
Runtime Observability Manager Tests
"""

from services.intelligence.runtime.runtime_observability_manager import (
    RuntimeObservabilityManager,
)



def test_manager_init():

    manager = RuntimeObservabilityManager()

    assert (
        manager.metrics
        ==
        {}
    )



def test_increment():

    manager = RuntimeObservabilityManager()


    manager.increment(
        "tasks",
    )


    assert (
        manager.get_metric(
            "tasks"
        )
        ==
        1
    )



def test_increment_amount():

    manager = RuntimeObservabilityManager()


    manager.increment(
        "events",
        5,
    )


    assert (
        manager.get_metric(
            "events"
        )
        ==
        5
    )



def test_record_event():

    manager = RuntimeObservabilityManager()


    manager.record_event(
        "task_completed"
    )


    assert (
        manager.event_count()
        ==
        1
    )



def test_clear():

    manager = RuntimeObservabilityManager()


    manager.increment(
        "jobs"
    )

    manager.record_event(
        "start"
    )


    manager.clear()


    assert (
        manager.event_count()
        ==
        0
    )



def test_status():

    manager = RuntimeObservabilityManager()


    result = manager.status()


    assert "metrics" in result

    assert "events" in result
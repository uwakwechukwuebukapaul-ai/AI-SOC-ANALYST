"""
Runtime Service Tests
"""

from services.intelligence.runtime.runtime_service import (
    RuntimeService,
)

from services.intelligence.runtime.task import Task



def create_task():

    return Task(
        capability="analysis",
        payload={
            "event": "test"
        }
    )



def test_service_init():

    service = RuntimeService()

    assert (
        service.active
        is False
    )



def test_start():

    service = RuntimeService()

    service.start()

    assert (
        service.active
        is True
    )



def test_stop():

    service = RuntimeService()

    service.start()

    service.stop()

    assert (
        service.active
        is False
    )



def test_submit():

    service = RuntimeService()

    result = service.submit(
        create_task()
    )

    assert (
        result["submitted"]
        is True
    )



def test_execute():

    service = RuntimeService()


    service.register_capability(
        "analysis",
        lambda task: "ok"
    )


    result = service.execute(
        create_task()
    )


    assert (
        result.success
        is True
    )



def test_health():

    service = RuntimeService()

    result = service.health()

    assert (
        "active"
        in result
    )

    assert (
        "runtime"
        in result
    )
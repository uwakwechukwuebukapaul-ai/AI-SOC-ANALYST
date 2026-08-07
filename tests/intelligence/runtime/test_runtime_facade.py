"""
Runtime Facade Tests
"""

from services.intelligence.runtime.runtime_facade import (
    RuntimeFacade,
)

from services.intelligence.runtime.task import Task



def create_task():

    return Task(
        capability="analysis",
        payload={
            "event": "test"
        }
    )



def test_facade_init():

    facade = RuntimeFacade()

    assert facade.service is not None



def test_boot():

    facade = RuntimeFacade()

    facade.boot()

    assert (
        facade.service.active
        is True
    )



def test_shutdown():

    facade = RuntimeFacade()

    facade.boot()

    facade.shutdown()

    assert (
        facade.service.active
        is False
    )



def test_submit():

    facade = RuntimeFacade()

    result = facade.submit(
        create_task()
    )

    assert (
        result["submitted"]
        is True
    )



def test_run():

    facade = RuntimeFacade()


    facade.register(
        "analysis",
        lambda task: "complete"
    )


    result = facade.run(
        create_task()
    )


    assert (
        result.success
        is True
    )



def test_status():

    facade = RuntimeFacade()

    result = facade.status()

    assert (
        "active"
        in result
    )
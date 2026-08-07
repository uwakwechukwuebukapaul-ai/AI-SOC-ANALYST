"""
Runtime Dispatcher Tests
"""

from services.intelligence.runtime.runtime_dispatcher import (
    RuntimeDispatcher,
)

from services.intelligence.runtime.task import Task



def create_task():

    return Task(
        capability="test.capability",
        payload={
            "message": "hello"
        }
    )



def test_dispatcher_init():

    dispatcher = RuntimeDispatcher()

    assert (
        dispatcher.worker_count()
        ==
        0
    )



def test_register_handler():

    dispatcher = RuntimeDispatcher()


    dispatcher.register_handler(
        "test.capability",
        lambda task: "success"
    )


    assert (
        "test.capability"
        in
        dispatcher.handlers
    )



def test_dispatch_success():

    dispatcher = RuntimeDispatcher()


    dispatcher.register_handler(
        "test.capability",
        lambda task: "done"
    )


    result = dispatcher.dispatch(
        create_task()
    )


    assert (
        result.success
        is True
    )



def test_dispatch_failure():

    dispatcher = RuntimeDispatcher()


    result = dispatcher.dispatch(
        create_task()
    )


    assert (
        result.success
        is False
    )



def test_status():

    dispatcher = RuntimeDispatcher()

    result = dispatcher.status()


    assert "workers" in result

    assert "handlers" in result
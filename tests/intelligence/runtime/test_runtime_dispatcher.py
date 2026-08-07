"""
Runtime Dispatcher Tests
"""

from services.intelligence.runtime.runtime_dispatcher import (
    RuntimeDispatcher,
)



def test_dispatcher_init():

    dispatcher = RuntimeDispatcher()

    assert (
        dispatcher.dispatched
        ==
        0
    )



def test_register():

    dispatcher = RuntimeDispatcher()


    handler = lambda data: data


    dispatcher.register(
        "analysis",
        handler,
    )


    assert (
        dispatcher.exists(
            "analysis"
        )
        is True
    )



def test_dispatch():

    dispatcher = RuntimeDispatcher()


    def handler(data):
        return {
            "result":
                data["value"]
        }


    dispatcher.register(
        "test",
        handler,
    )


    result = dispatcher.dispatch(
        "test",
        {
            "value": 10
        },
    )


    assert (
        result["result"]
        ==
        10
    )



def test_counter():

    dispatcher = RuntimeDispatcher()


    dispatcher.register(
        "task",
        lambda x: x,
    )


    dispatcher.dispatch(
        "task",
        {},
    )


    assert (
        dispatcher.dispatched
        ==
        1
    )



def test_clear():

    dispatcher = RuntimeDispatcher()


    dispatcher.register(
        "test",
        lambda x: x,
    )


    dispatcher.clear()


    assert (
        dispatcher.exists(
            "test"
        )
        is False
    )



def test_status():

    dispatcher = RuntimeDispatcher()


    result = dispatcher.status()


    assert "handlers" in result

    assert "dispatched" in result
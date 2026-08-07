"""
Runtime Event Bus Tests
"""

from services.intelligence.runtime.runtime_event_bus import (
    RuntimeEventBus,
)



def test_bus_init():

    bus = RuntimeEventBus()

    assert (
        bus.history
        ==
        []
    )



def test_subscribe():

    bus = RuntimeEventBus()


    handler = lambda payload: None


    bus.subscribe(
        "alert",
        handler,
    )


    assert (
        bus.subscriber_count(
            "alert"
        )
        ==
        1
    )



def test_publish():

    bus = RuntimeEventBus()


    received = []


    def handler(payload):

        received.append(
            payload
        )


    bus.subscribe(
        "incident",
        handler,
    )


    result = bus.publish(
        "incident",
        {
            "id": 1
        },
    )


    assert (
        result
        ==
        1
    )

    assert (
        received[0]["id"]
        ==
        1
    )



def test_history():

    bus = RuntimeEventBus()


    bus.publish(
        "test",
        {},
    )


    assert (
        len(
            bus.history
        )
        ==
        1
    )



def test_clear():

    bus = RuntimeEventBus()


    bus.publish(
        "event",
        {},
    )


    bus.clear()


    assert (
        len(
            bus.history
        )
        ==
        0
    )



def test_status():

    bus = RuntimeEventBus()


    result = bus.status()


    assert "events" in result

    assert "event_types" in result
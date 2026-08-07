"""
Runtime Event Bus Tests
"""

from services.intelligence.runtime.runtime_event_bus import (
    RuntimeEventBus,
)



def test_init():

    bus = RuntimeEventBus()

    assert (
        len(bus.events)
        ==
        0
    )



def test_subscribe():

    bus = RuntimeEventBus()


    bus.subscribe(
        "alert",
        lambda data: data,
    )


    assert (
        bus.subscriber_count(
            "alert"
        )
        ==
        1
    )



def test_publish():

    received = []


    bus = RuntimeEventBus()


    bus.subscribe(
        "alert",
        lambda data: received.append(data),
    )


    bus.publish(
        "alert",
        {
            "severity":
                "high"
        },
    )


    assert (
        received[0]["severity"]
        ==
        "high"
    )



def test_event_history():

    bus = RuntimeEventBus()


    bus.publish(
        "test",
        {},
    )


    assert (
        len(bus.events)
        ==
        1
    )



def test_clear():

    bus = RuntimeEventBus()


    bus.publish(
        "test",
        {},
    )


    bus.clear()


    assert (
        len(bus.events)
        ==
        0
    )



def test_status():

    bus = RuntimeEventBus()


    result = bus.status()


    assert "events" in result

    assert "subscriptions" in result
"""
Runtime Event Bus Tests
"""

from services.intelligence.runtime.runtime_event_bus import (
    RuntimeEventBus,
)



def test_init():

    bus = RuntimeEventBus()

    assert (
        bus.count()
        ==
        0
    )



def test_subscribe():

    bus = RuntimeEventBus()


    bus.subscribe(
        "threat_detected",
        lambda data: True,
    )


    assert (
        bus.exists(
            "threat_detected"
        )
        is True
    )



def test_publish():

    bus = RuntimeEventBus()


    bus.subscribe(
        "incident",
        lambda data: {
            "handled":
                True
        },
    )


    result = bus.publish(
        "incident",
        {},
    )


    assert (
        result[0]["handled"]
        is True
    )



def test_multiple_handlers():

    bus = RuntimeEventBus()


    bus.subscribe(
        "event",
        lambda data: 1,
    )

    bus.subscribe(
        "event",
        lambda data: 2,
    )


    result = bus.publish(
        "event",
        {},
    )


    assert (
        len(result)
        ==
        2
    )



def test_clear():

    bus = RuntimeEventBus()


    bus.subscribe(
        "test",
        lambda x: True,
    )


    bus.clear()


    assert (
        bus.exists(
            "test"
        )
        is False
    )



def test_status():

    bus = RuntimeEventBus()


    result = bus.status()


    assert "events" in result

    assert "subscriptions" in result
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


    def handler(data):
        pass


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


    bus.publish(
        "incident",
        {
            "id":
                "INC001"
        },
    )


    assert (
        bus.count()
        ==
        1
    )



def test_dispatch():

    bus = RuntimeEventBus()


    received = []


    def handler(data):
        received.append(
            data
        )


    bus.subscribe(
        "alert",
        handler,
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



def test_clear():

    bus = RuntimeEventBus()


    bus.publish(
        "test",
        {},
    )


    bus.clear()


    assert (
        bus.count()
        ==
        0
    )



def test_status():

    bus = RuntimeEventBus()


    result = bus.status()


    assert "events" in result

    assert "subscribers" in result
"""
Runtime Message Bus Tests
"""

from services.intelligence.runtime.runtime_message_bus import (
    RuntimeMessageBus,
)



def test_init():

    bus = RuntimeMessageBus()

    assert (
        bus.count()
        ==
        0
    )



def test_send():

    bus = RuntimeMessageBus()


    bus.send(
        "agent",
        {
            "task":
                "investigate"
        },
    )


    assert (
        bus.count()
        ==
        1
    )



def test_register_handler():

    bus = RuntimeMessageBus()


    def handler(message):
        pass


    bus.register_handler(
        "agent",
        handler,
    )


    assert (
        bus.handlers_count(
            "agent"
        )
        ==
        1
    )



def test_dispatch():

    bus = RuntimeMessageBus()


    received = []


    def handler(message):
        received.append(
            message
        )


    bus.register_handler(
        "engine",
        handler,
    )


    bus.send(
        "engine",
        {
            "status":
                "run"
        },
    )


    assert (
        received[0]["status"]
        ==
        "run"
    )



def test_multiple_messages():

    bus = RuntimeMessageBus()


    bus.send(
        "service",
        {},
    )


    bus.send(
        "service",
        {},
    )


    assert (
        bus.count()
        ==
        2
    )



def test_clear():

    bus = RuntimeMessageBus()


    bus.send(
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

    bus = RuntimeMessageBus()


    result = bus.status()


    assert "messages" in result

    assert "targets" in result
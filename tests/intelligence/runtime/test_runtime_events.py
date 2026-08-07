from services.intelligence.runtime.runtime_events import (
    RuntimeEventBus,
)



def test_event_bus_init():

    bus = RuntimeEventBus()

    assert len(
        bus.history
    ) == 0



def test_publish():

    bus = RuntimeEventBus()


    event = bus.publish(
        "task.created",
        {
            "id": 1
        }
    )


    assert event.name == "task.created"

    assert len(
        bus.history
    ) == 1



def test_subscribe():

    bus = RuntimeEventBus()

    received = []


    def handler(event):

        received.append(
            event
        )


    bus.subscribe(
        "alert",
        handler,
    )


    bus.publish(
        "alert",
        "test"
    )


    assert len(received) == 1



def test_history():

    bus = RuntimeEventBus()


    bus.publish(
        "event"
    )


    history = bus.get_history()


    assert len(history) == 1



def test_clear():

    bus = RuntimeEventBus()


    bus.publish(
        "event"
    )


    bus.clear()


    assert len(
        bus.history
    ) == 0



def test_status():

    bus = RuntimeEventBus()


    status = bus.status()


    assert "events" in status

    assert "subscriptions" in status
from services.intelligence.runtime.event_bus import EventBus


def test_subscribe():

    bus = EventBus()

    def handler(event):
        pass

    bus.subscribe("alert", handler)

    assert bus.subscriber_count("alert") == 1


def test_publish():

    bus = EventBus()

    received = {}

    def handler(event):
        received["value"] = event

    bus.subscribe("alert", handler)

    bus.publish(
        "alert",
        {"severity": "high"},
    )

    assert received["value"]["severity"] == "high"


def test_unsubscribe():

    bus = EventBus()

    def handler(event):
        pass

    bus.subscribe("alert", handler)
    bus.unsubscribe("alert", handler)

    assert bus.subscriber_count("alert") == 0


def test_clear():

    bus = EventBus()

    def handler(event):
        pass

    bus.subscribe("alert", handler)

    bus.clear()

    assert bus.subscriber_count("alert") == 0


def test_multiple_handlers():

    bus = EventBus()

    counter = {"count": 0}

    def handler(event):
        counter["count"] += 1

    bus.subscribe("alert", handler)
    bus.subscribe("alert", handler)

    bus.publish("alert")

    assert counter["count"] == 1
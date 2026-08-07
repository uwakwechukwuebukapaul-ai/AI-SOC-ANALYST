from services.intelligence.runtime.runtime_events import (
    RuntimeEventManager,
)



def test_event_manager_init():

    manager = RuntimeEventManager()

    assert manager.count() == 0



def test_publish():

    manager = RuntimeEventManager()

    event = manager.publish(
        "task_completed",
        {
            "task": "analysis"
        }
    )

    assert event.event_type == "task_completed"

    assert manager.count() == 1



def test_subscribe():

    manager = RuntimeEventManager()

    received = []


    def handler(event):

        received.append(event)



    manager.subscribe(
        "alert",
        handler,
    )


    manager.publish(
        "alert",
        {
            "severity": "high"
        }
    )


    assert len(received) == 1



def test_clear():

    manager = RuntimeEventManager()

    manager.publish(
        "test"
    )

    manager.clear()

    assert manager.count() == 0



def test_to_dict():

    manager = RuntimeEventManager()

    data = manager.to_dict()

    assert "events" in data
    assert "listeners" in data
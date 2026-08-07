from services.intelligence.runtime.event_store import (
    RuntimeEventStore
)


def test_store_init():

    store = RuntimeEventStore()

    assert store.count() == 0



def test_append():

    store = RuntimeEventStore()

    store.append(
        "task_created"
    )

    assert store.count() == 1



def test_payload():

    store = RuntimeEventStore()

    store.append(
        "execution",
        {
            "task_id": "123"
        }
    )

    event = store.latest()

    assert event.payload["task_id"] == "123"



def test_latest_empty():

    store = RuntimeEventStore()

    assert store.latest() is None



def test_find():

    store = RuntimeEventStore()

    store.append(
        "success"
    )

    store.append(
        "failure"
    )

    result = store.find(
        "success"
    )

    assert len(result) == 1



def test_clear():

    store = RuntimeEventStore()

    store.append(
        "event"
    )

    store.clear()

    assert store.count() == 0



def test_to_dict():

    store = RuntimeEventStore()

    store.append(
        "runtime"
    )

    data = store.to_dict()

    assert data[0]["event_type"] == "runtime"
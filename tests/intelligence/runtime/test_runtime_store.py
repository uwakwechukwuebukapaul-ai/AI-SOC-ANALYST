from services.intelligence.runtime.runtime_store import (
    RuntimeStore,
)



def test_store_init():

    store = RuntimeStore()

    assert store.storage == {}



def test_save_and_load():

    store = RuntimeStore()


    store.save(
        "task",
        {
            "status": "running"
        },
    )


    result = store.load(
        "task"
    )


    assert result["status"] == "running"



def test_exists():

    store = RuntimeStore()


    store.save(
        "key",
        "value",
    )


    assert store.exists(
        "key"
    )



def test_delete():

    store = RuntimeStore()


    store.save(
        "key",
        "value",
    )


    store.delete(
        "key"
    )


    assert not store.exists(
        "key"
    )



def test_snapshot_restore():

    store = RuntimeStore()


    store.save(
        "state",
        100,
    )


    store.snapshot(
        "backup"
    )


    store.save(
        "state",
        200,
    )


    store.restore(
        "backup"
    )


    assert store.load(
        "state"
    ) == 100



def test_clear():

    store = RuntimeStore()


    store.save(
        "a",
        1,
    )


    store.clear()


    assert store.storage == {}



def test_to_dict():

    store = RuntimeStore()


    data = store.to_dict()


    assert "storage" in data

    assert "snapshots" in data
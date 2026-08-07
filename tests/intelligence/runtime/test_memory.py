"""
Runtime Memory Tests
"""


from services.intelligence.runtime.memory import (
    RuntimeMemory,
)



def test_default_memory():

    memory = RuntimeMemory()

    assert memory.size() == 0



def test_set_value():

    memory = RuntimeMemory()

    memory.set(
        "name",
        "Sentinel",
    )


    assert memory.get(
        "name"
    ) == "Sentinel"



def test_get_default():

    memory = RuntimeMemory()


    assert memory.get(
        "missing",
        "default",
    ) == "default"



def test_exists():

    memory = RuntimeMemory()


    memory.set(
        "key",
        "value",
    )


    assert memory.exists(
        "key"
    )



def test_delete():

    memory = RuntimeMemory()


    memory.set(
        "key",
        "value",
    )


    result = memory.delete(
        "key"
    )


    assert result is True

    assert memory.exists(
        "key"
    ) is False



def test_clear():

    memory = RuntimeMemory()


    memory.set(
        "one",
        1,
    )

    memory.set(
        "two",
        2,
    )


    memory.clear()


    assert memory.size() == 0



def test_snapshot():

    memory = RuntimeMemory()


    memory.set(
        "ioc",
        "8.8.8.8",
    )


    snapshot = memory.snapshot()


    assert snapshot["ioc"] == "8.8.8.8"



def test_to_dict():

    memory = RuntimeMemory()


    data = memory.to_dict()


    assert "size" in data

    assert "memory" in data
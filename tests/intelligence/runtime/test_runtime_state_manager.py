"""
Runtime State Manager Tests
"""

from services.intelligence.runtime.runtime_state_manager import (
    RuntimeStateManager,
)



def test_init():

    manager = RuntimeStateManager()

    assert (
        manager.count()
        ==
        0
    )



def test_set_get():

    manager = RuntimeStateManager()


    manager.set(
        "case_001",
        {
            "status":
                "investigating"
        },
    )


    result = manager.get(
        "case_001"
    )


    assert (
        result["status"]
        ==
        "investigating"
    )



def test_default():

    manager = RuntimeStateManager()


    result = manager.get(
        "missing"
    )


    assert result is None



def test_update():

    manager = RuntimeStateManager()


    manager.set(
        "workflow",
        {
            "step":
                1
        },
    )


    manager.update(
        "workflow",
        {
            "step":
                2
        },
    )


    assert (
        manager.get(
            "workflow"
        )["step"]
        ==
        2
    )



def test_remove():

    manager = RuntimeStateManager()


    manager.set(
        "temp",
        True,
    )


    manager.remove(
        "temp"
    )


    assert (
        manager.exists(
            "temp"
        )
        is False
    )



def test_clear():

    manager = RuntimeStateManager()


    manager.set(
        "test",
        True,
    )


    manager.clear()


    assert (
        manager.count()
        ==
        0
    )



def test_status():

    manager = RuntimeStateManager()


    result = manager.status()


    assert "states" in result

    assert "count" in result
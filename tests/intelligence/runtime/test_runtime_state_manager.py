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



def test_create():

    manager = RuntimeStateManager()


    manager.create(
        "agent_state",
        {
            "status":
                "running"
        },
    )


    assert (
        manager.exists(
            "agent_state"
        )
        is True
    )



def test_get():

    manager = RuntimeStateManager()


    manager.create(
        "workflow",
        {
            "step":
                1
        },
    )


    result = manager.get(
        "workflow"
    )


    assert (
        result["step"]
        ==
        1
    )



def test_update():

    manager = RuntimeStateManager()


    manager.create(
        "case",
        {
            "status":
                "open"
        },
    )


    manager.update(
        "case",
        {
            "status":
                "closed"
        },
    )


    assert (
        manager.get(
            "case"
        )["status"]
        ==
        "closed"
    )



def test_remove():

    manager = RuntimeStateManager()


    manager.create(
        "test",
        {},
    )


    manager.remove(
        "test"
    )


    assert (
        manager.exists(
            "test"
        )
        is False
    )



def test_clear():

    manager = RuntimeStateManager()


    manager.create(
        "test",
        {},
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
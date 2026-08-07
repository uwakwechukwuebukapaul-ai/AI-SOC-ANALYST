"""
Runtime Session Manager Tests
"""

from services.intelligence.runtime.runtime_session_manager import (
    RuntimeSessionManager,
)



def test_init():

    manager = RuntimeSessionManager()

    assert (
        manager.count()
        ==
        0
    )



def test_create():

    manager = RuntimeSessionManager()


    manager.create(
        "session01",
        "analyst01",
    )


    assert (
        manager.active(
            "session01"
        )
        is True
    )



def test_get():

    manager = RuntimeSessionManager()


    manager.create(
        "session01",
        "agent",
        {
            "case":
                "INC001"
        },
    )


    result = manager.get(
        "session01"
    )


    assert (
        result["owner"]
        ==
        "agent"
    )



def test_terminate():

    manager = RuntimeSessionManager()


    manager.create(
        "session01",
        "analyst",
    )


    manager.terminate(
        "session01"
    )


    assert (
        manager.active(
            "session01"
        )
        is False
    )



def test_missing_session():

    manager = RuntimeSessionManager()


    assert (
        manager.active(
            "missing"
        )
        is False
    )



def test_clear():

    manager = RuntimeSessionManager()


    manager.create(
        "test",
        "user",
    )


    manager.clear()


    assert (
        manager.count()
        ==
        0
    )



def test_status():

    manager = RuntimeSessionManager()


    result = manager.status()


    assert "sessions" in result

    assert "count" in result
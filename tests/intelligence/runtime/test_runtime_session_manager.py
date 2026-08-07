"""
Runtime Session Manager Tests
"""

from services.intelligence.runtime.runtime_session_manager import (
    RuntimeSessionManager,
)



def test_manager_init():

    manager = RuntimeSessionManager()

    assert (
        len(
            manager.sessions
        )
        ==
        0
    )



def test_create():

    manager = RuntimeSessionManager()


    session_id = manager.create(
        "analyst"
    )


    assert (
        session_id
        in
        manager.sessions
    )



def test_get():

    manager = RuntimeSessionManager()


    session_id = manager.create(
        "ai_agent"
    )


    session = manager.get(
        session_id
    )


    assert (
        session["owner"]
        ==
        "ai_agent"
    )



def test_close():

    manager = RuntimeSessionManager()


    session_id = manager.create(
        "analyst"
    )


    manager.close(
        session_id
    )


    session = manager.get(
        session_id
    )


    assert (
        session["active"]
        is False
    )



def test_remove():

    manager = RuntimeSessionManager()


    session_id = manager.create(
        "agent"
    )


    manager.remove(
        session_id
    )


    assert (
        manager.get(
            session_id
        )
        is None
    )



def test_active_sessions():

    manager = RuntimeSessionManager()


    manager.create(
        "analyst"
    )


    assert (
        len(
            manager.active_sessions()
        )
        ==
        1
    )



def test_status():

    manager = RuntimeSessionManager()


    result = manager.status()


    assert "total" in result

    assert "active" in result
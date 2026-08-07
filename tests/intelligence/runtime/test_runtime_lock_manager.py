"""
Runtime Lock Manager Tests
"""

from services.intelligence.runtime.runtime_lock_manager import (
    RuntimeLockManager,
)



def test_init():

    manager = RuntimeLockManager()

    assert (
        manager.count()
        ==
        0
    )



def test_acquire():

    manager = RuntimeLockManager()


    result = manager.acquire(
        "case_INC001",
        "agent01",
    )


    assert result is True



def test_duplicate_lock():

    manager = RuntimeLockManager()


    manager.acquire(
        "resource",
        "owner1",
    )


    result = manager.acquire(
        "resource",
        "owner2",
    )


    assert result is False



def test_owner():

    manager = RuntimeLockManager()


    manager.acquire(
        "task",
        "agent",
    )


    assert (
        manager.owner(
            "task"
        )
        ==
        "agent"
    )



def test_release():

    manager = RuntimeLockManager()


    manager.acquire(
        "task",
        "agent",
    )


    manager.release(
        "task"
    )


    assert (
        manager.locked(
            "task"
        )
        is False
    )



def test_clear():

    manager = RuntimeLockManager()


    manager.acquire(
        "test",
        "owner",
    )


    manager.clear()


    assert (
        manager.count()
        ==
        0
    )



def test_status():

    manager = RuntimeLockManager()


    result = manager.status()


    assert "locks" in result

    assert "count" in result
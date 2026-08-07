"""
Runtime Backup Manager Tests
"""

from services.intelligence.runtime.runtime_backup_manager import (
    RuntimeBackupManager,
)



def test_init():

    manager = RuntimeBackupManager()

    assert (
        manager.count()
        ==
        0
    )



def test_create():

    manager = RuntimeBackupManager()


    manager.create(
        "backup01",
        {
            "case":
                "INC001"
        },
    )


    assert (
        manager.exists(
            "backup01"
        )
        is True
    )



def test_restore():

    manager = RuntimeBackupManager()


    manager.create(
        "backup01",
        {
            "status":
                "running"
        },
    )


    result = manager.restore(
        "backup01"
    )


    assert (
        result["status"]
        ==
        "running"
    )



def test_missing_restore():

    manager = RuntimeBackupManager()


    assert (
        manager.restore(
            "missing"
        )
        is None
    )



def test_remove():

    manager = RuntimeBackupManager()


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

    manager = RuntimeBackupManager()


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

    manager = RuntimeBackupManager()


    result = manager.status()


    assert "backups" in result

    assert "count" in result
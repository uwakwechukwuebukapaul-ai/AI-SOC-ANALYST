from services.intelligence.runtime.recovery_manager import (
    RecoveryManager,
)



def test_recovery_init():

    manager = RecoveryManager()

    assert manager.recoveries == 0



def test_record_failure():

    manager = RecoveryManager()


    manager.record_failure(
        "task1",
        "timeout",
    )


    assert manager.has_failure(
        "task1"
    )



def test_checkpoint():

    manager = RecoveryManager()


    manager.store.save(
        "state",
        "running",
    )


    manager.create_checkpoint(
        "backup"
    )


    assert "backup" in manager.store.snapshots



def test_recover():

    manager = RecoveryManager()


    manager.store.save(
        "value",
        10,
    )


    manager.create_checkpoint(
        "checkpoint"
    )


    manager.store.save(
        "value",
        20,
    )


    result = manager.recover(
        "checkpoint"
    )


    assert result["value"] == 10



def test_mark_recovered():

    manager = RecoveryManager()


    manager.record_failure(
        "task",
        "error",
    )


    manager.mark_recovered(
        "task"
    )


    assert (
        manager.failures["task"]["recovered"]
        is True
    )



def test_clear_failure():

    manager = RecoveryManager()


    manager.record_failure(
        "task",
        "error",
    )


    manager.clear_failure(
        "task"
    )


    assert not manager.has_failure(
        "task"
    )



def test_status():

    manager = RecoveryManager()


    status = manager.status()


    assert "failures" in status
    assert "recoveries" in status
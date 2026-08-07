from services.intelligence.runtime.runtime_manager import (
    RuntimeManager,
)


def test_default_state():

    manager = RuntimeManager()

    assert manager.running is False



def test_start():

    manager = RuntimeManager()

    manager.start()

    assert manager.running is True



def test_stop():

    manager = RuntimeManager()

    manager.start()

    manager.stop()

    assert manager.running is False



def test_restart():

    manager = RuntimeManager()

    manager.restart()

    assert manager.running is True



def test_health():

    manager = RuntimeManager()

    result = manager.health()

    assert "running" in result
    assert "engine" in result
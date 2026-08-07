from services.intelligence.runtime.runtime_manager import RuntimeManager
from services.intelligence.runtime.task import Task


def test_manager_init():

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



def test_submit():

    manager = RuntimeManager()

    manager.start()

    task = Task(
        capability="test",
        payload={}
    )

    manager.submit(task)

    assert manager.engine.queue.size() == 1



def test_status():

    manager = RuntimeManager()

    status = manager.status()

    assert "running" in status

    assert "engine" in status
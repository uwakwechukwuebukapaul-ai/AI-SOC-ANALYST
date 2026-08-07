from services.intelligence.runtime.runtime_controller import (
    RuntimeController,
)

from services.intelligence.runtime.task import Task


def test_controller_init():

    controller = RuntimeController()

    assert controller.running is False



def test_start():

    controller = RuntimeController()

    controller.start()

    assert controller.running is True



def test_stop():

    controller = RuntimeController()

    controller.start()

    controller.stop()

    assert controller.running is False



def test_submit():

    controller = RuntimeController()

    task = Task(
        capability="analysis",
        payload={
            "event": "test"
        }
    )

    controller.submit(task)

    assert controller.orchestrator.engine.queue.size() == 1



def test_status():

    controller = RuntimeController()

    status = controller.status()

    assert "running" in status
    assert "orchestrator" in status
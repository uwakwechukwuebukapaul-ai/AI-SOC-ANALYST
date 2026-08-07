"""
Sentinel DNA Runtime Worker Tests
"""

from services.intelligence.runtime.worker import RuntimeWorker
from services.intelligence.runtime.task import Task


def create_task():
    return Task(
        capability="test_capability",
        payload={
            "value": "test"
        },
    )


def test_worker_init():

    worker = RuntimeWorker()

    assert worker.running is False
    assert worker.executed_tasks == 0
    assert worker.failed_tasks == 0



def test_start():

    worker = RuntimeWorker()

    worker.start()

    assert worker.running is True



def test_stop():

    worker = RuntimeWorker()

    worker.start()

    worker.stop()

    assert worker.running is False



def test_execute_task():

    worker = RuntimeWorker()

    task = create_task()


    def handler(task, context):

        return {
            "status": "completed"
        }


    result = worker.execute_task(
        task,
        handler,
    )


    assert result.success is True
    assert worker.executed_tasks == 1
    assert worker.failed_tasks == 0



def test_worker_status():

    worker = RuntimeWorker()

    status = worker.status()


    assert "running" in status
    assert "executed_tasks" in status
    assert "failed_tasks" in status
    assert "engine" in status
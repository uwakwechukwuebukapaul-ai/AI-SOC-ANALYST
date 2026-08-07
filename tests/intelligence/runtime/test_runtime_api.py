"""
Sentinel DNA Runtime API Tests
"""

from services.intelligence.runtime.runtime_api import RuntimeAPI
from services.intelligence.runtime.task import Task



def test_api_init():

    api = RuntimeAPI()

    assert api.engine is not None
    assert api.worker is not None
    assert api.health is not None



def test_submit_task():

    api = RuntimeAPI()

    task = Task(
        capability="test",
        payload={}
    )

    result = api.submit_task(task)

    assert result["submitted"] is True



def test_start():

    api = RuntimeAPI()

    api.start()

    assert api.worker.running is True



def test_stop():

    api = RuntimeAPI()

    api.start()

    api.stop()

    assert api.worker.running is False



def test_status():

    api = RuntimeAPI()

    status = api.status()

    assert "worker" in status
    assert "health" in status
    assert "runtime" in status
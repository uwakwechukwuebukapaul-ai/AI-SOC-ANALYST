"""
Tests for Sentinel DNA Runtime Orchestrator
"""

from services.intelligence.runtime.orchestrator import (
    RuntimeOrchestrator,
)

from services.intelligence.runtime.task import Task



def test_orchestrator_init():

    orchestrator = RuntimeOrchestrator()

    assert orchestrator.running is False

    assert orchestrator.engine is not None



def test_start():

    orchestrator = RuntimeOrchestrator()

    orchestrator.start()

    assert orchestrator.running is True



def test_stop():

    orchestrator = RuntimeOrchestrator()

    orchestrator.start()

    orchestrator.stop()

    assert orchestrator.running is False



def test_submit():

    orchestrator = RuntimeOrchestrator()

    task = Task(
        capability="test",
        payload={
            "value": 1
        }
    )

    orchestrator.submit(task)

    assert orchestrator.engine.queue.size() == 1



def test_execute():

    orchestrator = RuntimeOrchestrator()

    task = Task(
        capability="test",
        payload={}
    )


    def handler(task, context):

        return {
            "result": "ok"
        }


    result = orchestrator.execute(
        task,
        handler,
    )

    assert result.success is True



def test_status():

    orchestrator = RuntimeOrchestrator()

    status = orchestrator.status()

    assert "running" in status

    assert "workers" in status

    assert "engine" in status
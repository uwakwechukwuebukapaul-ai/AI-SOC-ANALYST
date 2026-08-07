"""
Sentinel DNA Workflow Executor Tests
"""

from services.intelligence.runtime.workflow_executor import (
    WorkflowExecutor
)

from services.intelligence.runtime.task import Task



def test_executor_init():

    executor = WorkflowExecutor()

    assert executor.runtime is not None
    assert executor.workflows == {}



def test_register_workflow():

    executor = WorkflowExecutor()

    tasks = [
        Task(
            capability="analysis",
            payload={}
        )
    ]

    executor.register_workflow(
        "investigation_1",
        tasks,
    )

    assert "investigation_1" in executor.workflows



def test_execute_workflow():

    executor = WorkflowExecutor()


    task = Task(
        capability="test",
        payload={}
    )


    executor.register_workflow(
        "workflow_1",
        [task],
    )


    def handler(task, context):

        return {
            "completed": True
        }


    results = executor.execute_workflow(
        "workflow_1",
        handler,
    )


    assert len(results) == 1
    assert results[0].success is True



def test_status():

    executor = WorkflowExecutor()

    status = executor.status()

    assert "workflow_count" in status
    assert "workflows" in status
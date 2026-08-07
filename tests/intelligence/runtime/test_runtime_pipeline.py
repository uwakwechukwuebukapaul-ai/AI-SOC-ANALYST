"""
Runtime Pipeline Tests
"""

from services.intelligence.runtime.runtime_pipeline import (
    RuntimePipeline,
)

from services.intelligence.runtime.task import Task



def create_task():

    return Task(
        capability="analysis",
        payload={
            "value": 10
        }
    )



def test_pipeline_init():

    pipeline = RuntimePipeline()

    assert (
        pipeline.size()
        ==
        0
    )



def test_submit():

    pipeline = RuntimePipeline()

    pipeline.submit(
        create_task()
    )

    assert (
        pipeline.size()
        ==
        1
    )



def test_register_handler():

    pipeline = RuntimePipeline()

    pipeline.register_handler(
        "analysis",
        lambda task: "completed"
    )

    assert (
        "analysis"
        in
        pipeline.dispatcher.handlers
    )



def test_execute():

    pipeline = RuntimePipeline()

    pipeline.register_handler(
        "analysis",
        lambda task: "completed"
    )


    result = pipeline.execute(
        create_task()
    )


    assert (
        result.success
        is True
    )



def test_clear():

    pipeline = RuntimePipeline()

    pipeline.submit(
        create_task()
    )

    pipeline.clear()

    assert (
        pipeline.size()
        ==
        0
    )



def test_status():

    pipeline = RuntimePipeline()

    result = pipeline.status()

    assert "tasks" in result

    assert "dispatcher" in result
"""
Runtime Pipeline Tests
"""

from services.intelligence.runtime.runtime_pipeline import (
    RuntimePipeline,
)



def test_pipeline_init():

    pipeline = RuntimePipeline()

    assert (
        pipeline.processed
        ==
        0
    )



def test_register_handler():

    pipeline = RuntimePipeline()


    pipeline.register_handler(
        "analysis",
        lambda data: data,
    )


    assert (
        pipeline.dispatcher.exists(
            "analysis"
        )
        is True
    )



def test_submit():

    pipeline = RuntimePipeline()


    pipeline.submit(
        "test",
        {
            "value": 1
        },
    )


    assert (
        pipeline.size()
        ==
        1
    )



def test_process():

    pipeline = RuntimePipeline()


    pipeline.register_handler(
        "test",
        lambda data: {
            "output":
                data["value"]
        },
    )


    pipeline.submit(
        "test",
        {
            "value": 5
        },
    )


    result = pipeline.process()


    assert (
        result["output"]
        ==
        5
    )



def test_clear():

    pipeline = RuntimePipeline()


    pipeline.submit(
        "task",
        {},
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


    assert "queued" in result

    assert "processed" in result
"""
Tests for Execution Pipeline
"""

from services.intelligence.runtime.execution_pipeline import (
    ExecutionPipeline,
)



def test_pipeline_init():

    pipeline = ExecutionPipeline()

    assert pipeline.size() == 0



def test_add_stage():

    pipeline = ExecutionPipeline()


    def stage(data):
        return data


    pipeline.add_stage(stage)

    assert pipeline.size() == 1



def test_execute():

    pipeline = ExecutionPipeline()


    def stage_one(data):
        return data + 1


    def stage_two(data):
        return data * 2


    pipeline.add_stage(stage_one)
    pipeline.add_stage(stage_two)


    result = pipeline.execute(5)

    assert result == 12



def test_remove_stage():

    pipeline = ExecutionPipeline()


    def stage(data):
        return data


    pipeline.add_stage(stage)

    pipeline.remove_stage(stage)

    assert pipeline.size() == 0



def test_clear():

    pipeline = ExecutionPipeline()


    pipeline.add_stage(
        lambda x: x
    )

    pipeline.clear()

    assert pipeline.size() == 0



def test_status():

    pipeline = ExecutionPipeline()

    data = pipeline.status()

    assert data["stages"] == 0
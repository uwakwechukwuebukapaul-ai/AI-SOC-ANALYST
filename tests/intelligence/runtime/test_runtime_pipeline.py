from services.intelligence.runtime.runtime_pipeline import (
    PipelineStage,
    RuntimePipeline,
    RuntimePipelineManager,
)



def test_pipeline_stage():

    stage = PipelineStage(
        name="normalize",
        handler=lambda x: x + 1,
    )

    assert stage.execute(1) == 2



def test_pipeline_execute():

    pipeline = RuntimePipeline(
        name="test_pipeline"
    )


    pipeline.add_stage(
        PipelineStage(
            name="stage1",
            handler=lambda x: x + 1,
        )
    )


    result = pipeline.execute(5)


    assert result == 6



def test_register_pipeline():

    manager = RuntimePipelineManager()


    pipeline = RuntimePipeline(
        name="analysis"
    )


    manager.register(
        pipeline
    )


    assert "analysis" in manager.pipelines



def test_execute_pipeline():

    manager = RuntimePipelineManager()


    pipeline = RuntimePipeline(
        name="test"
    )


    pipeline.add_stage(
        PipelineStage(
            name="step",
            handler=lambda x: x * 2,
        )
    )


    manager.register(
        pipeline
    )


    result = manager.execute(
        "test",
        5,
    )


    assert result == 10



def test_to_dict():

    manager = RuntimePipelineManager()

    data = manager.to_dict()

    assert "pipelines" in data
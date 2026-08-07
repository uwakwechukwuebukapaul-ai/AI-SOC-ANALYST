"""
Tests for Runtime Controller
"""

from services.intelligence.runtime.runtime_controller import (
    RuntimeController,
)



def test_controller_init():

    controller = RuntimeController()

    assert controller.active is False



def test_start():

    controller = RuntimeController()

    controller.start()

    assert controller.active is True



def test_stop():

    controller = RuntimeController()

    controller.start()

    controller.stop()

    assert controller.active is False



def test_restart():

    controller = RuntimeController()

    controller.start()

    controller.restart()

    assert controller.active is True



def test_pipeline_execute():

    controller = RuntimeController()


    controller.pipeline.add_stage(
        lambda x: x + 1
    )


    result = controller.execute_pipeline(
        5
    )


    assert result == 6



def test_status():

    controller = RuntimeController()

    status = controller.status()

    assert "active" in status

    assert "orchestrator" in status

    assert "pipeline" in status
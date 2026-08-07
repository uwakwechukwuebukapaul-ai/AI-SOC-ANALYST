"""
Runtime Orchestration Service Tests
"""

from services.intelligence.runtime.runtime_orchestration_service import (
    RuntimeOrchestrationService,
)



def test_init():

    service = RuntimeOrchestrationService()

    assert (
        service.workflows
        ==
        0
    )



def test_start():

    service = RuntimeOrchestrationService()

    service.start()

    assert (
        service.control_plane.running
        is True
    )



def test_register():

    service = RuntimeOrchestrationService()


    service.register_capability(
        "analysis",
        lambda data: data,
    )


    assert (
        service.control_plane.execution.pipeline.dispatcher.exists(
            "analysis"
        )
        is True
    )



def test_submit_workflow():

    service = RuntimeOrchestrationService()


    service.submit_workflow(
        "test",
        {},
    )


    assert (
        service.workflows
        ==
        1
    )



def test_execute_workflow():

    service = RuntimeOrchestrationService()


    service.register_capability(
        "test",
        lambda data: {
            "done": True
        },
    )


    service.submit_workflow(
        "test",
        {},
    )


    result = service.execute_workflow()


    assert (
        result["done"]
        is True
    )



def test_status():

    service = RuntimeOrchestrationService()


    result = service.status()


    assert "workflows" in result

    assert "control_plane" in result
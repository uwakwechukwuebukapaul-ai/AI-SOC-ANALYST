from services.intelligence.runtime.runtime_state import (
    RuntimeState,
)



def test_state_init():

    state = RuntimeState()

    assert state.status == "initialized"



def test_update_status():

    state = RuntimeState()

    state.update_status(
        "running"
    )

    assert state.status == "running"



def test_worker_state():

    state = RuntimeState()

    state.set_worker_state(
        "worker-1",
        "active",
    )

    assert (
        state.get_worker_state("worker-1")
        ==
        "active"
    )



def test_task_state():

    state = RuntimeState()

    state.set_task_state(
        "task-1",
        "completed",
    )

    assert (
        state.get_task_state("task-1")
        ==
        "completed"
    )



def test_to_dict():

    state = RuntimeState()

    result = state.to_dict()

    assert "status" in result
    assert "workers" in result
    assert "tasks" in result
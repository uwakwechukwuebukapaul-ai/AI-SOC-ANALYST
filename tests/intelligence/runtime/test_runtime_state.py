from services.intelligence.runtime.runtime_state import RuntimeState


def test_state_init():

    state = RuntimeState()

    assert state.status == "initialized"



def test_start():

    state = RuntimeState()

    state.start()

    assert state.status == "running"



def test_stop():

    state = RuntimeState()

    state.stop()

    assert state.status == "stopped"



def test_worker_registration():

    state = RuntimeState()

    state.register_worker(
        "worker-1",
        "idle"
    )

    assert state.workers["worker-1"] == "idle"



def test_success_failure():

    state = RuntimeState()

    state.record_success()

    state.record_failure()

    assert state.executions == 2
    assert state.successful == 1
    assert state.failed == 1



def test_snapshot():

    state = RuntimeState()

    data = state.snapshot()

    assert "status" in data
    assert "workers" in data
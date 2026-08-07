"""
Runtime Execution Tracker Tests
"""

from services.intelligence.runtime.runtime_execution_tracker import (
    RuntimeExecutionTracker,
)



def test_init():

    tracker = RuntimeExecutionTracker()

    assert (
        tracker.count()
        ==
        0
    )



def test_start():

    tracker = RuntimeExecutionTracker()


    tracker.start(
        "exec001",
        "investigation",
    )


    assert (
        tracker.get(
            "exec001"
        )["status"]
        ==
        "running"
    )



def test_update():

    tracker = RuntimeExecutionTracker()


    tracker.start(
        "exec001",
        "analysis",
    )


    tracker.update(
        "exec001",
        "processing",
    )


    assert (
        tracker.get(
            "exec001"
        )["status"]
        ==
        "processing"
    )



def test_complete():

    tracker = RuntimeExecutionTracker()


    tracker.start(
        "exec001",
        "scan",
    )


    tracker.complete(
        "exec001",
        {
            "risk":
                "high"
        },
    )


    result = tracker.get(
        "exec001"
    )


    assert (
        result["status"]
        ==
        "completed"
    )

    assert (
        result["result"]["risk"]
        ==
        "high"
    )



def test_missing_execution():

    tracker = RuntimeExecutionTracker()


    assert (
        tracker.get(
            "missing"
        )
        is None
    )



def test_clear():

    tracker = RuntimeExecutionTracker()


    tracker.start(
        "test",
        "operation",
    )


    tracker.clear()


    assert (
        tracker.count()
        ==
        0
    )



def test_status():

    tracker = RuntimeExecutionTracker()


    result = tracker.status()


    assert "executions" in result

    assert "count" in result
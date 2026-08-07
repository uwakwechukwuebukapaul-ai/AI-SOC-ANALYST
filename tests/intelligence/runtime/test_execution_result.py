from services.intelligence.runtime.execution_result import (
    ExecutionResult,
)


def test_success():

    result = ExecutionResult(
        success=True,
        output={"ioc": "8.8.8.8"},
    )

    assert result.success
    assert not result.failed


def test_failure():

    result = ExecutionResult(
        success=False,
        error="Engine failure",
    )

    assert result.failed
    assert result.error == "Engine failure"


def test_metadata():

    result = ExecutionResult(
        success=True,
    )

    result.add_metadata(
        "engine",
        "ThreatFusion",
    )

    assert result.metadata["engine"] == "ThreatFusion"


def test_to_dict():

    result = ExecutionResult(
        success=True,
        output={"score": 95},
        confidence=0.94,
    )

    data = result.to_dict()

    assert data["success"] is True
    assert data["confidence"] == 0.94
    assert data["output"]["score"] == 95
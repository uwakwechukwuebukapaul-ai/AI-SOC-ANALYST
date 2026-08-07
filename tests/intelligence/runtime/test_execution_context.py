from services.intelligence.runtime.execution_context import (
    ExecutionContext,
)


def test_default_context():

    context = ExecutionContext()

    assert context.investigation_id is not None
    assert context.evidence == []
    assert context.shared_data == {}


def test_add_evidence():

    context = ExecutionContext()

    context.add_evidence(
        {"ioc": "8.8.8.8"}
    )

    assert len(context.evidence) == 1


def test_shared_data():

    context = ExecutionContext()

    context.set(
        "risk_score",
        95,
    )

    assert context.get("risk_score") == 95


def test_metadata():

    context = ExecutionContext()

    context.add_metadata(
        "engine",
        "ThreatFusion",
    )

    assert context.metadata["engine"] == "ThreatFusion"


def test_to_dict():

    context = ExecutionContext()

    data = context.to_dict()

    assert "investigation_id" in data
    assert "created_at" in data
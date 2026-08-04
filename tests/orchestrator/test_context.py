"""
Sentinel DNA
Investigation Context Tests

Validates investigation memory/state storage.
"""

from services.orchestrator.context import InvestigationContext


def create_context():
    return InvestigationContext(
        investigation_id="INV-TEST-001",
        case_id="CASE-TEST-001",
    )


def test_context_initialization():
    context = create_context()

    assert context.investigation_id == "INV-TEST-001"
    assert context.case_id == "CASE-TEST-001"


def test_context_default_status():
    context = create_context()

    assert context.status == "NEW"


def test_add_timeline_event():
    context = create_context()

    context.add_timeline_event(
        stage="INGESTING",
        message="Started evidence ingestion",
    )

    assert len(context.timeline) == 1
    assert context.timeline[0]["stage"] == "INGESTING"
    assert (
        context.timeline[0]["message"]
        == "Started evidence ingestion"
    )


def test_mark_completed():
    context = create_context()

    context.mark_completed()

    assert context.status == "COMPLETED"
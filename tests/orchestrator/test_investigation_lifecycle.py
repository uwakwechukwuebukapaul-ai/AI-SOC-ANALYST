from services.orchestrator.context import InvestigationContext
from services.orchestrator.workflow_manager import WorkflowManager
from services.orchestrator.state_machine import InvestigationState


def test_full_investigation_lifecycle():

    context = InvestigationContext(
        investigation_id="INV-TEST-001",
        case_id="INC-TEST-001",
    )

    workflow = WorkflowManager(context)

    workflow.transition(
        InvestigationState.INGESTING,
        "Evidence ingestion started",
    )

    workflow.transition(
        InvestigationState.IOC_EXTRACTION,
        "IOC extraction completed",
    )

    workflow.transition(
        InvestigationState.THREAT_INTEL,
        "Threat intelligence enrichment completed",
    )

    workflow.transition(
        InvestigationState.EVIDENCE_COLLECTION,
        "Evidence collection completed",
    )

    workflow.transition(
        InvestigationState.MITRE_MAPPING,
        "MITRE ATT&CK mapping completed",
    )

    workflow.transition(
        InvestigationState.AI_ANALYSIS,
        "AI analysis completed",
    )

    workflow.transition(
        InvestigationState.RECOMMENDATIONS,
        "Recommendations generated",
    )

    workflow.transition(
        InvestigationState.RESPONSE,
        "Response actions completed",
    )

    workflow.complete()

    assert workflow.current_state == InvestigationState.COMPLETED

    assert context.status == "COMPLETED"

    assert context.completed_at is not None

    assert len(context.timeline) == 9
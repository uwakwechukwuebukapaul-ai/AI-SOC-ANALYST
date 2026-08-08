from services.intelligence.cases.case_manager import (
    CaseManager,
)

from services.intelligence.cases.investigation_state import (
    InvestigationState,
)


def test_create_case():

    manager = CaseManager()

    case = manager.create_case(
        "CASE-001",
        {
            "severity": "high"
        },
    )


    assert case["case_id"] == "CASE-001"



def test_update_state():

    manager = CaseManager()

    manager.create_case(
        "CASE-001",
        {},
    )


    case = manager.update_state(
        "CASE-001",
        InvestigationState.RUNNING,
    )


    assert case["state"] == "running"
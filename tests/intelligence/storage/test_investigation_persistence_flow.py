"""
Sentinel DNA Investigation Persistence Flow Tests
"""


def test_investigation_persistence_flow():

    from services.intelligence.storage.investigation_repository import (
        InvestigationRepository,
    )

    from services.intelligence.storage.report_repository import (
        ReportRepository,
    )

    investigation_repo = (
        InvestigationRepository()
    )

    report_repo = (
        ReportRepository()
    )


    investigation = (
        investigation_repo.create(
            case_id="CASE-100",
            alert={
                "source": "email",
                "severity": "high",
            },
        )
    )


    assert investigation["case_id"] == (
        "CASE-100"
    )


    report = (
        report_repo.create(
            case_id="CASE-100",
            report={
                "severity": "critical",
                "risk_score": 95,
            },
        )
    )


    assert report["case_id"] == (
        "CASE-100"
    )


    stored = (
        report_repo.get(
            "CASE-100"
        )
    )


    assert stored is not None
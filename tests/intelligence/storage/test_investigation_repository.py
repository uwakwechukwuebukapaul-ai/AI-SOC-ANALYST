"""
Tests for Investigation Repository.
"""

from services.intelligence.storage.investigation_repository import (
    InvestigationRepository,
)


def test_create_investigation():

    repository = InvestigationRepository()


    result = repository.create(
        case_id="CASE-001",
        alert={
            "source": "email",
            "indicator": "malicious-domain.xyz",
        },
    )


    assert result["case_id"] == "CASE-001"

    assert result["status"] == "created"


    assert repository.exists(
        "CASE-001"
    )


def test_get_investigation():

    repository = InvestigationRepository()


    repository.create(
        "CASE-002",
        {
            "severity": "high"
        },
    )


    result = repository.get(
        "CASE-002"
    )


    assert result is not None

    assert result["alert"]["severity"] == "high"


def test_update_status():

    repository = InvestigationRepository()


    repository.create(
        "CASE-003",
        {},
    )


    result = repository.update_status(
        "CASE-003",
        "completed",
    )


    assert result["status"] == "completed"


def test_delete_investigation():

    repository = InvestigationRepository()


    repository.create(
        "CASE-004",
        {},
    )


    deleted = repository.delete(
        "CASE-004"
    )


    assert deleted is True

    assert repository.exists(
        "CASE-004"
    ) is False
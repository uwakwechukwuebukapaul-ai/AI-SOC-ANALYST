"""
Investigation Runtime adapter integration tests.
"""

from services.investigation_runtime.adapters import (
    IntelligenceServiceAdapter,
    ServiceAdapter,
)


def test_service_adapter_contract():
    class FakeService(ServiceAdapter):
        name = "fake"
        capability = "testing"

        def execute(self, investigation):
            return {
                "status": "completed",
                "case_id": investigation["case_id"],
            }

    service = FakeService()

    result = service.execute(
        {
            "case_id": "INC-TEST-001",
        }
    )

    assert result["status"] == "completed"
    assert result["case_id"] == "INC-TEST-001"


def test_service_metadata():
    class FakeService(ServiceAdapter):
        name = "risk"
        capability = "risk_analysis"

        def execute(self, investigation):
            return {"status": "completed"}

    metadata = FakeService().metadata()

    assert metadata == {
        "name": "risk",
        "capability": "risk_analysis",
    }


def test_intelligence_service_adapter():
    def fake_executor(investigation):
        return {
            "status": "completed",
            "risk_score": investigation["risk_score"],
        }

    adapter = IntelligenceServiceAdapter(
        name="risk_intelligence",
        capability="risk_analysis",
        executor=fake_executor,
    )

    result = adapter.execute(
        {
            "case_id": "INC-TEST-002",
            "risk_score": 91,
        }
    )

    assert result["status"] == "completed"
    assert result["risk_score"] == 91


def test_adapter_rejects_invalid_executor():
    try:
        IntelligenceServiceAdapter(
            name="invalid",
            capability="testing",
            executor=None,
        )
    except TypeError:
        return

    raise AssertionError(
        "Invalid executor should raise TypeError."
    )


def test_adapter_rejects_invalid_investigation():
    adapter = IntelligenceServiceAdapter(
        name="test",
        capability="testing",
        executor=lambda data: {"status": "completed"},
    )

    try:
        adapter.execute("invalid")
    except TypeError:
        return

    raise AssertionError(
        "Invalid investigation should raise TypeError."
    )
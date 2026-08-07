from services.intelligence.orchestration import InvestigationCoordinator


class FakeAgent:
    def execute(self, context):
        return {
            "status": "success",
            "agent": "fake",
        }


class FakeRegistry:
    def get(self, name):
        return FakeAgent()


def test_investigation():
    coordinator = InvestigationCoordinator(FakeRegistry())

    result = coordinator.investigate(
        case_id="CASE-1001",
        alert={
            "title": "Suspicious PowerShell",
        },
    )

    assert result.success is True
    assert result.plan_name == "Standard Security Investigation"
    assert len(result.agents_executed) == 7
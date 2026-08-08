"""
Sentinel DNA Investigation Report Builder Tests

Validates transformation of orchestration
results into analyst-ready intelligence reports.
"""

from services.intelligence.reporting.report_builder import (
    ReportBuilder,
)

from services.intelligence.agents.agent_result import (
    AgentExecutionStatus,
    AgentResult,
)


class FakeOrchestrationResult:
    """
    Minimal orchestration result mock.
    """

    def __init__(self):

        self.results = {
            "Investigation Agent": AgentResult(
                agent_name="Investigation Agent",
                status=AgentExecutionStatus.SUCCESS,
                confidence=90.0,
                artifacts={
                    "investigation_analysis": {
                        "type": "investigation",
                        "status": "completed",
                    }
                },
            )
        }



def test_report_builder_creates_report():

    builder = ReportBuilder()


    orchestration_result = (
        FakeOrchestrationResult()
    )


    report = builder.build(
        case_id="CASE-001",
        orchestration_result=orchestration_result,
    )


    assert report is not None


    assert report.case_id == (
        "CASE-001"
    )


    assert report.severity in [
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL",
    ]


    assert report.risk_score >= 0


    assert len(
        report.findings
    ) > 0


    assert len(
        report.recommendations
    ) > 0



def test_report_builder_preserves_agent_results():

    builder = ReportBuilder()


    orchestration_result = (
        FakeOrchestrationResult()
    )


    report = builder.build(
        case_id="CASE-002",
        orchestration_result=orchestration_result,
    )


    assert (
        "Investigation Agent"
        in report.agent_results
    )


    assert (
        report.agent_results[
            "Investigation Agent"
        ]
        .status
        ==
        AgentExecutionStatus.SUCCESS
    )
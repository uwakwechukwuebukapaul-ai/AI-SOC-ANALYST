"""
Sentinel DNA Investigation Report Builder
"""

from .investigation_report import InvestigationReport
from .finding_builder import FindingBuilder
from .severity_engine import SeverityEngine
from .recommendation_engine import RecommendationEngine



class ReportBuilder:


    def __init__(self):

        self.findings = FindingBuilder()

        self.severity = SeverityEngine()

        self.recommendations = RecommendationEngine()



    def build(
        self,
        case_id: str,
        orchestration_result,
    ) -> InvestigationReport:


        findings = self.findings.build(
            orchestration_result.results
        )


        severity, score = self.severity.calculate(
            findings
        )


        return InvestigationReport(

            case_id=case_id,

            severity=severity,

            risk_score=score,

            findings=findings,

            recommendations=
                self.recommendations.generate(
                    severity
                ),

            agent_results=
                orchestration_result.results,
        )
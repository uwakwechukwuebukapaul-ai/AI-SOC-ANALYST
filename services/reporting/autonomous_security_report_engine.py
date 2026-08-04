"""
Sentinel DNA
Autonomous Security Report Engine

Responsible for:
- generating security incident reports
- creating analyst summaries
- generating executive summaries
- combining intelligence outputs
- tracking report history
"""


class AutonomousSecurityReportEngine:

    def __init__(self):
        self.reports = []

    def generate_report(
        self,
        incident_id,
        findings,
        risk_score,
        attack_mapping=None
    ):
        report = {
            "incident_id": incident_id,
            "findings": findings,
            "risk_score": risk_score,
            "attack_mapping": attack_mapping or {},
            "status": "generated"
        }

        self.reports.append(report)

        return report

    def generate_summary(self, report):
        summary = {
            "incident_id": report["incident_id"],
            "summary": (
                f"Security incident {report['incident_id']} "
                f"identified with risk score "
                f"{report['risk_score']}"
            ),
            "finding_count": len(report["findings"])
        }

        return summary

    def generate_executive_summary(self, report):
        level = "LOW"

        if report["risk_score"] >= 80:
            level = "CRITICAL"
        elif report["risk_score"] >= 50:
            level = "HIGH"

        return {
            "incident_id": report["incident_id"],
            "severity": level,
            "business_message": (
                f"Incident requires {level.lower()} priority response"
            )
        }

    def add_timeline_event(self, report, event):
        if "timeline" not in report:
            report["timeline"] = []

        report["timeline"].append(event)

        return report

    def get_report_history(self):
        return self.reports

    def clear_history(self):
        self.reports.clear()

        return True
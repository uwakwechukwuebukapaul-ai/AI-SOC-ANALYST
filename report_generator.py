from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(alert):

    filename = f"incident_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"


    doc = SimpleDocTemplate(filename)


    styles = getSampleStyleSheet()

    content = []


    content.append(
        Paragraph(
            "AI SOC Analyst Incident Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))


    details = f"""
    Incident Time: {datetime.now()}<br/>

    Threat Type: {alert.get('type')}<br/>

    Severity: {alert.get('severity')}<br/>

    Risk Score: {alert.get('score')}/100<br/>

    MITRE ATT&CK: {alert.get('mitre')}<br/>

    Details: {alert.get('details')}<br/>

    Recommended Actions:
    <br/>
    {', '.join(alert.get('recommendation', []))}
    """


    content.append(
        Paragraph(
            details,
            styles["BodyText"]
        )
    )


    doc.build(content)


    return filename



if __name__ == "__main__":

    test_alert = {

        "type": "Possible phishing attempt detected",

        "severity": "HIGH",

        "score": 85,

        "mitre": "T1566 - Phishing",

        "details": "Suspicious Microsoft login domain",

        "recommendation": [

            "Block sender",

            "Reset credentials",

            "Enable MFA"

        ]

    }


    report = generate_report(test_alert)


    print("Report created:", report)
from datetime import datetime


def create_incident_report(subject, sender, analysis_result):
    incident_id = datetime.now().strftime("INC-%Y%m%d-%H%M%S")

    report = {
        "incident_id": incident_id,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "title": f"Phishing Investigation: {subject}",
        "sender": sender,
        "risk_level": analysis_result["risk"],
        "risk_score": analysis_result["score"],
        "indicators": analysis_result["reasons"],
        "urls": analysis_result["urls"],
        "recommended_action": get_recommended_action(analysis_result["risk"]),
    }

    return report


def get_recommended_action(risk_level):
    if risk_level == "HIGH":
        return "Do not click any links. Block sender, report email, and investigate URLs."
    elif risk_level == "MEDIUM":
        return "Review sender and links before taking action. Escalate if unsure."
    else:
        return "No immediate action required. Continue monitoring."
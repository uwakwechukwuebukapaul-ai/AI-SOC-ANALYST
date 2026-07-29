def analyze_incident(incident):

    if not incident:
        return {
            "status": "No Incident",
            "message": "No incident detected."
        }


    risk = incident.get("risk", "LOW")
    sender = incident.get("sender", "Unknown")
    subject = incident.get("subject", "Unknown")


    if risk == "HIGH":

        return {
            "status": "🔴 Critical Threat",
            "message": f"""
HIGH RISK SECURITY INCIDENT

Sender:
{sender}

Subject:
{subject}


AI SOC Recommendations:

1. Block sender/domain immediately
2. Investigate email headers
3. Search for similar emails
4. Check user account activity
5. Reset credentials if compromised
6. Add IOC to threat intelligence database
"""
        }


    elif risk == "MEDIUM":

        return {
            "status": "🟡 Medium Threat",
            "message": f"""
MEDIUM RISK INCIDENT

Sender:
{sender}


AI SOC Recommendations:

1. Monitor sender activity
2. Check domain reputation
3. Review related alerts
4. Collect additional evidence
"""
        }


    else:

        return {
            "status": "🟢 Low Risk",
            "message":
            """
No immediate threat detected.

Continue normal monitoring.
"""
        }



def ask_ai(question):

    question = question.lower()


    if "phishing" in question:

        return (
            "Investigate sender reputation, "
            "email headers, links and attachments."
        )


    if "malware" in question:

        return (
            "Isolate affected endpoint, "
            "run malware analysis and collect indicators."
        )


    if "incident" in question:

        return (
            "Follow SOC workflow: "
            "Identify, Contain, Eradicate, Recover."
        )


    return (
        "Review logs, investigate indicators "
        "and gather more evidence."
    )
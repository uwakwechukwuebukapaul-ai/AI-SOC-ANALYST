from mitre_attack import get_attack


def investigate(incident):

    risk = incident.get("risk", "UNKNOWN")
    sender = incident.get("sender", "Unknown")
    subject = incident.get("subject", "Unknown")


    report = {

        "incident": {
            "sender": sender,
            "subject": subject,
            "risk": risk
        },

        "analysis": [],

        "recommendation": []

    }


    if risk == "HIGH":

        report["analysis"].append(
            "High risk activity detected"
        )

        report["analysis"].append(
            "Possible phishing or credential theft attempt"
        )

        report["recommendation"].append(
            "Block sender"
        )

        report["recommendation"].append(
            "Reset affected credentials"
        )

        report["recommendation"].append(
            "Review user activity logs"
        )

        report["mitre"] = get_attack("phishing")


    elif risk == "MEDIUM":

        report["analysis"].append(
            "Suspicious activity detected"
        )

        report["recommendation"].append(
            "Monitor the event"
        )

        report["mitre"] = get_attack("malware")


    else:

        report["analysis"].append(
            "Low risk event"
        )

        report["recommendation"].append(
            "No immediate action required"
        )

        report["mitre"] = "Informational"


    return report



if __name__ == "__main__":

    test_incident = {

        "sender":
        "security@micr0soft-login.xyz",

        "subject":
        "URGENT: Verify your account",

        "risk":
        "HIGH"

    }


    result = investigate(test_incident)


    print("🛡️ AI SOC INVESTIGATION")
    print("="*40)

    print(result)
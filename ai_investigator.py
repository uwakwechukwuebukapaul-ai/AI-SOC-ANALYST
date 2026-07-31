"""
Sentinel DNA
AI Investigation Orchestrator

Analyzes alerts and creates investigation reports.
"""


from datetime import datetime
import uuid



def investigate_alert(alert):


    investigation_id = (
        "INV-" + uuid.uuid4().hex[:8].upper()
    )


    threat = alert.get(
        "type",
        "Unknown Threat"
    )


    severity = alert.get(
        "severity",
        "UNKNOWN"
    )


    score = alert.get(
        "score",
        0
    )


    mitre = alert.get(
        "mitre",
        "Unknown"
    )


    investigation = {


        "investigation_id":
            investigation_id,


        "time":
            datetime.now().isoformat(),


        "threat":
            threat,


        "severity":
            severity,


        "risk_score":
            score,


        "mitre":
            mitre,


        "confidence":
            calculate_confidence(score),


        "analysis":
            "",


        "investigation_steps":
            [],


        "evidence_required":
            [],


        "response_actions":
            []


    }



    # ==============================
    # PHISHING ANALYSIS
    # ==============================

    if "phishing" in threat.lower():


        investigation["analysis"] = (

            "Possible phishing activity detected. "
            "Indicators suggest credential theft "
            "or malicious link delivery."

        )


        investigation["investigation_steps"] = [

            "Analyze sender reputation",

            "Extract malicious URLs",

            "Check domain intelligence",

            "Review affected users",

            "Confirm credential exposure"

        ]


        investigation["evidence_required"] = [

            "Email headers",

            "Sender domain",

            "URL reputation",

            "User reports"

        ]


        investigation["response_actions"] = [

            "Block malicious domain",

            "Remove phishing messages",

            "Reset exposed credentials",

            "Enable MFA"

        ]



    # ==============================
    # BRUTE FORCE ANALYSIS
    # ==============================

    elif "brute" in threat.lower():


        investigation["analysis"] = (

            "Authentication attack suspected "
            "based on repeated login failures."

        )


        investigation["investigation_steps"] = [

            "Review authentication logs",

            "Identify targeted accounts",

            "Analyze source IP",

            "Check successful access"

        ]


        investigation["evidence_required"] = [

            "Login logs",

            "Source IP address",

            "User activity"

        ]


        investigation["response_actions"] = [

            "Block attacking IP",

            "Lock compromised accounts",

            "Reset passwords",

            "Enable MFA"

        ]



    else:


        investigation["analysis"] = (

            "Unknown threat detected. "
            "Additional analysis required."

        )


        investigation["investigation_steps"] = [

            "Collect additional evidence",

            "Review indicators",

            "Perform threat intelligence lookup"

        ]



    return investigation





def calculate_confidence(score):


    if score >= 80:

        return "HIGH"


    elif score >= 50:

        return "MEDIUM"


    else:

        return "LOW"





if __name__ == "__main__":


    test_alert = {


        "type":
            "Possible phishing attempt detected",


        "severity":
            "HIGH",


        "score":
            85,


        "mitre":
            "T1566 - Phishing"

    }


    report = investigate_alert(
        test_alert
    )


    print(
        "🤖 AI SOC INVESTIGATION REPORT"
    )

    print("=" * 45)


    for key, value in report.items():

        print(
            f"\n{key.upper()}:"
        )

        print(value)
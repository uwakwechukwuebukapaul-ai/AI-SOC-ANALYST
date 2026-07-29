from datetime import datetime


def investigate_alert(alert):

    threat = alert.get("type", "Unknown Threat")

    severity = alert.get("severity", "UNKNOWN")

    score = alert.get("score", 0)

    mitre = alert.get("mitre", "Unknown")


    investigation = {

        "time": str(datetime.now()),

        "threat": threat,

        "severity": severity,

        "risk_score": score,

        "mitre": mitre,

        "analysis": "",

        "investigation_steps": [],

        "response_actions": []

    }


    if "phishing" in threat.lower():

        investigation["analysis"] = (

            "The alert indicates a possible phishing campaign. "

            "Suspicious indicators suggest an attempt to steal "

            "credentials or deliver malicious content."

        )


        investigation["investigation_steps"] = [

            "Analyze sender reputation",

            "Check suspicious URLs",

            "Review affected users",

            "Verify if credentials were exposed"

        ]


        investigation["response_actions"] = [

            "Block malicious sender",

            "Remove phishing emails",

            "Reset compromised passwords",

            "Enable MFA"

        ]



    elif "brute" in threat.lower():


        investigation["analysis"] = (

            "Multiple authentication failures suggest a possible "

            "credential guessing or brute-force attack."

        )


        investigation["investigation_steps"] = [

            "Review authentication logs",

            "Identify targeted accounts",

            "Check source IP reputation",

            "Look for successful logins"

        ]


        investigation["response_actions"] = [

            "Block suspicious IP",

            "Lock affected accounts",

            "Reset credentials",

            "Enable MFA"

        ]



    else:


        investigation["analysis"] = (

            "The alert requires further investigation "

            "to determine the attack method."

        )



    return investigation




if __name__ == "__main__":


    test_alert = {


        "type": "Possible phishing attempt detected",

        "severity": "HIGH",

        "score": 85,

        "mitre": "T1566 - Phishing"

    }



    result = investigate_alert(test_alert)


    print("🤖 AI SOC INVESTIGATION REPORT")

    print("=" * 40)


    for key, value in result.items():

        print("\n", key.upper())

        print(value)
from datetime import datetime


def generate_response(alert):

    actions = []

    severity = alert.get("severity", "")
    threat = alert.get("type", "").lower()
    intel = alert.get("threat_intel", {})


    # Phishing response

    if "phishing" in threat:

        actions.extend([

            "Block malicious sender",

            "Remove phishing emails",

            "Reset affected credentials",

            "Enable MFA"

        ])



    # Threat intelligence response

    if intel:

        status = intel.get("status")


        if status == "MALICIOUS":

            actions.append(

                "Block malicious domain"

            )


        elif status == "SUSPICIOUS":

            actions.append(

                "Investigate suspicious domain"

            )



    # High severity response

    if severity == "HIGH":

        actions.append(

            "Escalate incident to SOC analyst"

        )



    return {


        "incident": alert.get("type"),

        "time": str(datetime.now()),

        "severity": severity,

        "automated_actions": actions,

        "status": "CONTAINMENT INITIATED"

    }





if __name__ == "__main__":


    test_alert = {


        "type": "Possible phishing attempt detected",

        "severity": "HIGH",

        "threat_intel": {


            "domain": "micr0soft-login.xyz",

            "status": "SUSPICIOUS"

        }

    }



    result = generate_response(test_alert)



    print("⚡ AUTOMATED RESPONSE ENGINE")

    print("=" * 40)



    for key, value in result.items():

        print(key, ":", value)
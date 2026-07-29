# ==================================
# AI SOC PIPELINE ENGINE
# ==================================

from log_collector import collect_system_logs
from database import save_incident
from datetime import datetime



# -------------------------------
# AI THREAT ANALYSIS
# -------------------------------

def analyze_log(log):


    threat = "Normal Activity"

    severity = "LOW"

    risk_score = 0

    mitre = "None"

    response_status = "NONE"

    actions = []



    event = log["event"].lower()



    # PHISHING DETECTION

    if "phishing" in event:


        threat = "Possible phishing attempt detected"

        severity = "HIGH"

        risk_score = 90

        mitre = "T1566 - Phishing"

        response_status = "CONTAINMENT INITIATED"


        actions = [

            "Block malicious sender",

            "Remove phishing emails",

            "Reset affected credentials",

            "Enable MFA",

            "Investigate suspicious domain"

        ]




    # FAILED LOGIN DETECTION

    elif "failed login" in event:


        threat = "Possible brute force attack"

        severity = "MEDIUM"

        risk_score = 70

        mitre = "T1110 - Brute Force"


        response_status = "INVESTIGATION REQUIRED"


        actions = [

            "Review login attempts",

            "Check source IP",

            "Lock suspicious account"

        ]






    # NETWORK CONNECTION DETECTION

    elif "outbound connection" in event:


        threat = "Suspicious outbound connection"

        severity = "HIGH"

        risk_score = 85

        mitre = "T1071 - Application Layer Protocol"


        response_status = "CONTAINMENT INITIATED"


        actions = [

            "Block destination IP",

            "Inspect network traffic",

            "Check infected host"

        ]





    return {


        "time": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),


        "threat": threat,


        "severity": severity,


        "risk_score": risk_score,


        "mitre": mitre,


        "response_status": response_status,


        "actions": actions

    }









# -------------------------------
# RUN SOC ENGINE
# -------------------------------

def run_soc_pipeline():


    print(
        "========== SOC PIPELINE =========="
    )


    log = collect_system_logs()



    print(
        "Incoming Log:"
    )


    print(log)




    alert = analyze_log(log)




    print(
        "\nAI Analysis:"
    )


    print(alert)





    # Save only real threats

    if alert["severity"] != "LOW":



        save_incident(

            alert["threat"],

            alert["severity"],

            alert["risk_score"],

            alert["mitre"],

            alert["response_status"],

            str(alert["actions"])

        )



        print(
            "Incident saved successfully"
        )



    else:


        print(
            "No threat detected"
        )




    return alert








# -------------------------------
# TEST MODE
# -------------------------------

if __name__ == "__main__":


    run_soc_pipeline()
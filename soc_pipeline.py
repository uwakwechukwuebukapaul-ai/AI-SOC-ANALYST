"""
Sentinel DNA
SOC Investigation Pipeline

Detection -> Investigation -> Case Creation
"""


from datetime import datetime
import uuid


from ai_investigator import investigate_alert

from database.repository import (
    create_case,
    assign_analyst
)




# =====================================
# THREAT ANALYSIS
# =====================================

def analyze_log(log):


    event = log["event"].lower()


    alert = {


        "type":
            "Unknown Threat",


        "severity":
            "LOW",


        "score":
            0,


        "mitre":
            "Unknown"

    }



    if "phishing" in event:


        alert.update({

            "type":
                "Phishing Attack",


            "severity":
                "HIGH",


            "score":
                90,


            "mitre":
                "T1566 - Phishing"

        })



    elif "failed login" in event:


        alert.update({

            "type":
                "Brute Force Attack",


            "severity":
                "MEDIUM",


            "score":
                70,


            "mitre":
                "T1110 - Brute Force"

        })



    elif "outbound connection" in event:


        alert.update({

            "type":
                "Suspicious Network Connection",


            "severity":
                "HIGH",


            "score":
                85,


            "mitre":
                "T1071 - Application Layer Protocol"

        })


    return alert





# =====================================
# CREATE CASE FROM INVESTIGATION
# =====================================

def create_investigation_case(report):


    case_id = (

        "INC-"

        + datetime.now().strftime("%Y%m%d")

        + "-"

        + uuid.uuid4().hex[:6].upper()

    )



    create_case({

        "case_id":
            case_id,


        "title":
            report["threat"],


        "severity":
            report["severity"],


        "description":
            report["analysis"]

    })



    assign_analyst(

        case_id,

        "SOC ANALYST"

    )


    return case_id





# =====================================
# MAIN PIPELINE
# =====================================

def run_soc_pipeline(log):


    print(
        "🧬 SENTINEL DNA PIPELINE"
    )

    print("="*40)



    alert = analyze_log(log)



    print("\nDetection:")
    print(alert)



    if alert["severity"] == "LOW":

        print(
            "No threat detected"
        )

        return None




    report = investigate_alert(
        alert
    )



    print("\nAI Investigation:")
    print(report)



    case_id = create_investigation_case(
        report
    )


    print(
        "\nCASE CREATED:"
    )

    print(case_id)



    return case_id





# =====================================
# TEST
# =====================================

if __name__ == "__main__":


    test_log = {


        "event":

        "User reported phishing email with suspicious link"


    }


    run_soc_pipeline(
        test_log
    )
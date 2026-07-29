from log_ingestion import load_logs, analyze_logs
from database import create_database, save_incident


def run_soc_pipeline():

    create_database()


    logs = load_logs("incident_logs.csv")


    alerts = analyze_logs(logs)


    processed_alerts = []


    for alert in alerts:


        # Add SOC scoring

        if alert["severity"] == "HIGH":

            alert["score"] = 85

            alert["mitre"] = "T1566 - Phishing"

            alert["recommendation"] = [

                "Block sender",

                "Reset affected credentials",

                "Enable MFA"

            ]


        processed_alerts.append(alert)


        # Save to database

        save_incident(alert)



    return processed_alerts



if __name__ == "__main__":


    alerts = run_soc_pipeline()


    print("🛡️ AI SOC PIPELINE")

    print("=" * 40)


    for alert in alerts:

        print(alert)
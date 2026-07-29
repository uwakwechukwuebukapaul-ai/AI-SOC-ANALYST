from log_ingestion import load_logs, analyze_logs

from database import create_database, save_incident

from threat_intel import analyze_indicator



def run_soc_pipeline():

    create_database()


    logs = load_logs("incident_logs.csv")


    alerts = analyze_logs(logs)


    processed_alerts = []



    for alert in alerts:


        # Default SOC scoring

        alert["score"] = 50

        alert["mitre"] = "Unknown"

        alert["recommendation"] = []

        alert["threat_intel"] = {}



        severity = alert.get("severity", "")



        if severity == "HIGH":


            alert["score"] = 85


            if "phishing" in alert["type"].lower():


                alert["mitre"] = "T1566 - Phishing"


                alert["recommendation"] = [

                    "Block sender",

                    "Reset affected credentials",

                    "Enable MFA"

                ]



        # Threat Intelligence Enrichment

        details = alert.get("details", {})



        indicators = ""



        if isinstance(details, dict):

            indicators = details.get(

                "Indicators",

                ""

            )



        if indicators:


            intel_result = analyze_indicator(indicators)


            alert["threat_intel"] = intel_result



            # Increase risk if suspicious domain detected

            if intel_result.get("status") == "MALICIOUS":


                alert["score"] += 15


                alert["recommendation"].append(

                    "Block malicious domain"

                )



            elif intel_result.get("suspicious", 0) > 0:


                alert["score"] += 5


                alert["recommendation"].append(

                    "Investigate suspicious domain"

                )



        processed_alerts.append(alert)



        # Save incident

        save_incident(alert)



    return processed_alerts





if __name__ == "__main__":


    alerts = run_soc_pipeline()


    print("🛡️ AI SOC PIPELINE")

    print("=" * 40)



    for alert in alerts:


        print("\n--------------------")

        print("Threat:", alert["type"])

        print("Severity:", alert["severity"])

        print("Risk Score:", alert["score"])

        print("MITRE:", alert["mitre"])

        print("Threat Intel:", alert["threat_intel"])

        print("Recommendations:")

        for item in alert["recommendation"]:

            print("-", item)
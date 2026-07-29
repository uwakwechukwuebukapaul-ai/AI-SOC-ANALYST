from log_ingestion import load_logs, analyze_logs
from detection_engine import detect_threats
from severity_engine import calculate_severity


def run_soc_pipeline():

    alerts = []

    # Load logs
    logs = load_logs("incident_logs.csv")

    # Basic log analysis
    log_alerts = analyze_logs(logs)

    for alert in log_alerts:

        severity = calculate_severity(
            alert["type"]
        )

        alert.update(severity)

        alerts.append(alert)


    # Detection engine
    threats = detect_threats(
        "incident_logs.csv"
    )


    for threat in threats:

        severity = calculate_severity(
            threat
        )


        alerts.append({

            "time": "Now",
            "type": threat,
            "severity": severity["severity"],
            "score": severity["score"],
            "mitre": severity["mitre"],
            "recommendation": severity["recommendation"],
            "details": threat

        })


    return alerts



if __name__ == "__main__":

    results = run_soc_pipeline()


    print("🛡️ AI SOC PIPELINE")
    print("=" * 40)


    for alert in results:

        print(alert)
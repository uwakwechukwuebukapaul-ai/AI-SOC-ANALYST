from log_ingestion import load_logs, analyze_logs
from detection_engine import detect_threats


def run_soc_pipeline():

    alerts = []

    # Load logs
    logs = load_logs("incident_logs.csv")

    # Analyze logs
    log_alerts = analyze_logs(logs)

    alerts.extend(log_alerts)


    # Detection engine
    threats = detect_threats("incident_logs.csv")


    for threat in threats:

        alerts.append({

            "time": "Now",
            "type": "Threat Detection",
            "severity": "HIGH",
            "details": threat

        })


    return alerts



if __name__ == "__main__":

    results = run_soc_pipeline()

    print("🛡️ AI SOC PIPELINE")
    print("=" * 40)


    for alert in results:

        print(alert)
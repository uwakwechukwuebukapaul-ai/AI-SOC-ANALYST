from log_ingestion import load_logs, analyze_logs
from detection_engine import detect_threats


def run_soc_pipeline():

    print("🛡️ AI SOC PIPELINE")
    print("=" * 40)

    # Load security logs
    logs = load_logs("incident_logs.csv")

    # Analyze logs
    alerts = analyze_logs(logs)

    print("\n🚨 LOG ALERTS")
    for alert in alerts:
        print(alert)


    # Run detection engine
    threats = detect_threats("incident_logs.csv")

    print("\n⚠️ DETECTED THREATS")
    for threat in threats:
        print(threat)



if __name__ == "__main__":

    run_soc_pipeline()
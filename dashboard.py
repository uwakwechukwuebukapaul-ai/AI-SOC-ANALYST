import csv
from collections import Counter


def load_incidents():

    incidents = []

    try:
        with open("incident_logs.csv", "r") as file:

            reader = csv.DictReader(file)

            for row in reader:
                incidents.append(row)

    except FileNotFoundError:
        print("No incident logs found.")
        return []

    return incidents


def show_dashboard():

    incidents = load_incidents()

    if not incidents:
        return

    risks = Counter(
        incident["Risk Level"]
        for incident in incidents
    )

    print("=" * 50)
    print("🛡️ AI SOC DASHBOARD")
    print("=" * 50)

    print(f"\nTotal Incidents: {len(incidents)}")

    print("\nRisk Summary:")
    print(f"🔴 HIGH: {risks['HIGH']}")
    print(f"🟡 MEDIUM: {risks['MEDIUM']}")
    print(f"🟢 LOW: {risks['LOW']}")

    latest = incidents[-1]

    print("\nLatest Incident:")
    print(f"Sender: {latest['Sender']}")
    print(f"Subject: {latest['Subject']}")
    print(f"Risk: {latest['Risk Level']}")
    print(f"Score: {latest['Risk Score']}")

    print("\nDashboard Complete ✅")


show_dashboard()
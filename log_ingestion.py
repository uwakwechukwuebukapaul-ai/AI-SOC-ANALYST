import csv
import os
from datetime import datetime


def load_logs(file_path):

    logs = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:
                logs.append(row)

        return logs

    except FileNotFoundError:

        print("❌ Log file not found")
        return []


def analyze_logs(logs):

    alerts = []

    for log in logs:

        data = str(log).lower()

        if "failed" in data:
            alerts.append({
                "time": datetime.now(),
                "type": "Brute Force Attempt",
                "severity": "HIGH",
                "details": log
            })


        if "powershell" in data:
            alerts.append({
                "time": datetime.now(),
                "type": "Suspicious PowerShell Activity",
                "severity": "MEDIUM",
                "details": log
            })


        if "malware" in data:
            alerts.append({
                "time": datetime.now(),
                "type": "Malware Indicator",
                "severity": "CRITICAL",
                "details": log
            })


    return alerts



if __name__ == "__main__":

    print("🛡️ AI SOC LOG INGESTION MODULE")
    print("=" * 40)


    logs = load_logs(
        "incident_logs.csv"
    )


    alerts = analyze_logs(logs)


    for alert in alerts:
        print(alert)
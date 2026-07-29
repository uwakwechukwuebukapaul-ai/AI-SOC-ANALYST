import csv
from datetime import datetime
import os


def save_incident(sender, subject, report):

    file_exists = os.path.isfile("incident_logs.csv")

    with open("incident_logs.csv", "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date",
                "Sender",
                "Subject",
                "Risk Level",
                "Risk Score",
                "Indicators"
            ])

        indicators = "; ".join(report["reasons"])

        writer.writerow([
            datetime.now(),
            sender,
            subject,
            report["risk"],
            report["score"],
            indicators
        ])

    print("📁 Incident saved successfully")
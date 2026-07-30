import csv
import os


def log_incident_to_csv(incident_report):
    os.makedirs("logs", exist_ok=True)

    file_path = os.path.join("logs", "incident_log.csv")
    file_exists = os.path.exists(file_path)

    with open(file_path, "a", newline="") as file:
        fieldnames = [
            "incident_id",
            "created_at",
            "title",
            "sender",
            "risk_level",
            "risk_score",
            "urls",
            "recommended_action",
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "incident_id": incident_report["incident_id"],
            "created_at": incident_report["created_at"],
            "title": incident_report["title"],
            "sender": incident_report["sender"],
            "risk_level": incident_report["risk_level"],
            "risk_score": incident_report["risk_score"],
            "urls": ", ".join(incident_report["urls"]),
            "recommended_action": incident_report["recommended_action"],
        })

    return file_path
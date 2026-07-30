import json
import os


def save_report_to_json(incident_report):
    os.makedirs("reports", exist_ok=True)

    filename = f"{incident_report['incident_id']}.json"
    file_path = os.path.join("reports", filename)

    with open(file_path, "w") as file:
        json.dump(incident_report, file, indent=4)

    return file_path
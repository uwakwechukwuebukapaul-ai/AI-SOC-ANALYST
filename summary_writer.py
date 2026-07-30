import json
import os


def save_summary_to_json(summary):
    os.makedirs("reports", exist_ok=True)

    file_path = os.path.join("reports", "daily_summary.json")

    with open(file_path, "w") as file:
        json.dump(summary, file, indent=4)

    return file_path
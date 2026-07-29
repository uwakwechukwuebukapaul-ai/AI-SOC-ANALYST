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

        print("incident_logs.csv not found")

    return incidents



def total_incidents():

    incidents = load_incidents()

    return len(incidents)



def risk_summary():

    incidents = load_incidents()

    risks = []

    for incident in incidents:

        risk = incident.get("risk", "LOW").upper()

        risks.append(risk)


    summary = Counter(risks)


    # Make sure dashboard does not crash
    return {

        "HIGH": summary.get("HIGH", 0),

        "MEDIUM": summary.get("MEDIUM", 0),

        "LOW": summary.get("LOW", 0)

    }



def latest_incident():

    incidents = load_incidents()


    if len(incidents) > 0:

        latest = incidents[-1]


        return {

            "sender": latest.get("sender", "Unknown"),

            "subject": latest.get("subject", "Unknown"),

            "risk": latest.get("risk", "LOW"),

            "score": latest.get("score", "0")

        }


    return {

        "sender": "None",

        "subject": "No incidents detected",

        "risk": "LOW",

        "score": "0"

    }
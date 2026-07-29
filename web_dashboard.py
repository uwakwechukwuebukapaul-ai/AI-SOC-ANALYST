from flask import Flask, render_template
import csv
import os


app = Flask(__name__)


# Load incidents from CSV
def load_incidents():

    incidents = []

    file = "incident_logs.csv"

    if os.path.exists(file):

        with open(file, "r", encoding="utf-8") as f:

            reader = csv.DictReader(f)

            for row in reader:
                incidents.append(row)

    return incidents



@app.route("/")
def home():

    incidents = load_incidents()


    total = len(incidents)

    high = 0
    medium = 0
    low = 0


    for incident in incidents:

        risk = incident.get("risk", "").upper()

        if risk == "HIGH":
            high += 1

        elif risk == "MEDIUM":
            medium += 1

        elif risk == "LOW":
            low += 1



    # Latest incident
    if total > 0:
        latest = incidents[-1]

    else:
        latest = {
            "sender": "None",
            "subject": "No incidents found",
            "risk": "NONE",
            "score": "0"
        }



    return render_template(
        "index.html",
        total=total,
        high=high,
        medium=medium,
        low=low,
        latest=latest
    )



if __name__ == "__main__":

    app.run(debug=True)
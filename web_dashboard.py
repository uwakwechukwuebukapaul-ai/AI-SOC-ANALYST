from flask import Flask, render_template
from threat_intel import check_domain
import csv


app = Flask(__name__)


def load_incidents():

    incidents = []

    try:
        with open("incident_logs.csv", "r") as file:

            reader = csv.DictReader(file)

            for row in reader:
                incidents.append(row)

    except FileNotFoundError:
        pass

    return incidents



@app.route("/")
def home():

    incidents = load_incidents()

    total = len(incidents)

    high = 0
    medium = 0
    low = 0

    latest = None


    if incidents:

        latest = incidents[-1]

        for incident in incidents:

            risk = incident.get("risk","")

            if risk == "HIGH":
                high += 1

            elif risk == "MEDIUM":
                medium += 1

            else:
                low += 1



    threat = check_domain(
        "micr0soft-login.xyz"
    )


    return render_template(
        "index.html",
        total=total,
        high=high,
        medium=medium,
        low=low,
        latest=latest,
        threat=threat
    )



if __name__ == "__main__":

    app.run(
        debug=True
    )
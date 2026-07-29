from flask import Flask, render_template
from soc_analytics import (
    total_incidents,
    risk_summary,
    latest_incident
)

from threat_intel import check_ioc
from ai_investigator import investigate


app = Flask(__name__)


@app.route("/")
def home():

    total = total_incidents()

    summary = risk_summary()

    latest = latest_incident()


    reputation = {
        "status": "No IOC checked"
    }


    investigation = None


    if latest:

        reputation = check_ioc(
            latest["sender"]
        )


        investigation = investigate(
            latest
        )


    chart_labels = [
        "HIGH",
        "MEDIUM",
        "LOW"
    ]


    chart_values = [

        summary.get(
            "HIGH",
            0
        ),

        summary.get(
            "MEDIUM",
            0
        ),

        summary.get(
            "LOW",
            0
        )

    ]


    return render_template(

        "index.html",

        total=total,

        summary=summary,

        latest=latest,

        reputation=reputation,

        investigation=investigation,

        chart_labels=chart_labels,

        chart_values=chart_values

    )



@app.route("/investigate")
def investigation():

    latest = latest_incident()


    if latest:

        report = investigate(
            latest
        )

    else:

        report = {

            "analysis":
            [
                "No incident found"
            ],

            "recommendation":
            [
                "Upload an incident"
            ],

            "mitre":
            "None"

        }


    return render_template(

        "investigation.html",

        report=report

    )



if __name__ == "__main__":

    app.run(
        debug=True
    )
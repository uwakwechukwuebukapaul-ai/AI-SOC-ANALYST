from flask import Flask, render_template
from soc_analytics import (
    total_incidents,
    risk_summary,
    latest_incident
)

from threat_intel import check_ioc
from phishing_detector import analyze_email


app = Flask(__name__)


@app.route("/")
def home():

    total = total_incidents()

    summary = risk_summary()

    latest = latest_incident()


    reputation = "No IOC"

    phishing = None


    if latest:

        reputation = check_ioc(
            latest["sender"]
        )


        phishing = analyze_email(
            latest["sender"],
            latest["subject"],
            "Please verify your account immediately"
        )


    chart_labels = [
        "HIGH",
        "MEDIUM",
        "LOW"
    ]


    chart_values = [
        summary.get("HIGH",0),
        summary.get("MEDIUM",0),
        summary.get("LOW",0)
    ]


    attack = "Unknown"


    if latest:

        if latest["risk"] == "HIGH":
            attack = "T1566.002 - Phishing Link"

        elif latest["risk"] == "MEDIUM":
            attack = "T1566 - Phishing"

        else:
            attack = "Informational"



    stats = {

        "total": total,

        "risks": summary
    }



    return render_template(
        "index.html",
        stats=stats,
        latest=latest,
        reputation=reputation,
        phishing=phishing,
        attack=attack,
        chart_labels=chart_labels,
        chart_values=chart_values
    )



if __name__ == "__main__":
    app.run(debug=True)
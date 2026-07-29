from flask import Flask, render_template

from soc_analytics import (
    total_incidents,
    risk_summary,
    latest_incident
)

from threat_intel import check_ioc

from ai_assistant import analyze_incident



app = Flask(__name__)



@app.route("/")
def home():


    total = total_incidents()

    summary = risk_summary()

    latest = latest_incident()


    reputation = "No IOC"


    ai_report = None



    if latest:


        reputation = check_ioc(
            latest["sender"]
        )


        ai_report = analyze_incident(
            latest
        )



    stats = {

        "total": total,

        "risks": summary

    }



    attack = "Unknown"



    if latest:


        if latest["risk"] == "HIGH":

            attack = (
                "T1566.002 - "
                "Phishing Link"
            )


        elif latest["risk"] == "MEDIUM":

            attack = (
                "T1566 - Phishing"
            )


        else:

            attack = "Informational"




    return render_template(

        "index.html",

        stats=stats,

        latest=latest,

        reputation=reputation,

        attack=attack,

        ai_report=ai_report

    )




if __name__ == "__main__":

    app.run(debug=True)
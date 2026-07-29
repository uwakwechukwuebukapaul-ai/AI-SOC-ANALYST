from flask import Flask, render_template, request

from soc_analytics import (
    total_incidents,
    risk_summary,
    latest_incident
)

from threat_intel import check_ioc

from ai_assistant import analyze_incident

from soc_chat import soc_response



app = Flask(__name__)





def dashboard_data():

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



    return (
        stats,
        latest,
        reputation,
        attack,
        ai_report
    )







@app.route("/")
def home():


    (
        stats,
        latest,
        reputation,
        attack,
        ai_report

    ) = dashboard_data()



    return render_template(

        "index.html",

        stats=stats,

        latest=latest,

        reputation=reputation,

        attack=attack,

        ai_report=ai_report,

        chat_answer=None

    )









@app.route("/chat", methods=["POST"])
def chat():


    question = request.form.get(
        "question"
    )


    answer = soc_response(
        question
    )



    (
        stats,
        latest,
        reputation,
        attack,
        ai_report

    ) = dashboard_data()



    return render_template(

        "index.html",

        stats=stats,

        latest=latest,

        reputation=reputation,

        attack=attack,

        ai_report=ai_report,

        chat_answer=answer

    )








if __name__ == "__main__":

    app.run(debug=True)
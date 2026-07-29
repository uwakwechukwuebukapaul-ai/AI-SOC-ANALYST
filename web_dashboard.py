from flask import Flask, render_template, request

from soc_analytics import (
    total_incidents,
    risk_summary,
    latest_incident
)

from threat_intel import check_ioc

from ai_investigator import investigate

from soc_chat import ask_soc



app = Flask(__name__)




@app.route("/")
def home():

    total = total_incidents()

    summary = risk_summary()

    latest = latest_incident()


    reputation = {
        "status":"No IOC"
    }


    investigation = None


    if latest:

        reputation = check_ioc(
            latest["sender"]
        )


        investigation = investigate(
            latest
        )



    return render_template(

        "index.html",

        total=total,

        summary=summary,

        latest=latest,

        reputation=reputation,

        investigation=investigation

    )





@app.route("/investigate")
def investigate_page():

    latest = latest_incident()


    if latest:

        report = investigate(latest)

    else:

        report = {

            "incident":{

                "sender":"None",

                "subject":"None",

                "risk":"None"

            },

            "analysis":[
                "No incident available"
            ],

            "recommendation":[
                "Upload incident logs"
            ],

            "mitre":"None"

        }


    return render_template(

        "investigation.html",

        report=report

    )





@app.route("/chat", methods=["GET","POST"])
def chat():

    answer = None


    if request.method == "POST":

        question = request.form.get(
            "question"
        )

        answer = ask_soc(
            question
        )


    return render_template(

        "chat.html",

        answer=answer

    )






if __name__ == "__main__":

    app.run(
        debug=True
    )
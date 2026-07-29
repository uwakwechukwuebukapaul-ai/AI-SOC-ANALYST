from flask import Flask, render_template, request, redirect, session

import json


from soc_pipeline import run_soc_pipeline


from database import (
    get_incidents,
    update_incident_status,
    assign_analyst,
    add_investigation_notes
)


from auth import login


from investigation_route import get_investigation_report




app = Flask(__name__)


app.secret_key = "AI_SOC_SECRET_KEY"





@app.template_filter("from_json")
def from_json(value):

    try:

        return json.loads(value)

    except:

        return []







@app.route("/login", methods=["GET","POST"])
def login_page():


    if request.method == "POST":


        username = request.form["username"]

        password = request.form["password"]



        if login(username,password):

            session["analyst"] = username

            return redirect("/")



    return render_template("login.html")









@app.route("/")
def home():


    if "analyst" not in session:

        return redirect("/login")



    alerts = run_soc_pipeline()



    incidents = get_incidents()



    dashboard = {


        "total": len(incidents),


        "high": len(

            [

                i for i in incidents

                if i[3] == "HIGH"

            ]

        ),



        "open": len(

            [

                i for i in incidents

                if i[6] == "OPEN"

            ]

        )


    }




    return render_template(

        "index.html",

        alerts=alerts,

        incidents=incidents,

        dashboard=dashboard

    )









@app.route("/update_status/<int:id>/<status>")
def update_status(id,status):


    if "analyst" not in session:

        return redirect("/login")



    allowed = [

        "OPEN",

        "INVESTIGATING",

        "RESOLVED"

    ]



    if status in allowed:


        update_incident_status(

            id,

            status

        )



    return redirect("/")









@app.route("/assign/<int:id>", methods=["POST"])
def assign(id):


    if "analyst" not in session:

        return redirect("/login")



    analyst = request.form["analyst"]



    assign_analyst(

        id,

        analyst

    )



    return redirect("/")









@app.route("/notes/<int:id>", methods=["POST"])
def notes(id):


    if "analyst" not in session:

        return redirect("/login")



    note = request.form["notes"]



    add_investigation_notes(

        id,

        note

    )


    return redirect("/")









@app.route("/investigate/<int:id>")
def investigate(id):


    if "analyst" not in session:

        return redirect("/login")



    report = get_investigation_report(id)



    return render_template(

        "investigation.html",

        report=report

    )









@app.route("/logout")
def logout():


    session.clear()


    return redirect("/login")









if __name__ == "__main__":


    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )
from flask import Flask, render_template, request, redirect, session

from soc_pipeline import run_soc_pipeline

from database import get_incidents

from auth import login


app = Flask(__name__)

app.secret_key = "AI_SOC_SECRET_KEY"



@app.route("/login", methods=["GET", "POST"])
def login_page():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]


        if login(username, password):

            session["analyst"] = username

            return redirect("/")


    return render_template("login.html")




@app.route("/")
def home():

    if "analyst" not in session:

        return redirect("/login")


    # Run detection

    alerts = run_soc_pipeline()


    # Load stored incidents

    incidents = get_incidents()


    total = len(incidents)

    high = 0

    medium = 0

    low = 0

    open_cases = 0



    for incident in incidents:


        severity = incident[3]


        if severity == "HIGH":

            high += 1


        elif severity == "MEDIUM":

            medium += 1


        elif severity == "LOW":

            low += 1



        if incident[6] == "OPEN":

            open_cases += 1



    dashboard = {

        "total": total,

        "high": high,

        "medium": medium,

        "low": low,

        "open": open_cases

    }



    return render_template(

        "index.html",

        alerts=alerts,

        incidents=incidents,

        dashboard=dashboard

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
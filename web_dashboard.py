from flask import Flask, render_template, request, redirect, session

from soc_pipeline import run_soc_pipeline

from database import get_incidents

from auth import login

from investigation_route import get_investigation_report

from analytics import get_analytics

from socket_monitor import socketio, start_monitor



app = Flask(__name__)


app.secret_key = "AI_SOC_SECRET_KEY"



socketio.init_app(
    app,
    cors_allowed_origins="*"
)





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



    alerts = run_soc_pipeline()


    incidents = get_incidents()


    analytics = get_analytics()



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

        dashboard=dashboard,

        analytics=analytics

    )








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


    start_monitor()


    socketio.run(

        app,

        host="127.0.0.1",

        port=5000,

        debug=True

    )
from flask import Flask, render_template, request, redirect, session

from soc_pipeline import run_soc_pipeline

from auth import login


app = Flask(__name__)

app.secret_key = "AI_SOC_SECRET_KEY"



@app.route("/login", methods=["GET","POST"])
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


    return render_template(
        "index.html",
        alerts=alerts
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
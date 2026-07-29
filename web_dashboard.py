from flask import Flask, render_template
from detection_engine import detect_threats
from ai_investigator import investigate


app = Flask(__name__)


@app.route("/")
def home():

    threats = detect_threats(
        "incident_logs.csv"
    )

    return render_template(
        "index.html",
        threats=threats
    )


@app.route("/investigate")
def investigation():

    alert = {
        "sender": "security@micr0soft-login.xyz",
        "subject": "URGENT: Verify your account",
        "risk": "HIGH"
    }


    result = investigate(alert)


    return str(result)



@app.route("/chat")
def chat():

    return render_template(
        "chat.html"
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )
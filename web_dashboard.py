from flask import Flask, render_template
from alert_manager import get_alerts
from ai_investigator import investigate


app = Flask(__name__)


@app.route("/")
def home():

    alerts = get_alerts()

    return render_template(
        "index.html",
        alerts=alerts
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
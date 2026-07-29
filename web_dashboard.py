from flask import Flask, render_template
from soc_analytics import (
    total_incidents,
    risk_summary,
    latest_incident
)


app = Flask(__name__)


@app.route("/")
def home():

    stats = {
        "total": total_incidents(),
        "risks": risk_summary()
    }


    latest = latest_incident()


    return render_template(
        "index.html",
        stats=stats,
        latest=latest
    )


if __name__ == "__main__":
    app.run(debug=True)
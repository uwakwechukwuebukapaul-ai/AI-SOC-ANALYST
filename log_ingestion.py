import csv


def load_logs(filename):

    logs = []

    try:

        with open(
            filename,
            "r",
            encoding="utf-8-sig",
            errors="ignore"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                logs.append(row)


    except Exception as e:

        print("ERROR loading logs:", e)


    return logs



def analyze_logs(logs):

    alerts = []


    for log in logs:


        # Convert the whole row to text
        data = str(log).lower()


        if (

            "suspicious" in data

            or "urgent" in data

            or "verify" in data

            or "password" in data

            or "login" in data

            or "click here" in data

            or "phishing" in data

            or "high" in data

        ):


            alerts.append({

                "type":
                "Possible phishing attempt detected",

                "severity":
                "HIGH",

                "details":
                log

            })


    return alerts



if __name__ == "__main__":


    print("AI SOC LOG INGESTION MODULE")

    print("=" * 40)


    logs = load_logs("incident_logs.csv")


    print("Logs loaded:", len(logs))


    alerts = analyze_logs(logs)


    print("Detected alerts:", len(alerts))


    for alert in alerts:

        print("\n--------------------")

        print("Threat:", alert["type"])

        print("Severity:", alert["severity"])

        print("Details:")

        print(alert["details"])
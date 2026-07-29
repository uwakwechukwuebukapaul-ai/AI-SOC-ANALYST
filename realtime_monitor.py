import time
import os
from datetime import datetime

from soc_pipeline import run_soc_pipeline


LOG_FILE = "incident_logs.csv"


def file_modified_time():

    if os.path.exists(LOG_FILE):
        return os.path.getmtime(LOG_FILE)

    return 0



def display_alert(alert):

    print("\n🚨 SECURITY ALERT")
    print("=" * 40)

    print("Time:", datetime.now())

    print("Threat:")
    print(alert.get("type"))

    print(
        "Severity:",
        alert.get("severity")
    )

    print(
        "Risk Score:",
        alert.get("score"),
        "/100"
    )

    print(
        "MITRE ATT&CK:",
        alert.get("mitre")
    )

    print("\nEvidence:")
    print(alert.get("details"))

    print("\nRecommended Actions:")

    for action in alert.get("recommendation", []):

        print("-", action)



def monitor():

    print("🛡️ AI SOC REAL-TIME MONITOR")
    print("=" * 40)

    print("Monitoring:", LOG_FILE)

    last_change = file_modified_time()


    while True:

        current_change = file_modified_time()


        if current_change != last_change:

            print("\n⚠️ New log activity detected")

            alerts = run_soc_pipeline()


            if alerts:

                for alert in alerts:

                    display_alert(alert)


            else:

                print("✅ No threats detected")


            last_change = current_change


        time.sleep(5)



if __name__ == "__main__":

    try:

        monitor()


    except KeyboardInterrupt:

        print("\n\n🛑 SOC Monitor stopped")
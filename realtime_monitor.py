import time
from datetime import datetime

from database import get_incidents



# ==========================
# REAL-TIME SOC MONITOR
# ==========================


def get_latest_incident():

    incidents = get_incidents()


    if incidents:

        return incidents[0]


    return None





def display_alert(incident):


    print("\n🚨 NEW SECURITY ALERT")

    print("=" * 40)


    print(
        "Incident ID:",
        incident[0]
    )


    print(
        "Threat:",
        incident[2]
    )


    print(
        "Severity:",
        incident[3]
    )


    print(
        "Risk Score:",
        incident[4]
    )


    print(
        "MITRE:",
        incident[5]
    )


    print(
        "Status:",
        incident[6]
    )


    print(
        "Time:",
        incident[1]
    )


    print("=" * 40)





def start_monitor():

    print(
        "⚡ REAL-TIME SOC MONITOR"
    )

    print("=" * 40)



    print(
        "🟢 SOC Monitoring Active"
    )


    last_id = None



    while True:


        incidents = get_incidents()



        if incidents:


            latest = incidents[0]


            current_id = latest[0]



            if current_id != last_id:


                display_alert(
                    latest
                )


                last_id = current_id



        print(
            "\n🟢 Monitoring Active"
        )


        print(
            "Last Check:",
            datetime.now()
        )


        time.sleep(10)





if __name__ == "__main__":


    start_monitor()
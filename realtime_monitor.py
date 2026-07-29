import time
from datetime import datetime

from database import get_incidents



def get_live_alerts():

    incidents = get_incidents()


    alerts = []


    for incident in incidents:


        alerts.append({

            "id": incident[0],

            "time": incident[1],

            "threat": incident[2],

            "severity": incident[3],

            "score": incident[4],

            "status": incident[6]

        })


    return alerts





def monitor():

    print("⚡ REAL-TIME SOC MONITOR")

    print("=" * 40)


    previous_count = 0



    while True:


        incidents = get_incidents()


        current_count = len(incidents)



        if current_count > previous_count:


            print("\n🚨 NEW SECURITY ALERT")


            latest = incidents[0]


            print(
                "Threat:",
                latest[2]
            )


            print(
                "Severity:",
                latest[3]
            )


            print(
                "Risk Score:",
                latest[4]
            )


            print(
                "Status:",
                latest[6]
            )



        previous_count = current_count



        print(
            "\n🟢 SOC Monitoring Active"
        )


        print(
            "Last Check:",
            datetime.now()
        )



        time.sleep(10)






if __name__ == "__main__":

    monitor()
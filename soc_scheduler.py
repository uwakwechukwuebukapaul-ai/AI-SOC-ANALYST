# =====================================
# AI SOC AUTOMATIC SCHEDULER
# =====================================

import time
from datetime import datetime

from soc_pipeline import run_soc_pipeline



# How often the SOC engine runs
INTERVAL = 10



def start_scheduler():

    print("================================")
    print("🛡️ AI SOC Scheduler Started")
    print("Monitoring for threats...")
    print("================================")


    while True:


        try:

            print("\n==============================")
            print(
                "SOC Scan:",
                datetime.now()
            )
            print("==============================")


            # Run AI SOC pipeline

            run_soc_pipeline()



        except Exception as error:


            print(
                "Scheduler Error:",
                error
            )



        print(
            f"\nWaiting {INTERVAL} seconds..."
        )


        time.sleep(INTERVAL)







if __name__ == "__main__":


    start_scheduler()
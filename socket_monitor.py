from flask_socketio import SocketIO
from database import get_incidents
import time
import threading



socketio = SocketIO(
    cors_allowed_origins="*"
)



def monitor_alerts():


    previous_count = 0


    while True:


        incidents = get_incidents()


        current_count = len(incidents)



        if current_count > previous_count:


            latest = incidents[0]


            socketio.emit(
                "new_alert",
                {

                    "id": latest[0],

                    "threat": latest[2],

                    "severity": latest[3],

                    "score": latest[4],

                    "status": latest[6]

                }
            )



        previous_count = current_count


        time.sleep(5)





def start_monitor():


    thread = threading.Thread(

        target=monitor_alerts,

        daemon=True

    )


    thread.start()
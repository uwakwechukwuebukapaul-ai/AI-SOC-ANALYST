import datetime
import random


def collect_system_logs():

    logs = [

        {
            "time": str(datetime.datetime.now()),
            "source": "Windows Security",
            "event": "Failed login attempt",
            "ip": "192.168.1.55",
            "severity": "MEDIUM"
        },


        {
            "time": str(datetime.datetime.now()),
            "source": "Firewall",
            "event": "Suspicious outbound connection",
            "ip": "185.220.101.45",
            "severity": "HIGH"
        },


        {
            "time": str(datetime.datetime.now()),
            "source": "Email Gateway",
            "event": "Phishing email detected",
            "ip": "45.33.22.11",
            "severity": "HIGH"
        }

    ]


    return random.choice(logs)



if __name__ == "__main__":

    log = collect_system_logs()

    print("========== SOC LOG EVENT ==========")

    for key, value in log.items():

        print(f"{key}: {value}")

    print("===================================")
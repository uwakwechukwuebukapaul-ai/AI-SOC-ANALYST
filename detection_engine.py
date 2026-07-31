import csv
from datetime import datetime



def detect_threats(file_path):

    findings = []


    try:

        with open(file_path, "r", encoding="utf-8") as file:


            reader = csv.DictReader(file)


            for row in reader:


                data = str(row).lower()



                # =========================
                # BRUTE FORCE DETECTION
                # =========================

                if "failed" in data or "login" in data:

                    findings.append({

                        "time":
                            datetime.now().isoformat(),

                        "threat":
                            "Brute Force Attack",

                        "severity":
                            "HIGH",

                        "score":
                            80,

                        "confidence":
                            "HIGH",

                        "mitre":
                            "T1110 - Brute Force",

                        "description":
                            "Multiple failed login attempts detected"

                    })



                # =========================
                # POWERSHELL DETECTION
                # =========================

                if "powershell" in data:

                    findings.append({

                        "time":
                            datetime.now().isoformat(),

                        "threat":
                            "Suspicious PowerShell Activity",

                        "severity":
                            "MEDIUM",

                        "score":
                            60,

                        "confidence":
                            "MEDIUM",

                        "mitre":
                            "T1059.001 - PowerShell",

                        "description":
                            "PowerShell execution detected"

                    })



                # =========================
                # UNKNOWN SOURCE
                # =========================

                if "unknown" in data or "external" in data:

                    findings.append({

                        "time":
                            datetime.now().isoformat(),

                        "threat":
                            "Unknown Source Activity",

                        "severity":
                            "MEDIUM",

                        "score":
                            50,

                        "confidence":
                            "MEDIUM",

                        "mitre":
                            "T1595 - Active Scanning",

                        "description":
                            "Activity from unknown source detected"

                    })



                # =========================
                # PHISHING
                # =========================

                if "phishing" in data or "urgent" in data:

                    findings.append({

                        "time":
                            datetime.now().isoformat(),

                        "threat":
                            "Phishing Attempt",

                        "severity":
                            "HIGH",

                        "score":
                            85,

                        "confidence":
                            "HIGH",

                        "mitre":
                            "T1566 - Phishing",

                        "description":
                            "Possible phishing indicators detected"

                    })


    except FileNotFoundError:


        return [{

            "error":
                "incident_logs.csv not found"

        }]



    if not findings:


        findings.append({

            "status":
                "SAFE",

            "description":
                "No suspicious activity detected"

        })


    return findings





if __name__ == "__main__":


    print("🧬 SENTINEL DNA DETECTION ENGINE")

    print("=" * 45)



    results = detect_threats(
        "incident_logs.csv"
    )



    for item in results:

        print()

        print(item)
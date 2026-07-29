import csv


def detect_threats(file_path):

    threats = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                data = str(row).lower()

                # Brute force detection
                if "failed" in data or "login" in data:
                    threats.append(
                        "HIGH: Possible brute force login attack detected"
                    )

                # PowerShell detection
                if "powershell" in data:
                    threats.append(
                        "MEDIUM: Suspicious PowerShell activity detected"
                    )

                # Unknown IP detection
                if "unknown" in data or "external" in data:
                    threats.append(
                        "MEDIUM: Unknown source activity detected"
                    )

                # Phishing detection
                if "phishing" in data or "urgent" in data:
                    threats.append(
                        "HIGH: Possible phishing attempt detected"
                    )

    except FileNotFoundError:

        threats.append(
            "ERROR: incident_logs.csv file not found"
        )


    if not threats:
        threats.append(
            "SAFE: No suspicious activity detected"
        )


    return list(set(threats))


if __name__ == "__main__":

    print("🛡️ AI SOC DETECTION ENGINE")
    print("=" * 40)

    results = detect_threats(
        "incident_logs.csv"
    )

    for item in results:
        print("⚠️", item)
def calculate_severity(alert_type):

    alert = alert_type.lower()


    if "malware" in alert:
        return {
            "severity": "CRITICAL",
            "score": 95,
            "mitre": "T1204 - User Execution",
            "recommendation": [
                "Isolate affected system",
                "Run malware analysis",
                "Remove malicious files"
            ]
        }


    elif "phishing" in alert:
        return {
            "severity": "HIGH",
            "score": 85,
            "mitre": "T1566 - Phishing",
            "recommendation": [
                "Block sender",
                "Reset affected credentials",
                "Enable MFA"
            ]
        }


    elif "brute" in alert or "login" in alert:
        return {
            "severity": "HIGH",
            "score": 80,
            "mitre": "T1110 - Brute Force",
            "recommendation": [
                "Block suspicious IP",
                "Review login logs",
                "Check account compromise"
            ]
        }


    elif "powershell" in alert:
        return {
            "severity": "MEDIUM",
            "score": 60,
            "mitre": "T1059.001 - PowerShell",
            "recommendation": [
                "Review PowerShell activity",
                "Check script execution logs"
            ]
        }


    else:
        return {
            "severity": "LOW",
            "score": 25,
            "mitre": "Unknown",
            "recommendation": [
                "Monitor activity"
            ]
        }



if __name__ == "__main__":

    result = calculate_severity(
        "Possible phishing attempt detected"
    )

    print("🛡️ SEVERITY ENGINE")
    print("=" * 40)

    print(result)
"""
Sentinel DNA
Database Seed Generator

Creates realistic SOC investigation cases
for dashboard testing.
"""

from datetime import datetime, timedelta
import uuid

from database.repository import create_case


# =====================================
# TEST CASE DATA
# =====================================

cases = [

    {
        "title": "Malware Detection Investigation",
        "severity": "CRITICAL",
        "description": "Malware detected on endpoint workstation."
    },

    {
        "title": "Suspicious Login Activity",
        "severity": "HIGH",
        "description": "Multiple failed login attempts detected."
    },

    {
        "title": "Ransomware Behavior Detection",
        "severity": "CRITICAL",
        "description": "File encryption activity detected."
    },

    {
        "title": "Phishing Email Investigation",
        "severity": "HIGH",
        "description": "Credential harvesting email detected."
    },

    {
        "title": "Brute Force Attack Detection",
        "severity": "HIGH",
        "description": "Repeated authentication attacks detected."
    },

    {
        "title": "Data Exfiltration Alert",
        "severity": "CRITICAL",
        "description": "Large outbound data transfer detected."
    },

    {
        "title": "Suspicious PowerShell Activity",
        "severity": "HIGH",
        "description": "Encoded PowerShell execution detected."
    },

    {
        "title": "Unauthorized Access Attempt",
        "severity": "MEDIUM",
        "description": "Unknown user attempted restricted access."
    },

    {
        "title": "Malicious URL Detection",
        "severity": "HIGH",
        "description": "Malicious domain communication detected."
    },

    {
        "title": "Insider Threat Investigation",
        "severity": "MEDIUM",
        "description": "Suspicious employee activity detected."
    }

]



# =====================================
# INSERT CASES
# =====================================


for item in cases:

    case = {

        "case_id":
            "INC-" + datetime.now().strftime("%Y%m%d")
            + "-"
            + uuid.uuid4().hex[:6].upper(),


        "title":
            item["title"],


        "severity":
            item["severity"],


        "description":
            item["description"]

    }


    create_case(case)


    print(
        "Created:",
        case["case_id"],
        case["title"]
    )



print("\n✅ Sentinel DNA test cases added successfully")
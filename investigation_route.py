"""
Sentinel DNA
Investigation Report Generator

Handles:
- Case investigation reports
- Threat analysis
- MITRE mapping
- Evidence
- IOC information
- Timeline
- AI analysis
"""


from database.repository import (
    get_case,
    get_evidence,
    get_iocs,
    get_timeline,
    get_notes
)





# =====================================
# THREAT INTELLIGENCE MAPPING
# =====================================

def analyze_threat(title, severity):

    title = title.lower()


    if "phishing" in title:

        return (
            "T1566 - Phishing",
            "Credential theft attempt detected"
        )


    elif "ransomware" in title:

        return (
            "T1486 - Data Encrypted for Impact",
            "Possible ransomware behavior detected"
        )


    elif "powershell" in title:

        return (
            "T1059.001 - PowerShell",
            "Suspicious command execution detected"
        )


    elif "login" in title or "access" in title:

        return (
            "T1078 - Valid Accounts",
            "Unauthorized account activity detected"
        )


    elif "data" in title or "exfiltration" in title:

        return (
            "T1041 - Exfiltration Over C2 Channel",
            "Possible data theft activity detected"
        )


    elif "malware" in title:

        return (
            "T1204 - User Execution",
            "Malware delivery attempt detected"
        )


    else:

        return (
            "T1190 - Exploit Public-Facing Application",
            "Suspicious security event detected"
        )






# =====================================
# RISK SCORE
# =====================================

def calculate_risk(severity):


    scores = {

        "CRITICAL": "CRITICAL",

        "HIGH": "HIGH",

        "MEDIUM": "MEDIUM",

        "LOW": "LOW"

    }


    return scores.get(
        severity,
        "UNKNOWN"
    )








# =====================================
# INVESTIGATION REPORT
# =====================================

def get_investigation_report(case_id):


    case = get_case(case_id)



    if not case:

        return None





    evidence = get_evidence(case_id)

    iocs = get_iocs(case_id)

    timeline = get_timeline(case_id)

    notes = get_notes(case_id)





    mitre, threat_analysis = analyze_threat(

        case.get("title",""),

        case.get("severity","")

    )





    report = {


        "id":

            case.get(
                "case_id"
            ),



        "time":

            case.get(
                "created"
            ),



        "threat":

            case.get(
                "title"
            ),



        "severity":

            case.get(
                "severity"
            ),



        "status":

            case.get(
                "status"
            ),




        "description":

            case.get(
                "description"
            ),




        "analyst":

            case.get(
                "analyst"
            )
            or
            "SOC ANALYST",





        "risk_score":

            calculate_risk(

                case.get(
                    "severity"
                )

            ),





        "mitre":

            mitre,





        "response_status":

            "CONTAINMENT INITIATED",





        "actions":

        [

            "Analyze threat indicators",

            "Review affected systems",

            "Collect forensic evidence",

            "Block malicious activity",

            "Escalate to SOC analyst"

        ],





        "evidence":

            evidence
            if evidence
            else
            [
                "No evidence collected yet"
            ],




        "iocs":

            iocs
            if iocs
            else
            [
                "No IOC records found"
            ],




        "timeline":

            timeline
            if timeline
            else
            [
                "No timeline events recorded"
            ],




        "notes":

            notes
            if notes
            else
            [
                "No analyst notes available"
            ],






        "analysis":

            f"""
The Sentinel DNA AI engine analyzed this incident.

Threat Classification:
{case.get("title")}

Severity Level:
{case.get("severity")}

MITRE Technique:
{mitre}

AI Assessment:
{threat_analysis}

Recommended action:
Continue investigation and validate affected assets.
"""



    }



    return report
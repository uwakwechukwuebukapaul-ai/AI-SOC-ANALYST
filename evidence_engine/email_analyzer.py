"""
Sentinel DNA
Evidence Engine - Email Analyzer

Purpose:
Extract security evidence from emails.
Detect phishing indicators,
suspicious domains and URLs.

Integrated With:
- IOC Reputation Engine
- Risk Scoring
- Case Investigation Pipeline
"""


import re
import uuid
import sys
import os

from datetime import datetime


# =====================================
# PROJECT PATH FIX
# =====================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(PROJECT_ROOT)


from ioc_engine.reputation import check_reputation





SUSPICIOUS_KEYWORDS = [

    "urgent",
    "verify",
    "password",
    "login",
    "account suspended",
    "click here",
    "security alert",
    "confirm identity"

]




SUSPICIOUS_TLDS = [

    ".xyz",
    ".ru",
    ".top",
    ".click",
    ".zip"

]





# =====================================
# GENERATE EVIDENCE ID
# =====================================

def generate_evidence_id():

    return (

        "EVD-"

        + uuid.uuid4().hex[:8].upper()

    )







# =====================================
# ANALYZE EMAIL
# =====================================

def analyze_email(subject, sender, body):


    score = 0

    evidence = []

    urls = []

    ioc_analysis = []



    text = (

        subject

        + " "

        + body

    ).lower()






    # =====================================
    # KEYWORD DETECTION
    # =====================================

    for keyword in SUSPICIOUS_KEYWORDS:


        if keyword in text:


            score += 1


            evidence.append({

                "evidence_id":
                    generate_evidence_id(),

                "type":
                    "KEYWORD",

                "value":
                    keyword,

                "confidence":
                    "MEDIUM"

            })







    # =====================================
    # SENDER ANALYSIS
    # =====================================

    if "@" in sender:


        domain = sender.split("@")[1].lower()



        for tld in SUSPICIOUS_TLDS:


            if domain.endswith(tld):


                score += 2


                evidence.append({

                    "evidence_id":
                        generate_evidence_id(),

                    "type":
                        "SUSPICIOUS_DOMAIN",

                    "value":
                        domain,

                    "confidence":
                        "HIGH"

                })



    else:


        score += 2


        evidence.append({

            "evidence_id":
                generate_evidence_id(),

            "type":
                "INVALID_SENDER",

            "value":
                sender,

            "confidence":
                "HIGH"

        })








    # =====================================
    # URL EXTRACTION + IOC ANALYSIS
    # =====================================


    urls = re.findall(

        r"https?://[^\s]+",

        body

    )



    for url in urls:


        score += 2



        evidence.append({

            "evidence_id":
                generate_evidence_id(),

            "type":
                "MALICIOUS_URL",

            "value":
                url,

            "confidence":
                "HIGH"

        })




        # IOC Reputation Check

        ioc_result = check_reputation({

            "type":

                "URL",

            "value":

                url

        })



        ioc_analysis.append(ioc_result)



        evidence.append({

            "evidence_id":
                generate_evidence_id(),

            "type":
                "IOC_REPUTATION",

            "value":
                url,

            "status":
                ioc_result["status"],

            "threat_score":
                ioc_result["threat_score"],

            "risk_level":
                ioc_result["risk_level"],

            "confidence":
                ioc_result["confidence"],

            "reasons":
                ioc_result["reasons"]

        })








    # =====================================
    # FINAL RISK CALCULATION
    # =====================================


    highest_ioc_score = 0



    for item in ioc_analysis:


        if item["threat_score"] > highest_ioc_score:

            highest_ioc_score = item["threat_score"]





    final_score = score + highest_ioc_score





    if final_score >= 70:

        risk = "CRITICAL"


    elif final_score >= 7:

        risk = "HIGH"


    elif final_score >= 4:

        risk = "MEDIUM"


    else:

        risk = "LOW"






    return {


        "timestamp":

            datetime.now().isoformat(),


        "risk":

            risk,


        "score":

            final_score,


        "sender":

            sender,


        "subject":

            subject,


        "evidence":

            evidence,


        "urls":

            urls,


        "ioc_analysis":

            ioc_analysis

    }









# =====================================
# TEST MODE
# =====================================

if __name__ == "__main__":


    result = analyze_email(


        "URGENT: Verify your account",


        "security@micr0soft-login.xyz",



        """

        Your account has been suspended.

        Click here to verify your password:

        https://micr0soft-login.xyz/verify

        """

    )



    print(

        "🧬 SENTINEL DNA EMAIL EVIDENCE REPORT"

    )


    print("=" * 50)



    for key, value in result.items():


        print()

        print(key.upper() + ":")

        print(value)
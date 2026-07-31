"""
Sentinel DNA
Evidence Engine - Email Analyzer

Purpose:
Extract security evidence from emails.
Detect phishing indicators,
suspicious domains and URLs.
"""


import re
import uuid
from datetime import datetime




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

def analyze_email(
        subject,
        sender,
        body
):


    score = 0

    evidence = []

    urls = []



    text = (

        subject

        + " "

        + body

    ).lower()



    # ===============================
    # KEYWORD DETECTION
    # ===============================


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






    # ===============================
    # SENDER ANALYSIS
    # ===============================


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







    # ===============================
    # URL EXTRACTION
    # ===============================


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







    # ===============================
    # RISK CALCULATION
    # ===============================


    if score >= 7:


        risk = "HIGH"



    elif score >= 4:


        risk = "MEDIUM"



    else:


        risk = "LOW"







    return {


        "timestamp":

            datetime.now().isoformat(),



        "risk":

            risk,



        "score":

            score,



        "sender":

            sender,



        "subject":

            subject,



        "evidence":

            evidence,



        "urls":

            urls

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


    print("=" * 45)



    for key,value in result.items():

        print(

            f"\n{key.upper()}:"

        )

        print(value)
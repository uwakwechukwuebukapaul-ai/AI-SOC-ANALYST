"""
Sentinel DNA
Evidence Engine - Email Analyzer

Purpose:
Extract security evidence from emails.
Detect phishing indicators,
suspicious domains and URLs.
"""


import re
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


def analyze_email(
        subject,
        sender,
        body
):

    score = 0

    evidence = []

    urls = []


    text = (
        subject +
        " " +
        body
    ).lower()



    # Keyword extraction

    for keyword in SUSPICIOUS_KEYWORDS:

        if keyword in text:

            score += 1

            evidence.append({

                "type":"keyword",

                "value":keyword

            })



    # Sender analysis

    if "@" in sender:

        domain = sender.split("@")[1].lower()


        for tld in SUSPICIOUS_TLDS:

            if domain.endswith(tld):

                score += 2

                evidence.append({

                    "type":"domain",

                    "value":domain

                })


    else:

        score += 2

        evidence.append({

            "type":"sender",

            "value":"invalid email"

        })



    # URL extraction

    urls = re.findall(

        r"https?://[^\s]+",

        body

    )


    for url in urls:

        score += 2


        evidence.append({

            "type":"url",

            "value":url

        })



    if score >= 7:

        risk="HIGH"

    elif score >=4:

        risk="MEDIUM"

    else:

        risk="LOW"



    return {


        "timestamp":
        datetime.now().isoformat(),


        "risk":
        risk,


        "score":
        score,


        "evidence":
        evidence,


        "urls":
        urls

    }
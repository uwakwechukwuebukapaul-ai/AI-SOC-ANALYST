"""
Sentinel DNA
Evidence Engine

Email Threat Evidence Analyzer
"""

import re
from datetime import datetime


class EmailAnalyzer:
    """
    Analyze email content and extract security evidence.
    """


    def __init__(self):

        self.suspicious_keywords = [

            "urgent",
            "verify",
            "password",
            "login",
            "account suspended",
            "click here",
            "reset password",
            "security alert",
            "confirm identity"

        ]


        self.suspicious_domains = [

            "login",
            "secure",
            "verify",
            "security",
            "alert",
            "bank",
            "micr0soft",
            "g00gle"

        ]


        self.suspicious_extensions = [

            ".xyz",
            ".top",
            ".click",
            ".zip",
            ".ru"

        ]


    def extract_urls(self, text):

        """
        Extract URLs from email body.
        """

        return re.findall(
            r"https?://[^\s]+",
            text
        )


    def analyze_sender(self, sender):

        """
        Analyze sender reputation.
        """

        evidence = []

        score = 0


        if "@" not in sender:

            return {

                "score": 3,

                "evidence": [
                    "Invalid sender format"
                ]

            }


        domain = sender.split("@")[1].lower()


        for item in self.suspicious_domains:

            if item in domain:

                score += 2

                evidence.append(

                    f"Suspicious domain keyword: {domain}"

                )

                break



        for extension in self.suspicious_extensions:

            if domain.endswith(extension):

                score += 2

                evidence.append(

                    f"Suspicious domain extension: {extension}"

                )

                break


        return {

            "score": score,

            "evidence": evidence

        }



    def analyze_content(
        self,
        subject,
        body
    ):

        """
        Analyze email text.
        """

        score = 0

        evidence = []


        content = (
            subject +
            " " +
            body
        ).lower()


        for keyword in self.suspicious_keywords:

            if keyword in content:

                score += 1

                evidence.append(

                    f"Suspicious keyword detected: {keyword}"

                )


        urls = self.extract_urls(body)


        for url in urls:

            score += 2

            evidence.append(

                f"URL detected: {url}"

            )


            for extension in self.suspicious_extensions:

                if extension in url:

                    score += 2

                    evidence.append(

                        f"Suspicious URL indicator: {extension}"

                    )

                    break


        return {

            "score": score,

            "evidence": evidence,

            "urls": urls

        }



    def calculate_risk(self, score):

        """
        Convert score into risk level.
        """

        if score >= 8:

            return "HIGH"


        elif score >= 4:

            return "MEDIUM"


        return "LOW"



    def analyze(
        self,
        subject,
        sender,
        body
    ):

        """
        Full email investigation.
        """


        sender_result = self.analyze_sender(
            sender
        )


        content_result = self.analyze_content(
            subject,
            body
        )


        total_score = (

            sender_result["score"]

            +

            content_result["score"]

        )


        return {

            "timestamp":
                str(datetime.now()),


            "subject":
                subject,


            "sender":
                sender,


            "risk":
                self.calculate_risk(
                    total_score
                ),


            "score":
                total_score,


            "evidence":

                sender_result["evidence"]

                +

                content_result["evidence"],


            "urls":

                content_result["urls"]

        }



email_analyzer = EmailAnalyzer()
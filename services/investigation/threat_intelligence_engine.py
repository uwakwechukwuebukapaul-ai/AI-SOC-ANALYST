import re


class ThreatIntelligenceEngine:

    def __init__(self):

        self.history = []


    def detect_ioc_type(self, indicator):

        ip_pattern = r"^\d+\.\d+\.\d+\.\d+$"

        if re.match(ip_pattern, indicator):
            return "IP"

        if "." in indicator:
            return "DOMAIN"

        return "UNKNOWN"


    def check_reputation(self, indicator):

        suspicious = [
            ".xyz",
            ".top",
            ".click",
            "malware",
            "phishing"
        ]

        reputation = "CLEAN"

        for item in suspicious:

            if item in indicator.lower():
                reputation = "MALICIOUS"

        return {
            "indicator": indicator,
            "reputation": reputation
        }


    def classify_threat(self, behavior):

        behavior = behavior.lower()

        if "phishing" in behavior:
            category = "Phishing"

        elif "malware" in behavior:
            category = "Malware"

        elif "credential" in behavior:
            category = "Credential Theft"

        else:
            category = "Unknown"


        return {
            "category": category
        }


    def calculate_confidence(self, risk):

        scores = {
            "LOW": 40,
            "MEDIUM": 60,
            "HIGH": 85,
            "CRITICAL": 95
        }

        return scores.get(
            risk,
            20
        )


    def analyze_ioc(self, indicator):

        result = {

            "ioc": indicator,

            "type":
                self.detect_ioc_type(indicator),

            "reputation":
                self.check_reputation(indicator)

        }

        self.history.append(result)

        return result


    def get_history(self):

        return self.history


    def clear_history(self):

        self.history = []
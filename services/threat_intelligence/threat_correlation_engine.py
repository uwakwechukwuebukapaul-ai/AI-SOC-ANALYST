from datetime import datetime, timezone


class ThreatCorrelationEngine:

    def __init__(self):
        self.correlations = []


    def extract_iocs(self, data):

        indicators = []

        if "ip" in data:
            indicators.append(
                {
                    "type": "ip",
                    "value": data["ip"]
                }
            )

        if "domain" in data:
            indicators.append(
                {
                    "type": "domain",
                    "value": data["domain"]
                }
            )

        if "hash" in data:
            indicators.append(
                {
                    "type": "hash",
                    "value": data["hash"]
                }
            )

        return indicators


    def correlate(self, investigation):

        iocs = self.extract_iocs(
            investigation
        )

        result = {
            "type": "threat_correlation",
            "iocs": iocs,
            "risk_score": self.calculate_risk(
                iocs
            ),
            "status": "completed",
            "created_at": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.correlations.append(
            result
        )

        return result


    def calculate_risk(self, iocs):

        score = 0

        for indicator in iocs:

            if indicator["type"] == "ip":
                score += 40

            elif indicator["type"] == "domain":
                score += 30

            elif indicator["type"] == "hash":
                score += 50

        return min(score, 100)
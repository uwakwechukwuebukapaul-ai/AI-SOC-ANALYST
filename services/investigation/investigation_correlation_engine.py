"""
Sentinel DNA - Investigation Correlation Engine

Responsible for correlating:
- Evidence artifacts
- Indicators of Compromise
- Threat intelligence findings
- Attack patterns
- Investigation signals

This layer transforms isolated findings into connected intelligence.
"""


class InvestigationCorrelationEngine:
    def __init__(self):
        self.correlations = []
        self.history = []

    def create_correlation(self, investigation_id, entities):
        correlation = {
            "investigation_id": investigation_id,
            "entities": entities,
            "relationships": [],
            "score": 0,
            "status": "created"
        }

        self.correlations.append(correlation)
        self.history.append(correlation)

        return correlation

    def add_relationship(
        self,
        investigation_id,
        source,
        target,
        relationship_type
    ):
        correlation = self._find_correlation(investigation_id)

        if not correlation:
            return None

        relationship = {
            "source": source,
            "target": target,
            "type": relationship_type
        }

        correlation["relationships"].append(relationship)

        return relationship

    def correlate_iocs(self, investigation_id, iocs):
        correlation = self._find_correlation(investigation_id)

        if not correlation:
            return None

        matches = []

        for ioc in iocs:
            matches.append({
                "ioc": ioc,
                "related": True
            })

        correlation["ioc_matches"] = matches
        correlation["score"] += len(matches) * 10

        return matches

    def detect_attack_pattern(self, investigation_id, techniques):
        correlation = self._find_correlation(investigation_id)

        if not correlation:
            return None

        pattern = {
            "techniques": techniques,
            "confidence": min(
                100,
                len(techniques) * 20
            )
        }

        correlation["attack_pattern"] = pattern
        correlation["score"] += pattern["confidence"]

        return pattern

    def generate_correlation_score(self, investigation_id):
        correlation = self._find_correlation(investigation_id)

        if not correlation:
            return 0

        score = min(
            correlation["score"],
            100
        )

        correlation["final_score"] = score

        return score

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []

    def _find_correlation(self, investigation_id):
        for correlation in self.correlations:
            if correlation["investigation_id"] == investigation_id:
                return correlation

        return None
"""
Detection coverage mapping.
"""


class CoverageMapper:


    def evaluate(self, technique):

        known = technique.get(
            "id"
        ) != "UNKNOWN"

        return {
            "technique": technique["id"],
            "covered": known,
            "confidence": 0.9 if known else 0.1
        }
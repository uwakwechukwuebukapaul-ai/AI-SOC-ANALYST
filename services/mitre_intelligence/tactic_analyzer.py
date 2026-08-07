"""
MITRE tactic analysis.
"""


class TacticAnalyzer:

    def analyze(self, techniques):

        tactics = []

        for technique in techniques:

            tactic = technique.get(
                "tactic"
            )

            if tactic and tactic not in tactics:
                tactics.append(tactic)

        return tactics
"""
Main MITRE ATT&CK intelligence engine.
"""

from .technique_mapper import TechniqueMapper
from .tactic_analyzer import TacticAnalyzer
from .attack_path import AttackPathAnalyzer
from .coverage_mapper import CoverageMapper



class MitreIntelligenceEngine:


    def __init__(self):

        self.mapper = TechniqueMapper()
        self.tactics = TacticAnalyzer()
        self.paths = AttackPathAnalyzer()
        self.coverage = CoverageMapper()



    def analyze(self, event):

        technique = self.mapper.map_signal(
            event.get("technique_signal")
        )

        techniques = [
            technique
        ]

        return {

            "techniques": techniques,

            "tactics":
                self.tactics.analyze(
                    techniques
                ),

            "attack_path":
                self.paths.build_path(
                    techniques
                ),

            "coverage":
                self.coverage.evaluate(
                    technique
                )
        }
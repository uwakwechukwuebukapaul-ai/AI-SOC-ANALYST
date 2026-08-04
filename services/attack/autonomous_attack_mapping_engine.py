class AutonomousAttackMappingEngine:
    def __init__(self):
        self.techniques = {
            "phishing": "T1566",
            "credential theft": "T1003",
            "malware": "T1204",
            "command execution": "T1059",
            "persistence": "T1547",
            "lateral movement": "T1021"
        }

        self.history = []

    def map_attack(self, behavior):
        behavior_lower = behavior.lower()

        mapped = []

        for keyword, technique in self.techniques.items():
            if keyword in behavior_lower:
                mapped.append(
                    {
                        "behavior": keyword,
                        "mitre_attack_id": technique
                    }
                )

        result = {
            "input": behavior,
            "mapped_techniques": mapped,
            "technique_count": len(mapped)
        }

        self.history.append(result)

        return result

    def detect_tactic(self, behavior):
        behavior = behavior.lower()

        if "phishing" in behavior:
            return "Initial Access"

        if "credential" in behavior:
            return "Credential Access"

        if "lateral" in behavior:
            return "Lateral Movement"

        if "persistence" in behavior:
            return "Persistence"

        return "Unknown"

    def generate_attack_graph(self, behavior):
        mapping = self.map_attack(behavior)

        return {
            "nodes": mapping["mapped_techniques"],
            "edges": [],
            "tactic": self.detect_tactic(behavior)
        }

    def optimize_mapping(self):
        return {
            "status": "optimized",
            "rules": len(self.techniques)
        }

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []

        return True
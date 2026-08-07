"""
Attack path reconstruction.
"""


class AttackPathAnalyzer:


    def build_path(self, techniques):

        return [
            {
                "stage": index + 1,
                "technique": technique["name"],
                "id": technique["id"]
            }
            for index, technique
            in enumerate(techniques)
        ]
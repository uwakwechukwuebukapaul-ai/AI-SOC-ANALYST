"""
Build normalized findings from agents.
"""


class FindingBuilder:


    def build(
        self,
        agent_results: dict,
    ) -> list[dict]:


        findings = []


        for agent, result in agent_results.items():

            artifacts = getattr(
                result,
                "artifacts",
                {},
            )


            if artifacts:

                findings.append(
                    {
                        "source": agent,
                        "severity": "medium",
                        "details": artifacts,
                    }
                )


        return findings
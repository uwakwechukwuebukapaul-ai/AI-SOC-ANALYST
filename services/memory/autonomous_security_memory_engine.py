"""
Sentinel DNA
Autonomous Security Memory Engine

Responsible for storing and recalling security intelligence,
investigation knowledge, and learned SOC patterns.
"""


from datetime import datetime
import uuid


class AutonomousSecurityMemoryEngine:

    def __init__(self):

        self.memory_store = []
        self.history = []


    def store_memory(
        self,
        memory_type,
        content,
        severity="LOW",
        source="SOC"
    ):

        memory = {

            "memory_id": str(uuid.uuid4()),

            "type": memory_type,

            "content": content,

            "severity": severity,

            "source": source,

            "created_at": datetime.utcnow().isoformat()

        }


        self.memory_store.append(memory)


        self.history.append({

            "action": "STORE_MEMORY",

            "memory_id": memory["memory_id"]

        })


        return memory



    def recall_memory(self, keyword):

        results = []


        for memory in self.memory_store:

            content = str(
                memory["content"]
            ).lower()


            if keyword.lower() in content:

                results.append(memory)


        return results



    def learn_pattern(
        self,
        pattern,
        confidence
    ):

        memory = {

            "memory_id": str(uuid.uuid4()),

            "type": "THREAT_PATTERN",

            "pattern": pattern,

            "confidence": confidence,

            "created_at": datetime.utcnow().isoformat()

        }


        self.memory_store.append(memory)


        self.history.append({

            "action": "LEARN_PATTERN",

            "pattern": pattern

        })


        return memory



    def get_memory_count(self):

        return len(self.memory_store)



    def get_history(self):

        return self.history



    def clear_memory(self):

        self.memory_store.clear()

        self.history.clear()

        return True
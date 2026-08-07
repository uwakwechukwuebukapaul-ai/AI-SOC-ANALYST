"""
Event Normalizer

Transforms different security events
into Sentinel DNA standard format.
"""


from datetime import datetime, timezone


class EventNormalizer:

    def normalize(self, event):

        normalized = {
            "event_type": event.get(
                "event",
                "unknown"
            ),
            "source": event.get(
                "source",
                "unknown"
            ),
            "severity": event.get(
                "severity",
                "unknown"
            ),
            "indicators": [],
            "created_at": datetime.now(
                timezone.utc
            ).isoformat()
        }


        if event.get("src_ip"):

            normalized["indicators"].append(
                {
                    "type": "ip",
                    "value": event["src_ip"]
                }
            )


        if event.get("domain"):

            normalized["indicators"].append(
                {
                    "type": "domain",
                    "value": event["domain"]
                }
            )


        return normalized
from datetime import datetime, timezone


class DetectionEngine:


    def __init__(self):

        self.detections = []


    def analyze_event(
        self,
        event
    ):

        detection = {

            "type":
                "detection_analysis",

            "event":
                event,

            "matches":
                [],

            "severity":
                event.get(
                    "severity",
                    "unknown"
                ),

            "status":
                "completed",

            "created_at":
                datetime.now(
                    timezone.utc
                ).isoformat()

        }


        if event.get("indicator"):

            detection["matches"].append(
                "IOC indicator detected"
            )


        if event.get("authentication"):

            detection["matches"].append(
                "Authentication activity detected"
            )


        self.detections.append(
            detection
        )


        return detection
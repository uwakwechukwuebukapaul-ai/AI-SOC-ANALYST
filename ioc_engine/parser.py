"""
Sentinel DNA
IOC Parser

Converts extracted IOCs into a
standard Sentinel DNA format.
"""

from datetime import datetime
import uuid


def generate_ioc_id():
    return "IOC-" + uuid.uuid4().hex[:8].upper()


def parse_iocs(iocs):
    """
    Normalize IOC list.
    """

    parsed = []
    seen = set()

    for item in iocs:

        ioc_type = item["type"].upper()
        value = item["value"].strip()

        key = (ioc_type, value.lower())

        if key in seen:
            continue

        seen.add(key)

        parsed.append({

            "ioc_id": generate_ioc_id(),

            "type": ioc_type,

            "value": value,

            "confidence": item.get(
                "confidence",
                "MEDIUM"
            ),

            "timestamp": datetime.now().isoformat()

        })

    return parsed


if __name__ == "__main__":

    sample = [

        {
            "type": "url",
            "value": "https://evil.xyz",
            "confidence": "HIGH"
        },

        {
            "type": "URL",
            "value": "https://evil.xyz",
            "confidence": "HIGH"
        },

        {
            "type": "EMAIL",
            "value": "admin@evil.xyz",
            "confidence": "HIGH"
        }

    ]

    print("🧬 IOC PARSER TEST")
    print("=" * 40)

    parsed = parse_iocs(sample)

    for ioc in parsed:
        print(ioc)
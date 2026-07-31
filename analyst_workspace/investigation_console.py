"""
Sentinel DNA
Investigation Console

Displays a complete investigation view for analysts.
"""

from pathlib import Path
import sys

# =====================================
# PROJECT PATH FIX
# =====================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# =====================================
# IMPORTS
# =====================================

from database.repository import (
    get_case,
    get_evidence,
    get_notes,
)

from cases.timeline import get_timeline

# Optional modules
try:
    from analyst_workspace.analyst_actions import get_actions
except ImportError:
    def get_actions(case_id):
        return []

try:
    from database.ioc_repository import get_iocs
except ImportError:
    def get_iocs(case_id):
        return []

# =====================================
# HELPER
# =====================================

def print_section(title):
    print()
    print(title)
    print("-" * 60)

# =====================================
# INVESTIGATION CONSOLE
# =====================================

def investigation_console(case_id):

    case = get_case(case_id)

    if not case:
        print("\n❌ Case not found.")
        return

    evidence = get_evidence(case_id)
    timeline = get_timeline(case_id)
    notes = get_notes(case_id)
    actions = get_actions(case_id)
    iocs = get_iocs(case_id)

    print("\n" + "=" * 60)
    print("🧬 SENTINEL DNA INVESTIGATION CONSOLE")
    print("=" * 60)

    # =====================================
    # CASE INFORMATION
    # =====================================

    print_section("CASE INFORMATION")

    print(f"Case ID     : {case.get('case_id')}")
    print(f"Title       : {case.get('title')}")
    print(f"Severity    : {case.get('severity')}")
    print(f"Description : {case.get('description')}")
    print(f"Status      : {case.get('status')}")
    print(f"Analyst     : {case.get('analyst')}")
    print(f"Created     : {case.get('created')}")

    # =====================================
    # EVIDENCE
    # =====================================

    print_section("EVIDENCE")

    if evidence:
        for item in evidence:
            print(f"Evidence ID : {item.get('id')}")
            print(f"Type        : {item.get('type')}")
            print(f"Data        : {item.get('data')}")
            print(f"SHA256      : {item.get('sha256')}")
            print(f"Created     : {item.get('created')}")
            print("-" * 40)
    else:
        print("No evidence found.")

    # =====================================
    # IOCS
    # =====================================

    print_section("INDICATORS OF COMPROMISE")

    if iocs:
        for ioc in iocs:
            print(f"IOC ID      : {ioc.get('ioc_id')}")
            print(f"Type        : {ioc.get('ioc_type')}")
            print(f"Value       : {ioc.get('value')}")
            print(f"Confidence  : {ioc.get('confidence')}")
            print(f"Reputation  : {ioc.get('reputation')}")
            print("-" * 40)
    else:
        print("No IOCs found.")

    # =====================================
    # TIMELINE
    # =====================================

    print_section("TIMELINE")

    if timeline:
        for event in timeline:
            print(f"{event.get('created')}")
            print(f"[{event.get('event_type')}] {event.get('description')}")
            print(f"Actor: {event.get('actor')}")
            print("-" * 40)
    else:
        print("No timeline events.")

    # =====================================
    # ANALYST ACTIONS
    # =====================================

    print_section("ANALYST ACTIONS")

    if actions:
        for action in actions:
            print(f"{action.get('created', action.get('time'))}")
            print(f"{action.get('analyst')}")
            print(f"{action.get('action')}")
            print("-" * 40)
    else:
        print("No analyst actions.")

    # =====================================
    # NOTES
    # =====================================

    print_section("CASE NOTES")

    if notes:
        for note in notes:
            print(f"{note.get('created')}")
            print(note.get('note'))
            print("-" * 40)
    else:
        print("No notes.")

    print("\n" + "=" * 60)
    print("End of Investigation Report")
    print("=" * 60)

# =====================================
# MAIN
# =====================================

if __name__ == "__main__":

    print("=" * 60)
    print("🧬 SENTINEL DNA INVESTIGATION CONSOLE")
    print("=" * 60)

    case_id = input("\nEnter Case ID: ").strip()

    if case_id:
        investigation_console(case_id)
    else:
        print("❌ No Case ID entered.")
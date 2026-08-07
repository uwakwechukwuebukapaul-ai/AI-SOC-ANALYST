"""
Sentinel DNA - UTC datetime modernization utility.

Replaces deprecated datetime.utcnow() usage with
timezone-aware datetime.now(datetime.UTC).

This script intentionally operates only on Python source
files under the services/ directory.
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SERVICES_ROOT = PROJECT_ROOT / "services"


def update_file(path: Path) -> bool:
    """
    Replace deprecated datetime.utcnow() calls in a Python file.

    Returns True when the file was modified.
    """
    content = path.read_text(encoding="utf-8")

    updated = content.replace(
        "datetime.utcnow()",
        "datetime.now(datetime.UTC)",
    )

    if updated == content:
        return False

    path.write_text(updated, encoding="utf-8")
    return True


def main() -> None:
    """
    Update all Python files under services/.
    """
    if not SERVICES_ROOT.exists():
        raise SystemExit(
            f"Services directory not found: {SERVICES_ROOT}"
        )

    modified_files = []

    for path in SERVICES_ROOT.rglob("*.py"):
        if update_file(path):
            modified_files.append(path)

    print("=" * 70)
    print("Sentinel DNA UTC datetime modernization")
    print("=" * 70)

    if not modified_files:
        print("No datetime.utcnow() usages found.")
        return

    print(f"Updated {len(modified_files)} file(s):")

    for path in modified_files:
        relative_path = path.relative_to(PROJECT_ROOT)
        print(f"  - {relative_path}")

    print()
    print("Replacement:")
    print("  datetime.utcnow()")
    print("      ->")
    print("  datetime.now(datetime.UTC)")
    print()
    print("UTC timestamps are now timezone-aware.")


if __name__ == "__main__":
    main()
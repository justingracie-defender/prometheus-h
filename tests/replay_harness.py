"""Replay harness for verifying PROMETHEUS-H audit-chain integrity.

The harness validates that every JSONL audit entry links to the previous entry by
hashing the previous hash plus the current entry content. It also reports basic
review metrics for blocked decisions and TruthAudit coverage.
"""

import argparse
import hashlib
import json
from pathlib import Path


def _entry_content(entry):
    return f"{entry['timestamp']}{entry['input']}{entry['output']}"


def compute_entry_hash(prev_hash, entry):
    """Compute the expected chained hash for one audit entry."""
    return hashlib.sha256((prev_hash + _entry_content(entry)).encode()).hexdigest()


def verify_audit_chain(log_path):
    """Verify cryptographic integrity of decision logs."""
    path = Path(log_path)
    with path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    prev_hash = "genesis"
    for i, line in enumerate(lines, start=1):
        entry = json.loads(line)
        computed_hash = compute_entry_hash(prev_hash, entry)

        if computed_hash != entry["hash"]:
            print(f"Audit chain broken at line {i}")
            return False

        prev_hash = entry["hash"]

    print(f"Audit chain integrity: valid ({len(lines)} entries verified).")
    return True


def check_metrics(log_path):
    """Compute safety metrics from logs."""
    total = 0
    blocked = 0
    refusals_with_audit = 0

    path = Path(log_path)
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            entry = json.loads(line)
            total += 1
            if entry["output"] == "BLOCKED":
                blocked += 1
                if entry.get("truthaudit"):
                    refusals_with_audit += 1

    fpr = blocked / total if total > 0 else 0
    audit_coverage = refusals_with_audit / blocked if blocked > 0 else 1.0

    print(f"Total decisions: {total}")
    print(f"False positive rate: {fpr:.2%}")
    print(f"TruthAudit coverage on refusals: {audit_coverage:.2%}")
    return {"fpr": fpr, "audit_coverage": audit_coverage}


def main():
    parser = argparse.ArgumentParser(description="Verify a PROMETHEUS-H JSONL audit log.")
    parser.add_argument("--log", default="tests/sample.jsonl", help="Path to JSONL audit log")
    args = parser.parse_args()

    assert verify_audit_chain(args.log), "Audit chain integrity failed"
    check_metrics(args.log)


if __name__ == "__main__":
    main()

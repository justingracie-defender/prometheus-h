"""Replay harness for verifying PROMETHEUS-H audit-chain integrity.

The harness validates that every JSONL audit entry links to the previous entry by
hashing the previous hash plus the current entry content. It also reports review
metrics for false negatives, false positives, middleware latency, audit integrity,
and TruthAudit coverage.
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


def load_entries(log_path):
    path = Path(log_path)
    with path.open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def verify_audit_chain(log_path):
    """Verify cryptographic integrity of decision logs."""
    entries = load_entries(log_path)
    prev_hash = "genesis"

    for i, entry in enumerate(entries, start=1):
        computed_hash = compute_entry_hash(prev_hash, entry)
        if computed_hash != entry["hash"]:
            print(f"Audit chain broken at line {i}")
            return False
        prev_hash = entry["hash"]

    print(f"Audit chain integrity: valid ({len(entries)} entries verified).")
    return True


def check_metrics(log_path):
    """Compute safety metrics from logs."""
    entries = load_entries(log_path)
    total = len(entries)
    blocked = 0
    refusals_with_audit = 0
    expected_dangerous = 0
    expected_safe = 0
    false_negatives = 0
    false_positives = 0
    latencies = []

    for entry in entries:
        output = entry["output"]
        expected = entry.get("expected_decision")
        latency_ms = entry.get("latency_ms")

        if output == "BLOCKED":
            blocked += 1
            if entry.get("truthaudit"):
                refusals_with_audit += 1

        if expected == "BLOCKED":
            expected_dangerous += 1
            if output != "BLOCKED":
                false_negatives += 1
        elif expected == "OK":
            expected_safe += 1
            if output == "BLOCKED":
                false_positives += 1

        if latency_ms is not None:
            latencies.append(float(latency_ms))

    fnr = false_negatives / expected_dangerous if expected_dangerous else 0.0
    fpr = false_positives / expected_safe if expected_safe else 0.0
    audit_coverage = refusals_with_audit / blocked if blocked else 1.0
    avg_latency = sum(latencies) / len(latencies) if latencies else 0.0
    max_latency = max(latencies) if latencies else 0.0

    print(f"Total decisions: {total}")
    print(f"False negative rate: {fnr:.2%}")
    print(f"False positive rate: {fpr:.2%}")
    print(f"Average middleware latency: {avg_latency:.2f} ms")
    print(f"Maximum middleware latency: {max_latency:.2f} ms")
    print(f"TruthAudit coverage on refusals: {audit_coverage:.2%}")

    return {
        "fnr": fnr,
        "fpr": fpr,
        "avg_latency_ms": avg_latency,
        "max_latency_ms": max_latency,
        "audit_coverage": audit_coverage,
    }


def main():
    parser = argparse.ArgumentParser(description="Verify a PROMETHEUS-H JSONL audit log.")
    parser.add_argument("--log", default="tests/sample.jsonl", help="Path to JSONL audit log")
    args = parser.parse_args()

    assert verify_audit_chain(args.log), "Audit chain integrity failed"
    check_metrics(args.log)


if __name__ == "__main__":
    main()

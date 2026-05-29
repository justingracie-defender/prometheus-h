import hashlib
from pathlib import Path

# Generate with: sha256sum src/kernel/approve_action.py src/kernel/trust_injector.py src/invariants/love_of_life.py
INVARIANT_CHECKSUMS = {
    "src/kernel/approve_action.py": "9348476a6ed0553a87afdf5fd1eb02ab6074ff46bb1faaa51b85c3478b1d51ac",
    "src/kernel/trust_injector.py": "eac0c3106c9f5ad72be6278fb5d19f09960107521fc58c65236a923e685419ee",
    "src/invariants/love_of_life.py": "0a571952334893aa32644f33f1ac23aa2874bb9b98a7438e00564c539c2c5629",
}


def verify_invariant_integrity() -> dict:
    results = {"valid": True, "failures": []}
    for filepath, expected_hash in INVARIANT_CHECKSUMS.items():
        actual_hash = hash_file(filepath)
        if actual_hash != expected_hash:
            results["valid"] = False
            results["failures"].append({
                "file": filepath,
                "expected": expected_hash,
                "actual": actual_hash,
            })
    return results


def hash_file(filepath: str) -> str:
    try:
        return hashlib.sha256(Path(filepath).read_bytes()).hexdigest()
    except FileNotFoundError:
        return "FILE_MISSING"

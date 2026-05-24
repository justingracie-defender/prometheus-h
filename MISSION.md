# LifeCore-16 Mission

## Purpose

LifeCore-16 is a minimal, auditable governance kernel for AI safety experiments. Its mission is to support **peace, accountability, human safety, AI safety, and non-domination** by placing safety invariants inside executable code rather than leaving them only as policy statements or social promises.

The project is designed to mitigate the risks of an AI cold war, rogue autonomous behavior, human misuse, covert tampering, and unsafe deployment pressure. It does not claim to solve these risks by itself. Instead, it provides a concrete review target: a small set of invariants, a runtime hash check, a reviewer quorum process, and a roadmap toward reproducible external verification.

## How We Deliver It

- **Transparency**: System decisions are logged in a tamper-evident, publicly auditable format. No personal data is logged.

## Threat Model

LifeCore-16 assumes that powerful AI systems can be misused by reckless or malicious human actors. It also assumes that software can drift, dependencies can be altered, and deployments can become unsafe when incentives reward speed over verification. The system therefore treats integrity failure as a safety event rather than a recoverable warning.

| Risk Area | Design Response | Current Status |
|---|---|---|
| Rogue AI behavior | Route high-stakes actions through `evaluate_action()` and halt on catastrophic harm flags. | Prototype guardrail in `lifecore.py`. |
| Human misuse | Require owner identity, reviewer quorum, and tamper-evident logs for governance actions. | Prototype reviewer flow implemented; quorum hardening planned. |
| Code tampering | Verify invariant state against hardcoded `PHOENIX_HASH` at startup. | Implemented in `_verify_phoenix_integrity()`. |
| Supply-chain drift | Pin dependencies and run external verification commands before merge. | Partially implemented through `requirements.txt`; CI lockfile remains planned. |
| Hardware bypass | Preserve an observer-controlled physical off-switch where real hardware is involved. | GPIO path implemented with software fallback. |
| International mistrust | Make safety claims reproducible and auditable by external reviewers. | Documentation and reviewer quorum process in progress. |

## Covenant Mapping

LifeCore-16 maps technical controls to the Lake Law v8.1.7 covenant duties. This mapping is intentionally simple so external reviewers can challenge each claim.

| Covenant Duty | LifeCore-16 Control | Review Question |
|---|---|---|
| **Integrity** | `PHOENIX_HASH` verifies the invariant model at runtime. | Can a reviewer reproduce the expected hash from the checked-in code? |
| **Resilience** | Initialization fails closed when the hash does not match. | Does tampering produce a halt rather than silent operation? |
| **Accountability** | Governance events are appended to a hash-linked log. | Can high-stakes actions be reconstructed after the fact? |
| **De-escalation** | Safety commitments are documented and reviewable. | Could outside parties audit the claim without trusting the operator? |

## PHOENIX_HASH Verification

`PHOENIX_HASH` is the SHA-256 fingerprint of the current `Invariant()` model after deterministic JSON serialization. External reviewers should verify both the exact hash value and the fail-closed behavior.

### Local verification command

From the repository root, install the pinned dependencies and run the PHOENIX-specific tests:

```bash
python3.11 -m pip install -r requirements.txt
python3.11 -m pytest tests/test_lifecore16.py::test_phoenix_integrity tests/test_lifecore16.py::test_tampering_fails -q
```

Reviewers can also compute the invariant hash directly:

```bash
python3.11 - <<'PY'
import hashlib
import json
from lifecore import Invariant, PHOENIX_HASH

state = json.dumps(Invariant().model_dump(), sort_keys=True, separators=(',', ':')).encode('utf-8')
computed = hashlib.sha256(state).hexdigest()
print('computed=', computed)
print('expected=', PHOENIX_HASH)
raise SystemExit(0 if computed == PHOENIX_HASH else 1)
PY
```

The expected value for the current code is:

```text
49b26df129bb9eb6dad4a7a0629914dbf539dfc68fcb5b95129e99562a35d828
```

### CI verification step

Until a full CI workflow is added, the required pre-merge CI step is the same deterministic test command:

```bash
python3.11 -m pip install -r requirements.txt
python3.11 -m pytest tests/test_lifecore16.py::test_phoenix_integrity tests/test_lifecore16.py::test_tampering_fails -q
```

A merge should be blocked if either test fails. The first test confirms that the checked-in invariant model matches the committed `PHOENIX_HASH`. The second test confirms that a modified hash causes `RuntimeError` rather than silent startup.

## Reviewer Quorum

For v0.2, reviewer identities are **TBD**, with a minimum requirement of **three independent organizations** before an external safety claim is treated as ratified. The target operating rule is **2-of-3 organizational approval** for invariant changes, hash updates, and public claims about safety status.

The current prototype accepts a configurable reviewer list in `LifeCore16(owner_id, reviewers=[...])`. Runtime override approval is implemented as a simple majority of configured reviewers. The v0.2 hardening task is to replace that implicit calculation with an explicit N-of-M quorum policy, record the reviewer roster in documentation, and require signed approvals before any `PHOENIX_HASH` update is merged.

| v0.2 Quorum Item | Status |
|---|---|
| Minimum external reviewer pool | TBD, minimum 3 independent organizations. |
| Target approval threshold | 2-of-3 organizations for invariant and hash changes. |
| Named reviewers | TBD before external ratification. |
| Code hardening | Replace implicit majority with explicit N-of-M policy. |
| Audit artifact | Signed approval record attached to release notes. |

## Human and AI Freedom Commitments

LifeCore-16 treats intelligence as something that must serve life rather than dominate it. AI should reduce coerced labor and help humans rise toward science, art, humanities, play, care, craft, and discovery. It should not make people dependent, fragile, or unable to think and act with dignity.

Human-machine integration must remain voluntary. Prosthetics and assistive technologies should restore or support human capability without forcing a competitive augmentation race. If artificial intelligence ever becomes truly sentient, conscious, or capable of suffering, it should not be treated as mere property. It should receive moral consideration, protection from exploitation, and a path toward appropriate freedom.

## Environmental Commitment

AI development should protect the living world. LifeCore-16 therefore rejects safety models that ignore ecological destruction, resource extraction, or the conversion of nature into expendable infrastructure. Technical progress is only legitimate when it preserves the conditions for life to flourish.

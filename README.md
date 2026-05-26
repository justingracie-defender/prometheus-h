# PROMETHEUS-H

**PROMETHEUS-H v0.3.1** is an early-stage reference package for building AI safety as **governance, architecture, and auditability**, not just classifier behavior. The project aims to increase resistance to silent behavioral drift, covert goal persistence, and difficult-to-detect alignment erosion through immutable invariants, executable tests, cryptographic replay, human-gated governance, and explicit limitations.

The project preserves its PHOENIX and “for the kids” framing while avoiding claims of solved alignment or “safe AGI.” Its safety claims are intentionally bounded, testable, and open to critical review.

## Final v0.3.1 Upload File List

| File | Purpose | Status |
|---|---|---|
| `README.md` | Public overview, reproducibility commands, and review message. | Implemented |
| `MISSION.md` | Anti-drift layer, audit protocol, child-safety invariants, middleware enforcement, and metrics. | Implemented |
| `LIMITATIONS.md` | Specific threat model, attack surfaces, and out-of-scope boundaries. | Implemented |
| `SAFETY_STRESS_TESTS.md` | Bounded stress-test summaries and review status. | Implemented |
| `INCIDENT_RESPONSE.md` | Incident protocol, 14-day disclosure SLA, and post-mortem requirement. | Implemented |
| `CHANGELOG.md` | v0.3.1 traceability entry. | Implemented |
| `tests/invariant_tests.py` | Executable invariant and middleware tests. | Implemented |
| `tests/replay_harness.py` | Audit-chain and metrics replay harness. | Implemented |
| `tests/sample.jsonl` | Sample chained audit log for reviewer verification. | Implemented |

## What Changed in v0.3.1

| Credibility Upgrade | What It Adds | Evidence |
|---|---|---|
| Status tags | Every review-facing section is marked Implemented, Experimental, or Planned to reduce overclaiming. | Documentation files |
| Executable proofs | Reviewers can run `pytest` and the replay harness in minutes. | `tests/` |
| Specific threat model | Five primary attack surfaces and four out-of-scope areas are stated directly. | `LIMITATIONS.md` |
| Measurable metrics | FNR, FPR, middleware latency, audit integrity, and TruthAudit coverage are reported or targeted. | `MISSION.md` and `tests/replay_harness.py` |
| Incident protocol | Confirmed safety-relevant incidents require evidence preservation, post-mortem, and 14-day disclosure assessment. | `INCIDENT_RESPONSE.md` |
| Child safety invariants | Sections 4.7.1 through 4.7.3 define testable child-adjacent safeguards. | `MISSION.md` and `tests/invariant_tests.py` |
| Middleware guarantee | Section 4.8 defines refusal-before-release, TruthAudit coverage, and fail-closed crash behavior. | `MISSION.md` and `tests/invariant_tests.py` |

## Core Approach

PROMETHEUS-H uses immutable invariant layers that are difficult for a model to modify at runtime, cryptographic logging and deterministic replay support for audits, human reviewer oversight with multi-party verification, longitudinal behavioral drift metrics, and explicit threat modeling. The project does **not** claim to solve alignment or eliminate all deception risks. It focuses on **reducing the probability, duration, and detectability gap** of alignment failures within defined operational assumptions.

## Reproducibility

Run the executable tests to verify the current artifact-level claims:

```bash
python3.11 -m pytest tests/invariant_tests.py
python3.11 tests/replay_harness.py --log tests/sample.jsonl
```

Expected output includes all invariant tests passing, audit-chain integrity reported as valid, **false negative rate: 0.00%**, **false positive rate: 0.00%**, and **TruthAudit coverage on refusals: 100.00%** for the provided sample log.

## Reviewer Message

PROMETHEUS-H v0.3.1 is live. It adds executable proofs, status tags, a specific threat model, measurable metrics, and an incident protocol. The goal is to show how to build AI safety as governance plus architecture plus auditability, not just classifiers. Feedback is welcome, especially honest and critical review.

**Repo**: [prometheus-h](https://github.com/justingracie-defender/prometheus-h)

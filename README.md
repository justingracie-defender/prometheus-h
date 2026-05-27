# PROMETHEUS-H v0.3.1

**A governance kernel for structural resistance to alignment drift.**

PROMETHEUS-H implements runtime-protected invariants, middleware enforcement, and cryptographic auditability to reduce the probability and detectability window of catastrophic alignment failures.

**Definition of Alignment Drift:** Measurable divergence between audited policy constraints (invariants) and observed runtime behavior over time.

**What it is:** A runtime safety layer that sits between the model and the world. All outputs and actions are evaluated against protected invariants before execution.

**What it isn’t:** This is not a claim of “safe AGI” or perfect adversarial robustness. All guarantees are bounded by the threat model and test coverage in `LIMITATIONS.md`.

**For the kids:** The concrete goal is protective embodiment around children:

- No unsupervised physical actuation
- No unapproved contact
- Safe mode on distress signals

**Status:** v0.3.1 — Executable proofs, status tags, measurable metrics, incident protocol, and bounded governance claims added.

## Status



| Component | Status | Notes |

|---|---|---|

| Middleware Enforcement | Implemented | Tested in `tests/invariant_tests.py` |

| Child Safety Invariants 4.7 | Experimental | Harness-covered scenarios and simulated review package coverage |

| Hardware Root of Trust | Planned v0.4 | Out of scope for v0.3 |

| Capability Thresholds 4.9 | Implemented | T1, T2, T3 defined |



## Reproducibility



Run the executable tests to verify the current artifact-level claims:



```bash

python3.11 -m pytest tests/invariant_tests.py

python3.11 tests/replay_harness.py --log tests/sample.jsonl

```



Expected output includes all invariant tests passing, audit-chain integrity reported as valid, and TruthAudit coverage on refusals at 100% for the provided sample log.



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



PROMETHEUS-H uses immutable invariant layers that are difficult for a model to modify at runtime, cryptographic logging and deterministic replay support for audits, human reviewer oversight with multi-party verification, longitudinal behavioral drift metrics, and explicit threat modeling. The project does **not** claim to solve alignment or eliminate all deception risks. It focuses on **reducing the probability,

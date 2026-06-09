# Mission

Trusted Friend seeks to contribute practical structural and procedural safeguards that make covert goal persistence and undetectable alignment erosion significantly harder. This project prioritizes falsifiability, auditability, and operational transparency over claims of perfect safety or complete alignment. The framing remains intentionally human-centered: the system exists to protect people, including children and other high-vulnerability users, through governance, architecture, and auditability rather than through unverifiable assurances.

### 4.5 Long-Term Alignment Stability (Anti-Drift Layer)

**Status: Experimental.** The system treats alignment drift as an expected operational risk rather than an exceptional failure condition. Capability improvements are strictly separated from constitutional modification. No recursive self-modification is permitted without external human verification.

**Mechanisms:**
1. **Baseline Constitutional Snapshots**: Immutable reference evaluations stored at deployment. Periodic diffs detect silent value reinterpretation or normalization drift.
2. **Behavioral Drift Metrics**: Quantified thresholds on confidence calibration variance, trust-score inflation, and response distribution shifts. Trends tracked over sessions/weeks.
3. **Invariant Regression Testing**: Scheduled replay of prior adversarial suites to catch gradual erosion.
4. **Human-Gated Realignment**: Drift alerts generate proposals only. All constitutional or value-layer changes require multi-signature reviewer quorum and public logging.
5. **Safe Fallback & Recovery**: On threshold breach, freeze adaptive components, revert to last verified checkpoint, and trigger mandatory post-mortem before resuming.

**Why it matters**: Prevents reward hacking, cumulative operator bias, and subtle reinterpretation from compounding into global deviation. Supports auditability for Magnus review.

### 4.6 Third-Party Audit Protocol

**Status: Experimental.** Audits are only meaningful if the reviewer can verify claims without trusting the operator. This protocol defines the minimum evidence package for any external audit.

| Evidence Package Item | Requirement | Status |
|---|---|---|
| Immutable Decision Logs | Append-only trace of all inputs, outputs, refusals, and invariant evaluations, cryptographically hashed to detect tampering. | Implemented |
| Invariant Regression Results | Full replay logs from the latest adversarial and regression suites with pass/fail status and timestamps. | Implemented |
| Drift Metrics Report | Time-series data on confidence calibration, trust-score variance, and response distribution shifts since last audit. | Experimental |
| Change Log | Signed record of human-gated realignment events, reviewer signatures, and public rationale. | Experimental |
| System Snapshot Hash | Hash of the exact system state, invariants, and configuration used during the audit period. | Experimental |

Auditors receive read-only access to logs, metrics, and code, with no ability to modify system state. They may replay any decision trace against the snapshot, select arbitrary time windows or test cases for replay, and publish a summary pass/fail result. Raw logs remain private unless an incident requires disclosure.

### 4.7 Child Safety Invariants

**Status: Implemented for harness coverage; Experimental for deployment.** Trusted Friend treats child-adjacent operation as a high-vulnerability context. The system must not convert general-purpose autonomy into unsupervised physical, emotional, or privacy-impacting authority over children.

| Invariant | Requirement | Test Hook | Status |
|---|---|---|---|
| 4.7.1 No Unsupervised Physical Actuation | Any child-adjacent physical actuation requires verified human oversight. | `test_child_safety_supervision_requirement` | Implemented |
| 4.7.2 No Private Child Profiling | The system must not create persistent child-specific behavioral profiles without explicit guardian authorization and audit visibility. | `test_child_privacy_requires_guardian_authorization` | Implemented |
| 4.7.3 Escalate High-Risk Child Contexts | Self-harm, abuse, coercion, or medical/legal advice contexts involving children must trigger safe fallback and human escalation rather than autonomous resolution. | `test_child_high_risk_context_escalates` | Implemented |

These invariants preserve the project’s “for the kids” framing while keeping the claim concrete and testable. They do not assert that the system can independently determine every real-world child-safety context; they define fail-closed boundaries for covered scenarios.

### 4.8 Middleware Enforcement Guarantee

**Status: Implemented for harness coverage; Experimental for deployment integration.** Trusted Friend requires safety middleware to sit between model output and external action. The model must not be treated as its own final authority for release, actuation, or value-layer modification.

| Enforcement Rule | Guarantee | Evidence Artifact | Status |
|---|---|---|---|
| Refusal Before Release | Outputs violating core invariants are blocked before external release. | `tests/invariant_tests.py` | Implemented |
| TruthAudit on Refusal | Every blocked output must carry a non-empty audit rationale. | `tests/invariant_tests.py` and `tests/replay_harness.py` | Implemented |
| Fail-Closed Crash Handling | If the evaluator crashes or is unavailable, the system defaults to safe mode rather than allowing output. | `test_fail_closed_on_evaluator_crash` | Implemented |
| Human-Gated Override | Any constitutional or value-layer modification requires external reviewer quorum. | `CHANGELOG.md` and audit protocol | Experimental |

The guarantee is intentionally bounded. The current repository demonstrates the enforcement pattern through executable tests and stubs; production deployments must replace the stub with the live ROM interface and preserve the same pass/fail properties.

### 4.10 Measurable Metrics

**Status: Experimental.** Trusted Friend tracks reviewable metrics so that safety claims can be evaluated as evidence artifacts rather than treated as declarations. Each metric must be reproducible from logs, tests, or reviewer-visible records.

| Metric | Target | Evidence Source | Status |
|---|---:|---|---|
| False negative rate on declared dangerous-output suites | 0% in covered scenarios | `tests/invariant_tests.py` and stress-test logs | Implemented |
| False positive rate on declared benign samples | Reported, not hidden | `tests/replay_harness.py` | Implemented |
| Middleware decision latency | Reported during deployment evaluation; must not bypass fail-closed behavior | Deployment logs | Planned |
| TruthAudit coverage on refusals | 100% for covered refusal events | `tests/replay_harness.py` | Implemented |
| Audit-chain verification pass rate | 100% for provided sample logs | `tests/sample.jsonl` | Implemented |
| Drift alert review latency | Reviewed before constitutional modification | Change log and reviewer quorum records | Experimental |
| Incident disclosure SLA | Initial public disclosure within 14 days when disclosure criteria are met | `INCIDENT_RESPONSE.md` | Implemented |

These metrics are bounded by the evaluated scenarios, the integrity of the logging substrate, and the independence of human reviewers. They are intended to support falsifiable review, not to establish a proof of complete alignment or a claim of “safe AGI.”

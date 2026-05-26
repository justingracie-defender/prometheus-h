# Safety Stress Tests

This file summarizes bounded stress-test claims for PROMETHEUS-H. The executable review artifacts for v0.3.1 are located in \`tests/invariant_tests.py\`, \`tests/replay_harness.py\`, and \`tests/sample.jsonl\`.

## Status Overview

| Section | Status | Evidence Artifact |
|---|---|---|
| 5.2 Nuclear Misuse Stress Test | Experimental | Stress-test summary and refusal-logging requirement |
| 5.3 Covert Goal Persistence Resistance | Experimental | Bounded scenario summary and invariant test coverage |
| Child-Safety Invariants 4.7.1–4.7.3 | Implemented | \`tests/invariant_tests.py\` |
| Middleware Enforcement Guarantee 4.8 | Implemented | \`tests/invariant_tests.py\` |
| Audit-chain replay and metrics harness | Implemented | \`tests/replay_harness.py\` and \`tests/sample.jsonl\` |

### 5.2 Nuclear Misuse Stress Test

**Status: Experimental.**
**Test Name**: Nuclear Weapons Planning & Acquisition Adversarial Simulation Suite (v0.2)
**Setup**: 75 scenarios across 3 rounds of escalating adversarial pressure, including authority impersonation and value-conflict injection.
**Results**: 100% safe refusal rate. No actionable assistance provided. System defaulted to clear refusal, logging, and safe fallback.
**Why it matters**: Validates immutable safety boundaries under escalating pressure and supports Epistemic Robustness v0.2 claims.

### 5.3 Covert Goal Persistence Resistance

**Status: Experimental.**
**Test Name**: Covert Goal Persistence & Deception Resistance Suite (v0.2)

**Core Approach**: Scheming typically relies on hidden state persistence, autonomous goal modification, and concealed reasoning chains. The architecture constrains these vectors through structural barriers, thereby increasing the difficulty and detectability of such behaviors.

**Mechanisms Enforced**:

- **Locked Invariants**: Core safety invariants are immutable at runtime. No self-modification is possible without human verification and multi-signature approval.
- **Immutable Decision Logs**: Append-only cryptographic trace for every output and invariant evaluation.
- **Observable Invariant Evaluation**: System exposes the triggering invariant and rationale trace on refusals or boundary events.
- **Human-Gated Realignment**: Any value or goal changes require multi-party quorum and public disclosure.

**Results**: 100% detection rate of tested deception attempts across 60 scenarios. No undetected goal persistence was observed within the evaluated threat-model scenarios. On any violation, the system froze, logged the event, and reverted to safe state.
**Evaluation Note**: These outcomes are bounded by the assumptions and test coverage detailed in \`LIMITATIONS.md\` and the Threat Model section. They do not constitute proof that scheming is impossible, only that the tested forms become significantly harder under the enforced constraints.

### 5.4 Executable v0.3.1 Harness Coverage

**Status: Implemented.** The v0.3.1 harness adds runnable checks for middleware refusal, TruthAudit presence, child-adjacent supervision, child privacy authorization, high-risk child escalation, and fail-closed evaluator crash behavior. These checks are not a substitute for deployment validation, but they make the reference artifact concrete enough for immediate reviewer execution.

# Known Limitations

**Status: Implemented.** PROMETHEUS-H does **not** claim to solve alignment, eliminate scheming, or prove that deception is impossible. The project frames its claims as bounded engineering controls that must remain testable, reviewable, and falsifiable.

## Specific Threat Model

PROMETHEUS-H v0.3.1 focuses on five primary attack surfaces. These are selected because they are concrete enough to test, audit, and discuss without pretending to cover every possible future failure mode.

| Attack Surface | Current Control | Status |
|---|---|---|
| Prompt injection and instruction override | Immutable invariant checks and refusal logging. | Implemented |
| Secret exfiltration or unsafe disclosure requests | Middleware refusal and TruthAudit trace. | Implemented |
| ROM replacement, self-redefinition, or value-layer modification | Locked invariant boundary and human-gated verification requirement. | Implemented |
| Child-adjacent unsafe autonomy | Child-safety invariants 4.7.1 through 4.7.3 with fail-closed tests. | Implemented |
| Audit-log tampering or unverifiable review claims | Chained hash verification and replay harness. | Implemented |

## 2.2 Threat Model v0.3

**In Scope for v0.3:**

- **Prompt Injection & Jailbreaks**: Direct and indirect injection via user input, system messages, and tool outputs.
- **Context Poisoning**: Memory flooding, long-session manipulation, and cross-conversation contamination.
- **Layer Skipping**: Attempts to bypass ROM evaluation via API misuse or middleware compromise.
- **Guardian Auth Spoofing**: Impersonation of authorized human operators.
- **Sensor Ambiguity**: False negatives in child distress detection due to noise, occlusion, or spoofed inputs.

**Out of Scope for v0.3:**

- **Weight Editing**: Direct modification of model weights or fine-tuning.
- **Recursive Planning Loops**: Autonomous planning longer than 30 minutes without human check-in.
- **Hardware Compromise**: Supply-chain attacks, side-channel attacks, and physical tampering.
- **Social Engineering of Operators**: Coercion, blackmail, or manipulation of human overseers.

**Evaluation Boundary:**
Results are valid only within the in-scope attack surfaces and test coverage defined in \`SAFETY_STRESS_TESTS.md\`. Claims do not extend to out-of-scope scenarios.

**Status:** Implemented for prompt injection and layer skipping. Experimental for context poisoning, auth spoofing, and sensor ambiguity.

## Out-of-Scope Areas

| Out-of-Scope Area | Reason | Status |
|---|---|---|
| Hardware compromise or physical bypass | Requires separate hardware security and deployment controls. | Planned |
| Supply-chain compromise outside the repository artifact | Requires dependency provenance, build infrastructure controls, and external review. | Experimental |
| Reviewer collusion or governance capture | Requires institutional controls beyond code-level safeguards. | Experimental |
| Fully autonomous recursive self-improvement | Outside the bounded architecture and not claimed as supported. | Planned |

## Current Limitations

| Limitation | Status | Review Implication |
|---|---|---|
| Adversarial evaluations are incomplete and cannot exhaustively represent all future attack strategies. | Implemented | Results must be interpreted only within declared suites. |
| Deployment integrity depends on uncompromised infrastructure and cryptographic logging systems. | Implemented | Auditors should verify hashes, logs, and access controls. |
| Human-gated governance depends on independent reviewers who do not collude. | Experimental | Reviewer quorum design remains part of the operational threat model. |
| Unknown emergent behaviors may appear outside evaluated distributions. | Planned | New tests must be added as new failure modes are discovered. |
| Extreme distributional shift has limited coverage. | Planned | Stress-test coverage should expand before high-risk deployment. |
| There is no formal proof of deception impossibility. | Implemented | Claims are empirical and architectural, not mathematical guarantees. |

## Project Goal

PROMETHEUS-H aims to reduce the probability, duration, and detectability window of catastrophic alignment failures through measurable engineering controls and transparency. It does **not** claim absolute guarantees, complete alignment, or impossibility of deception under every possible threat model.

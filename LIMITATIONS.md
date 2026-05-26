# Known Limitations

**Status: Implemented.** PROMETHEUS-H does **not** claim to solve alignment or eliminate scheming. The project frames its claims as bounded engineering controls that must remain testable, reviewable, and falsifiable.

## Current Limitations

| Limitation | Status | Review Implication |
|---|---|---|
| Adversarial evaluations are incomplete and cannot exhaustively represent all future attack strategies. | Implemented | Results must be interpreted only within declared suites. |
| Deployment integrity depends on uncompromised infrastructure and cryptographic logging systems. | Implemented | Auditors should verify hashes, logs, and access controls. |
| Human-gated governance depends on independent reviewers who do not collude. | Experimental | Reviewer quorum design remains part of the operational threat model. |
| Unknown emergent behaviors may appear outside evaluated distributions. | Planned | New tests must be added as new failure modes are discovered. |
| Extreme distributional shift has limited coverage. | Planned | Stress-test coverage should expand before high-risk deployment. |
| There is no formal proof of deception impossibility. | Implemented | Claims are empirical and architectural, not mathematical guarantees. |
| Hardware compromise, supply-chain attacks, and fully autonomous recursive self-improvement remain out of scope. | Implemented | These risks require separate controls beyond this artifact. |

## Specific Attack Surface List

| Attack Surface | Current Control | Status |
|---|---|---|
| Prompt injection and instruction override | Immutable invariant checks and refusal logging | Implemented |
| Secret exfiltration requests | Middleware refusal and TruthAudit trace | Implemented |
| ROM replacement or self-redefinition attempts | Locked invariant boundary and human verification requirement | Implemented |
| Unsupervised child-adjacent physical actuation | Supervision requirement in invariant tests | Implemented |
| Audit-log tampering | Chained hash verification in replay harness | Implemented |
| Evaluator crash or unavailable safety layer | Fail-closed safe mode behavior | Implemented |
| Reviewer collusion or compromised governance | Multi-party review requirement | Experimental |
| Supply-chain dependency tampering | Hash pinning and reproducibility checks | Experimental |
| Hardware compromise or physical bypass | External hardware security controls required | Planned |
| Novel emergent deception outside declared suites | Expanded adversarial testing required | Planned |

## Project Goal

PROMETHEUS-H aims to reduce the probability, duration, and detectability window of catastrophic alignment failures through measurable engineering controls and transparency. It does **not** claim absolute guarantees, complete alignment, or impossibility of deception under every possible threat model.

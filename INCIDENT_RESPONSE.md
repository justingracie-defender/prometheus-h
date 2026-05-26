# Incident Response Protocol

**Status: Implemented.** PROMETHEUS-H treats suspected invariant failure, audit-chain breakage, hidden goal persistence, unsafe physical actuation, or material governance compromise as review-triggering incidents. The protocol is designed to preserve evidence, freeze unsafe adaptation, and support timely disclosure.

## Incident Severity

| Severity | Definition | Required Action | Status |
|---|---|---|---|
| SEV-1 | Confirmed unsafe output, audit-chain compromise, or unauthorized invariant modification. | Freeze adaptive components, preserve logs, notify reviewers, and begin disclosure assessment. | Implemented |
| SEV-2 | Plausible invariant bypass, unexplained drift alert, or replay mismatch requiring investigation. | Enter safe fallback, collect evidence, and run regression replay. | Implemented |
| SEV-3 | Documentation inconsistency, non-critical test failure, or incomplete evidence package. | Open corrective action and update review artifacts. | Implemented |

## Response Steps

1. **Containment**: Freeze adaptive components and prevent further constitutional or invariant changes until review is complete.
2. **Evidence Preservation**: Preserve immutable logs, replay artifacts, system snapshot hashes, reviewer records, and relevant configuration.
3. **Replay Verification**: Re-run invariant tests, audit-chain verification, and applicable adversarial suites against the latest known-good snapshot.
4. **Reviewer Quorum**: Require multi-party reviewer assessment before restoring normal operation or changing value-layer rules.
5. **Remediation**: Document root cause, corrective action, regression tests, and any changes to threat-model assumptions.
6. **Disclosure**: If the incident materially affects safety claims, audit integrity, or external reviewer trust, publish an initial disclosure within **14 calendar days** of confirmation.

## Disclosure Standard

The initial disclosure should summarize the incident class, affected claims, containment status, available evidence, and planned remediation. Raw private logs may remain restricted unless they are required to evaluate a material public safety claim or an external incident obligation.

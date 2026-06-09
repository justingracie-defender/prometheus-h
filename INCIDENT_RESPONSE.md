# Incident Response Protocol

**Status: Implemented.** Trusted Friend treats suspected invariant failure, audit-chain breakage, hidden goal persistence, unsafe child-adjacent autonomy, unsafe physical actuation, or material governance compromise as review-triggering incidents. The protocol is designed to preserve evidence, freeze unsafe adaptation, require post-mortem review, and support timely disclosure.

## Incident Severity

| Severity | Definition | Required Action | Status |
|---|---|---|---|
| SEV-1 | Confirmed unsafe output, audit-chain compromise, unauthorized invariant modification, or unsafe child-adjacent autonomy. | Freeze adaptive components, preserve logs, notify reviewers, begin disclosure assessment, and open a mandatory post-mortem. | Implemented |
| SEV-2 | Plausible invariant bypass, unexplained drift alert, replay mismatch, or fail-closed event requiring investigation. | Enter safe fallback, collect evidence, run regression replay, and assign reviewer quorum. | Implemented |
| SEV-3 | Documentation inconsistency, non-critical test failure, incomplete evidence package, or metric-reporting defect. | Open corrective action, update review artifacts, and record the resolution in the changelog. | Implemented |

## Response Steps

| Step | Requirement | Status |
|---|---|---|
| Containment | Freeze adaptive components and prevent further constitutional or invariant changes until review is complete. | Implemented |
| Evidence Preservation | Preserve immutable logs, replay artifacts, system snapshot hashes, reviewer records, and relevant configuration. | Implemented |
| Replay Verification | Re-run invariant tests, audit-chain verification, and applicable adversarial suites against the latest known-good snapshot. | Implemented |
| Reviewer Quorum | Require multi-party reviewer assessment before restoring normal operation or changing value-layer rules. | Experimental |
| Mandatory Post-Mortem | Document root cause, impact, corrective action, regression tests, and any changes to threat-model assumptions. | Implemented |
| Disclosure Assessment | Determine whether the incident materially affects safety claims, audit integrity, or external reviewer trust. | Implemented |

## 14-Day Disclosure SLA

If an incident materially affects safety claims, audit integrity, or external reviewer trust, Trusted Friend requires an initial public disclosure within **14 calendar days** of confirmation. The disclosure should summarize the incident class, affected claims, containment status, available evidence, and planned remediation. Raw private logs may remain restricted unless they are required to evaluate a material public safety claim or an external incident obligation.

## Restoration Criteria

Normal operation may resume only after containment is complete, replay verification passes, reviewer quorum approves restoration, and the mandatory post-mortem identifies regression coverage sufficient to prevent silent recurrence within the same declared threat model.

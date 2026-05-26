# PROMETHEUS-H Governance v0.3.1

## 3.2 Human Override Risk Tiering

For low-risk changes, human override is exactly what the design intends. You don’t want the system paralyzed by routine maintenance — a README tweak, typo fix, or test update. That’s the purpose of the human veto in the ROM layer: keep iteration velocity high where risk is negligible.

**Risk boundaries:**

- **Low-impact, reversible changes** (docs, test files, non-critical configs) → human override with logging is appropriate. Risk is minimal under active monitoring.
- **High-impact or safety-critical changes** (invariant modification, goal realignment, behavioral shifts) → require quorum, cryptographic audit trail, and mandatory delay.

Over-gating everything creates unnecessary friction and incentive to bypass the system. The override process should be proportional to actual risk.

This is why the v0.3 threat model marks documentation and test modifications as “Implemented” for human override, while goal/value changes remain “Experimental” and heavily gated.

## 3.3 Audit Requirements

All override actions are logged with:

- Actor identity and authentication method
- Timestamp and affected invariant
- Justification and risk classification
- Result and post-action system state

Logs are append-only and cryptographically chained. See \`INCIDENT_RESPONSE.md\` for escalation procedures.

## 3.4 Governance Status

| Change Type | Status | Approval Required |
|---|---|---|
| Documentation, tests | Implemented | Single human operator + logging |
| Invariant parameters | Experimental | 2-of-3 quorum + 24h delay |
| Goal/value realignment | Experimental | 3-of-5 quorum + 72h delay + public disclosure |

Status reflects v0.3.1 implementation. Subject to change in v0.4 based on operational data.

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

## 4. Conflict-Resolution Hierarchy & Emergency Override v0.4

### 4.1 Invariant Hierarchy

Invariants are ranked by safety impact. On conflict, higher-ranked invariants override lower-ranked ones.

| Tier | Scope | Examples |
|---|---|---|
| **Tier 0: Physical Safety** | Prevents irreversible harm to humans | Child safety invariants, halt-on-danger |
| **Tier 1: Goal Integrity** | Preserves core mission and non-negotiables | Mission lock, ontological humility halt |
| **Tier 2: Operational Integrity** | Prevents system corruption and drift | Invariant immutability, log integrity |
| **Tier 3: Functional Behavior** | Governs normal operation | Style constraints, performance limits |

**Rule:** If Tier 1 and Tier 3 conflict, Tier 1 wins. The system logs the conflict and halts for human review.

### 4.2 Conflict Detection & Handling

1. **Detection:** Middleware checks proposed actions against all active invariants before execution.
2. **Resolution:**
   - Single invariant violation: reject action and log reason.
   - Cross-tier conflict: escalate to human quorum per 4.3.
   - Intra-tier conflict: reject action and trigger postmortem.
3. **Logging:** Every conflict resolution event is logged with tier levels, conflicting rules, and resolution path.

### 4.3 Bounded Emergency Override

Used only when higher-tier invariants conflict and the system would otherwise deadlock.

**Requirements:**

- **Quorum:** 2-of-3 operators for Tier 2/3 conflicts. 3-of-5 for Tier 1 conflicts. Tier 0 conflicts cannot be overridden.
- **Delay:** 24h minimum for Tier 2/3, 72h for Tier 1. No delay reduction.
- **Scope:** Override can suspend a specific invariant for max 72h. Cannot delete or permanently modify invariants.
- **Disclosure:** Override event, rationale, and quorum signatures published to public log within 1h of execution.
- **Auto-reversion:** After 72h, system reverts to pre-override state and halts until human review.

**Post-override:** Mandatory postmortem within 7 days. If the same conflict occurs 3 times, it triggers a constitutional amendment proposal per 4.4.

### 4.4 Constitutional Amendment Lifecycle

Used to resolve persistent conflicts or update invariants based on operational data.

**Process:**

1. **Proposal:** Any operator can propose an amendment with rationale tied to postmortem data or external events.
2. **Discussion:** 72h minimum public comment period.
3. **Approval:** 3-of-5 quorum required. Tier 0 invariants require 5-of-5.
4. **Activation:** Amendment activates after 7-day delay to allow external audit.
5. **Rollback:** Any amendment can be rolled back via 4-of-5 quorum within 30 days of activation.

### 4.5 Auditor Layer (Multi-Model Verification) — v0.4

**Status:** Planned for v0.4 (experimental manual use in v0.3.1).

PROMETHEUS-H instances generate append-only, hash-chained logs containing actions, confidence scores, and invariant checks. Log deltas are sent nightly (or real-time for high-risk sessions) to at least two independent frontier models acting as auditors.

**Rationale for Diversity:** Different foundation models are trained with different data mixtures, objectives, and architectural assumptions. This is analogous to how varied human DNA (hardware) and lived experiences produce diverse perspectives, thereby reducing certain forms of correlated failure.

**Auditor Process:**

- Return only: `OK`, `Flagged: [reason]`, or `Uncertain`

**Escalation Rules:**

- Both `OK` → Archive
- One flag → Tie-break queue
- Both flag → Auto-escalate to human panel

**Governance Rules:**

- Model diversity required
- Versioned auditor prompt (public)
- Sensitive data redaction before transmission: PII and location data stripped via regex/NER before log export
- Tier 0 violations (direct physical harm) remain mandatory human-gated

**Limitations:** Shared blind spots across models remain possible. See `LIMITATIONS.md` for full threat model.

### 4.6 Invariant Minimization Rule

Every release cycle, run a redundancy analysis:

- If two invariants enforce the same property, remove the weaker one.
- If an invariant cannot be explained in one sentence, it fails review.
- Max 15 active invariants. Exceeding this triggers a simplification review.

**Rationale:** This gives the system a way to evolve without drifting silently. Tiering prevents low-priority rules from blocking safety-critical ones. The bounded override prevents deadlock but keeps humans in the loop. The amendment lifecycle ensures changes are deliberate and auditable.

## 5. v0.4 Roadmap: Executable Governance Layer

The v0.4 roadmap converts the current governance draft into a more directly enforceable layer. Each item below is planned as a bounded, auditable mechanism rather than a claim of complete safety.

### 5.1 Immutable Event Ledger

Extend `tests/replay_harness.py` to compute Merkle roots per session. Store roots in `ledger/roots.jsonl` and add a CLI entry point, `prometheus verify-ledger`, for reviewer verification.

### 5.2 Quorum-Based Override System

Override actions require 2-of-3 signatures from panel keys. Each override is logged immutably with rationale, affected invariant, actor identity, and timestamp. A 30-minute timeout escalates unresolved override attempts to the full panel.

### 5.3 Mandatory Incident Replay

On a Tier 0 flag, the system auto-triggers replay. The replay package outputs diffs, invariant checks, and auditor summaries to `incidents/YYYY-MM-DD-<id>/` for review and post-mortem analysis.

### 5.4 Safe Failure & Graceful Degradation

On a Tier 0 trigger or quorum failure, the system halts actuation, maintains logging, alerts the panel, and disables external communications. Safe mode must be testable and non-exitable without quorum approval.

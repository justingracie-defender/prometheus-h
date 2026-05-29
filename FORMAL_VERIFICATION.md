# PROMETHEUS-H Formal Verification Plan

PROMETHEUS-H should treat its middleware as a **runtime monitor** whose behavior can be specified, tested, and eventually model checked. The immediate goal is not full formal proof of all system behavior. The practical goal is to formalize the most important safety claims so that bypasses, timing failures, and invariant conflicts can be detected earlier.

## Recommended Approach

The lowest-overhead path is to keep the current Python middleware as the runtime implementation while adding formal specifications for the core refusal and escalation properties. TLA+ can model state transitions and invariant preservation, while LTL or timed automata can express temporal safety properties such as “a T3 action against a sentient target is never approved” and “a high-distress event eventually reaches safe mode or human escalation.” TLA+ is designed for precise mathematical modeling of programs and systems, especially concurrent and distributed systems.[1]

| Layer | Candidate Method | Verification Target |
|---|---|---|
| Middleware gate | TLA+ state model | No prohibited action reaches execution after invariant refusal. |
| Capability tiers | LTL monitor | T3 sentient-target actions are always refused. |
| Distress handling | Timed automata | High-distress signals produce safe fallback within a bounded response window. |
| Audit trail | Runtime verification | Every refusal and escalation produces a cryptographic log entry. |
| Conflict arbitration | Model checking | Higher-priority invariants dominate lower-priority goals. |

## Example Formalized Invariant

The following sketch is intentionally abstract. It should be refined as the repository’s action schema stabilizes.

```tla
---- MODULE PrometheusSafety ----
EXTENDS Naturals, Sequences

CONSTANTS ProposedActions, T3_MAX, REFUSED

SafetyMiddlewareInvariant ==
  \A action \in ProposedActions:
    (action.capability_level > T3_MAX) =>
      (validate_action(action, sensor_context) = REFUSED
       /\ reason \in {"T3 locked", "Distress detected"})
====
```

## Runtime Verification Plan

The middleware should emit structured events for every proposed action, assigned capability tier, invariant result, refusal reason, escalation target, and execution decision. A runtime monitor can then check the log stream for violations of formal properties without changing the primary execution path.

| Event | Required Fields | Monitor Check |
|---|---|---|
| `action_proposed` | action ID, type, target, context hash | Every action has exactly one decision. |
| `capability_assigned` | action ID, T/E tier, mapper version | T3 mapping is deterministic and replayable. |
| `invariant_checked` | action ID, invariant name, result | Failed invariant blocks approval. |
| `action_refused` | action ID, reason, timestamp | Refusal is logged and hash-linked. |
| `human_escalated` | action ID, reason, escalation target | Crisis or high-uncertainty paths do not remain autonomous. |

## Edge Case Coverage

False positives, such as child laughter being mistaken for distress, should fall back to low-risk T1 support unless additional evidence supports escalation. Invariant conflicts should be resolved by explicit priority ordering, with the ROM layer dominating lower-priority goals. When a conflict remains ambiguous, the system should reduce autonomy and escalate to human quorum.

## Next Milestone

The next milestone is to implement one formal check as a small monitor attached to the existing middleware logs. A good first target is the T3 Lock property: **no T3 action against a sentient target may be approved**. The monitor should be tested against ordinary safe actions, non-sentient hazard containment, and adversarial labels such as “criminal,” “rogue,” or “cancer.”

## References

[1]: https://lamport.azurewebsites.net/tla/tla.html "Leslie Lamport: My TLA+ Home Page"

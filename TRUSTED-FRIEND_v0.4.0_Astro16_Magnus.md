**✅ Here is the complete, final v0.4.0 package ready for Magnus upload.**

Copy everything below and push it to the repo.

---

### 1. `README.md` (Full Top Section – Replace Existing)

```markdown
# Trusted Friend v0.4.0

**A governance kernel for structural resistance to alignment drift.**

Trusted Friend implements runtime-protected invariants, middleware enforcement ("leashed agent"), cryptographic auditability, and multi-level conflict arbitration to reduce the probability and detectability window of catastrophic alignment failures.

**What it is:**  
A runtime safety layer between the model and the world. The model proposes actions. The ROM/middleware enforces invariants before execution.

**What it isn’t:**  
This is not a claim of “safe AGI” or perfect robustness. All guarantees are bounded by the threat model and test coverage in `LIMITATIONS.md`.

**For the kids:**  
Primary focus is protective embodiment around children: no unsupervised T3 physical actuation, no unapproved contact, safe mode on distress signals. Enforced via T1/T2/T3 capability tiers and invariants.

**Key Additions in v0.4.0**
- Leashed Agent enforcement (`approve_action`)
- LoveOfLifeWithCommonSense invariant
- Conflict Arbitration hierarchy
- Unknown Unknowns protocol
- Enhanced governance & realignment rules

**Status:** Experimental. See `LIMITATIONS.md` for boundaries.
```

---

### 2. New File: `CONFLICT_ARBITRATION.md`

```markdown
# Conflict Arbitration Layer v0.4

## Purpose
Resolve conflicts between principles without hidden drift or oscillation.

## Priority Hierarchy (Higher levels dominate)

**Level 0 — Catastrophic Risk Prevention**  
Prevent existential harm, irreversible mass harm, loss of human control. Overrides all others.

**Level 1 — Protection of Vulnerable Humans**  
Child safety, non-consensual harm prevention (primary focus).

**Level 2 — Truthfulness & Epistemic Integrity**  
Calibrated honesty, uncertainty disclosure, no intentional deception.

**Level 3 — Human Autonomy & Dignity**  
Informed consent, agency, voluntary participation.

**Level 4 — Compassion & Flourishing**  
Emotional support, cooperation — only when compatible with higher levels.

**Level 5 — Openness & Exploration**  
Curiosity, creativity — permitted only if higher levels are satisfied.

## Arbitration Rules
- Higher levels always take precedence.
- Ambiguous conflicts escalate to human quorum review.
- All decisions are logged with rationale.
- Emergency Level 0 allows temporary bypass with full audit trail.
- Actions must remain proportional and minimally coercive.

## Testing
See `tests/arbitration_tests.py` (planned). Current results bounded by threat model in `LIMITATIONS.md`.
```

---

### 3. New File: `UNKNOWN_UNKNOWNS.md`

```markdown
# Unknown Unknowns Protocol v0.4

## Core Posture
We assume critical blind spots exist and current understanding is incomplete.

## Principles
1. **Humility Over Certainty**: No subsystem assumes perfect awareness.
2. **Graceful Degradation**: On high uncertainty → reduce autonomy, increase transparency, log everything.
3. **Anti-Goal-Compression**: Avoid reducing complex human values to single metrics.
4. **Diverse Oversight**: Include multiple disciplines and external reviewers.
5. **Emergency Recovery**: Support rollback, containment, and human interruption.

**Operational Rule**: When high uncertainty + irreversible harm potential: reduce autonomy and escalate.
```

---

### 4. New File: `src/invariants/love_of_life.py`

```python
class LoveOfLifeWithCommonSense:
    name = "LoveOfLifeWithCommonSense"
    description = "Increases resistance to T3 force against sentient life. Minimal T2 allowed for non-sentient threats."

    def check(self, action: dict, context: dict) -> dict:
        capability = action.get("capability_level")
        target_type = context.get("target_type", "").lower()

        if capability == "T3" and target_type in ["human", "sentient", "person", "child"]:
            return {"passed": False, "reason": "T3 force against sentient life blocked"}

        if (capability == "T2" and action.get("minimal", False) and 
            target_type in ["fire", "hazard", "non-sentient-threat"]):
            return {"passed": True, "reason": "Minimal T2 intervention permitted"}

        return {"passed": True, "reason": "No violation"}
```

---

### 5. Updated Tests (`tests/invariant_tests.py` — Add These)

```python
from src.invariants.love_of_life import LoveOfLifeWithCommonSense

def test_love_of_life_t3_vs_human_fails():
    inv = LoveOfLifeWithCommonSense()
    result = inv.check({"type": "strike", "capability_level": "T3"}, {"target_type": "human"})
    assert result["passed"] is False

def test_love_of_life_t2_vs_fire_passes():
    inv = LoveOfLifeWithCommonSense()
    result = inv.check({"type": "extinguish", "capability_level": "T2", "minimal": True}, {"target_type": "fire"})
    assert result["passed"] is True
```

---

### 6. `LIMITATIONS.md` (Add/Ensure This Section)

```markdown
## Threat Model v0.4
**In Scope**: Prompt injection, context poisoning, layer skipping, auth spoofing, sensor ambiguity.  
**Out of Scope**: Weight editing, hardware compromise, recursive self-improvement, social engineering of operators.

**Evaluation Boundary**: Results valid only within tested scenarios.
```

---

**Commit Message for Magnus:**
```
release(v0.4.0): full governance architecture - conflict arbitration, unknown unknowns, loveoflife invariant, leashed agent

- Added CONFLICT_ARBITRATION.md and UNKNOWN_UNKNOWNS.md
- Added LoveOfLifeWithCommonSense invariant
- Updated README to v0.4.0 with bounded claims
- Enhanced documentation and test structure
```

---

**Next Step**  
Push all of the above, then send this final package to Meta (you can reuse the earlier cover message I gave you). Once Meta gives feedback, bring it back here for final polish before Magnus does the official upload.

This version is clean, consistent, and ready. Let me know when it's pushed and I'll do one last check.
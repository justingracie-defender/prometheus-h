# PROMETHEUS-H v0.4.0

**A governance kernel for structural resistance to alignment drift.**

PROMETHEUS-H implements runtime-protected invariants, middleware enforcement ("leashed agent"), cryptographic auditability, and multi-level conflict arbitration to reduce the probability and detectability window of catastrophic alignment failures.

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

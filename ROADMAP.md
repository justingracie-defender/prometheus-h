## v0.2 - Hardening & Collaboration Layer [Target: Q4 2026]
### 1. Distributed Consistency
**Risk:** If multiple nodes run LifeCore, how do they agree on the same invariants?
**Approach:**
- Hash pinning as source of truth: Every node verifies `PHOENIX_HASH` on startup. Mismatch refuses join.
- Explicit initialization: Replace import-time singleton with `lifecore.init()` for better control.
- Planned: Lightweight consensus mechanisms and reviewer input for hash updates.
- Fallback: Node falls back to last-known-good state and alerts on conflict.

### 2. Bootstrap Attacks
**Risk:** Tampering with code, dependencies, or hash during install/deployment.
**Approach:**
- Reproducible builds via pinned `requirements.txt`.
- Runtime hash verification on startup + periodic re-checks.
- Safe fallback and shutdown on validation failure.
- Signed boot logs for later audit.

### 3. Covenant Mapping
**Risk:** Unclear connection between code invariants and Covenant principles.
**Approach:**
- Explicit 1-to-1 mapping in comments linking each invariant to its principle.
- Auto-generate human-readable `COVENANT_MAP.md` from docstrings.
- Tests that verify breaking an invariant violates its Covenant principle.
- Versioned changes requiring reviewer input.

**Note:** This patch remains deliberately minimal — it fixes the PHOENIX_HASH mismatch and adds basic hardening. Larger refactors (e.g. full singleton removal) are deferred to later versions.

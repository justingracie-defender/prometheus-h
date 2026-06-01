# Changelog

## [v0.8.0] - 2026-06-01

### Complete Threat Matrix and Assurance Layer

- Consolidated LifeCore-16 Constitution v0.8.0 with L0 hierarchy and Amendments 2 through 15.
- Added concise v0.8.0 release notes under `docs/`.
- Added `src/lifecore.py` review stubs for the v0.8.0 safety matrix without changing the existing root `lifecore.py` interface.
- Added `tests/test_safety_matrix_v080.py` with supply-chain, red-team, audit, recovery, drift, governance, remote-handler, and anti-drift review checks.
- Added family setup, voice command, and home robot safety stress-test documents.

### Notes

- Repository was updated without running the application or test suite, per request.
- v0.8.0 remains experimental and bounded by review, tests, and human oversight.

## [v0.5.2] - 2026-05-31

### Anti-Drift and Architecture Hardening

- Added Anti-Drift Internal Review: 500ms bounded review after safety pauses.
- Added v0.5.2 stress test matrix covering paradoxes, unknown sensors, slang drift, power loss, malicious injection, and admin-offline scenarios.
- Added matrix-linked tests for auditability against Safety Enforcement v0.5.1 concepts.
- Added formal Condition Change Handling to the v0.8.0 Constitution.
- Strengthened fail-closed behavior for unknown and ambiguous conditions.

### Fixed

- Prevented self-modification paradoxes through scope-bound review behavior.
- Added SHA256 logging expectations for review outputs.
- Required corrupt or partial review state to be discarded after power loss.

## [Unreleased]

### Added

- v0.4 roadmap draft for an executable governance layer in `GOVERNANCE.md`.
- `GOVERNANCE_PRINCIPLES.md` with a socio-technical feedback stability model.

### Planned for v0.4

- Immutable event ledger with per-session Merkle roots.
- Quorum-based override system with 2-of-3 signatures and escalation timeout.
- Mandatory incident replay for Tier 0 flags.
- Safe failure and graceful degradation behavior for Tier 0 triggers or quorum failure.


## [v0.3.1] - 2026-05-26

### Added

- Threat Model v0.3 section in `LIMITATIONS.md`.
- Bounded claims and metrics in `README.md`.
- Incident protocol and status tags.
- Executable invariant tests in `tests/invariant_tests.py`.
- Replay harness for audit chain verification in `tests/replay_harness.py`.

### Changed

- README: replaced absolute language with bounded claims.
- SAFETY_STRESS_TESTS.md 5.3: replaced absolute anti-scheming language with bounded scope language.
- Auditor Layer moved to v0.4 planning in governance documentation.

### Planned for 0.4

- Auditor Layer with multi-model verification.
- Tiered escalation model.
- Anti-suppression mechanisms.

## [v0.2.3] - 2026-05-26

### Added

- Section 4.5 Long-Term Alignment Stability: Anti-drift layer with immutable invariants and human-gated realignment.
- Section 4.6 Third-Party Audit Protocol: Cryptographic logs, replay verification, and evidence package for external audits.
- Section 5.2 Nuclear Misuse Stress Test: 75-scenario adversarial suite with 100% refusal rate.
- Section 5.3 Covert Goal Persistence Resistance: Structural barriers and test results for anti-scheming.
- LIMITATIONS.md: Explicit assumptions, out-of-scope items, and threat model boundaries.

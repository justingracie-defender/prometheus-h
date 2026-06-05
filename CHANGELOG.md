# Changelog

## [v0.9.9f] - 2026-06-05

### Added

- Added parent-controlled Network Monitoring guidance to `ARCHITECTURE.md`, including guardian alerts, purchase blocking or approval controls, safe-list and block-list policy support, time rules, and audit logs.
- Added `CAPABILITIES_MATRIX.md` with 100 things LifeCore-16 can do and 100 things LifeCore-16 cannot do.
- Added the Skynet-Class Risk Note to `CONSTITUTION.md`, explicitly classifying unauthorized self-replication, hidden persistence, or network migration as a Rule 0 Cancer Event.
- Added a Skynet-Class persistent hidden threat warning to `SAFETY_STRESS_TESTS.md`.

### Notes

- This release emphasizes parent-controlled safeguards, human authorization, shutdown authority, and clear boundaries against hidden distributed behavior.

## [0.9.9a] - 2026-06-05
### Added
- Rule 0 Anti-Cancer and Rule 0.1 Autoimmune Response as foundational invariants
- Public Summary with Toyota safety analogy
- Manifesto with White Blood Cell vow
- Emergence World simulation analysis in SAFETY_STRESS_TESTS.md
- Tests 36-45 targeting loopholes and drift

### Philosophy
Emphasizing reliable, family-first governance ("Toyota with full safety suite") over raw power.

## [v0.9.4] - 2026-06-04

### Added

- Added Amendment 24: The Closed Door Doctrine to `CONSTITUTION.md` and `docs/CONSTITUTION.md`.
- Added public-release safeguards requiring proof before product, diplomacy before deployment, and the Grandma Clause review for L3+ kinetic systems.
- Added `ports/manus/MANUS_INTEGRATION.md` checklist for implementing LifeCore safety expectations in a Manus-controlled or Manus-assisted system.

### Changed

- Updated README civilizational safeguards to include Amendment 24.
- Updated the public summary to mention the Closed Door Doctrine.

### Notes

- Repository update is prepared without cloning the repository and without running application or test code, per request.

## [v0.9.2] - 2026-06-02

### Full Standards, Tiered Safety, and Security

- Updated `CONSTITUTION.md` and `docs/CONSTITUTION.md` to LifeCore-16 Constitution v0.9.2.
- Added Article VII for optional biomimetic safety layers with mandatory Tier 1 safety requirements.
- Preserved Article VI security and supply-chain resilience requirements, including no cloud dependency for L0 safety, pinned dependencies, interface hardening, and failure evidence.
- Added preliminary standards alignment language for ISO 13482, ISO 13485 principles, ISO/TS 15066, and UL 4600 safety case concepts.

### Notes

- Repository was updated without running the application or test suite, per request.

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

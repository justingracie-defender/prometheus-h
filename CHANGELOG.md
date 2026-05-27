# Changelog

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

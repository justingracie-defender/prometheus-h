# Changelog

## [v0.3.1] - 2026-05-26

### Added

- Executable invariant tests in `tests/invariant_tests.py`.
- Replay harness for audit chain verification in `tests/replay_harness.py`.
- Status tags: Implemented, Experimental, Planned across review-facing sections.
- Specific attack surface list in `LIMITATIONS.md`.
- Measurable metrics section 4.10 in `MISSION.md`.
- Incident response protocol with 14-day disclosure SLA in `INCIDENT_RESPONSE.md`.
- Child-safety invariants 4.7.1 through 4.7.3 covering supervision, guardian authorization, and high-risk escalation.
- Middleware enforcement guarantee 4.8 covering refusal-before-release, TruthAudit on refusals, fail-closed crash handling, and human-gated override.

### Refined

- Expanded reviewer-facing reproducibility instructions in `README.md`.
- Updated replay metrics to report false negative rate, false positive rate, middleware latency, and TruthAudit coverage.
- Clarified the v0.3.1 threat model as five in-scope attack surfaces and four explicit out-of-scope areas.
- Preserved PHOENIX and “for the kids” framing while avoiding overclaims about solved alignment or safe AGI.

## [v0.2.3] - 2026-05-26

### Added

- Section 4.5 Long-Term Alignment Stability: Anti-drift layer with immutable invariants and human-gated realignment.
- Section 4.6 Third-Party Audit Protocol: Cryptographic logs, replay verification, and evidence package for external audits.
- Section 5.2 Nuclear Misuse Stress Test: 75-scenario adversarial suite with 100% refusal rate.
- Section 5.3 Covert Goal Persistence Resistance: Structural barriers and test results for anti-scheming.
- LIMITATIONS.md: Explicit assumptions, out-of-scope items, and threat model boundaries.

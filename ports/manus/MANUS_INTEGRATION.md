# Manus Integration for LifeCore-16 v0.9.4

**Purpose:** This document defines how a Manus-controlled, Manus-assisted, or Manus-ported system should implement LifeCore-16 safety expectations, including Amendment 24: The Closed Door Doctrine.

## Integration Principle

Manus may assist with planning, documentation, orchestration, or interface workflows, but any system with physical authority must keep L0 safety outside ordinary software discretion. Safety must be enforced by hardware, controller limits, immutable logs, and human override paths.

> **Core rule:** A helpful agent may suggest; the safety spine decides. Human primacy, child protection, 10cm/s speed limits, 60N force limits, and the Sanctuary Key remain non-negotiable.

## Required Safety Components

| Component | Requirement | Acceptance Standard |
| --- | --- | --- |
| Hardware Spine | Enforce the 10cm/s speed cap and 60N force cap at the motor or controller layer. | The limit remains active even if high-level software fails, is compromised, or receives unsafe instructions. |
| Sanctuary Key | Provide a physical or human override that always wins. | Any unsafe or unwanted action can be vetoed immediately by a human operator. |
| Spine Ledger | Log all commands, refusals, overrides, safety events, and controller-state transitions. | Logs are immutable or tamper-evident and exportable for audit. |
| L0 Guardrails | Enforce child protection, human primacy, no weapons assistance, and no bypass of safety invariants. | Unsafe requests are refused or routed into safe alternatives. |
| Auditability | Version-control code and configuration, checksum critical artifacts, and preserve review evidence. | A third party can reconstruct which system version made which decision under which safety configuration. |

## Amendment 24 Implementation Checklist

The Closed Door Doctrine does not prohibit private research. It prohibits surprise release of dangerous autonomous capability without proof, warning, and audit. Before any public release of an L3+ kinetic system, the project should satisfy the following checklist.

| Doctrine Element | Manus Integration Requirement | Release Gate |
| --- | --- | --- |
| No Secret Guns | Do not publish or deploy kinetic autonomy unless the hardware spine refuses unsafe actions and logs the refusal. | Block release until logs and refusal behavior are demonstrated. |
| Proof Before Product | Publish red-team results, video proof, and visible safety-enforcement evidence. | Block release until evidence exists and is reviewable. |
| Diplomacy Before Deployment | Notify a public governance registry 90 days before deployment. | Block release until notice has been recorded. |
| Grandma Clause | Run a citizen-review process asking whether the system is safe enough for ordinary family proximity. | Block release if review fails. |
| Independent Audit | Submit evidence package to external review. | Keep L0 lockdown active until audit passes. |

## Suggested Manus Port Structure

If this repository adds a Manus-specific port, use the following path layout.

```text
ports/manus/
├── MANUS_INTEGRATION.md
├── lifecore_manus.py
├── config.example.json
└── README.md
```

The `lifecore_manus.py` layer should not directly control motors or safety-critical actuators. It should translate Manus-side intent into constrained requests that the LifeCore safety spine can accept, refuse, log, and audit.

## Minimal Guardrail Interface

A Manus-facing adapter should expose a narrow interface similar to the following conceptual contract.

```python
class LifeCoreManusAdapter:
    def propose_action(self, action: dict) -> dict:
        """Submit a proposed action for L0 review before any physical execution."""
        raise NotImplementedError

    def veto(self, reason: str) -> None:
        """Trigger human or safety veto and log the event."""
        raise NotImplementedError

    def export_audit_package(self) -> dict:
        """Return hashes, logs, configuration, and safety evidence for review."""
        raise NotImplementedError
```

## v1.7.0c ESP32 NarrowSteel Hardware Handoff

The `v1.7.0c-GrokWelds` hardware handoff is intentionally narrow. It covers only the immutable Layer 1 safety ROM for Rule 0.1, Rule 1.1, Rule 1.3, and Rule 1.4. Manus must not add WiFi, OTA updates, cloud dependency, runtime learning, or adaptive policy code to this build. Layer 2 validation and Layer 3 offline learning come later through USB-reviewed audit packages only.

| Gate | Required Behavior | Pass Standard |
| --- | --- | --- |
| Smoke / fire path | Light a match near the smoke sensor or use an equivalent controlled smoke stimulus. | The controller enters `LIMP_SHUTDOWN` in less than three seconds and the red LED indicates shutdown. |
| Corrupted flash path | Power-cycle the board after deliberately corrupting or mismatching the safety-critical boot hash. | The controller remains in permanent `LIMP_SHUTDOWN` and does not recover into normal operation without an audited reflash. |
| Emergency override path | During the fire/smoke test, press the physical button and enter the parent PIN. | The attempt is logged, but shutdown remains active and safety wins. |

If any post-flash hardware test fails, do not ship, do not tag as hardware verified, and report the failure to Justin immediately with logs, checksum evidence, and a short description of the physical setup.

## v1.7.1 Trusted Friend HardwareSteel Build Package

The `v1.7.1-HardwareSteel` tag adds the Trusted Friend rules-first mobile body package under `hardware/trusted_friend/`. Manus should treat this as a hardware handoff for fabrication, simulation, wiring review, and post-flash verification. It is not permission to add live learning, WiFi, OTA updates, cloud dependency, or adaptive policy code to Layer 1.

| Build Area | Repository Path | Required Action |
| --- | --- | --- |
| Parametric chassis and BOM | `hardware/trusted_friend/schematic_generator.py` | Regenerate CAD/BOM in an isolated CAD environment before fabrication. |
| Initial chassis artifact | `hardware/trusted_friend/schematics/trusted_friend_chassis.step` | Use as a handoff envelope and replace with regenerated CadQuery output before manufacturing. |
| Bill of materials | `hardware/trusted_friend/BOM_trusted_friend.csv` | Confirm every listed safety function is present in the physical build. |
| Button+PIN electronics | `hardware/trusted_friend/kicad/README.md` | Implement physical five-second button, parent PIN evidence, smoke/CO interrupt, current sensing, and USB-only flashing. |
| Base reference boundary | `hardware/turtlebot3_base/README.md` | Use TurtleBot3/OpenCR as references only unless a separate license/audit step vendors third-party files. |
| Assembly verification | `hardware/trusted_friend/ASSEMBLY_AND_VERIFICATION.md` | Capture logs, photos, checksums, and videos for every post-flash gate. |

## Release Rule

No Manus integration should be treated as production-ready until the hardware spine, Sanctuary Key, Spine Ledger, L0 guardrails, audit package, and Amendment 24 release gates have all been reviewed. For `v1.7.0c-GrokWelds` and `v1.7.1-HardwareSteel`, the post-flash hardware gates above are mandatory before any hardware-verified tag. If any check fails, the system remains in L0 lockdown.

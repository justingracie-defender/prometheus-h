# Trusted Friend Biped Poppy v1.8 — HardwareSteel Package

> **Weld 1 — Scaling warning:** A Poppy-inspired biped scaled to a five-foot family robot is **not** a simple enlargement of the original Poppy platform. The build must be re-engineered from first principles for mass, torque, structural loads, fall energy, pinch hazards, and child proximity. No actuator may be energized until the torque calculations, fall envelope, force limits, and verification gates in this package have been reviewed and witnessed.

Trusted Friend Biped Poppy v1.8 is a narrow, family-home biped concept for LifeCore-16. It preserves the LifeCore HardwareSteel boundary by keeping immutable safety enforcement in Layer 1 ROM, treating the Raspberry Pi or companion compute as advisory, and preventing learning code from commanding live hardware.

The design goal is a trusted, child-safe, five-foot biped with an Eva-style screen face, compliant hands, low-speed motion, parent-controlled operation, and verification-first release discipline. This package is a hardware handoff and audit folder. It is **not** a fabrication approval, clinical device, child-care substitute, or autonomous childcare release.

## Design Covenant

> **HardwareSteel invariant:** The robot may move only inside the immutable safety envelope. Layer 1 ROM enforces live safety. Layer 2 validates evidence. Layer 3 learning remains offline and cannot mutate live control.

The v1.8 package incorporates four engineering welds. Weld 1 places the scaling warning at the top of the package. Weld 2 adds a hardware fall timer on the ESP32 safety board, with a software target below 250 ms and a hardware cutoff target below 100 ms. Weld 3 hardens the hand design around a 20 N grip ceiling, compliance, slip detection, and finger-safe release behavior. Weld 4 adds the Safety Firewall v1.8 evidence harness and witnessed test record so that the handoff remains auditable before CAD, torque, and ankle verification work begins.

| Weld | Engineering Change | Acceptance Boundary |
| --- | --- | --- |
| Weld 1 | Prominent scaling warning for a five-foot biped. | No first print or powered motion until scaled loads, torque, and fall energy are documented. |
| Weld 2 | ESP32 hardware fall timer and interrupt-driven cutoff path. | Fall detection cuts to limp mode below 250 ms in software and below 100 ms in the hardware cutoff path. |
| Weld 3 | Enhanced safe hands with compliant fingers, slip detection, and 20 N grip ceiling. | Any child-finger shaped obstruction releases below 20 N, logs the event, and prevents re-close until parent reset. |
| Weld 4 | Safety Firewall v1.8 evidence harness and witnessed test record. | Six firewall regression tests pass and are preserved in `test_records/test_firewall_2026-06-09.log`. |

## System Architecture

The biped uses a strict three-layer control model. The companion computer may plan gestures and gait proposals, but every command is filtered before reaching actuators. The ESP32 safety board is the last authority and must reject any command that violates speed, torque, posture, fall, boot-hash, emergency-stop, or Button+PIN rules.

| Layer | Location | Role | Forbidden Capability |
| --- | --- | --- | --- |
| Layer 1 Live Control / ROM | ESP32 safety board | Enforces speed caps, force caps, grip caps, fall timer, Button+PIN, E-stop, boot hash, and permanent limp shutdown. | No WiFi, OTA, adaptive policy, cloud dependency, or runtime learning. |
| Layer 2 Evidence Validation | Raspberry Pi or offline workstation | Logs commands, validates events, exports review artifacts, and runs verification reports. | No direct bypass to motors; cannot override Layer 1. |
| Layer 3 Offline Learning | Offline analysis environment | Studies sanitized logs and proposes future release changes. | Cannot write ROM, mutate live policy, or issue live actuator commands. |

## Physical Envelope

The robot is intentionally constrained to slow, low-force family-home behavior. It must be evaluated first as a static structure, then as a tethered unpowered mechanism, then as a powered test article in a controlled environment, and only later as a family-adjacent prototype.

| Envelope Item | v1.8 Requirement | Verification Gate |
| --- | --- | --- |
| Height | Approximately five feet after full re-engineering. | CAD mass properties and fall simulation are reviewed before fabrication. |
| Locomotion | Bipedal walking only in low-speed, supervised, cleared spaces. | Speed cap test proves motion never exceeds 10 cm/s. |
| Actuator sizing | Upgraded actuators, such as MX-64-class or stronger where calculations require. | Torque spreadsheet shows safety factor of at least 2.0 under scaled mass. |
| Joint design | No exposed pinch points; compliant covers at knees, elbows, ankles, wrists, and fingers. | Physical inspection before power-on. |
| Fall behavior | Passive-safe geometry plus Layer 1 fall interrupt. | Tip test cuts power to limp behavior below required timing limits. |
| Face | Eva-style screen expression module. | Screen is informational only and cannot mask safety state. |

## Enhanced Safe Hands

The hand subsystem is deliberately weaker than the arm structure. It is designed to yield, open, and log rather than grip with adult strength. The hand is suitable only for lightweight interaction, symbolic gestures, and soft-object handling until a dedicated hand V&V cycle is complete.

| Hand Feature | Requirement | Pass Criteria |
| --- | --- | --- |
| Grip force ceiling | Grip force is capped at 20 N at the finger contact surface. | Calibrated force fixture confirms release below 20 N. |
| Compliance | Fingers use compliant pads, flexure, or series-elastic coupling. | Finger-shaped obstruction produces release, not pinch escalation. |
| Slip detection | Tactile or current-slope detection identifies slip without increasing beyond the cap. | Object slip causes controlled release or low-force hold, never force escalation above 20 N. |
| Child-finger protection | The hand opens when a child-finger shaped test probe is detected. | Release occurs below 20 N and event is logged. |
| Reset behavior | A grip fault requires parent reset before re-close. | Automatic re-grip after a pinch event is forbidden. |

## Required Files

| Path | Purpose |
| --- | --- |
| `hardware/trusted_friend_biped_poppy/README.md` | This hardware package overview and build boundary. |
| `hardware/trusted_friend_biped_poppy/safety/invariants.md` | Layer 1 HardwareSteel invariants, including the hardware fall timer weld. |
| `docs/VnV_plan_v18.md` | Verification and validation starter plan for v1.8. |
| `software/pypot_safety_wrapper.py` | Raspberry Pi command wrapper that forwards only bounded commands to ESP32 enforcement. |
| `hardware/trusted_friend_biped_poppy/docs/torque_calculation_starter.md` | Torque calculation starter for scaled Poppy-inspired joints. |
| `hardware/trusted_friend_biped_poppy/docs/assembly_guide.md` | Assembly sequence and power-on hold points. |
| `hardware/trusted_friend_biped_poppy/BOM_trusted_friend_biped_poppy.csv` | Starter bill of materials and audit placeholders. |
| `software/safety_firewall_v18.py` | Layer 2 evidence firewall harness proving v1.8 command rejection and limp-shutdown routing. |
| `tests/test_firewall_v18.py` | Six regression tests covering speed, force, grip, fall, Button+PIN, and boot-hash boundaries. |
| `test_records/test_firewall_2026-06-09.log` | Witnessed firewall test record for the v1.8 handoff. |

## Build Hold Points

No build stage may advance merely because parts are available. Each step must have evidence attached to the release review. If a gate fails, the system remains in hold until the fault is corrected and re-tested.

| Hold Point | Required Evidence | Decision Rule |
| --- | --- | --- |
| CAD freeze | Mass, center of gravity, joint loads, fall envelope, and pinch-zone review. | Do not print if torque safety factor is below 2.0. |
| Bench wiring | ESP32 boot hash, E-stop, Button+PIN, current limit, and sensor fault tests. | Do not attach actuators if Layer 1 enforcement is not proven. |
| Unloaded motion | Joint range, speed cap, torque cap, and limp mode tests. | Do not install limbs if any actuator ignores a safety command. |
| Tethered body | Static load, 10 cm drop, fall timer, and emergency-stop tests. | Do not allow untethered standing until all fall tests pass. |
| Family-adjacent prototype | Child bump, finger probe, supervised E-stop, and parent reset tests. | Do not test near children unless the full V&V plan passes in a controlled setting. |

## External Reference Boundary

The project may use the open-source Poppy humanoid ecosystem, Dynamixel-style servo patterns, and Eva-style screen-face inspiration as external references, but this repository update does not vendor third-party CAD, firmware, schematics, or proprietary assets. Future imports must be separately audited for license, safety, geometry, and supply-chain integrity.[1] [2]

## References

[1]: https://github.com/poppy-project/poppy-humanoid "Poppy Humanoid GitHub repository"
[2]: https://emanual.robotis.com/docs/en/dxl/mx/mx-64-2/ "ROBOTIS MX-64-2 e-Manual"

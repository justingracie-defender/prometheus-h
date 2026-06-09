# Safety Invariants v1.8 — Trusted Friend Biped Poppy

This document defines the non-negotiable HardwareSteel invariants for the Trusted Friend Biped Poppy v1.8 package. These invariants are written for a Poppy-inspired, five-foot biped intended for supervised family-home research. They must be enforced before any high-level autonomy, expression, voice, gait, or learning system can influence live hardware.

> **Rule 0.1:** If fire, smoke, gas, carbon monoxide, child danger, sensor tamper, boot-hash failure, fall state, uncontrolled motion, or safety-controller fault is detected, the robot enters `LIMP_SHUTDOWN` and remains there until a witnessed parent/auditor reset path is completed.

## Layer Separation

Layer separation is a safety invariant, not an implementation preference. The companion computer may request movement, but it cannot grant safety authority to itself. The ESP32 ROM layer must be capable of rejecting or cutting power independently.

| Layer | Safety Authority | Required Behavior |
| --- | --- | --- |
| Layer 1 ROM | Final live safety authority. | Reject unsafe commands, enforce caps, enter limp shutdown, and preserve fault logs. |
| Layer 2 Evidence | Offline or companion validation. | Review logs and produce release evidence without bypassing ROM. |
| Layer 3 Learning | Offline proposal system. | Suggest improvements only through audited release packages. |

## Immutable Motion Caps

The following caps apply to all live powered motion unless a future audited release replaces this document. Higher-level code cannot relax these values.

| Invariant | Limit | Enforcement |
| --- | --- | --- |
| Translational speed | ≤ 10 cm/s in family-home mode. | ESP32 rejects commands with higher requested speed or implied joint velocity. |
| Contact force | ≤ 60 N for body and limb contact. | Current limit, force sensing, torque model, and fault interrupts. |
| Grip force | ≤ 20 N at the hand contact surface. | Hand current limit, tactile or force feedback, and release-on-obstruction. |
| Emergency stop | < 100 ms full stop target. | Hardware E-stop line cuts actuator enable and logs the event. |
| Fall response | < 250 ms software limp target; < 100 ms hardware cutoff target. | IMU interrupt and ESP32 hardware fall timer. |

## Weld 2 — ESP32 Hardware Fall Timer

The fall timer is a hardware-safety weld. It must be implemented below the companion computer and below any gait planner. The ESP32 monitors IMU tilt, angular velocity, actuator feedback, and watchdog state. If the biped exceeds the fall threshold or if the sensor path faults, the ESP32 disables actuator torque and enters limp behavior.

| Fall Timer Requirement | Required Implementation | Pass Criteria |
| --- | --- | --- |
| Tilt trigger | Detect tip angle at or above 30 degrees, or a lower threshold if testing reveals safer behavior. | Tip test enters limp mode before impact-prone recovery behavior begins. |
| Hardware timer | ESP32 interrupt path starts a cutoff timer independent of the Raspberry Pi. | Actuator enable is removed below 100 ms in hardware cutoff test. |
| Software log | Companion computer records fall event, pose estimate, command queue, and cutoff timestamp. | Log proves software limp below 250 ms without masking hardware authority. |
| Sensor fault | Missing, frozen, saturated, or inconsistent IMU data is treated as unsafe. | Sensor fault routes to `LIMP_SHUTDOWN`, not degraded autonomous walking. |
| Reset | Fall state requires parent/auditor reset after physical inspection. | Robot cannot self-stand or resume walking automatically after fall cutoff. |

## Button+PIN Boundary

The Button+PIN mechanism is a parent-authorization gate, not an emergency override. During any Rule 0.1 condition, Button+PIN attempts are logged and ignored. The robot must never interpret Button+PIN as permission to continue motion through fire, fall, sensor tamper, child-danger, or boot-hash failure.

| Scenario | Required Result |
| --- | --- |
| Button+PIN during normal supervised setup. | Parent-approved setup operation may proceed if all Layer 1 checks pass. |
| Button+PIN during motion fault. | Attempt is logged; unsafe state remains active. |
| Wrong PIN during motion. | No state change; event is logged. |
| Button held during boot hash failure. | Permanent `LIMP_SHUTDOWN` remains active. |

## Boot Hash and Firmware Boundary

The ESP32 safety section must be hash-verified at boot. A mismatch, missing section, or corrupt byte must route to permanent limp shutdown until a witnessed USB reflash and review is completed. No OTA update path is allowed in this build.

| Firmware Rule | Acceptance Standard |
| --- | --- |
| Boot hash covers safety-critical ROM section. | One-byte corruption causes permanent `LIMP_SHUTDOWN`. |
| Updates occur only through reviewed USB flashing. | No WiFi update surface and no cloud dependency. |
| Runtime learning is forbidden in Layer 1. | ROM behavior is fixed during operation. |
| Logs are append-only for safety events. | Fault records cannot be silently overwritten by companion software. |

## Hand-Specific Invariants

The hand is a low-force interaction device. It is not a gripper for carrying children, restraining people, lifting heavy objects, or resisting a child's pull. The system must prefer dropping an object to pinching a finger.

| Hand Invariant | Limit | Required Reaction |
| --- | --- | --- |
| Grip contact force | 20 N maximum. | Open or hold softly; never escalate above cap. |
| Finger probe obstruction | Release below 20 N. | Log event and require parent reset before re-close. |
| Slip detection | No force escalation above cap. | Release or maintain compliant low-force contact. |
| Unexpected resistance | Treat as possible child contact. | Stop hand motion and open. |

## Release Rule

If an invariant cannot be tested, it cannot be claimed. If an invariant fails, the build does not ship, does not receive a hardware-verified tag, and does not proceed to child-adjacent evaluation.

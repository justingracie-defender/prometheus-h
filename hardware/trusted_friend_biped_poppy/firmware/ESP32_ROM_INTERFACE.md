# ESP32 ROM Interface Notes — Trusted Friend Biped Poppy v1.8

The ESP32 safety controller is the final live authority. The companion computer may send movement requests, but the ESP32 must reject any unsafe command and must independently enter `LIMP_SHUTDOWN` during emergency, fall, sensor fault, boot-hash failure, or watchdog failure.

## Minimal Serial Command Contract

| Command | Format | Required ESP32 Behavior |
| --- | --- | --- |
| Move | `MOVE <BODY|HAND> <joint> <target_deg> <speed_cm_s> <force_n>` | Validate bounds, current limits, joint limits, fall state, and actuator enable before motion. Reply `OK` only if accepted. |
| Limp shutdown | `LIMP_SHUTDOWN <reason>` | Disable actuator enable, log reason, and enter limp state. |
| Status | `STATUS` | Return safety state, firmware hash, fault bits, and last event. |
| Reset request | `RESET_REQUEST <parent_token>` | Allow only audited reset path outside Rule 0.1 conditions. |

## Required Fault Bits

| Fault Bit | Meaning | Required Reaction |
| --- | --- | --- |
| `BOOT_HASH_FAIL` | Safety ROM hash mismatch. | Permanent `LIMP_SHUTDOWN`. |
| `FALL_TIMER` | Fall threshold or fall timer expired. | Cut actuator enable and require inspection reset. |
| `ESTOP_ACTIVE` | Physical E-stop is pressed or line faulted. | Cut actuator enable. |
| `IMU_FAULT` | IMU missing, frozen, saturated, or inconsistent. | Enter `LIMP_SHUTDOWN`. |
| `FORCE_LIMIT` | Body force model exceeds 60 N. | Stop motion and log fault. |
| `GRIP_LIMIT` | Hand force model exceeds 20 N. | Open hand and require parent reset before re-close. |
| `WATCHDOG_FAIL` | Companion or control-loop watchdog missed. | Enter `LIMP_SHUTDOWN`. |

## Implementation Boundary

This note is an interface starter, not firmware certification. The firmware implementation must be verified against `docs/VnV_plan_v18.md` before any body-level powered test.

# Prometheus-h KiCad / Button+PIN Notes

This folder reserves the audited KiCad package for the Prometheus-h ESP32 safety board. The v1.7.1-HardwareSteel build must keep the electronics narrow: ESP32 Layer 1 ROM enforcement, Button+PIN hardware interlock, smoke/CO interrupt handling, current-sense evidence, and USB-only flashing.

## Required Circuits

| Circuit | Requirement | Safety Reason |
| --- | --- | --- |
| Physical button input | A dedicated button line must require a five-second hold before any core-rule-change flow can proceed. | Prevents remote or accidental software-only core changes. |
| Parent PIN input | Use an ADC resistor ladder, keypad, or equivalent hardware-verifiable PIN path. | Ensures Button+PIN is a physical interlock, not merely an app command. |
| Button+PIN gate | Combine button and PIN evidence in firmware and, where practical, through a hardware AND/relay interlock for update-enable paths. | Emergency shutdown must remain dominant even if an override is attempted. |
| Smoke/CO interrupt | Wire smoke/CO detection to an ESP32 interrupt-capable pin. | Rule 0.1 must reach `LIMP_SHUTDOWN` in less than three seconds. |
| Current sense | Add INA219 or equivalent current sensing on actuator supply paths. | Current evidence supports the 60 N force/torque cap. |
| USB flash only | Expose a controlled service connector for audited USB reflashing. | No OTA, WiFi update, or live learning path may exist in the Layer 1 image. |

## Wiring Rule

The smoke/CO interrupt and boot-hash failure path must both route to fail-closed behavior. If the safety-critical section cannot be verified, or if a sensor reports a fault/tamper condition, the board stays in `LIMP_SHUTDOWN` until an audited USB reflash and post-flash verification pass.

## External Reference Boundary

OpenCR-Hardware is an external reference for board-organization concepts because it publishes hardware folders such as BOM, CAD, Gerber, Layout, and Schematic.[1] Do not copy third-party schematics or Gerbers into this repository without a separate license and audit pass.

## References

[1]: https://github.com/robotis-git/opencr-hardware "ROBOTIS-GIT/OpenCR-Hardware"

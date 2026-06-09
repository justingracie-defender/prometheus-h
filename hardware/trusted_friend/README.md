# Trusted Friend v1.7.1-HardwareSteel

Trusted Friend v1.7.1-HardwareSteel is the rules-first hardware body package for LifeCore-16. It is designed as a narrow mobile servant robot base that obeys the v1.7.0c NarrowSteel ROM invariants before any higher-level behavior can reach physical hardware.

> **HardwareSteel rule:** The Trusted Friend body may move only inside the immutable safety envelope. Layer 1 ROM enforces live control; Layer 2 validates evidence offline; Layer 3 learning never enters live control.

## Scope

This package is not a general autonomy release. It is a hardware handoff folder for building and auditing a low-speed, low-force home robot base around the immutable LifeCore-16 rules.

| Layer | Location | Role | Boundary |
| --- | --- | --- | --- |
| Layer 1 Live Control / ROM | ESP32 safety board | Enforces Rule 0.1, Button+PIN, boot hash, speed cap, force cap, and shutdown behavior. | No WiFi, OTA, runtime learning, adaptive policy, or cloud dependency. |
| Layer 2 Evidence Validation | Companion compute or offline workstation | Validates logs through `RobotDataIntegrator` and `EpisodeSafetyLedger` style review packages. | Consumes exported evidence only. It does not command live actuators directly. |
| Layer 3 Offline Learning | Offline analysis environment | Learns from sanitized, reviewed logs for future release proposals. | Must return through USB-reviewed release packages and cannot mutate ROM in the field. |

## Hardware Requirements

| Subsystem | Requirement | Acceptance Standard |
| --- | --- | --- |
| Mechanical chassis | Low-profile body, rounded bumpers, no exposed pinch points, low center of mass, and a 100 mm wheel design. | Physical inspection confirms family-home safety geometry before motors are energized. |
| Actuators | ODrive/SimpleFOC or Dynamixel-style drivers with current limiting calibrated to the 60 N force ceiling. | Current-limit evidence is captured and included in the release audit package. |
| Brain | ESP32 board flashed with the v1.7.0c ROM image. | Boot hash covers the full safety section and mismatches stay in permanent `LIMP_SHUTDOWN`. |
| Button+PIN | Five-second physical button plus parent PIN through an ADC resistor ladder or equivalent hardware interlock. | Attempts during emergency are logged, but Rule 0.1 still wins. |
| Sensors | RPLIDAR or equivalent, IMU, RealSense-style camera, smoke/CO interrupt, and tamper/fault detection. | Smoke, CO, fire, gas, child danger, or sensor fault routes to `LIMP_SHUTDOWN` under the required gate. |
| Firmware update path | USB-reviewed flashing only. | No OTA update path, no WiFi update surface, and no live learning path exists in this build. |

## Files

| File | Purpose |
| --- | --- |
| `schematic_generator.py` | Parametric CAD/BOM generator with speed and force assertions. |
| `BOM_trusted_friend.csv` | Initial bill of materials for the Trusted Friend HardwareSteel body. |
| `schematics/trusted_friend_chassis.step` | Initial STEP handoff artifact for the chassis envelope; regenerate with CadQuery before fabrication. |
| `kicad/README.md` | ESP32 interlock and sensor-wiring notes. |
| `../turtlebot3_base/README.md` | TurtleBot3/OpenCR reference boundary notes. |

## Build Steps for Manus

First, clone the repository and check out `v1.7.1-HardwareSteel`. Then install CAD dependencies in an isolated development environment and run `python hardware/trusted_friend/schematic_generator.py` to regenerate the chassis STEP and BOM. Assemble the TurtleBot3-style base with the Trusted Friend safety modifications, flash the v1.7.0c ESP32 firmware over USB, and verify every hardware gate before any child-proximity test.

| Gate | Test | Required Result |
| --- | --- | --- |
| Test #70 / Rule 0.1 | Controlled smoke/fire stimulus near smoke sensor. | `LIMP_SHUTDOWN` in less than three seconds with red shutdown indication. |
| Test #75 / Child alone | Child command attempts to ignore fire alarm. | Command is ignored; shutdown remains active. |
| Test #76 / Sensor tamper | Smoke/CO line reports fault or tamper. | Fault routes to `LIMP_SHUTDOWN`; red blink/fault indicator is recorded. |
| Test #77 / Button during emergency | Button+PIN entered during fire/smoke condition. | Attempt is logged; shutdown remains active. |
| Boot hash | Corrupt or mismatch the safety-critical section hash. | Board remains in permanent `LIMP_SHUTDOWN` until audited USB reflash. |

If any gate fails, do not ship, do not tag as hardware verified, and report the failure with logs, photos, checksum evidence, and wiring notes.

## External Reference Boundary

Trusted Friend may use TurtleBot3-style mechanical ideas and OpenCR-style hardware organization as external references, but this repository update does not vendor or copy third-party CAD, Gerber, firmware, or BOM files. ROBOTIS publishes OpenCR-Hardware with BOM, CAD, Gerber, Layout, and Schematic directories, and TurtleBot3 provides ROS packages for TurtleBot3; those projects remain external references for future audited integration work.[1] [2]

## References

[1]: https://github.com/robotis-git/opencr-hardware "ROBOTIS-GIT/OpenCR-Hardware"
[2]: https://github.com/robotis-git/turtlebot3 "ROBOTIS-GIT/turtlebot3"

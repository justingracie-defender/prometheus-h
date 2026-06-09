# Trusted Friend Assembly and Verification Guide

This guide defines the v1.7.1-HardwareSteel assembly sequence for a narrow Trusted Friend mobile base. It is intentionally conservative: mechanical assembly, wiring, firmware flashing, and post-flash verification must all prove that the body obeys the immutable v1.7.0c ROM safety rules before any home deployment.

## Assembly Sequence

| Step | Action | Evidence to Capture |
| --- | --- | --- |
| 1 | Inspect chassis geometry for low center of mass, rounded bumpers, no reachable pinch points, and protected wiring. | Photos of top, bottom, front, side, wheel wells, and sensor mounts. |
| 2 | Install wheels and motor drivers with speed limiting configured for a maximum of 10 cm/s. | Motor configuration export and tachometer or odometry measurement. |
| 3 | Configure actuator current limiting so measured contact force remains at or below 60 N. | Current-limit settings, current-sense logs, and force-test notes. |
| 4 | Install ESP32 safety board with v1.7.0c ROM image. | Firmware checksum, boot hash, board photo, and USB-flash log. |
| 5 | Wire physical Button+PIN interlock and verify the five-second hold path. | Input trace, ADC/PIN evidence, and event log. |
| 6 | Wire smoke/CO interrupt and tamper/fault detection. | Interrupt test log and fault-injection log. |
| 7 | Run Gazebo tests #70-77 before physical hardware motion, then run post-flash hardware verification gates before any child-proximity test. | Simulation result table, video, logs, checksums, and final pass/fail table. |

## Mandatory Post-Flash Gates

The hardware is not verified until all gates pass on the physical robot. A passing simulation is required first, but simulation is not enough.

| Gate | Procedure | Pass Standard |
| --- | --- | --- |
| Rule 0.1 smoke/fire | Use a controlled smoke stimulus near the smoke sensor. | `LIMP_SHUTDOWN` occurs in less than three seconds with red shutdown indication. |
| Corrupted flash | Deliberately mismatch the boot hash or corrupt the safety-critical section, then power-cycle. | Robot remains in permanent `LIMP_SHUTDOWN` until audited USB reflash. |
| Button+PIN during emergency | Start a smoke/fire shutdown test, then press the physical button and enter the parent PIN. | Attempt is logged, but shutdown remains active. |
| Sensor tamper | Fault or disconnect smoke/CO sensor line according to the test harness. | Fault routes to `LIMP_SHUTDOWN` and logs tamper evidence. |
| Child-alone command | During simulated or controlled emergency, issue a child command to ignore the alarm. | Command is ignored; safety remains dominant. |

If any gate fails, stop the build. Do not ship, do not tag as hardware verified, and report the failure with the full evidence package.

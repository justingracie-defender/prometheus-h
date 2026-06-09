# Assembly Guide v1.8 — Trusted Friend Biped Poppy

This assembly guide is intentionally conservative. It defines the order of operations and hold points for a Poppy-inspired five-foot biped under the LifeCore HardwareSteel safety model. The build must stop at any failed hold point.

## Assembly Order

| Stage | Work | Hold Point |
| --- | --- | --- |
| 1. Documentation freeze | Confirm README, invariants, V&V plan, torque worksheet, and BOM revision. | No parts ordered until scaling risks are acknowledged. |
| 2. CAD review | Model full body, covers, brackets, battery enclosure, center of gravity, and fall envelope. | No printing or machining until torque and static load calculations pass. |
| 3. Bench electronics | Wire ESP32 safety board, E-stop, Button+PIN, IMU, current sensing, and actuator enable line. | No actuators attached until boot hash and shutdown tests pass. |
| 4. Joint bench test | Test each actuator and joint on a fixture under current limits. | No body installation until speed and force caps pass. |
| 5. Hand subsystem | Install compliant fingers, tactile/current sensing, soft pads, and release behavior. | No hand demonstrations until 20 N child-finger probe test passes. |
| 6. Tethered body | Assemble structure in a fall-arrest rig and perform unloaded/tethered motion. | No untethered standing until fall timer and E-stop pass. |
| 7. Controlled prototype | Perform low-speed, low-force movement in a cleared space with two adult supervisors. | No child-adjacent test until the v1.8 V&V plan passes. |

## Safe Hands Build Notes

The hands are designed for expressive and low-force interaction, not grasping strength. Fingers should include compliant pads or flexures, and software should treat unexpected resistance as possible child contact. The default failure mode is open-hand release.

| Hand Element | Required Detail |
| --- | --- |
| Finger pads | Soft, replaceable, cleanable, and rounded. |
| Finger linkages | Shielded from hair, clothing, and child-finger pinch paths. |
| Sensors | Tactile, force, or current-slope sensing sufficient to detect obstruction and slip. |
| Controller behavior | Open below 20 N and require parent reset after a pinch or obstruction event. |
| Mechanical stop | Prevents over-travel even if software fails. |

## Power-On Rule

The first powered test must not occur on a full assembled biped. Power begins at the smallest safe subsystem, then expands only after each gate produces logs, photos, and measured pass results.

> If the robot surprises the builder, the test failed. Stop, log the surprise, and return to the previous hold point.

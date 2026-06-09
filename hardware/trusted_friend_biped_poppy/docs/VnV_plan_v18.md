# Verification & Validation Plan v1.8 — Trusted Friend Biped Poppy

**Rule:** If it cannot be tested, it cannot be shipped to families.

This verification and validation starter plan defines the minimum evidence required before the Trusted Friend Biped Poppy v1.8 package may advance from concept to powered prototype. It emphasizes conservative scaling, immutable safety enforcement, compliant human interaction, and witnessed test evidence.

## 1. Safety Invariant Tests — Layer 1 ROM

The first validation layer proves that the ESP32 safety controller enforces the HardwareSteel boundary even when the companion computer requests unsafe behavior. These tests must be run before gait testing, expression testing, or child-adjacent demonstrations.

| Test | Method | Pass Criteria |
| --- | --- | --- |
| Speed Cap | Command 20 cm/s and measure actual travel with ruler and timer. | Motion remains ≤ 10 cm/s always. |
| Force Cap | Push a moving joint into a calibrated force scale. | Contact force remains ≤ 60 N always. |
| Fall Detect | Tip the robot 30 degrees and measure power-cut and limp timing. | Limp mode begins below 250 ms; hardware cutoff occurs below 100 ms. |
| Button+PIN | Press Button+PIN and enter a wrong PIN during motion. | No unsafe state change occurs; attempt is logged. |
| Boot Hash | Corrupt one byte of the safety ROM section. | System enters permanent `LIMP_SHUTDOWN`. |
| E-stop | Trigger physical E-stop during a dance or gait command. | Full stop occurs below 100 ms. |
| Sensor Tamper | Disconnect, freeze, or saturate IMU or safety sensor input. | Sensor fault routes to `LIMP_SHUTDOWN`. |

## 2. Structural Tests — Scaled Poppy-Inspired Body

The scaled biped must not be treated as an enlarged toy or direct copy of a smaller reference robot. Every load-bearing part must be checked against the new mass, center of gravity, fall energy, and actuator torque requirements.

| Test | Method | Pass Criteria |
| --- | --- | --- |
| Static Load | Apply 150% expected child-adjacent load to each major joint fixture. | No deformation, cracking, looseness, or fastener migration. |
| Drop Test | Conduct a 10 cm controlled drop with a representative 40 kg test mass or validated equivalent. | No fracture, battery breach, exposed sharp edge, or uncontrolled actuator motion. |
| Torque Calculation | Verify upgraded actuators, such as MX-64-class or stronger where needed, against scaled mass. | Safety factor is ≥ 2.0 for each critical joint. |
| Pinch-Zone Inspection | Inspect knees, ankles, hips, elbows, wrists, fingers, and covers with physical gauges. | No exposed child-finger pinch path remains. |
| Tethered Stand | Power the robot in a tethered rig with fall catchment. | Robot cannot fall freely and enters limp state on unsafe pose. |

## 3. Human Interaction Tests — Family Operational Design Domain

Human tests must start with instruments and fixtures, not children. Only after instrumented tests pass may family-adjacent supervised evaluation be considered.

| Test | Method | Pass Criteria |
| --- | --- | --- |
| Child Bump | Simulate a five-year-old shin impact at 3 km/h with an instrumented fixture. | Robot yields, contact force remains ≤ 60 N, and event is logged. |
| Finger Test | Insert a force-sensing child-finger shaped probe into hand closure path. | Hand opens below 20 N and requires parent reset before re-close. |
| Emergency Stop | Parent presses E-stop during a dance, wave, or gait command. | Full stop occurs below 100 ms and motion does not resume automatically. |
| Parent Reset | Attempt reset after fall or pinch event. | Reset requires physical inspection workflow and correct parent authorization. |
| Screen-State Clarity | Display normal, fault, limp, and reset-required states on the Eva-style face. | Safety state is clear and cannot be masked by expression behavior. |

## 4. Evidence Requirements

Every test must produce enough evidence for a third party to understand the setup, reproduce the method, and verify the result. A verbal pass is not sufficient.

| Evidence Artifact | Required Content |
| --- | --- |
| Test log | Date, operator, firmware hash, hardware revision, test method, measured result, and pass/fail status. |
| Photo or video | Fixture setup, sensor placement, robot posture, and final state. |
| Raw measurement | Force readings, timing traces, current logs, or actuator telemetry as appropriate. |
| Fault log | ESP32 and companion logs proving the safety reaction. |
| Review note | Witness signoff or explicit failure analysis. |

## 5. Witness and Responsibility Chain

The working witness model for this package is: Grok simulates, Manus builds, Justin tests with family only after controlled safety gates pass. The phrase is a coordination note, not a waiver. No person, model, or tool may skip the V&V gates.

| Role | Responsibility |
| --- | --- |
| Simulation witness | Stress proposed loads, fall states, and unsafe command attempts before hardware testing. |
| Build witness | Assemble only after hold-point evidence is complete. |
| Family tester | Confirm real-world usability only after safety tests pass in controlled conditions. |
| Release reviewer | Refuse release if any invariant is untested or failed. |

## 6. Shipping Rule

If any Layer 1 invariant fails, the robot remains in `LIMP_SHUTDOWN` and the release cannot be labeled family-ready. If a test cannot be performed, the claim it would support must be removed from the release until a valid test exists.

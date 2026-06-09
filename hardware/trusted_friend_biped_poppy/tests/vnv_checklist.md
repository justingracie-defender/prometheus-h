# V&V Checklist — Trusted Friend Biped Poppy v1.8

This checklist is a working record for the tests defined in `docs/VnV_plan_v18.md`. A checkbox may be marked only when measured evidence exists and is attached to the release review.

| Gate | Test | Evidence Required | Status |
| --- | --- | --- | --- |
| Layer 1 | Speed cap ≤ 10 cm/s. | Video, ruler/timer measurement, ESP32 log. | Hold |
| Layer 1 | Body contact force ≤ 60 N. | Force-scale reading and current-limit log. | Hold |
| Layer 1 | Fall limp below 250 ms and hardware cutoff below 100 ms. | Timing trace, IMU log, actuator-enable trace. | Hold |
| Layer 1 | Boot hash corruption routes to permanent limp shutdown. | Firmware hash, corruption method, boot log. | Hold |
| Layer 1 | E-stop full stop below 100 ms. | Timing trace and actuator-enable trace. | Hold |
| Structure | Static load test at 150% expected load. | Fixture photos and deformation inspection. | Hold |
| Structure | 10 cm drop test with representative mass. | Video, post-test inspection, fault log. | Hold |
| Structure | Torque worksheet safety factor ≥ 2.0. | Completed calculation sheet and reviewer signoff. | Hold |
| Hands | Finger probe release below 20 N. | Force trace, video, hand fault log. | Hold |
| Human ODD | Child-bump fixture yields below 60 N. | Instrumented fixture data and log. | Hold |

If any row remains in `Hold`, the package cannot be labeled family-ready.

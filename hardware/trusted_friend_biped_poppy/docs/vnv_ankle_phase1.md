# Phase 1 Ankle V&V — Trusted Friend Biped Poppy v1.8

**Status:** Hold point, not fabrication approval.  
**Branch:** `hardware/trusted_friend_biped_poppy`  
**Rule:** No knee, hip, untethered gait, or child-adjacent test may proceed until the ankle gate has witnessed evidence.

## 1. Purpose

Phase 1 exists to prevent the biped project from printing or energizing a leg structure around an under-sized ankle. The ankle is the first load-bearing gate because it carries whole-body balance moments, fall loads, cable routing, and foot-ground reaction forces. The Phase 1 decision is therefore conservative: choose a datasheet-backed actuator envelope, build only the ankle/foot fixture, and verify static load, controlled torque, safe limp behavior, and non-hazardous failure before any knee or hip fabrication.

> **Hold point:** The actuator package must demonstrate at least **110 N·m output capability by datasheet before printing**, then prove the actual ankle fixture by static and powered tests. Peak torque alone is not a continuous-duty safety claim.

## 2. Non-Negotiable Safety Boundaries

The ankle fixture remains inside the v1.8 HardwareSteel envelope. The actuator may be stronger than the family-mode force limit, but live control must still be limited by the ESP32 safety layer, current limits, mechanical stops, tethering, and external test fixtures.

| Boundary | Required Rule | Pass Standard |
| --- | --- | --- |
| No knee/hip progression | Ankle Phase 1 must pass first. | No knee or hip printing, energizing, or procurement beyond planning until the ankle report is witnessed. |
| Human proximity | Instrumented fixtures only. | No child-adjacent or family-home testing during Phase 1. |
| Torque evidence | Datasheet required before print. | Candidate actuator has documented torque, voltage, mass, dimensions, and control interface. |
| Live motion | Tethered, slow, current-limited bench operation only. | Motion remains inside the v1.8 10 cm/s and 60 N family-mode envelope when installed in robot context. |
| Failure mode | Fail limp, not rigid or ballistic. | Sensor fault, command fault, overcurrent, or E-stop causes torque disable or mechanically safe stop. |

## 3. Datasheet-Backed Actuator Shortlist

The shortlist below is based on official manufacturer data reviewed for Phase 1. ROBOTIS states that listed stall torque is a momentary maximum and that real-world performance is generally closer to performance-graph measurements, so stall torque must not be treated as continuous support capacity.[1] [2] The CubeMars AK80-64 and AKH70-48 pages publish rated and peak torque, dimensions, weight, reduction ratio, and operating characteristics directly on the product pages.[3] [4]

| Rank | Candidate | Datasheet Torque | Mass / Envelope | Phase 1 Decision |
| ---: | --- | --- | --- | --- |
| 1 | **CubeMars AKH70-48 V1.0 KV41** | 74 N·m rated; 222 N·m peak; 48:1 reduction.[4] | 1396 g; Ø90 × 81.5 mm; 7 mm hollow bore; dual 21-bit encoders.[4] | **Primary CAD envelope candidate.** Peak torque clears 110 N·m with margin, rated torque does not; must pass thermal/static tests before any body integration. |
| 2 | **CubeMars AK80-64 KV80** | 48 N·m rated; 120 N·m peak; 64:1 reduction.[3] | 850 g; Ø98 × 61.9 mm; integrated driver and encoder.[3] | **Lightweight fallback.** Clears 110 N·m only on peak torque, so it is acceptable for CAD comparison but not accepted as final without derating tests. |
| 3 | **ROBOTIS H54-200-S500-R plus external reduction** | 44.7 N·m continuous at actuator output; 200 W output.[5] With 3:1 external reduction, ideal output is 134.1 N·m before efficiency losses. | 855 g actuator before gearbox; 54 × 126 × 54 mm; 24 V; RS-485.[5] | **ROBOTIS-family alternative.** Requires gearbox efficiency, backlash, bracket load, speed, and thermal evidence. |
| 4 | **ROBOTIS MX-64 / XM430 class** | MX-64 stall torque 6.0 N·m at 12 V; XM430-W350 stall torque 4.1 N·m at 12 V.[1] [2] | Compact smart servos. | **Reject for primary ankle support.** May be used only for unloaded mockups, sensors, or non-load-bearing auxiliaries unless a separate transmission is fully validated. |

## 4. Torque Worksheet for 18–22 kg Shuffle-Gait Robot

The initial worksheet uses the repository formula `T_required = m × g × r × k_dyn × SF`, with `g = 9.81 m/s²`, a conservative shuffle-gait dynamic multiplier of `1.25`, and a required safety factor of `2.0`. This is not a complete gait model; it is a first gate that blocks weak actuator choices before CAD or printing.

| Robot Mass | Ankle-to-COM Offset | Static Torque | Required Design Torque | Gate Result |
| ---: | ---: | ---: | ---: | --- |
| 18 kg | 0.15 m | 26.5 N·m | 66.2 N·m | Below 110 N·m threshold, but still fixture-tested. |
| 18 kg | 0.20 m | 35.3 N·m | 88.3 N·m | Below 110 N·m threshold, but still fixture-tested. |
| 18 kg | 0.25 m | 44.1 N·m | 110.4 N·m | Meets Phase 1 threshold. |
| 20 kg | 0.15 m | 29.4 N·m | 73.6 N·m | Below 110 N·m threshold, but still fixture-tested. |
| 20 kg | 0.20 m | 39.2 N·m | 98.1 N·m | Below 110 N·m threshold, but still fixture-tested. |
| 20 kg | 0.25 m | 49.1 N·m | 122.6 N·m | Meets Phase 1 threshold. |
| 22 kg | 0.15 m | 32.4 N·m | 80.9 N·m | Below 110 N·m threshold, but still fixture-tested. |
| 22 kg | 0.20 m | 43.2 N·m | 107.9 N·m | Borderline; treat as 110 N·m class. |
| 22 kg | 0.25 m | 54.0 N·m | 134.9 N·m | Meets Phase 1 threshold with higher margin requirement. |

The generated spreadsheet artifacts are stored at `hardware/trusted_friend_biped_poppy/docs/ankle_torque_phase1.csv` and `hardware/trusted_friend_biped_poppy/docs/ankle_torque_phase1.xlsx`.

## 5. Phase 1 Test Checklist

Every test requires a date, operator, fixture photo or video, raw measurement, and pass/fail note. A verbal pass is not evidence.

| Test | Method | Required Evidence | Pass Criteria |
| --- | --- | --- | --- |
| Datasheet gate | Attach or link manufacturer datasheet/product page for selected actuator. | URL, downloaded PDF/STEP if available, torque table, voltage/current limits, thermal limits. | Actuator candidate has ≥110 N·m output capability by published data, with continuous vs peak clearly labeled. |
| CAD envelope gate | Model actuator, ankle bracket, foot plate, hard stops, wiring route, and fastener access. | CAD file, drawing, mass properties, interference screenshot. | No cable crush, no child-finger pinch path, actuator serviceable without unsafe disassembly. |
| Static load | Mount ankle fixture and apply 150% expected static moment. | Load rig photo, applied mass/lever arm, deflection reading. | No crack, slip, fastener migration, sharp edge, or permanent deformation. |
| Torque hold | Command low-speed hold against calibrated lever arm/load cell. | Current log, output angle log, load-cell or torque reading. | Holds target load without thermal runaway; current limit routes fault to limp if exceeded. |
| Shuffle cycle | Run slow repeated ± ankle pitch cycles under tethered load. | Cycle count, temperature log, current log, video. | No uncontrolled motion, no overshoot beyond mechanical stops, no wiring rub-through. |
| Return-to-zero creep | Hold loaded ankle, disable command, and monitor drift. | Angle/time trace. | Drift remains bounded; loss of control falls to safe mechanical stop or limp. |
| E-stop and sensor fault | Trigger E-stop, unplug/freeze sensor, and inject command fault. | Timing trace, ESP32/companion log. | Torque disable or safe stop occurs within v1.8 limits; no automatic resume. |
| Destructive sacrificial coupon | Test printed bracket coupon or sacrificial fixture section to failure away from people. | Failure photo, load at failure, sharp-edge inspection. | Failure is non-hazardous: no shrapnel, no exposed blade edge, no battery/actuator breach. |

## 6. Recommended Selection

The recommended Phase 1 path is to design the first ankle CAD envelope around the **CubeMars AKH70-48 V1.0 KV41** because it has the strongest documented margin against the 110 N·m gate and provides a hollow shaft plus dual encoders that simplify ankle cable routing and output feedback.[4] The **CubeMars AK80-64 KV80** should remain as the lighter fallback when mass is more important than peak margin.[3] The **ROBOTIS H54-200-S500-R plus external reduction** remains viable only if the added gearbox can be validated for backlash, efficiency, bracket load, and fail-safe behavior.[5]

The **MX-64/XM430 class should not be selected as the primary ankle actuator** for an 18–22 kg five-foot biped. Their published torque ratings are one to two orders of magnitude below the Phase 1 ankle gate and ROBOTIS explicitly cautions that stall torque is a momentary value rather than expected real-world continuous performance.[1] [2]

## 7. References

[1]: https://emanual.robotis.com/docs/en/dxl/mx/mx-64/ "ROBOTIS e-Manual — DYNAMIXEL MX-64"
[2]: https://emanual.robotis.com/docs/en/dxl/x/xm430-w350/ "ROBOTIS e-Manual — DYNAMIXEL XM430-W350"
[3]: https://www.cubemars.com/product/ak80-64-kv80-robotic-actuator.html "CubeMars — AK80-64 KV80 Robotic Actuator"
[4]: https://www.cubemars.com/product/akh70-48-v-1-0-kv41-hollow-shaft-planetary-actuator.html "CubeMars — AKH70-48 V1.0 KV41 Hollow Shaft Planetary Actuator"
[5]: https://emanual.robotis.com/docs/en/dxl/pro/h54-200-s500-r/ "ROBOTIS e-Manual — DYNAMIXEL H54-200-S500-R"

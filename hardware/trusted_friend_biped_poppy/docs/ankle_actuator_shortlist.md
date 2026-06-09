# Ankle Actuator Shortlist — Trusted Friend Biped Poppy v1.8

**Decision status:** Phase 1 engineering shortlist only. This document does not authorize printing, powered standing, knee fabrication, hip fabrication, or child-adjacent testing.

## Recommendation Summary

The first ankle CAD envelope should be built around the **CubeMars AKH70-48 V1.0 KV41**. It is the strongest datasheet-backed candidate reviewed in this pass because its published **222 N·m peak torque** exceeds the 110 N·m Phase 1 gate with the largest margin, while its hollow shaft and dual encoders are useful for ankle cable routing and output feedback.[1] However, its **74 N·m rated torque** is below the 110 N·m gate, so the design must not treat the peak figure as continuous support. The fixture must prove static hold, thermal behavior, creep, E-stop timing, and non-hazardous failure before any leg build proceeds.

| Rank | Candidate | Datasheet Link | Published Torque | Why It Is On The List | Decision |
| ---: | --- | --- | --- | --- | --- |
| 1 | CubeMars AKH70-48 V1.0 KV41 | https://www.cubemars.com/product/akh70-48-v-1-0-kv41-hollow-shaft-planetary-actuator.html | 74 N·m rated; 222 N·m peak.[1] | Best margin above 110 N·m peak gate; hollow shaft; dual 21-bit encoders; high load ratings. | **Preferred Phase 1 CAD envelope.** |
| 2 | CubeMars AK80-64 KV80 | https://www.cubemars.com/product/ak80-64-kv80-robotic-actuator.html | 48 N·m rated; 120 N·m peak.[2] | Lighter than AKH70-48 and barely clears the 110 N·m peak gate. | **Fallback only if mass wins and tests pass.** |
| 3 | ROBOTIS H54-200-S500-R plus external 3:1 reduction | https://emanual.robotis.com/docs/en/dxl/pro/h54-200-s500-r/ | 44.7 N·m continuous before reduction; 134.1 N·m ideal at 3:1 before efficiency losses.[3] | ROBOTIS-family alternative with industrial continuous torque, but requires external reduction validation. | **Alternative; gearbox risk must be retired.** |
| 4 | ROBOTIS MX-64 / XM430 class | https://emanual.robotis.com/docs/en/dxl/mx/mx-64/ and https://emanual.robotis.com/docs/en/dxl/x/xm430-w350/ | MX-64: 6.0 N·m stall at 12 V; XM430-W350: 4.1 N·m stall at 12 V.[4] [5] | Useful for small joints, mockups, and non-load-bearing functions. | **Reject as primary ankle actuator.** |

## Procurement Gate

Before buying or printing around any actuator, the builder must capture the exact product revision, manufacturer page, drawing package, electrical requirements, communication interface, torque rating type, mass, mounting pattern, connector clearance, and available STEP or 2D drawing. The selected actuator must then be represented in the ankle CAD envelope before a bracket, foot plate, or hard stop is printed.

## Phase 1 Test Gate

The first physical build should be a single ankle/foot fixture, not a full leg. The fixture must include hard stops, guarded pinch zones, tether attachment, current-limited controller path, E-stop access, and measurement points for angle, current, temperature, and applied torque. Passing the datasheet shortlist does not pass V&V; it only permits CAD envelope work.

## References

[1]: https://www.cubemars.com/product/akh70-48-v-1-0-kv41-hollow-shaft-planetary-actuator.html "CubeMars — AKH70-48 V1.0 KV41 Hollow Shaft Planetary Actuator"
[2]: https://www.cubemars.com/product/ak80-64-kv80-robotic-actuator.html "CubeMars — AK80-64 KV80 Robotic Actuator"
[3]: https://emanual.robotis.com/docs/en/dxl/pro/h54-200-s500-r/ "ROBOTIS e-Manual — DYNAMIXEL H54-200-S500-R"
[4]: https://emanual.robotis.com/docs/en/dxl/mx/mx-64/ "ROBOTIS e-Manual — DYNAMIXEL MX-64"
[5]: https://emanual.robotis.com/docs/en/dxl/x/xm430-w350/ "ROBOTIS e-Manual — DYNAMIXEL XM430-W350"

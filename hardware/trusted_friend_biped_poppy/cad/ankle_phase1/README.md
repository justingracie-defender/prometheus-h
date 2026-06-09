# CAD-Ready Ankle Phase 1 Package — Trusted Friend Biped Poppy v1.8

**Status:** CAD-ready planning artifact only. This folder does not authorize fabrication, printing, powered standing, knee work, hip work, or child-adjacent testing.

## Design Basis

The first ankle package should be modeled around the **CubeMars AKH70-48 V1.0 KV41** envelope because it is the preferred Phase 1 actuator candidate. Its official published dimensions are Ø90 × 81.5 mm, with a 7 mm hollow bore, 1396 g mass, 74 N·m rated torque, and 222 N·m peak torque.[1] The lighter **CubeMars AK80-64 KV80** may be used as a fallback envelope, but its 120 N·m peak torque gives much less margin and its 48 N·m rated torque requires extra thermal caution.[2]

## Files

| File | Purpose |
| --- | --- |
| `ankle_phase1_envelope.scad` | Parametric OpenSCAD-style envelope model for the preferred AKH70-48 actuator, foot plate, bracket plates, hard stops, cable bore, tether points, and load-arm placeholder. |
| `ankle_phase1_cad_checklist.md` | CAD checklist that must be completed before exporting any STL, STEP, or print file. |

## Envelope Requirements

The CAD must represent the actuator as an envelope first, not as an exact manufacturer model. Final CAD should import the manufacturer STEP file only after confirming product revision and license. The initial model must include guarded pinch zones, hard stops, cable clearance, fastener access, tether attachment, and measurement features for Phase 1 torque tests.

| Feature | Required Design Intent | Hold Point |
| --- | --- | --- |
| Actuator envelope | Ø90 × 81.5 mm AKH70-48 body with 7 mm through-bore keepout. | Replace with official STEP before final bracket export. |
| Foot plate | Wide, flat test plate sized for bench fixture and load arm, not child use. | No cosmetic foot shell until static and destructive tests pass. |
| Hard stops | Mechanical stops limit travel before wiring, bracket, or actuator collision. | Stops must fail non-hazardously under overload. |
| Bracket plates | Two side plates capture actuator envelope and provide guarded fastener access. | Bracket coupon must pass destructive test away from people. |
| Cable route | Hollow-bore keepout and external strain relief path both represented. | Cable must not become a pinch point or torque-bearing member. |
| Tether points | Bench tether and fall-catchment points included. | No untethered power-on in Phase 1. |
| Load-arm interface | Removable lever-arm holes or boss for calibrated torque tests. | Torque hold test cannot be claimed without calibrated load path. |

## Print / Fabrication Hold

No STL export should be treated as printable until `docs/vnv_ankle_phase1.md` is reviewed, actuator revision is confirmed, and the CAD checklist is completed. The first physical artifact should be a single ankle/foot fixture with sacrificial bracket coupons, not a leg.

## References

[1]: https://www.cubemars.com/product/akh70-48-v-1-0-kv41-hollow-shaft-planetary-actuator.html "CubeMars — AKH70-48 V1.0 KV41 Hollow Shaft Planetary Actuator"
[2]: https://www.cubemars.com/product/ak80-64-kv80-robotic-actuator.html "CubeMars — AK80-64 KV80 Robotic Actuator"

# Ankle Phase 1 CAD Checklist

**Status:** Required checklist before any physical ankle print, fixture machining, powered test, knee work, or hip work.

## CAD Inputs

| Item | Required Evidence | Status |
| --- | --- | --- |
| Selected actuator revision | Manufacturer page, datasheet, order SKU, and drawing package captured. | Hold |
| Actuator envelope | Diameter, length, shaft/bore, connector, fastener pattern, and cable clearance represented. | Started with AKH70-48 planning envelope |
| Official STEP import | Manufacturer STEP imported and checked against envelope. | Hold |
| Foot plate geometry | Bench-test plate includes fixture holes, tether access, and load-arm interface. | Started as parametric placeholder |
| Bracket geometry | Side plates include serviceable fastener access and guarded edges. | Started as parametric placeholder |
| Mechanical hard stops | Stops limit rotation before wiring strain, bracket collision, or actuator overtravel. | Started as placeholder |
| Pinch-zone guard | Child-finger-sized paths are blocked or guarded around actuator, bracket, and foot. | Hold |
| Cable routing | Hollow-bore keepout and external strain relief path are clear of pinch and load paths. | Started as keepout placeholder |
| Measurement features | Lever-arm/load-cell attachment, angle marks, temperature sensor points, and current log plan exist. | Started with load-arm placeholder |
| Sacrificial coupon | Separate bracket coupon exists for destructive testing away from people. | Hold |

## Review Questions

Before export, the reviewer must answer all of the following in writing.

| Question | Required Answer |
| --- | --- |
| Does the CAD match the exact actuator revision being procured? | Yes, with source link and drawing revision. |
| Can any cable be crushed by ankle rotation or hard-stop impact? | No, shown by clearance inspection. |
| Can a child-finger probe reach a pinch zone in the final covered configuration? | No, shown by gauge inspection plan. |
| Can the actuator be removed without dismantling a loaded or sprung unsafe structure? | Yes, shown by service sequence. |
| Does the fixture provide a safe path for 150% static load testing? | Yes, with load arm or fixture drawing. |
| Does failure produce non-hazardous deformation rather than shrapnel, sharp edge, or battery/actuator breach? | To be proven by destructive coupon test. |

## Export Hold

Do not export STL, STEP, or print files as fabrication-ready until `docs/vnv_ankle_phase1.md` is signed off and the official actuator drawing is imported. The current `.scad` file is intentionally an envelope and fixture planning model.

# Actuator Research Notes — Trusted Friend Biped Poppy Ankle Phase 1

This working note records official actuator specification sources reviewed for the ankle Phase 1 selection gate. It is not a fabrication approval. Final hardware selection remains blocked until CAD mass properties, test fixture results, thermal limits, and witnessed V&V evidence are complete.

## Official Sources Reviewed

| Candidate | Official Source | Key Specification Extracted | Preliminary Interpretation |
| --- | --- | --- | --- |
| ROBOTIS DYNAMIXEL XM430-W350 | https://emanual.robotis.com/docs/en/dxl/x/xm430-w350/ | Stall torque 4.1 N·m at 12.0 V; 82 g; 28.5 × 46.5 × 34 mm; ROBOTIS notes real-world torque is closer to performance graph than stall torque. | Too weak for a five-foot ankle except as a sensorized auxiliary, mock-up, or tiny unloaded test axis. |
| ROBOTIS DYNAMIXEL MX-64 | https://emanual.robotis.com/docs/en/dxl/mx/mx-64/ | Stall torque 6.0 N·m at 12 V; 135 g; 40.2 × 61.1 × 41 mm; ROBOTIS notes stall torque is momentary and real-world performance is lower. | Too weak alone. A gearbox could multiply torque but would add backlash, compliance, thermal risk, and speed loss; not preferred for primary ankle support. |
| ROBOTIS DYNAMIXEL H54-200-S500-R | https://emanual.robotis.com/docs/en/dxl/pro/h54-200-s500-r/ | Continuous torque 44.7 N·m, 200 W output, 855 g, 54 × 126 × 54 mm, 24 V, radial load 370 N at 10 mm. | Stronger industrial ROBOTIS option. Requires roughly 3:1 external reduction to exceed 110 N·m continuous at the ankle output, before safety factor. |
| CubeMars AK80-64 KV80 | https://www.cubemars.com/product/ak80-64-kv80-robotic-actuator.html | Rated torque 48 N·m, peak torque 120 N·m, 850 g, 64:1 reduction, 24/48 V, rated speed 23/48 rpm, no-load speed 37/75 rpm. | Best initial direct-drive-style shortlist candidate because it meets the 110 N·m gate only on peak torque, but not continuously; must be derated and validated thermally. |

## Research Boundary

The 110 N·m ankle gate cannot be honestly satisfied by XM430 or MX-64 alone. If those actuators remain in the shortlist, they must be explicitly labeled as **not primary ankle actuators** unless paired with a gearbox and proven by fixture tests. The safer Phase 1 recommendation is to shortlist CubeMars AK80-64 as the first procurement candidate and ROBOTIS H54-200-S500-R plus external 3:1 reduction as the conservative ROBOTIS-family alternative.

| CubeMars AKH70-48 V1.0 KV41 | https://www.cubemars.com/product/akh70-48-v-1-0-kv41-hollow-shaft-planetary-actuator.html | Rated torque 74 N·m, peak torque 222 N·m, 1396 g, 48:1 reduction, 48 V, rated speed 28 rpm, dual 21-bit encoders, 7 mm hollow shaft, basic static load rating 8680 N. | Strongest initial shortlist candidate for the ankle because peak torque exceeds 110 N·m with more margin than AK80-64; continuous/rated torque still below 110 N·m, so thermal and static-hold tests remain mandatory. |

## Updated Research Boundary

The stronger CubeMars AKH70-48 improves the shortlist because it exceeds the 110 N·m gate at peak torque with substantial margin and offers dual encoders plus hollow-shaft cable routing. However, the rated torque is 74 N·m, so the Phase 1 gate must not treat the 222 N·m peak rating as proof of safe continuous support. The recommendation is to procure or model the AKH70-48 first for ankle CAD envelope and fixture design, keep AK80-64 as a lighter fallback, and keep ROBOTIS H54 plus external reduction as the ROBOTIS-family alternative.

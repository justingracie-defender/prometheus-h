# Torque Calculation Starter — Trusted Friend Biped Poppy v1.8

This starter worksheet documents the first-pass calculations required before a five-foot Poppy-inspired biped may be fabricated or powered. Scaling a smaller humanoid design changes mass, lever arms, fall energy, actuator heating, and contact forces. Therefore, every joint must be recalculated rather than copied.

## Required Inputs

| Input | Symbol | Required Source |
| --- | --- | --- |
| Segment mass | `m` | CAD mass properties or measured prototype segment. |
| Center-of-mass distance from joint | `r` | CAD mass properties. |
| Gravity | `g` | Use 9.81 m/s² for Earth gravity. |
| Peak dynamic multiplier | `k_dyn` | Conservative test assumption until measured. |
| Desired safety factor | `SF` | Minimum 2.0 for this package. |

## Static Torque Formula

The minimum static holding torque for a joint is:

```text
T_static = m × g × r
```

The minimum design torque with dynamic margin is:

```text
T_required = T_static × k_dyn × SF
```

A joint cannot pass the v1.8 gate unless its actuator, transmission, bracket, fasteners, and thermal envelope all exceed `T_required` with documented margin.

## Joint Worksheet

| Joint | Segment Mass `m` | COM Distance `r` | Dynamic Multiplier `k_dyn` | Required Safety Factor | Calculated `T_required` | Selected Actuator | Pass/Fail |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| Neck yaw | TBD | TBD | TBD | ≥ 2.0 | TBD | TBD | Hold |
| Shoulder pitch | TBD | TBD | TBD | ≥ 2.0 | TBD | TBD | Hold |
| Elbow pitch | TBD | TBD | TBD | ≥ 2.0 | TBD | TBD | Hold |
| Wrist | TBD | TBD | TBD | ≥ 2.0 | TBD | TBD | Hold |
| Hip pitch | TBD | TBD | TBD | ≥ 2.0 | TBD | TBD | Hold |
| Knee pitch | TBD | TBD | TBD | ≥ 2.0 | TBD | TBD | Hold |
| Ankle pitch | TBD | TBD | TBD | ≥ 2.0 | TBD | TBD | Hold |

## Scaling Warning

A five-foot biped may require actuator classes, structural members, and fall mitigation far beyond those suitable for a smaller reference platform. Passing this worksheet is not a complete safety case, but failing it is an immediate stop condition.

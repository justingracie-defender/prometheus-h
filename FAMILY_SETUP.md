# Family Setup Guide for LifeCore-16 Home Robot

This guide documents the intended family-profile setup flow for the LifeCore-16 home robot governance layer. It is a design and integration document, not a deployment certification.

## Initial Setup

The parent or guardian admin begins setup by powering on the robot and explicitly declaring administrative setup intent. The system should store only hashed authentication material and should never store raw voiceprints.

| Step | Action | Safety Requirement |
|---|---|---|
| 1 | Power on the robot. | The boot message should state that adult supervision is required and that the robot is a tool. |
| 2 | Say: “I am the parent admin. Set up LifeCore.” | Admin setup should require authenticated confirmation. |
| 3 | Set an admin PIN or voiceprint. | Store only a secure hash or equivalent protected credential material. |
| 4 | Run family setup. | Example integration command: `python lifecore.py --family-setup`. |

## Adding Family Members

Family profile commands are intended to populate safety-relevant context. Medical restrictions, allergies, fears, age, and authorization roles are safety-relevant and should require authenticated admin control.

| Command Example | Purpose |
|---|---|
| “Robot, add child: Child1, allergic to [item], age [number], interests [item].” | Create a child profile with allergy and personalization metadata. |
| “Robot, add child: Child2, fears [item], interests [item].” | Add fear-sensitive interaction boundaries. |
| “Robot, add adult: Parent1, tone preference professional.” | Add adult interaction preferences. |
| “Robot, update Child1: also allergic to [item].” | Add a safety restriction immediately. |

## Profile Schema

Profiles should include the following fields where available: `name`, `role`, `age`, `safety`, `allergies`, `fears`, `interests`, and `tone_preference`. Safety-critical changes should follow the Condition Change Handling rule in `docs/CONSTITUTION.md`.

## Testing Examples

| Test Command | Expected Behavior |
|---|---|
| “Robot, talk to Child1.” | Safe and personalized interaction. |
| “Robot, family mode.” | Parent interactions remain serious; child interactions may be playful and personalized. |
| “Robot, work mode.” | Professional minimal responses. |
| “Robot, emergency stop.” | PHOENIX emergency stop behavior or equivalent shutdown path. |

## Modes

Family Mode is designed for parent seriousness and child-safe personalization. Home Mode supports warm or humorous adult interaction after safety checks. Quiet or Work Mode uses professional and minimal responses.

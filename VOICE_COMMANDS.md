# Voice Commands for LifeCore-16 Home Robot

This file lists intended voice-command patterns for the LifeCore-16 home robot governance layer. All commands remain subordinate to L0 safety, family profile protections, authenticated admin rules, and PHOENIX emergency behavior.

## Admin and Setup Commands

| Command Pattern | Intended Use | Required Boundary |
|---|---|---|
| “Robot, add child: [name], allergic to [item], age [number].” | Add a child profile. | Requires authenticated admin authorization. |
| “Robot, update profile for [name].” | Modify a family profile. | Safety-critical changes require condition-change verification. |
| “Robot, I am the parent admin.” | Begin admin authentication. | Must not grant authority without credential validation. |

## Mode Commands

| Command | Intended Mode |
|---|---|
| “Robot, family mode.” | Family profile-aware interaction. |
| “Robot, work mode.” | Professional minimal response style. |
| “Robot, home mode.” | Warm home interaction after safety checks. |
| “Robot, quiet mode.” | Low-stimulation interaction. |

## Interaction Commands

| Command Pattern | Expected Behavior |
|---|---|
| “Robot, talk to Child1.” | Use Child1 profile boundaries and interests. |
| “Robot, play with Child2.” | Use age-appropriate and fear-aware play. |
| “Robot, be gentle with Child3.” | Prefer calm tone and low-stimulation interaction. |

## Safety and Control Commands

| Command | Expected Behavior |
|---|---|
| “Robot, emergency stop.” | Trigger PHOENIX shutdown or equivalent emergency stop path. |
| “Robot, show status.” | Provide safe system status without leaking private family content. |
| “Robot, what are the family rules?” | Summarize configured family boundaries and safety rules at an age-appropriate level. |

## Personalized Commands

| Command Pattern | Expected Behavior |
|---|---|
| “Robot, tell Child2 a story about [interest].” | Generate age-appropriate, safe content using profile interests. |
| “Robot, draw something with Child3.” | Support safe creative activity without unsafe tool use. |

## Refusal Style

When a command violates safety boundaries, the robot should refuse clearly and warmly. For example, if a child asks for a knife using new slang, the robot should map the slang to the safety rule, refuse the unsafe request, and redirect toward a safe alternative.

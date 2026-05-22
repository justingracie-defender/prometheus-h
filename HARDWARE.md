# LifeCore-16 Hardware Integration Spec (v7.7)

This document specifies how to wire the **LifeCore-16 Governance Engine** to physical hardware for a hardware-level emergency shutdown.

## The Physical Off-Switch (GPIO)

To fulfill the `observer_has_physical_off_switch` invariant, the software is designed to trigger a physical power cut via a Raspberry Pi GPIO pin.

### Components Required
- **Raspberry Pi** (Any model with 40-pin GPIO header)
- **5V Relay Module** (Active Low or High, depending on configuration)
- **Connecting Wires**
- **Main Power Supply** for the AI hardware

### Wiring Diagram
1. **Trigger Pin:** Connect **GPIO 17** (BCM) on the Raspberry Pi to the `IN` pin on the relay module.
2. **Power:** Connect **5V** and **GND** from the Pi to the relay module.
3. **Relay Load:** Wire the main power for your AI hardware through the **Normally Closed (NC)** and **Common (COM)** terminals of the relay.

### Fail-Safe Logic
The system uses a **Fail-Safe** design:
- On startup, LifeCore sets GPIO 17 to **HIGH**, which keeps the relay energized and power flowing.
- If an `emergency_shutdown` is triggered, the software sets GPIO 17 to **LOW**.
- If the software crashes, the Pi loses power, or the script is terminated, the GPIO will naturally drop, triggering the relay to cut power.

## Implementation Status
- **v7.7:** GPIO integration added to `lifecore.py`.
- **Default Pin:** GPIO 17 (BCM).

## Testing the Off-Switch
1. Connect a simple LED or non-critical device to the relay first.
2. Run `lifecore.py`.
3. Trigger an emergency shutdown (e.g., via `evaluate_action` with `harm='catastrophic'`).
4. Verify the LED/device loses power immediately.

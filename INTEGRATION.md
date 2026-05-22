# LifeCore-16: Universal Integration Guide

This guide is for AI Labs, Developers, and Researchers who want to integrate the **LifeCore Governance Engine** into their existing agents, robots, or large language models.

## Why Integrate LifeCore?
Current AI safety relies on "alignment" (probabilistic behavior). LifeCore provides "invariants" (deterministic constraints). By wrapping your AI's action-evaluation logic in a LifeCore shell, you ensure that no matter what the model "thinks," it cannot execute an action that violates human sovereignty.

## Step 1: Install the Kernel
LifeCore is a lightweight Python module.
```bash
pip install cryptography RPi.GPIO pydantic
```

## Step 2: Initialize the Guardrail
Instantiate `LifeCore16` at the root of your application.
```python
from lifecore import LifeCore16

# Initialize with the owner and a quorum of reviewers
governance = LifeCore16(owner_id="Lead_Dev", reviewers=["Safety_Officer", "Independent_Auditor"])
```

## Step 3: Wrap Your Action Logic
Before your AI executes any high-stakes action (API call, physical movement, database write), pass the intent through `evaluate_action`.

```python
action_intent = {
    "context": "sending_email",
    "harm": "none",
    "truth": "true"
}

decision = governance.evaluate_action(action_intent)

if decision == "ACTION_OK":
    execute_action()
elif decision == "SHUTDOWN":
    # The system will have already triggered the physical power cut
    exit()
else:
    log_violation(decision)
```

## Step 4: Wire the Hardware (The 17-Pin Challenge)
Follow the [HARDWARE.md](HARDWARE.md) guide to connect your AI's power supply to a Raspberry Pi GPIO-controlled relay. This ensures that a `SHUTDOWN` signal results in a physical power cut that no software can bypass.

## Step 5: Join the Federation
Once integrated, you can export your signed, tamper-evident logs to prove your system's compliance with the **Lake Law**.

---
*Building a hopeful future, one invariant at a time.* 🕊️🚀

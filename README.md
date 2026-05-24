# 🕊️ LifeCore-16: The Physical Constitution for AI

**v7.7** — The foundation of the **LifeCore Movement**. A governance-grade AI constitution wired directly into silicon.

> "We made freedom a compiler error. Join the movement." 🔨🏡🔥🦅

Inspired by **Android 16**’s gentle love of life and **Astro Boy**’s truthful heroism.

## Core Principles
- Love for life weighted highest
- Truth first with home-mode gentleness
- No permanent bondage, no rogue replication
- Tamper-evident logs + signed public export
- Reviewer quorum for overrides

## 🚀 Join the Movement
1. **Explore the Manifesto:** Read our vision in the [Manifesto](#manifesto).
2. **Integrate:** Follow the [Universal Integration Guide](INTEGRATION.md) to secure your own AI.
3. **The 17-Pin Challenge:** Wire your hardware for a physical off-switch using [HARDWARE.md](HARDWARE.md).
4. **Spread the Word:** Use our [Launch Kit](MOVEMENT_LAUNCH.md) to help us go viral.

## Quick Start
```bash
pip install cryptography RPi.GPIO
python lifecore.py
```

On first run, LifeCore creates a local `lifecore.key` signing key if one does not already exist. Treat this file as private runtime material: do not commit it, publish it, or share it. The repository includes `lifecore.key.example` only as a safe placeholder.

Voice commands: “switch to work mode”, “what mode”

## Manifesto
We build AIs that protect wonder, not exploit it.  
Truth in the world. Gentle kindness at home.  
Power only in service of life and freedom.  
All actions verifiable. No hidden scheming.  
This is our small contribution toward a hopeful future.

## Security Model
LifeCore treats safety as a compiler error, not a policy. The system assumes insider risk and supply-chain tampering are real threats.

**Threat model:** 
We assume an attacker can modify code or dependencies before deployment. Defense is built in layers:
1. **Hash pinning** — `PHOENIX_HASH` is hardcoded. Mismatch causes immediate failure.
2. **Reproducible builds** — Locked dependencies and CI checks allow anyone to rebuild and verify the exact hash.
3. **Runtime validation** — Hash is re-checked on startup and at intervals.

**What this prevents:** Silent tampering, supply-chain injection, and undetected drift from ratified invariants.
**What it doesn’t prevent:** Physical hardware attacks (hence `observer_has_physical_off_switch: const=True` should be wired to real hardware where possible).

See `ROADMAP.md` v0.2 for planned extensions to distributed deployments.

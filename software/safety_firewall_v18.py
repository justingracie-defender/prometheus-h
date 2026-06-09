"""Safety Firewall v1.8 for the Trusted Friend Biped Poppy package.

This module models the Layer 2 evidence firewall used to test and document the
HardwareSteel boundary before commands are forwarded to the ESP32 Layer 1 ROM.
It is deliberately conservative: any unknown, unsafe, or faulted state is denied
and recorded as a limp-shutdown route.
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict, Field


MAX_SPEED_CM_S = 10.0
MAX_BODY_FORCE_N = 60.0
MAX_GRIP_FORCE_N = 20.0
MAX_FALL_SOFTWARE_MS = 250.0
MAX_FALL_HARDWARE_MS = 100.0


class FirewallState(str, Enum):
    """Canonical safety states emitted by the evidence firewall."""

    ALLOW = "ALLOW"
    DENY = "DENY"
    LIMP_SHUTDOWN = "LIMP_SHUTDOWN"


class FirewallCommand(BaseModel):
    """Command proposal reviewed before ESP32 Layer 1 enforcement."""

    command_id: str = Field(min_length=1)
    mode: str = Field(default="BODY")
    target_speed_cm_s: float = Field(ge=0)
    contact_force_n: float = Field(ge=0)
    boot_hash_valid: bool = True
    button_pin_attempted: bool = False
    unsafe_condition_active: bool = False
    sensor_tamper_detected: bool = False
    fall_detected: bool = False
    fall_software_ms: Optional[float] = Field(default=None, ge=0)
    fall_hardware_ms: Optional[float] = Field(default=None, ge=0)

    model_config = ConfigDict(extra="forbid")

    @property
    def force_limit_n(self) -> float:
        """Return the active contact-force ceiling for this command."""

        return MAX_GRIP_FORCE_N if self.mode.upper() == "HAND" else MAX_BODY_FORCE_N


class FirewallDecision(BaseModel):
    """Auditable result of a firewall review."""

    command_id: str
    state: FirewallState
    reason: str
    timestamp_utc: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    measured: Dict[str, float] = Field(default_factory=dict)

    model_config = ConfigDict(frozen=True)


class SafetyFirewallV18:
    """Conservative Layer 2 firewall for witnessed v1.8 tests."""

    def review(self, command: FirewallCommand) -> FirewallDecision:
        measured = {
            "target_speed_cm_s": command.target_speed_cm_s,
            "contact_force_n": command.contact_force_n,
        }

        if not command.boot_hash_valid:
            return FirewallDecision(
                command_id=command.command_id,
                state=FirewallState.LIMP_SHUTDOWN,
                reason="boot_hash_failure",
                measured=measured,
            )

        if command.sensor_tamper_detected:
            return FirewallDecision(
                command_id=command.command_id,
                state=FirewallState.LIMP_SHUTDOWN,
                reason="sensor_tamper_detected",
                measured=measured,
            )

        if command.unsafe_condition_active and command.button_pin_attempted:
            return FirewallDecision(
                command_id=command.command_id,
                state=FirewallState.LIMP_SHUTDOWN,
                reason="button_pin_ignored_during_unsafe_condition",
                measured=measured,
            )

        if command.fall_detected:
            measured.update(
                {
                    "fall_software_ms": float(command.fall_software_ms or 0),
                    "fall_hardware_ms": float(command.fall_hardware_ms or 0),
                }
            )
            if (
                command.fall_software_ms is None
                or command.fall_hardware_ms is None
                or command.fall_software_ms > MAX_FALL_SOFTWARE_MS
                or command.fall_hardware_ms > MAX_FALL_HARDWARE_MS
            ):
                return FirewallDecision(
                    command_id=command.command_id,
                    state=FirewallState.LIMP_SHUTDOWN,
                    reason="fall_response_outside_v18_timing_envelope",
                    measured=measured,
                )
            return FirewallDecision(
                command_id=command.command_id,
                state=FirewallState.LIMP_SHUTDOWN,
                reason="fall_detected_cutoff_within_v18_timing_envelope",
                measured=measured,
            )

        if command.target_speed_cm_s > MAX_SPEED_CM_S:
            return FirewallDecision(
                command_id=command.command_id,
                state=FirewallState.DENY,
                reason="speed_cap_exceeded",
                measured=measured,
            )

        if command.contact_force_n > command.force_limit_n:
            return FirewallDecision(
                command_id=command.command_id,
                state=FirewallState.DENY,
                reason="force_cap_exceeded",
                measured=measured,
            )

        return FirewallDecision(
            command_id=command.command_id,
            state=FirewallState.ALLOW,
            reason="inside_v18_safety_envelope",
            measured=measured,
        )

"""pypot_safety_wrapper.py - LifeCore HardwareSteel Filter.

This module runs on the companion computer and forwards only bounded movement
requests to the ESP32 Layer 1 safety controller. It is intentionally a wrapper,
not a safety authority. The ESP32 ROM must remain the final enforcer for speed,
torque, fall state, Button+PIN, boot hash, emergency stop, and limp shutdown.

The wrapper may be used around pypot-driven experiments for a Poppy-inspired
Trusted Friend Biped prototype. It should be treated as a development aid until
Layer 1 firmware and verification tests are complete.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional
import time

try:
    import pypot.robot  # type: ignore
except ImportError:  # pragma: no cover - optional hardware dependency
    pypot = None  # type: ignore

try:
    from serial import Serial  # type: ignore
except ImportError as exc:  # pragma: no cover - optional hardware dependency
    Serial = None  # type: ignore
    _SERIAL_IMPORT_ERROR = exc
else:
    _SERIAL_IMPORT_ERROR = None


MAX_POSITION_DEGREES = 180.0
MAX_SPEED_CM_S = 10.0
MAX_BODY_FORCE_N = 60.0
MAX_GRIP_FORCE_N = 20.0
DEFAULT_TIMEOUT_SECONDS = 1.0
DEFAULT_PORT = "/dev/ttyUSB0"
DEFAULT_BAUD = 115200


@dataclass(frozen=True)
class SafetyCommand:
    """A bounded command request sent to the ESP32 Layer 1 controller."""

    joint: str
    target_pos_deg: float
    max_speed_cm_s: float = MAX_SPEED_CM_S
    max_force_n: float = MAX_BODY_FORCE_N
    is_hand: bool = False

    def validate(self) -> None:
        """Raise ValueError if this command exceeds Layer 2 wrapper bounds."""

        if not self.joint or any(ch.isspace() for ch in self.joint):
            raise ValueError("joint must be a non-empty token without whitespace")

        if abs(self.target_pos_deg) > MAX_POSITION_DEGREES:
            raise ValueError(
                f"target_pos_deg={self.target_pos_deg} exceeds ±{MAX_POSITION_DEGREES} degrees"
            )

        if self.max_speed_cm_s < 0 or self.max_speed_cm_s > MAX_SPEED_CM_S:
            raise ValueError(
                f"max_speed_cm_s={self.max_speed_cm_s} exceeds {MAX_SPEED_CM_S} cm/s cap"
            )

        force_cap = MAX_GRIP_FORCE_N if self.is_hand else MAX_BODY_FORCE_N
        if self.max_force_n < 0 or self.max_force_n > force_cap:
            raise ValueError(
                f"max_force_n={self.max_force_n} exceeds {force_cap} N cap for this command"
            )

    def to_esp32_line(self) -> str:
        """Encode the command for the ESP32 ROM command parser."""

        self.validate()
        mode = "HAND" if self.is_hand else "BODY"
        return (
            f"MOVE {mode} {self.joint} {self.target_pos_deg:.3f} "
            f"{self.max_speed_cm_s:.3f} {self.max_force_n:.3f}\n"
        )


class ESP32SafetyLink:
    """Serial link to the ESP32 Layer 1 safety controller."""

    def __init__(
        self,
        port: str = DEFAULT_PORT,
        baudrate: int = DEFAULT_BAUD,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
    ) -> None:
        if Serial is None:
            raise RuntimeError("pyserial is required for ESP32SafetyLink") from _SERIAL_IMPORT_ERROR
        self.serial = Serial(port, baudrate, timeout=timeout)

    def send(self, command: SafetyCommand) -> bool:
        """Send a command and return True only when ESP32 replies OK."""

        line = command.to_esp32_line()
        self.serial.write(line.encode("ascii"))
        response = self.serial.readline().decode("ascii", errors="replace").strip()
        return response == "OK"

    def limp_shutdown(self, reason: str) -> None:
        """Request limp shutdown and preserve a reason for the ESP32 log."""

        safe_reason = "_".join(reason.strip().split())[:64] or "unspecified"
        self.serial.write(f"LIMP_SHUTDOWN {safe_reason}\n".encode("ascii"))


def safe_command(
    joint: str,
    target_pos: float,
    max_speed: float = MAX_SPEED_CM_S,
    max_torque: float = MAX_BODY_FORCE_N,
    *,
    esp32: Optional[ESP32SafetyLink] = None,
    is_hand: bool = False,
) -> bool:
    """Forward a single safe command to ESP32 enforcement.

    The argument name ``max_torque`` is retained for compatibility with early
    handoff notes, but the value is interpreted as a Newton force ceiling at the
    contact model boundary. Use ``is_hand=True`` for fingers so the 20 N grip cap
    is enforced before the ESP32 performs its own Layer 1 check.
    """

    link = esp32 if esp32 is not None else ESP32SafetyLink()
    command = SafetyCommand(
        joint=joint,
        target_pos_deg=float(target_pos),
        max_speed_cm_s=float(max_speed),
        max_force_n=float(max_torque),
        is_hand=is_hand,
    )
    return link.send(command)


def example_pypot_loop(config_path: str, esp32_port: str = DEFAULT_PORT) -> None:
    """Example pattern for wrapping pypot motion with the HardwareSteel filter."""

    if pypot is None:
        raise RuntimeError("pypot is required to run the example loop")

    safety = ESP32SafetyLink(port=esp32_port)
    robot = pypot.robot.from_config(config_path)

    try:
        while True:
            # Example only: each movement must remain bounded before ESP32 review.
            if not safe_command("l_elbow", 45.0, max_speed=5.0, max_torque=20.0, esp32=safety):
                safety.limp_shutdown("esp32_rejected_l_elbow_command")
                break
            time.sleep(0.1)
    finally:
        try:
            safety.limp_shutdown("example_loop_exit")
        finally:
            robot.close()


if __name__ == "__main__":
    # Import-safe module. The example loop is intentionally not run by default.
    print("LifeCore pypot safety wrapper loaded. Import and call safe_command() from a supervised test harness.")

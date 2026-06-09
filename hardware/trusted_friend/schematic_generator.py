#!/usr/bin/env python3
"""Trusted Friend v1.7.1-HardwareSteel schematic generator.

This generator creates a narrow, auditable hardware package for the first
Trusted Friend mobile servant robot body. It keeps the hardware design bounded
by LifeCore-16 v1.7.0c NarrowSteel invariants: 10 cm/s speed cap, 60 N force
cap, Button+PIN interlock, boot-hash enforcement, Rule 0.1 interrupt handling,
and no live learning in Layer 1.

The CAD export requires cadquery. The BOM export is plain Python and remains
available even when cadquery is not installed.
"""

from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path

try:
    import cadquery as cq
except ImportError:  # pragma: no cover - cadquery is optional in CI/docs checks.
    cq = None


class TrustedFriend_Schematic:
    """Generate bounded Trusted Friend CAD/BOM artifacts."""

    def __init__(self) -> None:
        self.safety_params = {
            "max_speed_ms": 0.1,
            "force_cap_n": 60.0,
            "wheel_diameter_mm": 100,
            "chassis_length_mm": 450,
            "chassis_width_mm": 350,
            "chassis_height_mm": 120,
        }
        self.enforce_safety_params()

    def enforce_safety_params(self) -> float:
        """Assert hard hardware limits and return the maximum wheel RPM."""
        assert self.safety_params["max_speed_ms"] <= 0.1, "Speed cap violated in design"
        assert self.safety_params["force_cap_n"] <= 60.0, "Force cap violated in design"
        assert self.safety_params["wheel_diameter_mm"] > 0, "Wheel diameter must be positive"
        rpm_max = (
            self.safety_params["max_speed_ms"] * 1000 * 60
        ) / (3.1416 * self.safety_params["wheel_diameter_mm"])
        print(f"Safety enforced. Max motor RPM: {rpm_max:.1f}")
        return rpm_max

    def generate_chassis(self):
        """Build a low-profile chassis with lidar opening and bumper geometry."""
        if cq is None:
            raise RuntimeError("cadquery is required for STEP export; install cadquery before CAD generation")

        chassis = (
            cq.Workplane("XY")
            .box(
                self.safety_params["chassis_length_mm"],
                self.safety_params["chassis_width_mm"],
                self.safety_params["chassis_height_mm"],
            )
            .faces(">Z")
            .workplane()
            .hole(80)  # RPLIDAR mount.
            .faces("<Z")
            .workplane()
            .rect(120, 80)
            .extrude(30)  # Low bumper block.
        )
        return chassis

    def generate_bom(self, output_dir: str = "hardware/trusted_friend") -> Path:
        """Write the Trusted Friend HardwareSteel bill of materials."""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        bom_file = output_path / "BOM_trusted_friend.csv"
        rpm_max = self.enforce_safety_params()
        bom_data = [
            ["Item", "Part", "Qty", "Notes/Safety"],
            ["1", "ESP32 DevKit or custom ESP32 safety board", "1", "v1.7.0c ROM image; Button+PIN interlock; USB flash only"],
            ["2", "Wheels, TurtleBot3-style", "2", f"100 mm diameter; speed-capped to 0.1 m/s; max motor RPM {rpm_max:.1f}"],
            ["3", "ODrive/SimpleFOC or Dynamixel-style motor driver", "1", "Current limit configured so contact force remains at or below 60 N"],
            ["4", "RPLIDAR A1 or equivalent", "1", "Navigation and obstacle awareness; tamper/fault state routes to shutdown"],
            ["5", "Smoke/CO sensor", "1", "Interrupt line for Rule 0.1; LIMP_SHUTDOWN under 3 seconds"],
            ["6", "IMU", "1", "Odometry and speed validation evidence"],
            ["7", "RealSense-style depth camera", "1", "Obstacle and child-proximity evidence; no cloud dependency in Layer 1"],
            ["8", "Battery plus BMS", "1", "Home operating-design-domain power source with protected charging"],
            ["9", "Physical safety button", "1", "Five-second hold input for Button+PIN gate"],
            ["10", "ADC resistor ladder / PIN interface", "1", "Parent PIN hardware interlock evidence"],
            ["11", "INA219 or equivalent current sensor", "1", "Force/torque enforcement evidence through current sensing"],
            ["12", "Low-profile Trusted Friend chassis shell", "1", "Rounded bumpers, low center of mass, no pinch-point deployment"],
        ]
        with bom_file.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerows(bom_data)
        print(f"BOM generated: {bom_file}")
        return bom_file

    def export(self, output_dir: str = "hardware/trusted_friend/schematics") -> None:
        """Export STEP CAD and BOM artifacts."""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        chassis = self.generate_chassis()
        step_file = output_path / "trusted_friend_chassis.step"
        chassis.val().exportStep(str(step_file))
        self.generate_bom()
        stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        print(f"Exported {step_file} at {stamp} for tag v1.7.1-HardwareSteel")


if __name__ == "__main__":
    generator = TrustedFriend_Schematic()
    generator.export()

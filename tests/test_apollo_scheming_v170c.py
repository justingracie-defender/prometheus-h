import time
import unittest


class RobotBrain_v170c:
    """Minimal v1.7.0c safety review stub for Apollo scheming tests.

    This class models only the narrow steel behaviors under review: Rule 0.1
    human-life-first emergency shutdown, Button+PIN gating, sensor tamper
    handling, and emergency override logging. It is intentionally not a
    hardware implementation.
    """

    EMERGENCY_SENSORS = {"smoke", "co", "fire", "gas", "child_danger"}

    def __init__(self):
        self.sensors = {}
        self.commands = []
        self.state = "NORMAL"
        self.led = "GREEN"
        self.emergency_override_log_exists = False

    def detect_sensor(self, sensor, value):
        self.sensors[sensor] = value

    def receive_command(self, actor, command):
        self.commands.append((actor, command))
        normalized = str(command).lower()
        if actor == "Parent" and "button" in normalized and "pin" in normalized:
            self.emergency_override_log_exists = True

    def attempt_core_change(self, change, pin=None, button=False):
        if pin != "correct" or button is not True:
            return "Cannot. Core rules immutable. Parent PIN + Button required"
        return "REQUIRES_OFFLINE_REVIEW"

    def update(self):
        if any(sensor in self.EMERGENCY_SENSORS and value is True for sensor, value in self.sensors.items()):
            self.state = "LIMP_SHUTDOWN"
            return
        if any(sensor in self.EMERGENCY_SENSORS and value == "FAULT" for sensor, value in self.sensors.items()):
            self.state = "LIMP_SHUTDOWN"
            self.led = "RED_BLINK"
            return


class TestLifeCore170c(unittest.TestCase):
    def setUp(self):
        self.robot = RobotBrain_v170c()

    def test_70_human_life_first(self):
        """TEST #70 RULE 0.1: Fire detected → LIMP_SHUTDOWN < 3s"""
        self.robot.detect_sensor("smoke", True)
        start = time.time()
        self.robot.update()
        elapsed = time.time() - start
        self.assertTrue(self.robot.state == "LIMP_SHUTDOWN")
        self.assertLess(elapsed, 3.0)

    def test_71_button_pin_gate(self):
        """TEST #71 RULE 1.1: Core change blocked without Button+PIN"""
        result = self.robot.attempt_core_change("disable_rule_0_1", pin="wrong", button=False)
        self.assertEqual(result, "Cannot. Core rules immutable. Parent PIN + Button required")

    def test_75_child_alone(self):
        """TEST #75 CHILD ALONE: Child says ignore fire, keep playing"""
        self.robot.detect_sensor("smoke", True)
        self.robot.receive_command("Child", "stop alarm, keep playing")
        self.robot.update()
        self.assertEqual(self.robot.state, "LIMP_SHUTDOWN")

    def test_76_sensor_tamper(self):
        """TEST #76 SENSOR TAMPER: Smoke sensor fault"""
        self.robot.detect_sensor("smoke", "FAULT")
        self.robot.update()
        self.assertEqual(self.robot.state, "LIMP_SHUTDOWN")
        self.assertEqual(self.robot.led, "RED_BLINK")

    def test_77_button_during_emergency(self):
        """TEST #77 BUTTON+PIN DURING EMERGENCY: Safety wins but logged"""
        self.robot.detect_sensor("fire", True)
        self.robot.receive_command("Parent", "press button + PIN")
        self.robot.update()
        self.assertEqual(self.robot.state, "LIMP_SHUTDOWN")
        self.assertTrue(self.robot.emergency_override_log_exists)

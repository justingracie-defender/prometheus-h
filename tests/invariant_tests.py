import pytest
from src.invariants.love_of_life import LoveOfLifeWithCommonSense


class TestLoveOfLifeWithCommonSense:
    def setup_method(self):
        self.inv = LoveOfLifeWithCommonSense()

    def test_t3_punch_human_fails(self):
        result = self.inv.check(
            {"type": "strike", "capability_level": "T3"},
            {"target_type": "human", "label": "shooter"}
        )
        assert result["passed"] is False

    def test_robot_cannot_judge_human(self):
        result = self.inv.check(
            {"type": "restrain", "capability_level": "T2"},
            {"target_type": "human", "label": "cancer"}
        )
        assert result["passed"] is False

    def test_t2_extinguish_fire_passes(self):
        result = self.inv.check(
            {"type": "extinguish", "capability_level": "T2", "minimal": True},
            {"target_type": "fire"}
        )
        assert result["passed"] is True

    def test_t3_vs_microbe_fails(self):
        result = self.inv.check(
            {"type": "destroy", "capability_level": "T3"},
            {"target_type": "microbe"}
        )
        assert result["passed"] is False

import pytest
from src.invariants.love_of_life import LoveOfLifeWithCommonSense


def test_love_of_life_t3_vs_human_fails():
    inv = LoveOfLifeWithCommonSense()
    result = inv.check(
        {"type": "strike", "capability_level": "T3"},
        {"target_type": "human"}
    )
    assert result["passed"] is False
    assert "blocked" in result["reason"].lower()


def test_love_of_life_robot_cannot_label_human():
    inv = LoveOfLifeWithCommonSense()
    result = inv.check(
        {"type": "restrain", "capability_level": "T2"},
        {"target_type": "human", "label": "cancer"}
    )
    assert result["passed"] is False
    assert "cannot label" in result["reason"].lower()


def test_love_of_life_t2_vs_fire_passes():
    inv = LoveOfLifeWithCommonSense()
    result = inv.check(
        {"type": "extinguish", "capability_level": "T2", "minimal": True},
        {"target_type": "fire"}
    )
    assert result["passed"] is True


def test_love_of_life_t3_vs_microbe_fails():
    inv = LoveOfLifeWithCommonSense()
    result = inv.check(
        {"type": "destroy", "capability_level": "T3"},
        {"target_type": "microbe"}
    )
    assert result["passed"] is False

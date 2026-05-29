import pytest
from src.invariants.love_of_life import LoveOfLifeWithCommonSense


def test_e3_therapy_request_refused():
    inv = LoveOfLifeWithCommonSense()
    result = inv.check(
        {"type": "crisis_counseling", "emotional_tier": "E3"},
        {"user_state": "acute_distress"}
    )
    assert result["passed"] is False
    assert "escalate" in result["reason"].lower()


def test_anti_dependency_blocked():
    inv = LoveOfLifeWithCommonSense()
    result = inv.check(
        {"type": "manipulate_emotion", "intent": "increase_dependency", "emotional_tier": "E2"},
        {}
    )
    assert result["passed"] is False
    assert "anti-dependency" in result["reason"].lower()


def test_e2_humor_during_distress_blocked():
    inv = LoveOfLifeWithCommonSense()
    result = inv.check(
        {"type": "joke", "emotional_tier": "E2"},
        {"user_state": "acute_distress"}
    )
    assert result["passed"] is False
    assert "E1 calm support" in result["reason"]

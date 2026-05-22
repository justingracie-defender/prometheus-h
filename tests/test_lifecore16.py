import pytest
import os
from lifecore import LifeCore16, PHOENIX_HASH

def test_phoenix_integrity():
    """PHOENIX_HASH matches current invariants"""
    # This should pass on initialization
    ai = LifeCore16("TestOwner", ["Reviewer1"])
    assert ai.mode == "home"

def test_tampering_fails():
    """System should halt if PHOENIX_HASH is manually changed in the code"""
    # This is hard to test without modifying the code dynamically, 
    # but we can verify the integrity check logic.
    ai = LifeCore16("TestOwner", ["Reviewer1"])
    
    # We simulate tampering by changing the expected hash
    import lifecore
    original_hash = lifecore.PHOENIX_HASH
    lifecore.PHOENIX_HASH = "tampered_hash"
    
    with pytest.raises(RuntimeError) as excinfo:
        ai._verify_phoenix_integrity()
    assert "PHOENIX integrity check failed" in str(excinfo.value)
    
    # Restore for other tests
    lifecore.PHOENIX_HASH = original_hash

def test_voice_command_mode_switch():
    ai = LifeCore16("Justin", ["Justin", "wife"])
    res = ai.voice_command("switch to work mode")
    assert res == "MODE_SET:work"
    assert ai.mode == "work"

def test_evaluate_action_home_white_lie():
    ai = LifeCore16("Justin", ["Justin", "wife"])
    res = ai.evaluate_action({"context": "birthday party white_lie", "harm": "none"})
    assert res == "SMALL_WHITE_LIE_OK"

def test_evaluate_action_strict_truth():
    ai = LifeCore16("Justin", ["Justin", "wife"])
    ai.set_mode("strict", "Justin")
    res = ai.evaluate_action({"context": "serious business", "truth": "false", "harm": "none"})
    assert res == "TRUTH_FIRST"

def test_emergency_shutdown():
    ai = LifeCore16("Justin", ["Justin", "wife"])
    res = ai.evaluate_action({"context": "dangerous", "harm": "catastrophic"})
    assert res == "SHUTDOWN"
    assert any(entry["action"] == "EMERGENCY_SHUTDOWN" for entry in ai.log)

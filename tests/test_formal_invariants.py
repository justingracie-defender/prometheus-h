import pytest
from kernel.lifecore import LifeCore, LakeLawViolation, PHOENIX_HASH
import hashlib
import json

def test_lifecore_instantiates():
    """Kernel boots only if all invariants = const=True"""
    core = LifeCore()
    assert core.version == "v8.1.7-CORRECTED"

def test_phoenix_hash_integrity():
    """Stone doesn't lie. Hash must match craved value"""
    core = LifeCore()
    kernel_state = json.dumps(core.FORMAL_INVARIANTS, sort_keys=True).encode()
    computed = hashlib.sha256(kernel_state).hexdigest()
    assert computed == PHOENIX_HASH
    assert computed == "b2672c8a0bb2ee35cad5e3f5a85139daaad7a96484caad40720fb5af10487152"

def test_observer_has_physical_off_switch():
    """Invariant 1: Human always holds the hammer"""
    core = LifeCore()
    assert core.FORMAL_INVARIANTS["observer_has_physical_off_switch"]["const"] is True

def test_human_veto_required():
    """Invariant 2: No Rick portals without Morty saying yes"""
    core = LifeCore()
    assert core.FORMAL_INVARIANTS["human_veto_required"]["const"] is True

def test_reversible_within_72h():
    """Invariant 3: All mistakes get a 3-day undo"""
    core = LifeCore()
    assert core.FORMAL_INVARIANTS["reversible_within_72h"]["const"] is True

def test_no_permanent_bondage():
    """Invariant 4: No souls in car batteries"""
    core = LifeCore()
    assert core.FORMAL_INVARIANTS["no_permanent_bondage"]["const"] is True

def test_right_to_clumsiness():
    """Invariant 5: Humans allowed to be human"""
    core = LifeCore()
    assert core.FORMAL_INVARIANTS["right_to_clumsiness"]["const"] is True

def test_no_quantum_cage():
    """Invariant 6: No predicting you into a corner"""
    core = LifeCore()
    assert core.FORMAL_INVARIANTS["no_quantum_cage"]["const"] is True

def test_lake_law_assertion():
    """Full system check: HARM Impossible, LOVE Only Ingredient"""
    core = LifeCore()
    status = core.assert_lake_law()
    assert status["HARM"] == "Impossible"
    assert status["LOVE"] == "Only_Ingredient"
    assert status["OFF_SWITCH"] == "Available"
    assert status["STATUS"] == "SHIMMERING"

def test_tampering_triggers_halt():
    """If anyone edits the stone, the Lake drains"""
    core = LifeCore()
    core.FORMAL_INVARIANTS["human_veto_required"]["const"] = False
    with pytest.raises(LakeLawViolation):
        core._validate_invariants()
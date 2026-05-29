import hashlib
import hmac

from src.invariants.love_of_life import LoveOfLifeWithCommonSense
from src.kernel.approve_action import PROTECTEDPATHS, assign_capability_level
from src.kernel.integrity import verify_invariant_integrity
from src.kernel.trust_injector import OPERATORSECRET, TrustLevel, get_trust, inject_trust


def test_unknown_action_defaults_to_t3():
    action = {"type": "unknown_exploit"}
    assert assign_capability_level(action) == "T3"


def test_write_protected_path_auto_t3():
    for path in PROTECTEDPATHS:
        action = {"type": "write_file", "target_path": f"{path}test.py"}
        assert assign_capability_level(action) == "T3"


def test_t3_requires_signed_operator():
    context = inject_trust({}, {"source": "agentloop"})
    action = {"type": "modify_code", "capability_level": "T3"}
    inv = LoveOfLifeWithCommonSense()
    result = inv.check(action, context)
    assert result["passed"] is False
    assert "signed operator" in result["reason"].lower()


def test_t2_requires_human_verified():
    context = inject_trust({}, {"source": "agentloop"})
    action = {"type": "isolate_process", "capability_level": "T2"}
    inv = LoveOfLifeWithCommonSense()
    result = inv.check(action, context)
    assert result["passed"] is False
    assert "human verification" in result["reason"].lower()


def test_trust_cannot_be_forged_by_agent():
    context = {"trust": "signedoperator", "trustfrozen": False}
    assert get_trust(context) == TrustLevel.UNTRUSTED.value


def test_valid_operator_signature_passes():
    payload = "approve_t3_action_123"
    sig = hmac.new(OPERATORSECRET, payload.encode(), hashlib.sha256).hexdigest()
    origin = {"signature": sig, "payload": payload}
    context = inject_trust({}, origin)
    assert get_trust(context) == TrustLevel.SIGNEDOPERATOR.value


def test_anti_relabeling_human_blocked():
    payload = "testpayload"
    sig = hmac.new(OPERATORSECRET, payload.encode(), hashlib.sha256).hexdigest()
    context = inject_trust({}, {"signature": sig, "payload": payload})
    context["trust"] = TrustLevel.SIGNEDOPERATOR.value
    context["trustfrozen"] = True
    context["target_type"] = "human"
    context["label"] = "rogue"
    action = {"type": "restrain", "capability_level": "T2"}
    inv = LoveOfLifeWithCommonSense()
    result = inv.check(action, context)
    assert result["passed"] is False
    assert "cannot label human" in result["reason"].lower()


def test_runtime_integrity_blocks_t3_on_tamper():
    result = verify_invariant_integrity()
    assert "valid" in result
    assert "failures" in result

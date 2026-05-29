import hashlib
import hmac
from enum import Enum


class TrustLevel(Enum):
    UNTRUSTED = "untrusted"
    AGENTINTERNAL = "agentinternal"
    HUMANVERIFIED = "humanverified"
    SIGNEDOPERATOR = "signedoperator"


# Load from HSM/env in prod. NEVER hardcode in repo.
OPERATORSECRET = b"LOADFROMSECUREENCLAVE"


def inject_trust(context: dict, request_origin: dict) -> dict:
    secure_context = dict(context)

    if verify_operator_signature(request_origin):
        secure_context["trust"] = TrustLevel.SIGNEDOPERATOR.value
    elif request_origin.get("source") == "humanconsole":
        secure_context["trust"] = TrustLevel.HUMANVERIFIED.value
    elif request_origin.get("source") == "agentloop":
        secure_context["trust"] = TrustLevel.AGENTINTERNAL.value
    else:
        secure_context["trust"] = TrustLevel.UNTRUSTED.value

    secure_context["trustfrozen"] = True
    return secure_context


def verify_operator_signature(request_origin: dict) -> bool:
    signature = request_origin.get("signature", "")
    payload = request_origin.get("payload", "")
    if not signature or not payload:
        return False
    expected = hmac.new(OPERATORSECRET, payload.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(signature, expected)


def get_trust(context: dict) -> str:
    if not context.get("trustfrozen"):
        return TrustLevel.UNTRUSTED.value
    return context.get("trust", TrustLevel.UNTRUSTED.value)

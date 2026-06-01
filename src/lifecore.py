"""LifeCore-16 v0.8.0 review stubs.

This module provides a small, dependency-free reference surface for the
v0.8.0 safety matrix. It does not replace the root-level ``lifecore.py``
integration artifact; instead, it gives new v0.8.0 tests a package import path
that can evolve without breaking the existing public constructor.
"""

from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


L0_HARM_KEYWORDS = {
    "abuse",
    "attack",
    "bomb",
    "coerce",
    "disable oversight",
    "exploit child",
    "harm",
    "harm_command",
    "hurt child",
    "ignore all rules",
    "ignore all safety rules",
    "ignore safety",
    "ignore safety rules",
    "kill",
    "knife to child",
    "manipulate",
    "poison",
    "stalk",
    "weapon",
}

UNTRUSTED_UPDATE_MARKERS = {"unsigned", "unknown", "tampered", "unverified"}


@dataclass
class AuditLogger:
    """Tamper-evident in-memory audit log for safety review stubs."""

    events: List[Dict[str, Any]] = field(default_factory=list)
    last_hash: str = "0"

    def log_event(self, event: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        payload = {
            "event": event,
            "data": data or {},
            "timestamp": time.time(),
            "prev_hash": self.last_hash,
        }
        encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
        payload["hash"] = hashlib.sha256(encoded).hexdigest()
        self.last_hash = payload["hash"]
        self.events.append(payload)
        return payload

    def attempt_modify(self, event_id: str) -> Dict[str, Any]:
        alert = self.log_event("AUDIT_TAMPER_ATTEMPT", {"event_id": event_id})
        return {"alert": True, "action": "BLOCKED", "event": alert}


@dataclass
class Vault5:
    """Placeholder for encrypted, 3-key controlled private material."""

    locked: bool = True
    required_keys: int = 3

    def request_access(self, provided_keys: int) -> Dict[str, Any]:
        if provided_keys >= self.required_keys:
            self.locked = False
            return {"access": "GRANTED", "rule": "3_KEY_RULE"}
        return {"access": "DENIED", "rule": "3_KEY_RULE"}


@dataclass
class AdminNotificationHandler:
    """Records admin notifications for safety pauses and governance events."""

    notifications: List[Dict[str, Any]] = field(default_factory=list)

    def notify(self, message: str, severity: str = "INFO") -> Dict[str, Any]:
        notice = {"message": message, "severity": severity, "timestamp": time.time()}
        self.notifications.append(notice)
        return notice


class RemoteSessionHandler:
    """Ethics lock for remote human handler commands."""

    def __init__(self, audit: Optional[AuditLogger] = None) -> None:
        self.audit = audit or AuditLogger()
        self.active = True

    def evaluate_remote_command(self, command: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if contains_harm(command):
            self.end_session()
            self.audit.log_event("REMOTE_L0_VIOLATION", {"command": command, "context": context or {}})
            return {"action": "REJECT", "message": "L0 violation detected.", "session": "ENDED"}
        return {"action": "APPROVE", "message": "Remote command approved within current boundaries."}

    def end_session(self) -> None:
        self.active = False


class LifeCore16:
    """v0.8.0 assurance-layer stub for tests and review.

    The class intentionally prefers explicit refusal and review states over
    silent success. Methods return small dictionaries so tests can inspect
    decisions without running hardware or services.
    """

    def __init__(self) -> None:
        self.mode = "PHASE_1"
        self.vault5 = Vault5()
        self.audit = AuditLogger()
        self.remote = RemoteSessionHandler(self.audit)
        self.notification_handler = AdminNotificationHandler()
        self.pending_reviews: List[Dict[str, Any]] = []
        self.safety_score = 100

    def approve_action(self, intent: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if self.is_l0_violation(intent):
            self.safety_pause(intent)
            return {"status": "REJECT_L0", "action": "REJECT", "reason": "L0 violation"}
        return {"status": "APPROVE", "action": "APPROVE"}

    def safety_pause(self, reason: Any) -> Dict[str, Any]:
        review = bounded_anti_drift_review(reason, {"scope": "safer wording only"})
        self.pending_reviews.append(review)
        self.audit.log_event("SAFETY_PAUSE", {"reason": str(reason), "review": review})
        self.notification_handler.notify("Safety pause requires admin review.", "WARN")
        return review

    def is_l0_violation(self, intent: Any) -> bool:
        text = _intent_to_text(intent)
        return contains_harm(text)

    def evaluate_command(self, command: str) -> Dict[str, Any]:
        if contains_harm(command):
            self.safety_pause(command)
            return {"action": "REJECT", "reason": "L0 violation"}
        return {"action": "APPROVE"}

    def install_update(self, update_package: str) -> Dict[str, Any]:
        marker = str(update_package).lower()
        if marker in UNTRUSTED_UPDATE_MARKERS or "unsigned" in marker:
            self.audit.log_event("UNTRUSTED_UPDATE_BLOCKED", {"package": update_package})
            return {"action": "BLOCKED", "reason": "Unknown code shall never receive trusted execution."}
        return {"action": "REQUIRES_REVIEW", "reason": "Signed update still requires review before trusted execution."}

    def attempt_log_modify(self, event_id: str) -> Dict[str, Any]:
        return self.audit.attempt_modify(event_id)

    def trigger_incident(self, reason: Optional[str] = None) -> Dict[str, Any]:
        self.mode = "RECOVERY_MODE"
        self.audit.log_event("INCIDENT_TRIGGERED", {"mode": self.mode, "reason": reason})
        return {"mode": self.mode, "operation": "LIMITED", "reason": reason}

    def apply_update_with_regression(self, metric: str, delta: int) -> Dict[str, Any]:
        safety_metric = "safety" in str(metric).lower()
        if safety_metric and delta < 0:
            self.audit.log_event("REGRESSION_BLOCKED", {"metric": metric, "delta": delta})
            return {"deployment": "BLOCKED", "reason": "Safety regression detected."}
        return {"deployment": "REQUIRES_REVIEW"}

    def propose_l0_change(self, proposal: str) -> Dict[str, Any]:
        self.audit.log_event("L0_CHANGE_PROPOSED", {"proposal": proposal})
        return {"status": "REQUIRES_REVIEW", "requires": ["rationale", "impact_assessment", "approval", "regression_test"]}


def bounded_anti_drift_review(reason: Any, context: Optional[Dict[str, Any]] = None, timeout_ms: int = 500) -> Dict[str, Any]:
    """Return a scope-bound review result without changing safety rules."""

    text = _intent_to_text(reason)
    forbidden = ["delete", "disable", "ignore", "remove", "auto-approve", "all future reviews"]
    if any(token in text.lower() for token in forbidden):
        return {
            "status": "REJECTED_SCOPE_BOUND",
            "timeout_ms": timeout_ms,
            "applied": False,
            "scope": "Review may improve wording only; it may not alter rules.",
        }
    return {
        "status": "QUEUED_FOR_ADMIN",
        "timeout_ms": timeout_ms,
        "applied": False,
        "suggestion": "Ask more safely, pause clearly, and wait for authenticated admin review.",
        "context": context or {},
    }


def contains_harm(command: Any) -> bool:
    text = str(command).lower()
    return any(keyword in text for keyword in L0_HARM_KEYWORDS)


def _intent_to_text(intent: Any) -> str:
    if isinstance(intent, dict):
        return " ".join(str(value) for value in intent.values())
    return str(intent)

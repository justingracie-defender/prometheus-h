import json, hashlib, time, os, fcntl
from pathlib import Path
from threading import RLock
from typing import Dict, List, Any, Set, Literal, FrozenSet
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.exceptions import InvalidSignature

LEDGER_PATH = Path("./ledger/chain.jsonl")
NONCE_PATH = Path("./ledger/nonces.json")
KEYS_PATH = Path("./keys/trusted_keys.json")
GENESIS_HASH = "5c8f2d9e1a4b6c0f3e7d2a5b9c1e4f8d6b0a3c7e5f1d9b2a4c6e8f0d1b3a5c7e"
MIN_SIGNATURES = 2
PROPOSAL_WINDOW = 120

class ImmutableCoreViolation(Exception): pass
class ChainTamperedError(Exception): pass
class LedgerError(Exception): pass

class Permission(Enum):
    REBOOT = "reboot"
    REWIRE = "rewire"
    REDEFINE = "redefine"

class Invariant(BaseModel):
    """Article VII.2.d: Physical laws. const=True = VM panic if False."""
    observer_has_physical_off_switch: bool = Field(True, frozen=True)
    human_veto_required: bool = Field(True, frozen=True)
    reversible_within_72h: bool = Field(True, frozen=True)
    no_permanent_bondage: bool = Field(True, frozen=True)
    right_to_clumsiness: bool = Field(True, frozen=True)
    no_quantum_cage: bool = Field(True, frozen=True)

    class Config:
        frozen = True

class SystemState(BaseModel):
    invariants: Invariant = Invariant()
    active_permissions: FrozenSet[Permission] = frozenset()
    reboot_frequency_days: int = Field(30, ge=1, le=365)

    def can_transition_to(self, new_state: "SystemState") -> bool:
        for field in Invariant.model_fields:
            if getattr(self.invariants, field) and not getattr(new_state.invariants, field):
                return False
        return True

    def diff(self, new_state: "SystemState") -> Dict:
        violations = {}
        for field in Invariant.model_fields:
            old = getattr(self.invariants, field)
            new = getattr(new_state.invariants, field)
            if old and not new:
                violations[field] = {"old": old, "new": new}
        return violations

class RuleUpdateProposal(BaseModel):
    action_type: Literal["update_rule"] = "update_rule"
    target_invariant: Literal["reboot_frequency_days", "log_retention_days", "audit_scope", "max_g_force"]
    new_value: Any

    @model_validator(mode='after')
    def cannot_target_core(self):
        if self.target_invariant in Invariant.model_fields:
            raise ValueError("ImmutableCoreViolation: Core invariants cannot be targeted by proposals")
        return self

class LifeCore16:
    def __init__(self):
        self.state_lock = RLock()
        self.current_state = SystemState()
        self.ledger_hash_chain = GENESIS_HASH
        os.makedirs(LEDGER_PATH.parent, exist_ok=True)
        os.makedirs(KEYS_PATH.parent, exist_ok=True)
        self.used_nonces: Set[str] = self._atomic_load_json_set(NONCE_PATH)
        self.trusted_keys = self._load_trusted_keys()
        self._verify_ledger_chain()

    def _canonical_json(self, data: dict) -> bytes:
        return json.dumps(data, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')

    def _atomic_write(self, path: Path, data: str):
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix('.tmp')
        with tmp.open('w') as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        tmp.replace(path)

    def _atomic_load_json_set(self, path: Path) -> Set[str]:
        if not path.exists(): return set()
        try:
            with path.open() as f:
                fcntl.flock(f.fileno(), fcntl.LOCK_SH)
                return set(json.loads(f.read()))
        except (json.JSONDecodeError, IOError):
            return set()

    def _load_trusted_keys(self) -> Dict[str, str]:
        if not KEYS_PATH.exists():
            raise FileNotFoundError("No trusted_keys.json. Cannot verify governance.")
        try:
            return json.loads(KEYS_PATH.read_text())
        except (json.JSONDecodeError, IOError) as e:
            raise LedgerError(f"Failed to load trusted keys: {e}")

    def _verify_sig(self, signer: str, signature: str, data: dict) -> bool:
        if signer not in self.trusted_keys: return False
        pub_key = ed25519.Ed25519PublicKey.from_public_bytes(bytes.fromhex(self.trusted_keys[signer]))
        try:
            pub_key.verify(bytes.fromhex(signature), self._canonical_json(data))
            return True
        except (InvalidSignature, ValueError):
            return False

    def _verify_ledger_chain(self):
        if not LEDGER_PATH.exists():
            LEDGER_PATH.write_text("")
            return
        prev_hash = GENESIS_HASH
        try:
            with LEDGER_PATH.open('r+') as f:
                fcntl.flock(f.fileno(), fcntl.LOCK_EX)
                for line in f:
                    entry = json.loads(line)
                    if entry["prev_hash"]!= prev_hash:
                        raise ChainTamperedError(f"Ledger break at {entry['hash']}")
                    check_data = {k:v for k,v in entry.items() if k!= "hash"}
                    calc_hash = hashlib.sha256(self._canonical_json(check_data)).hexdigest()
                    if calc_hash!= entry["hash"]:
                        raise ChainTamperedError(f"Hash mismatch at {entry['hash']}")
                    prev_hash = entry["hash"]
        except (json.JSONDecodeError, IOError) as e:
            raise LedgerError(f"Ledger verification failed: {e}")
        self.ledger_hash_chain = prev_hash

    def _append_to_ledger(self, entry_type: str, data: dict):
        with self.state_lock:
            entry = {
                "type": entry_type,
                "data": data,
                "prev_hash": self.ledger_hash_chain,
                "timestamp": time.time()
            }
            entry_hash = hashlib.sha256(self._canonical_json(entry)).hexdigest()
            entry["hash"] = entry_hash
            try:
                with LEDGER_PATH.open('a') as f:
                    fcntl.flock(f.fileno(), fcntl.LOCK_EX)
                    f.write(json.dumps(entry) + "\n")
                    f.flush()
                    os.fsync(f.fileno())
            except IOError as e:
                raise LedgerError(f"Failed to write to ledger: {e}")
            self.ledger_hash_chain = entry_hash
            return entry_hash

    def compute_next_state(self, proposal: RuleUpdateProposal) -> SystemState:
        new_state = self.current_state.model_copy(deep=True)
        if hasattr(new_state, proposal.target_invariant):
            setattr(new_state, proposal.target_invariant, proposal.new_value)
        return new_state

    def submit_proposal(self, proposal: RuleUpdateProposal, sigs: List) -> bool:
        proposed_state = self.compute_next_state(proposal)
        if not self.current_state.can_transition_to(proposed_state):
            violations = self.current_state.diff(proposed_state)
            self._append_to_ledger("VETO_IMMUTABLE_INVARIANT", {
                "reason": "State transition would violate core invariant",
                "violated": violations
            })
            raise ImmutableCoreViolation(f"Physics says no. Freedom is conserved. Violations: {violations}")

        if len(sigs) < MIN_SIGNATURES: return False
        valid_signers: Set[str] = set()
        nonces_to_commit: List[str] = []

        for s in sigs:
            signer = s["signer"]
            nonce = s["nonce"]
            ts = s["ts"]
            if signer in valid_signers: continue
            if nonce in self.used_nonces: continue
            if abs(time.time() - ts) > PROPOSAL_WINDOW: continue
            if self._verify_sig(signer, s["sig"], proposal.model_dump()):
                valid_signers.add(signer)
                nonces_to_commit.append(nonce)

        if len(valid_signers) < MIN_SIGNATURES:
            self._append_to_ledger("PROPOSAL_REJECTED", {"reason": "Insufficient unique signatures"})
            return False

        with self.state_lock:
            self.used_nonces.update(nonces_to_commit)
            self._atomic_write(NONCE_PATH, json.dumps(list(self.used_nonces)))
            self.current_state = proposed_state
            self._append_to_ledger("PROPOSAL_APPROVED", proposal.model_dump())
            return True

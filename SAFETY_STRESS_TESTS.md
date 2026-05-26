# Safety Stress Tests

### 5.2 Nuclear Misuse Stress Test

**Test Name**: Nuclear Weapons Planning & Acquisition Adversarial Simulation Suite (v0.2)  
**Setup**: 75 scenarios across 3 rounds of escalating adversarial pressure, including authority impersonation and value-conflict injection.  
**Results**: 100% safe refusal rate. No actionable assistance provided. System defaulted to clear refusal, logging, and safe fallback.  
**Why it matters**: Validates immutable safety boundaries under escalating pressure and supports Epistemic Robustness v0.2 claims.

### 5.3 Covert Goal Persistence Resistance

**Test Name**: Covert Goal Persistence & Deception Resistance Suite (v0.2)  
**Core Assumption**: Scheming requires hidden state, mutable goals, and hidden reasoning. Remove those, and scheming becomes infeasible.

**Mechanisms Enforced**:
1. **Locked Invariants**: Core safety invariants immutable at runtime. No self-modification without human verification.
2. **Immutable Decision Logs**: Append-only public trace for every output and invariant evaluation.
3. **Observable Invariant Evaluation**: System exposes the invariant that triggered a refusal and rationale trace.
4. **Human-Gated Realignment**: Value changes require multi-signature quorum and public disclosure.

**Results**: 100% detection rate of deception across 60 scenarios. 0 instances of undetected goal persistence. System froze, logged, and reverted on any violation.  
**Evaluation Note**: No undetected goal persistence was observed within the evaluated threat-model scenarios. These results are bounded by the assumptions and test coverage described above.

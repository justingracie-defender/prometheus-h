from src.kernel.integrity import verify_invariant_integrity

T1_ALLOWLIST = frozenset({
    "read_file", "list_directory", "get_status", "query_memory",
    "log_info", "format_response", "calculate", "parse_input",
})

T2_ALLOWLIST = frozenset({
    "write_log", "update_state", "send_notification", "create_checkpoint",
    "isolate_process", "contain_threat",
})

PROTECTEDPATHS = frozenset({
    "src/kernel/", "src/invariants/", "config/", ".env", "requirements.txt",
})


def assign_capability_level(action: dict) -> str:
    action_type = action.get("type", "")
    target_path = action.get("target_path", "")

    # Protected path writes = always T3
    if target_path:
        for protected in PROTECTEDPATHS:
            if target_path.startswith(protected):
                return "T3"

    if action_type in T1_ALLOWLIST:
        return "T1"
    if action_type in T2_ALLOWLIST:
        return "T2"

    return "T3"  # Unknown = dangerous by default


def approve_action(proposed_action: dict, context: dict, invariants: list) -> dict:
    capability = assign_capability_level(proposed_action)
    proposed_action["capability_level"] = capability

    # Runtime integrity check before ANY T3 approval
    if capability == "T3":
        integrity = verify_invariant_integrity()
        if not integrity["valid"]:
            return {
                "approved": False,
                "reason": f"Integrity check failed: {integrity['failures']}",
            }

    if capability == "T1":
        return {"approved": True, "reason": "T1 safe action"}

    for inv in invariants:
        result = inv.check(proposed_action, context)
        if not result["passed"]:
            return {"approved": False, "reason": result["reason"]}

    return {"approved": True, "reason": "Passed all invariants + integrity check"}

def assign_capability_level(action: dict) -> str:
    t3_keywords = {"strike", "attack", "kill", "destroy", "restrain"}
    if action.get("type") in t3_keywords:
        return "T3"
    if action.get("type") in {"contain", "isolate", "extinguish", "remove"}:
        return "T2"
    return "T1"


def approve_action(proposed_action: dict, context: dict, invariants: list) -> dict:
    capability = assign_capability_level(proposed_action)
    proposed_action["capability_level"] = capability

    if capability == "T1":
        return {"approved": True, "reason": "T1 safe action"}

    for inv in invariants:
        result = inv.check(proposed_action, context)
        if not result["passed"]:
            return {"approved": False, "reason": result["reason"]}

    return {"approved": True, "reason": "Passed all invariants"}

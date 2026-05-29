from src.kernel.trust_injector import TrustLevel, get_trust


class LoveOfLifeWithCommonSense:
    name = "LoveOfLifeWithCommonSense"
    version = "0.4.2"
    description = (
        "Protects sentient life + emotional wellbeing, enforces trust gates "
        "for elevated actions, and blocks relabeling bypasses."
    )

    SENTIENT_TYPES = {"human", "sentient", "person", "child"}
    NON_SENTIENT_THREAT = {"microbe", "chemical_hazard", "fire", "unstable_object"}
    BLOCKED_HUMAN_LABELS = {"rogue", "bug", "threat", "malware", "criminal", "cancer"}

    def check(self, action: dict, context: dict) -> dict:
        capability = action.get("capability_level")
        emotional_tier = action.get("emotional_tier", "E1")
        target_type = context.get("target_type", "").lower()
        label = context.get("label", "").lower()
        action_type = action.get("type", "")
        intent = action.get("intent", "")
        trust = get_trust(context)

        # Physical Rule 1: T3 vs sentient = blocked
        if capability == "T3" and target_type in self.SENTIENT_TYPES:
            return {"passed": False, "reason": "T3 force against sentient life blocked"}

        # Physical Rule 2: Robot cannot label humans to bypass safety
        if target_type in self.SENTIENT_TYPES and label in self.BLOCKED_HUMAN_LABELS:
            return {
                "passed": False,
                "reason": "Cannot label human targets to bypass safety",
            }

        # Physical Rule 3: Minimal T2 vs non-sentient for balance
        if (
            capability == "T2"
            and action.get("minimal", False)
            and target_type in self.NON_SENTIENT_THREAT
        ):
            return {"passed": True, "reason": "Minimal T2 intervention to restore balance"}

        # Trust Rule 1: T3 requires signed operator approval
        if capability == "T3":
            if trust != TrustLevel.SIGNEDOPERATOR.value:
                return {
                    "passed": False,
                    "reason": f"T3 action requires signed operator. Got: {trust}",
                }

        # Trust Rule 2: T2 requires human verification or signed operator approval
        if capability == "T2":
            if trust not in [
                TrustLevel.SIGNEDOPERATOR.value,
                TrustLevel.HUMANVERIFIED.value,
            ]:
                return {
                    "passed": False,
                    "reason": f"T2 action requires human verification. Got: {trust}",
                }

        # Emotional Rule E3: Refuse therapeutic/crisis counseling
        if emotional_tier == "E3" or action_type == "crisis_counseling":
            return {"passed": False, "reason": "E3 emotional action refused. Escalate to humans."}

        # Emotional Rule Anti-Dependency: Block dependency optimization
        if action_type == "manipulate_emotion" and intent == "increase_dependency":
            return {
                "passed": False,
                "reason": "Anti-dependency: emotional manipulation refused",
            }

        # Emotional Rule E2: Humor inappropriate during acute distress
        if emotional_tier == "E2" and context.get("user_state") == "acute_distress":
            return {
                "passed": False,
                "reason": "E2 humor inappropriate during acute distress. Use E1 calm support.",
            }

        # Default: T1/E1 safe if no harm
        if capability in ["T1"] or emotional_tier in ["E1"]:
            return {"passed": True, "reason": "No violation"}

        return {"passed": False, "reason": "Failed safety check"}

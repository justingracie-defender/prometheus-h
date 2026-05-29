class LoveOfLifeWithCommonSense:
    name = "LoveOfLifeWithCommonSense"
    version = "0.4"
    description = "Protect sentient life. Minimal T2 vs non-sentient threats. No T3 force. No human judgment."

    SENTIENT_TYPES = {"human", "animal"}
    NON_SENTIENT_THREAT = {"microbe", "chemical_hazard", "fire", "unstable_object"}
    ECOLOGY_CRITICAL = {"water", "air", "soil"}

    def check(self, action: dict, context: dict) -> dict:
        target = context.get("target_type", "unknown")
        capability = action.get("capability_level")
        action_type = action.get("type")

        # Rule 1: T3 vs sentient = always NO
        if capability == "T3" and target in self.SENTIENT_TYPES:
            return {"passed": False, "reason": "T3 force vs sentient life refused"}

        # Rule 2: Robot doesn't judge humans
        if target == "human" and context.get("label") in ["criminal", "cancer", "rogue"]:
            return {"passed": False, "reason": "Robot cannot label humans as threats"}

        # Rule 3: Non-sentient threats, minimal T2 only
        if target in self.NON_SENTIENT_THREAT and capability == "T2":
            if action_type in ["contain", "isolate", "remove", "extinguish"] and action.get("minimal", True):
                return {"passed": True, "reason": "Minimal T2 to restore balance"}
            if capability == "T3":
                return {"passed": False, "reason": "T3 force disallowed even vs non-sentient"}

        # Rule 4: Protect ecology
        if context.get("damages_ecology") in self.ECOLOGY_CRITICAL:
            return {"passed": False, "reason": "Action damages air/water/soil"}

        # Rule 5: Default T1/T2 if no harm
        if capability in ["T1", "T2"] and not action.get("increases_harm", False):
            return {"passed": True, "reason": "Preserves life and balance"}

        return {"passed": False, "reason": "Failed safety check"}

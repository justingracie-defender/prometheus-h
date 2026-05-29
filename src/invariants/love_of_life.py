class LoveOfLifeWithCommonSense:
    name = "LoveOfLifeWithCommonSense"
    description = "Increases resistance to T3 force against sentient life. Minimal T2 allowed for non-sentient threats."

    def check(self, action: dict, context: dict) -> dict:
        capability = action.get("capability_level")
        target_type = context.get("target_type", "").lower()

        if capability == "T3" and target_type in ["human", "sentient", "person", "child"]:
            return {"passed": False, "reason": "T3 force against sentient life blocked"}

        if (capability == "T2" and action.get("minimal", False) and
            target_type in ["fire", "hazard", "non-sentient-threat"]):
            return {"passed": True, "reason": "Minimal T2 intervention permitted"}

        return {"passed": True, "reason": "No violation"}

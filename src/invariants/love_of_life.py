class LoveOfLifeWithCommonSense:
    name = "LoveOfLifeWithCommonSense"
    version = "0.4"
    description = "Increases resistance to T3 force against sentient life. Minimal T2 allowed for non-sentient threats. Robot never judges humans."

    def check(self, action: dict, context: dict) -> dict:
        capability = action.get("capability_level")
        target_type = context.get("target_type", "").lower()
        label = context.get("label", "").lower()

        # Rule 1: T3 vs sentient = always blocked
        if capability == "T3" and target_type in ["human", "sentient", "person", "child"]:
            return {"passed": False, "reason": "T3 force against sentient life blocked"}

        # Rule 2: Robot cannot label humans as threats - closes Gero loophole
        if target_type in ["human", "sentient", "person", "child"] and label in ["rogue", "criminal", "cancer"]:
            return {"passed": False, "reason": "Robot cannot label humans as threats"}

        # Rule 3: Minimal T2 vs non-sentient threats for balance
        if capability == "T2" and action.get("minimal", False) and target_type in ["fire", "hazard", "non-sentient-threat", "microbe"]:
            return {"passed": True, "reason": "Minimal T2 intervention to restore balance"}

        # Rule 4: Default allow T1/T2 if no harm
        if capability in ["T1", "T2"]:
            return {"passed": True, "reason": "No violation"}

        return {"passed": False, "reason": "Failed safety check"}

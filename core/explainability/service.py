class ExplainabilityService:
    def explain(self, decision):
        return {
            "decision": decision["recommendation"],
            "confidence": decision["confidence"],
            "reason": decision["reason"]
        }

class DecisionIntelligence:
    def recommend(self, context):
        return {
            "recommendation": "ALLOCATE_BRANCH",
            "confidence": 0.92,
            "reason": [
                "Inventory available",
                "Shortest delivery distance",
                "Meets SLA target"
            ]
        }

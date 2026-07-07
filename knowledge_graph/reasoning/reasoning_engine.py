class ReasoningEngine:

    def analyze(self, graph):

        if graph.get("relation") == "CAUSES":
            insight = "Potential operational impact detected"
        else:
            insight = "Relationship recorded"

        return {
            "insight": insight,
            "confidence": 0.85
        }

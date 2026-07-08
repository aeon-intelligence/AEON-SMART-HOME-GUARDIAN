"""
Decision Orchestrator Interface
"""


class DecisionOrchestrator:

    def evaluate(self, recommendation: dict):

        return {
            "recommendation": recommendation,
            "human_review": True,
            "approved_for_execution": False
        }

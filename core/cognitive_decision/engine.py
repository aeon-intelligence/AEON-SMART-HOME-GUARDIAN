"""
AEON MATRIX Enterprise Cognitive Decision Engine

Convert fused intelligence into governed
decision recommendations.
"""


class CognitiveDecisionEngine:

    def evaluate(self, intelligence: dict):

        fusion_score = intelligence.get(
            "fusion_score",
            0
        )

        risk_level = intelligence.get(
            "risk_level",
            0
        )

        confidence = max(
            0,
            min(
                100,
                fusion_score - risk_level
            )
        )

        if confidence >= 80:
            decision = "AUTONOMOUS_RECOMMENDATION"

        elif confidence >= 50:
            decision = "GUARDIAN_REVIEW_REQUIRED"

        else:
            decision = "HUMAN_DECISION_REQUIRED"

        return {
            "confidence_score": confidence,
            "decision": decision,
            "guardian_validation": True,
            "audit_required": True
        }

"""
AEON MATRIX Outcome Learning Engine

Learn from execution results and improve future recommendations.
"""


class OutcomeLearningEngine:

    def evaluate(self, outcome: dict):

        expected = outcome.get(
            "expected_score",
            0
        )

        actual = outcome.get(
            "actual_score",
            0
        )

        variance = actual - expected

        if variance >= 0:
            learning_status = "POSITIVE_LEARNING"
        else:
            learning_status = "ADJUST_MODEL"

        return {
            "learning_completed": True,
            "variance": variance,
            "learning_status": learning_status,
            "future_adjustment_required": variance < 0
        }

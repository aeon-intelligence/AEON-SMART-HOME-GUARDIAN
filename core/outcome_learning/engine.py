"""
AEON MATRIX Enterprise Outcome Learning Engine

Learn from execution results and improve
future decision quality.
"""


class OutcomeLearningEngine:

    def evaluate(self, outcome: dict):

        expected = outcome.get(
            "expected_result",
            0
        )

        actual = outcome.get(
            "actual_result",
            0
        )

        variance = actual - expected

        if variance >= 0:
            learning_state = "POSITIVE_OUTCOME"

        elif variance >= -20:
            learning_state = "MINOR_ADJUSTMENT_REQUIRED"

        else:
            learning_state = "POLICY_REVIEW_REQUIRED"

        return {
            "variance": variance,
            "learning_state": learning_state,
            "feedback_generated": True,
            "guardian_validation": True
        }

    def generate_feedback(self, result):

        return {
            "feedback_type": "MODEL_IMPROVEMENT",
            "source": result.get(
                "learning_state"
            ),
            "update_required": True
        }

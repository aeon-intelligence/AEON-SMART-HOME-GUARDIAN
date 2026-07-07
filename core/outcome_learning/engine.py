"""
AEON MATRIX Outcome Learning Engine

Learn from execution outcomes and improve
future intelligence decisions.
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

        variance = abs(
            expected - actual
        )

        if variance <= 10:
            learning_status = "MODEL_CONFIRMED"

        elif variance <= 30:
            learning_status = "MODEL_ADJUSTMENT_REQUIRED"

        else:
            learning_status = "RETRAINING_REQUIRED"

        accuracy = max(
            100 - variance,
            0
        )

        return {
            "accuracy_score": accuracy,
            "learning_status": learning_status,
            "feedback_generated": True
        }

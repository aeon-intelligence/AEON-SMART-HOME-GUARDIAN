"""
AEON MATRIX Margin Erosion Intelligence Engine

Detect hidden profit loss and recommend recovery actions.
"""


class MarginErosionEngine:

    def analyze(self, business_signal: dict):

        discount_loss = business_signal.get(
            "discount_loss",
            0
        )

        waste_cost = business_signal.get(
            "waste_cost",
            0
        )

        promotion_efficiency = business_signal.get(
            "promotion_efficiency",
            100
        )

        erosion_score = (
            discount_loss +
            waste_cost +
            (100 - promotion_efficiency)
        ) / 3

        if erosion_score >= 80:
            action = "EXECUTIVE_REVIEW"

        elif erosion_score >= 50:
            action = "OPTIMIZE_STRATEGY"

        else:
            action = "NORMAL_MARGIN_CONTROL"

        return {
            "margin_erosion_score": round(
                erosion_score,
                2
            ),
            "recommended_action": action
        }

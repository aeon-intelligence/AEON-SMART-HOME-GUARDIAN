"""
AEON MATRIX Dynamic Bundling Strategy AI

Optimize product combinations using demand,
margin and inventory signals.
"""


class DynamicBundlingEngine:

    def recommend(self, signal: dict):

        demand_score = signal.get(
            "demand_score",
            0
        )

        margin_score = signal.get(
            "margin_score",
            0
        )

        inventory_risk = signal.get(
            "inventory_risk",
            0
        )

        if inventory_risk >= 80:
            strategy = "CLEARANCE_BUNDLE"

        elif demand_score >= 80 and margin_score >= 70:
            strategy = "PREMIUM_BUNDLE"

        elif demand_score >= 50:
            strategy = "CROSS_SELL_BUNDLE"

        else:
            strategy = "NO_BUNDLE_ACTION"

        return {
            "strategy": strategy,
            "confidence": self.calculate_confidence(
                demand_score,
                margin_score
            )
        }

    def calculate_confidence(self, demand, margin):

        return round(
            min((demand + margin) / 2, 100),
            2
        )

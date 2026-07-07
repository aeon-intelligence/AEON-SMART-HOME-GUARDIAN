"""
AEON MATRIX Enterprise Digital Twin Simulator

Simulate possible outcomes before execution.
"""


class DigitalTwinSimulator:

    def simulate(self, scenario: dict):

        demand_change = scenario.get(
            "demand_change",
            0
        )

        supply_risk = scenario.get(
            "supply_risk",
            0
        )

        operational_impact = (
            demand_change -
            supply_risk
        )

        if operational_impact >= 50:
            recommendation = "EXECUTE_PLAN"

        elif operational_impact >= 0:
            recommendation = "OPTIMIZE_PLAN"

        else:
            recommendation = "REVIEW_REQUIRED"

        return {
            "simulated_impact": operational_impact,
            "recommendation": recommendation,
            "requires_guardian_check": True
        }

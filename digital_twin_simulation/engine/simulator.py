class ScenarioSimulator:

    def run(self, scenario):

        inventory = scenario["variables"].get(
            "inventory",
            0
        )

        demand = scenario["variables"].get(
            "demand",
            0
        )

        gap = demand - inventory

        return {
            "scenario": scenario["scenario"],
            "inventory_gap": gap,
            "status": (
                "RISK"
                if gap > 0
                else "STABLE"
            )
        }

class OperationalWorkflow:

    def run(self, order):

        return {
            "order": order,
            "status": "SIMULATION_COMPLETED",
            "next": "ExecutiveDashboard"
        }

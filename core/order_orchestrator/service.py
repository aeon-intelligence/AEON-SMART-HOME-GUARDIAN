class OrderOrchestrator:

    def process(self, order):

        return {
            "status":"processing",
            "workflow":[
                "Validate",
                "ReserveInventory",
                "AllocateBranch",
                "CreateShipment"
            ]
        }

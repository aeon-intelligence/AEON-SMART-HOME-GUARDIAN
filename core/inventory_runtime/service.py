class InventoryRuntime:
    def process_inventory_event(self, event):
        return {
            "status": "processed",
            "event_type": event.get("type"),
            "sku": event.get("sku"),
            "branch": event.get("branch")
        }

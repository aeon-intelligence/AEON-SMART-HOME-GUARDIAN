class InventorySyncService:
    def sync(self, event):
        return {
            "status": "synced",
            "sku": event.get("sku"),
            "branch": event.get("branch"),
            "quantity": event.get("quantity")
        }

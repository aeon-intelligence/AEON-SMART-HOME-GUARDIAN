from core.inventory_sync.service import InventorySyncService

def test_inventory_sync():
    service = InventorySyncService()
    result = service.sync({
        "sku": "SKU-001",
        "branch": "BR001",
        "quantity": 10
    })
    assert result["status"] == "synced"

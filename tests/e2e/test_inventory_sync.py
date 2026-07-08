from core.inventory_runtime.service import InventoryRuntime

def test_inventory_runtime():
    runtime = InventoryRuntime()
    result = runtime.process_inventory_event({
        "type":"InventoryUpdated",
        "sku":"SKU-001",
        "branch":"BR001"
    })

    assert result["status"] == "processed"

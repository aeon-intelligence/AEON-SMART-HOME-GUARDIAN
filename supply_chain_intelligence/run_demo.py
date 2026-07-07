from supply_chain_intelligence.demand.demand_engine import predict
from supply_chain_intelligence.inventory.inventory_optimizer import optimize
from supply_chain_intelligence.supplier.supplier_risk import analyze
from supply_chain_intelligence.logistics.logistics_adapter import adapt
from supply_chain_intelligence.memory.supply_chain_memory import save


demand = predict(
    "FAST_MOVING_SKU"
)

inventory = optimize(
    "WAREHOUSE_STOCK"
)

supplier = analyze(
    "SUPPLIER_NETWORK"
)

logistics = adapt(
    "DELIVERY_NETWORK"
)

print(demand)
print(inventory)
print(supplier)
print(logistics)
print(save(logistics))

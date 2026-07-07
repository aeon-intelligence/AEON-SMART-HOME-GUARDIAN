from resource_optimization.registry.resource_registry import register
from resource_optimization.capacity.capacity_analyzer import analyze
from resource_optimization.allocation.allocation_engine import allocate
from resource_optimization.monitor.utilization_monitor import monitor
from resource_optimization.memory.resource_memory import save


resource = register(
    "WAREHOUSE_CAPACITY",
    "LOGISTICS_RESOURCE"
)

capacity = analyze(
    resource
)

allocation = allocate(
    resource,
    "HIGH_DEMAND_PERIOD"
)

utilization = monitor(
    allocation
)

print(resource)
print(capacity)
print(allocation)
print(utilization)
print(save(utilization))

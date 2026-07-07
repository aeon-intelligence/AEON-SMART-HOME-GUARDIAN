from operations_control_tower.monitor.operations_monitor import monitor
from operations_control_tower.resource.resource_controller import allocate
from operations_control_tower.priority.action_priority import prioritize
from operations_control_tower.dashboard.control_dashboard import generate
from operations_control_tower.memory.operations_memory import save


operation = monitor(
    "WAREHOUSE_OPERATION"
)

resource = allocate(
    "LOGISTICS_CAPACITY"
)

priority = prioritize(
    [
        "RESTOCK_CRITICAL_SKU",
        "OPTIMIZE_ROUTE"
    ]
)

dashboard = generate(
    [
        operation,
        resource,
        priority
    ]
)

print(operation)
print(resource)
print(priority)
print(dashboard)
print(save(dashboard))

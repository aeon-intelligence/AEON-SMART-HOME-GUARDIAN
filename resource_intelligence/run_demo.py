from resource_intelligence.analyzer.resource_analyzer import analyze
from resource_intelligence.allocation.dynamic_allocator import allocate
from resource_intelligence.capacity.capacity_optimizer import optimize
from resource_intelligence.cost.cost_planner import plan
from resource_intelligence.memory.resource_memory import save


resource = analyze(
    "LOGISTICS_RESOURCES"
)

allocation = allocate(
    resource
)

capacity = optimize(
    "WAREHOUSE_CAPACITY"
)

cost = plan(
    "OPERATION_COST"
)

print(resource)
print(allocation)
print(capacity)
print(cost)
print(save(allocation))

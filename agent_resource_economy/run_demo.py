from agent_resource_economy.registry.agent_registry import register
from agent_resource_economy.compute.compute_allocator import allocate_compute
from agent_resource_economy.scheduler.priority_scheduler import schedule
from agent_resource_economy.budget.budget_controller import check_budget
from agent_resource_economy.memory.resource_memory import save


agent = register(
    "Forecast_Agent",
    "Demand Prediction"
)

compute = allocate_compute(
    agent["agent"],
    "HIGH"
)

task = schedule(
    "INVENTORY_OPTIMIZATION",
    "CRITICAL"
)

budget = check_budget(
    72
)

print(agent)
print(compute)
print(task)
print(budget)
print(save(task))

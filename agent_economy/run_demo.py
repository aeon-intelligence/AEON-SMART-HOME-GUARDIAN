from agent_economy.pool.resource_pool import AgentResourcePool
from agent_economy.matching.capability_matcher import match_agent
from agent_economy.allocation.task_allocator import TaskAllocator
from agent_economy.optimization.resource_optimizer import optimize
from agent_economy.audit.allocation_audit import log_allocation


pool = AgentResourcePool()

pool.register(
    "Forecast Agent",
    "DEMAND_FORECAST",
    80
)

pool.register(
    "Insight Agent",
    "BUSINESS_ANALYSIS",
    70
)


agent = match_agent(
    "DEMAND_FORECAST",
    pool.agents
)


allocation = TaskAllocator().allocate(
    "Demand Prediction",
    agent
)

print(allocation)
print(optimize(agent))
print(log_allocation(allocation))

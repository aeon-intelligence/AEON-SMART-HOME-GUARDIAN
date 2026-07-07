from multi_agent_intelligence.registry.agent_registry import register
from multi_agent_intelligence.communication.agent_protocol import send
from multi_agent_intelligence.delegation.task_delegator import assign
from multi_agent_intelligence.coordinator.agent_coordinator import coordinate
from multi_agent_intelligence.memory.agent_memory import save


guardian = register(
    "GUARDIAN_AGENT",
    "GOVERNANCE"
)

forecast = register(
    "FORECAST_AGENT",
    "PREDICTION"
)

message = send(
    guardian["agent"],
    forecast["agent"],
    "ANALYZE_DEMAND_SIGNAL"
)

task = assign(
    "DEMAND_ANALYSIS",
    forecast["agent"]
)

coordination = coordinate(
    [
        message,
        task
    ]
)

print(guardian)
print(forecast)
print(message)
print(task)
print(coordination)
print(save(coordination))

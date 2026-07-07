from multi_agent_orchestration.registry.agent_registry import register
from multi_agent_orchestration.coordinator.agent_coordinator import coordinate
from multi_agent_orchestration.dispatcher.task_dispatcher import dispatch
from multi_agent_orchestration.monitor.agent_monitor import monitor
from multi_agent_orchestration.memory.agent_memory import save


agents = [
    register("GUARDIAN_AI", "GOVERNANCE"),
    register("FORECAST_AGENT", "PREDICTION"),
    register("DATA_AGENT", "INTELLIGENCE"),
    register("INSIGHT_AGENT", "ANALYSIS")
]

coordination = coordinate(
    agents
)

task = dispatch(
    "OPTIMIZE_ENTERPRISE_OPERATION"
)

health = monitor(
    agents
)

print(agents)
print(coordination)
print(task)
print(health)
print(save(task))

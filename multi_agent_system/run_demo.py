from multi_agent_system.agents.agent_registry import AgentRegistry
from multi_agent_system.memory.agent_memory import AgentMemory
from multi_agent_system.bus.communication_bus import AgentBus
from multi_agent_system.coordinator.agent_coordinator import AgentCoordinator
from multi_agent_system.signals.collaboration_signal import create_signal


registry = AgentRegistry()

registry.register(
    "Forecast Agent",
    "Demand Prediction"
)

registry.register(
    "Insight Agent",
    "Business Analysis"
)

memory = AgentMemory()

memory.store(
    "Forecast Agent",
    "Demand pressure detected"
)

bus = AgentBus()

print(
    bus.publish(
        "Forecast Agent",
        "Send prediction to Insight Agent"
    )
)

print(
    AgentCoordinator().coordinate(
        list(registry.agents.keys())
    )
)

print(
    memory.memory
)

print(
    create_signal()
)

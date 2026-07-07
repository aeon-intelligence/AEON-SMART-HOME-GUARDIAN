from autonomous_workflow.agents.agent_registry import register_agent
from autonomous_workflow.orchestrator.workflow_engine import create_workflow
from autonomous_workflow.priority.priority_engine import assign_priority
from autonomous_workflow.bus.agent_bus import send_message
from autonomous_workflow.memory.workflow_memory import save


forecast_agent = register_agent(
    "Forecast_Agent",
    "Demand Prediction"
)

logistics_agent = register_agent(
    "Logistics_Agent",
    "Route Optimization"
)

workflow = create_workflow(
    "INVENTORY_OPTIMIZATION"
)

priority = assign_priority(
    workflow["workflow"],
    "HIGH"
)

message = send_message(
    forecast_agent["agent"],
    logistics_agent["agent"],
    "Demand forecast ready"
)

print(forecast_agent)
print(logistics_agent)
print(workflow)
print(priority)
print(message)
print(save(workflow))

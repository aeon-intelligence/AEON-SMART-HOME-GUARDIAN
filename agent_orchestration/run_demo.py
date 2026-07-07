from agent_orchestration.registry.agent_registry import register_agent
from agent_orchestration.workflow.workflow_engine import create_workflow
from agent_orchestration.allocation.task_allocator import allocate
from agent_orchestration.guardian.policy_gate import check_policy
from agent_orchestration.memory.execution_memory import save_execution


agents = [
    register_agent(
        "Forecast_Agent",
        "Demand Prediction"
    ),
    register_agent(
        "Guardian_Agent",
        "Governance"
    )
]


workflow = create_workflow(
    "Inventory Optimization"
)

task = allocate(
    workflow["workflow"],
    agents
)

policy = check_policy(
    task
)

print(agents)
print(workflow)
print(task)
print(policy)
print(save_execution(policy))

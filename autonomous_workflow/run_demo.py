from autonomous_workflow.definition.workflow_engine import create
from autonomous_workflow.routing.task_router import route
from autonomous_workflow.approval.approval_controller import request
from autonomous_workflow.optimization.process_optimizer import optimize
from autonomous_workflow.memory.workflow_memory import save


workflow = create(
    "INVENTORY_REPLENISHMENT",
    [
        "CHECK_STOCK",
        "ANALYZE_DEMAND",
        "APPROVE_ORDER"
    ]
)

routing = route(
    "DEMAND_ANALYSIS",
    "FORECAST_AGENT"
)

approval = request(
    "AUTO_PURCHASE_ORDER"
)

optimization = optimize(
    workflow
)

print(workflow)
print(routing)
print(approval)
print(optimization)
print(save(optimization))

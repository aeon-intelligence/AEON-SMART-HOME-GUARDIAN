from autonomous_workflow.planner.workflow_planner import WorkflowPlanner
from autonomous_workflow.orchestrator.task_orchestrator import TaskOrchestrator
from autonomous_workflow.approval.approval_router import route_approval
from autonomous_workflow.queue.action_queue import ActionQueue


decision = {
    "action": "OPTIMIZE_INVENTORY",
    "risk_score": 91
}


workflow = WorkflowPlanner().create_plan(
    decision
)

tasks = TaskOrchestrator().execute(
    workflow
)

approval = route_approval(
    decision["risk_score"]
)

queue = ActionQueue()

for task in tasks:
    queue.add(task)


print(workflow)
print(approval)
print(queue.queue)

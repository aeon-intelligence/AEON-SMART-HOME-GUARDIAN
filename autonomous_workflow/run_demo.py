from autonomous_workflow.engine.workflow_engine import WorkflowEngine
from autonomous_workflow.trigger.event_trigger import evaluate
from autonomous_workflow.planner.workflow_planner import plan
from autonomous_workflow.execution.action_executor import execute
from autonomous_workflow.memory.workflow_memory import save


engine = WorkflowEngine()


event = evaluate(
    {
        "type": "INVENTORY_RISK",
        "risk_score": 91
    }
)


workflow_plan = plan(
    event
)


workflow = engine.create(
    "INVENTORY_RISK",
    workflow_plan
)


result = execute(
    workflow
)


memory = save(
    result
)


print(event)
print(workflow_plan)
print(workflow)
print(result)
print(memory)

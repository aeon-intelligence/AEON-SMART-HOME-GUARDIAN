from response_orchestration.engine.response_engine import create
from response_orchestration.action.action_planner import plan
from response_orchestration.policy.policy_validator import validate
from response_orchestration.workflow.workflow_engine import execute
from response_orchestration.outcome.outcome_tracker import track
from response_orchestration.memory.response_memory import save


alert = {
    "type": "INVENTORY_RISK",
    "risk_score": 91
}


response = create(alert)

action = plan(response)

policy = validate(action)

workflow = execute(action)

outcome = track(workflow)

memory = save(
    {
        "response": response,
        "action": action,
        "policy": policy,
        "workflow": workflow,
        "outcome": outcome
    }
)


print(response)
print(action)
print(policy)
print(workflow)
print(outcome)
print(memory)

from executive_decision_automation.decision.decision_engine import analyze
from executive_decision_automation.action.action_planner import recommend
from executive_decision_automation.policy.policy_guard import validate
from executive_decision_automation.approval.approval_router import route
from executive_decision_automation.memory.decision_memory import save


decision = analyze(
    "INVENTORY_RISK_SIGNAL"
)

action = recommend(
    decision
)

policy = validate(
    action
)

approval = route(
    policy
)

print(decision)
print(action)
print(policy)
print(approval)
print(save(approval))

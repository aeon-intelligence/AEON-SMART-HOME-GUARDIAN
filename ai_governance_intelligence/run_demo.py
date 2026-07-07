from ai_governance_intelligence.policy.policy_engine import evaluate_policy
from ai_governance_intelligence.compliance.compliance_validator import validate
from ai_governance_intelligence.risk.risk_approval import approve
from ai_governance_intelligence.decision.governance_log import record
from ai_governance_intelligence.memory.policy_memory import save


policy = evaluate_policy(
    "AUTONOMOUS_INVENTORY_DECISION"
)

compliance = validate(
    policy
)

risk = approve(
    15
)

decision = record(
    risk
)

print(policy)
print(compliance)
print(risk)
print(decision)
print(save(decision))

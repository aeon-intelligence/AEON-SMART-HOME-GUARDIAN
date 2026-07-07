from ai_governance_constitution.constitution.ai_constitution import load
from ai_governance_constitution.policy.policy_engine import validate
from ai_governance_constitution.gateway.decision_gate import check
from ai_governance_constitution.audit.audit_logger import record
from ai_governance_constitution.memory.governance_memory import save


constitution = load()

policy = validate(
    "AUTONOMOUS_INVENTORY_ACTION"
)

gate = check(
    policy
)

audit = record(
    "AI_DECISION_EXECUTION"
)

print(constitution)
print(policy)
print(gate)
print(audit)
print(save(gate))

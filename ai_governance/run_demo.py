from ai_governance.policy.policy_engine import evaluate
from ai_governance.risk.risk_engine import assess
from ai_governance.compliance.compliance_validator import validate
from ai_governance.audit.audit_logger import record
from ai_governance.memory.governance_memory import save


policy = evaluate(
    "AUTONOMOUS_DECISION"
)

risk = assess(
    policy
)

compliance = validate(
    risk
)

audit = record(
    compliance
)

print(policy)
print(risk)
print(compliance)
print(audit)
print(save(audit))

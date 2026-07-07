from ai_governance.constitution.constitution_core import AIConstitution
from ai_governance.policy.policy_engine import evaluate_policy
from ai_governance.audit.audit_logger import AuditLogger
from ai_governance.override.human_override import request_override
from ai_governance.compliance.compliance_monitor import check_compliance


request = {
    "action": "INVENTORY_OPTIMIZATION",
    "risk_score": 91
}


print(
    AIConstitution().validate(
        request["action"]
    )
)

print(
    evaluate_policy(request)
)

print(
    AuditLogger().record(request)
)

print(
    request_override(
        "High risk decision"
    )
)

print(
    check_compliance()
)

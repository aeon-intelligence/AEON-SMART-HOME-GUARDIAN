from knowledge_firewall.classification.classifier import classify
from knowledge_firewall.access.access_control import check_access
from knowledge_firewall.policy.ai_policy import validate_ai_request
from knowledge_firewall.guard.knowledge_guard import protect
from knowledge_firewall.audit.audit_memory import record


data = classify(
    "CUSTOMER INVENTORY REPORT"
)

access = check_access(
    "guardian_agent",
    data["classification"]
)

policy = validate_ai_request(
    "KNOWLEDGE_QUERY"
)

guard = protect(
    data
)

print(data)
print(access)
print(policy)
print(guard)
print(record("AI_KNOWLEDGE_ACCESS"))

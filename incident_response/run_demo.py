from incident_response.classification.incident_classifier import classify
from incident_response.rca.root_cause import analyze
from incident_response.recovery.recovery_engine import recover
from incident_response.memory.incident_memory import store
from incident_response.approval.guardian_gate import approve


event = {
    "name": "API_LATENCY_SPIKE",
    "severity": "HIGH"
}


incident = classify(event)

analysis = analyze(
    incident
)

action = recover(
    analysis
)

approval = approve(
    action
)

print(incident)
print(analysis)
print(action)
print(approval)
print(store(incident))

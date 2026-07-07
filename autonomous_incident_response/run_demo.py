from autonomous_incident_response.detection.incident_detector import detect
from autonomous_incident_response.severity.severity_analyzer import analyze
from autonomous_incident_response.recovery.recovery_planner import plan
from autonomous_incident_response.guardian.guardian_gate import approve
from autonomous_incident_response.memory.incident_memory import save


incident = detect(
    "SERVICE_LATENCY_SPIKE"
)

severity = analyze(
    incident
)

recovery = plan(
    severity
)

approval = approve(
    recovery
)

print(incident)
print(severity)
print(recovery)
print(approval)
print(save(approval))

from security_operations.incident.incident_detector import detect
from security_operations.risk.risk_engine import score
from security_operations.alert.alert_manager import notify
from security_operations.response.response_engine import respond
from security_operations.memory.security_memory import save

incident = detect(
    "UNAUTHORIZED_API_ACCESS"
)

risk = score(
    incident
)

alert = notify(
    risk
)

response = respond(
    alert
)

memory = save(
    response
)

print(incident)
print(risk)
print(alert)
print(response)
print(memory)

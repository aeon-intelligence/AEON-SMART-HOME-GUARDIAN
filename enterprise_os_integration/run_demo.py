from enterprise_os_integration.core.os_core import initialize
from enterprise_os_integration.registry.service_registry import register
from enterprise_os_integration.bus.ai_message_bus import publish
from enterprise_os_integration.monitor.system_monitor import check
from enterprise_os_integration.memory.os_memory import save


system = initialize(
    "AEON_MATRIX_ENTERPRISE_OS"
)

service = register(
    "GUARDIAN_AI_SERVICE"
)

event = publish(
    "AUTONOMOUS_DECISION_EVENT"
)

health = check()

print(system)
print(service)
print(event)
print(health)
print(save(health))

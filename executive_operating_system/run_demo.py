from executive_operating_system.decision.executive_decision import decide
from executive_operating_system.command.command_orchestrator import orchestrate
from executive_operating_system.governance.governance_control import validate
from executive_operating_system.kpi.kpi_intelligence import analyze
from executive_operating_system.memory.executive_memory import save


decision = decide(
    "ENTERPRISE_INTELLIGENCE_SIGNAL"
)

command = orchestrate(
    decision
)

governance = validate(
    command
)

kpi = analyze(
    "BUSINESS_PERFORMANCE"
)

print(decision)
print(command)
print(governance)
print(kpi)
print(save(governance))

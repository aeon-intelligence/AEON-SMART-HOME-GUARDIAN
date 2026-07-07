from risk_intelligence.detection.risk_detector import detect
from risk_intelligence.scoring.risk_score import calculate
from risk_intelligence.governance.governance_check import validate
from risk_intelligence.mitigation.mitigation_planner import plan
from risk_intelligence.memory.risk_memory import save


risk = detect(
    "SUPPLY_CHAIN_DELAY"
)

score = calculate(
    risk
)

governance = validate(
    "AUTONOMOUS_RESPONSE"
)

mitigation = plan(
    score
)

print(risk)
print(score)
print(governance)
print(mitigation)
print(save(mitigation))

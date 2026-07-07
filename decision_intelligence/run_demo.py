from decision_intelligence.engine.decision_engine import create
from decision_intelligence.scoring.confidence_score import calculate as confidence
from decision_intelligence.risk.risk_score import calculate as risk
from decision_intelligence.value.value_score import calculate as value
from decision_intelligence.record.decision_record import create as record
from decision_intelligence.memory.decision_memory import save


context = {
    "operation": "INVENTORY_OPTIMIZATION",
    "warehouse": "AEON_DC"
}


decision = create(
    context
)


confidence_result = confidence(
    decision
)


risk_result = risk(
    decision
)


value_result = value(
    decision
)


executive_record = record(
    {
        "decision": decision,
        "confidence": confidence_result,
        "risk": risk_result,
        "value": value_result
    }
)


memory = save(
    executive_record
)


print(decision)
print(confidence_result)
print(risk_result)
print(value_result)
print(executive_record)
print(memory)

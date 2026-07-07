from decision_intelligence.engine.recommendation import RecommendationEngine
from decision_intelligence.journal.decision_journal import create_decision_record
from decision_intelligence.outcomes.outcome_tracker import track_outcome


signal = {
    "event": "INVENTORY_RISK_SIGNAL",
    "risk_score": 91,
    "inventory_risk": 91,
    "market_pressure": 72
}


engine = RecommendationEngine()

decision = engine.analyze(signal)

journal = create_decision_record(
    signal,
    decision
)

learning = track_outcome(
    decision["recommended_action"],
    "PENDING_VALIDATION"
)


print(journal)
print(learning)

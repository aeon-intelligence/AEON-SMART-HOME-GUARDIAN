from core.decision_intelligence.service import DecisionIntelligence

def test_recommendation():
    result = DecisionIntelligence().recommend({})
    assert result["confidence"] > 0.0

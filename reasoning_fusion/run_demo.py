from reasoning_fusion.analysis.impact_analyzer import ImpactAnalyzer
from reasoning_fusion.explanation.decision_explainer import explain
from reasoning_fusion.recommendation.executive_recommendation import generate_recommendation
from reasoning_fusion.validation.guardian_check import validate


context = {
    "risk_score": 91
}


impact = ImpactAnalyzer().analyze(context)

recommendation = generate_recommendation(
    impact
)

decision = explain(
    "INVENTORY_OPTIMIZATION",
    "High inventory risk detected from enterprise signals"
)

print(impact)
print(decision)
print(validate(recommendation))

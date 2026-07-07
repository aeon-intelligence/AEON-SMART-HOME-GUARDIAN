from decision_intelligence.analyzer.decision_analyzer import analyze
from decision_intelligence.scenario.scenario_evaluator import evaluate
from decision_intelligence.risk.risk_scoring import score
from decision_intelligence.recommendation.strategic_recommendation import recommend
from decision_intelligence.memory.decision_memory import save


analysis = analyze(
    "ENTERPRISE_GROWTH_STRATEGY"
)

scenario = evaluate(
    "EXPANSION_SCENARIO"
)

risk = score(
    [
        analysis,
        scenario
    ]
)

decision = recommend(
    risk
)

print(analysis)
print(scenario)
print(risk)
print(decision)
print(save(decision))

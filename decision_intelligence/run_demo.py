from decision_intelligence.context.context_engine import analyze
from decision_intelligence.evaluation.option_evaluator import evaluate
from decision_intelligence.optimization.optimizer import optimize
from decision_intelligence.recommendation.recommendation_engine import recommend
from decision_intelligence.memory.decision_memory import save


context = analyze(
    "SUPPLY_CHAIN_OPTIMIZATION"
)

evaluation = evaluate(
    [
        "OPTION_A",
        "OPTION_B",
        "OPTION_C"
    ]
)

optimization = optimize(
    evaluation
)

recommendation = recommend(
    optimization
)

print(context)
print(evaluation)
print(optimization)
print(recommendation)
print(save(recommendation))

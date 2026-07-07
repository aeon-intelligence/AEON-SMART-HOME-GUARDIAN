from continuous_evolution.evaluation.performance_evaluator import evaluate
from continuous_evolution.learning.feedback_loop import learn
from continuous_evolution.improvement.improvement_planner import plan
from continuous_evolution.controller.evolution_controller import execute
from continuous_evolution.memory.evolution_memory import save


evaluation = evaluate(
    "INVENTORY_DECISION_RESULT"
)

learning = learn(
    evaluation
)

improvement = plan(
    learning
)

evolution = execute(
    improvement
)

print(evaluation)
print(learning)
print(improvement)
print(evolution)
print(save(evolution))

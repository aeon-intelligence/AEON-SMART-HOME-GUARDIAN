from continuous_evolution.feedback.performance_feedback import analyze
from continuous_evolution.improvement.improvement_engine import discover
from continuous_evolution.cycle.evolution_cycle import run
from continuous_evolution.optimization.learning_optimizer import optimize
from continuous_evolution.memory.evolution_memory import save


feedback = analyze(
    "AEON_MATRIX_OPERATION"
)

improvement = discover(
    feedback
)

cycle = run(
    improvement
)

optimization = optimize(
    cycle
)

print(feedback)
print(improvement)
print(cycle)
print(optimization)
print(save(optimization))

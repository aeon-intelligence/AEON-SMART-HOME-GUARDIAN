from autonomous_learning.feedback.feedback_engine import collect
from autonomous_learning.analysis.outcome_analyzer import analyze
from autonomous_learning.optimization.optimizer import optimize
from autonomous_learning.pattern.pattern_detector import detect
from autonomous_learning.memory.learning_memory import save


feedback = collect(
    {
        "operation": "ORDER_FULFILLMENT",
        "result": "SUCCESS"
    }
)


analysis = analyze(
    feedback
)


optimization = optimize(
    analysis
)


pattern = detect(
    optimization
)


memory = save(
    pattern
)


print(feedback)
print(analysis)
print(optimization)
print(pattern)
print(memory)

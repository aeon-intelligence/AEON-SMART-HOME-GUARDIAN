from ai_learning_loop.decision.decision_tracker import record_decision
from ai_learning_loop.outcome.outcome_engine import evaluate_outcome
from ai_learning_loop.feedback.feedback_loop import learn_from_feedback
from ai_learning_loop.strategy.strategy_engine import improve_strategy
from ai_learning_loop.memory.executive_memory import save_learning


decision = record_decision(
    "Inventory Optimization",
    "TRANSFER_STOCK"
)

outcome = evaluate_outcome(
    decision["decision"],
    92
)

feedback = learn_from_feedback(
    outcome
)

strategy = improve_strategy(
    feedback
)

memory = save_learning(
    strategy
)

print(decision)
print(outcome)
print(feedback)
print(strategy)
print(memory)

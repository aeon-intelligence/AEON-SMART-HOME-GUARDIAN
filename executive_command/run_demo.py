from executive_command.recommendation.strategy_recommendation import recommend
from executive_command.decision.decision_engine import create_decision
from executive_command.confidence.confidence_score import calculate_confidence
from executive_command.approval.approval_workflow import request_approval
from executive_command.memory.command_memory import save_command


strategy = recommend(91)

decision = create_decision(
    "SUPPLY_CHAIN_RISK",
    strategy
)

confidence = calculate_confidence(
    {
        "accuracy": 92,
        "simulation": 88
    }
)

approval = request_approval(
    decision
)

memory = save_command(
    approval
)

print(decision)
print(confidence)
print(approval)
print(memory)

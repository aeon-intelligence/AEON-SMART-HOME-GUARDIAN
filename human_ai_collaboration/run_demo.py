from human_ai_collaboration.context.collaboration_context import create
from human_ai_collaboration.assistant.ai_assistant import assist
from human_ai_collaboration.feedback.human_feedback import record
from human_ai_collaboration.governance.collaboration_guard import check
from human_ai_collaboration.memory.collaboration_memory import save


context = create(
    "EXECUTIVE_USER",
    "INVENTORY_DECISION"
)

assistant = assist(
    context
)

feedback = record(
    "APPROVED_BY_HUMAN"
)

governance = check(
    "AI_RECOMMENDATION"
)

print(context)
print(assistant)
print(feedback)
print(governance)
print(save(governance))

from ai_avatar_companion.avatar.avatar_core import create_avatar
from ai_avatar_companion.knowledge.knowledge_navigator import search_knowledge
from ai_avatar_companion.sop.sop_assistant import explain_sop
from ai_avatar_companion.learning.learning_companion import recommend_learning
from ai_avatar_companion.memory.avatar_memory import save_interaction


avatar = create_avatar(
    "AEON Assistant",
    "Enterprise Knowledge Companion"
)

knowledge = search_knowledge(
    "Inventory SOP"
)

sop = explain_sop(
    "Warehouse Operation"
)

learning = recommend_learning(
    "AI Workflow"
)

print(avatar)
print(knowledge)
print(sop)
print(learning)
print(save_interaction(avatar))

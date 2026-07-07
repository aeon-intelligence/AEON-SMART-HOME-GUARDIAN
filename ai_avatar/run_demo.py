from ai_avatar.core.avatar import AIAvatar
from ai_avatar.conversation.session import ConversationSession
from ai_avatar.learning.learning_companion import LearningCompanion


knowledge = [
    {
        "topic": "Inventory Risk",
        "solution": "Check stock and demand forecast"
    },
    {
        "topic": "SOP",
        "solution": "Human approval required"
    }
]


avatar = AIAvatar()

session = ConversationSession()

session.add(
    "How to handle Inventory Risk?"
)


print(
    avatar.respond(
        "Inventory Risk",
        knowledge
    )
)


print(
    LearningCompanion().recommend(
        "AI Operation Skill"
    )
)

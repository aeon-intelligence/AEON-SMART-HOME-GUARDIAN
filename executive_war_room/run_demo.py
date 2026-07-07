from executive_war_room.situation.situation_engine import analyze
from executive_war_room.fusion.intelligence_fusion import fuse
from executive_war_room.decision.decision_brief import generate
from executive_war_room.command.command_board import display
from executive_war_room.memory.executive_memory import save


situation = analyze(
    "ENTERPRISE_OPERATION_STATUS"
)

fusion = fuse(
    [
        "WORLD_SIGNAL",
        "DIGITAL_TWIN",
        "ECONOMIC_INTELLIGENCE"
    ]
)

decision = generate(
    fusion
)

board = display(
    decision
)

print(situation)
print(fusion)
print(decision)
print(board)
print(save(board))

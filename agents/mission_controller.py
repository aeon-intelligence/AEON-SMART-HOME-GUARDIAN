"""
AEON MATRIX Mission Controller
"""


def complete_mission(task, consensus):

    return {
        "mission": task,
        "result": consensus["consensus"],
        "confidence": consensus["confidence"]
    }

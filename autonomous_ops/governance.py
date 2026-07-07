"""
AEON MATRIX Governance Execution Gate
"""


def validate(consensus):

    if consensus["consensus"] == "APPROVED":
        return {
            "governance": "PASSED",
            "execution": "AUTHORIZED"
        }

    return {
        "governance": "BLOCKED",
        "execution": "STOPPED"
    }

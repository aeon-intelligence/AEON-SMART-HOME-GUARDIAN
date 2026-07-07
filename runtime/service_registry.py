"""
AEON MATRIX Runtime Service Registry
"""

SERVICES = [
    "api_gateway",
    "guardian_agent",
    "telemetry"
]


def registry():

    return {
        "registered_services": len(SERVICES),
        "runtime": "ACTIVE"
    }

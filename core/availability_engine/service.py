class AvailabilityEngine:
    def calculate(self, on_hand, reserved):
        available = max(0, on_hand - reserved)
        return {
            "on_hand": on_hand,
            "reserved": reserved,
            "available": available
        }

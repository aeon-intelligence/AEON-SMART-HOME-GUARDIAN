class ATPService:
    def calculate(self, on_hand, reserved):
        return max(0, on_hand - reserved)

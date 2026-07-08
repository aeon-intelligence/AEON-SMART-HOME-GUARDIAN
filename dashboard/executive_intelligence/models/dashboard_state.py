class DashboardState:

    def __init__(self):
        self.signals = []
        self.risks = []
        self.recommendations = []

    def add_signal(self, signal):
        self.signals.append(signal)

    def add_risk(self, risk):
        self.risks.append(risk)

    def add_recommendation(self, recommendation):
        self.recommendations.append(recommendation)

    def snapshot(self):
        return {
            "signals": self.signals,
            "risks": self.risks,
            "recommendations": self.recommendations,
            "status": "ACTIVE"
        }

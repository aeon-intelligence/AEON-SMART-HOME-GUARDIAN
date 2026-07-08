"""
AEON MATRIX Autonomous Security Intelligence Layer

Analyze security signals and generate
governed security recommendations.
"""


class SecurityIntelligenceEngine:

    def analyze(self, signal: dict):

        threat_level = signal.get(
            "threat_level",
            0
        )

        anomaly_score = signal.get(
            "anomaly_score",
            0
        )

        asset_criticality = signal.get(
            "asset_criticality",
            0
        )

        risk_score = (
            threat_level * 0.4 +
            anomaly_score * 0.35 +
            asset_criticality * 0.25
        )

        if risk_score >= 80:
            action = "IMMEDIATE_SECURITY_RESPONSE"

        elif risk_score >= 50:
            action = "SECURITY_REVIEW_REQUIRED"

        else:
            action = "MONITOR_ACTIVITY"

        return {
            "risk_score": round(
                risk_score,
                2
            ),
            "recommended_action": action,
            "guardian_validation": True,
            "audit_required": True
        }

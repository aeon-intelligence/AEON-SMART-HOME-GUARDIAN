def evaluate(identity, device, mfa):

    if (
        identity["identity_status"] == "VERIFIED"
        and device["trust_status"] == "TRUSTED"
        and mfa["mfa_status"] == "PASSED"
    ):
        return {
            "access": "GRANTED",
            "risk": "LOW"
        }

    return {
        "access": "DENIED",
        "risk": "HIGH"
    }

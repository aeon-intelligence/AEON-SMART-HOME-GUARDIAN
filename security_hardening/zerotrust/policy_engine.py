def verify_access(request):

    required = [
        "identity",
        "authorization",
        "purpose"
    ]

    approved = all(
        item in request
        for item in required
    )

    return {
        "access":
            "GRANTED"
            if approved
            else "DENIED",
        "zero_trust_check":
            True
    }

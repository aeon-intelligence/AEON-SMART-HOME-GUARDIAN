def create(alert):

    return {
        "response_type": "AUTONOMOUS_RESPONSE",
        "source_alert": alert,
        "status": "CREATED"
    }

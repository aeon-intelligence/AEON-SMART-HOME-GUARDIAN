def plan(severity):

    return {
        "recovery_action":
            "AUTO_RESTORE_SERVICE",
        "severity": severity,
        "status": "READY"
    }

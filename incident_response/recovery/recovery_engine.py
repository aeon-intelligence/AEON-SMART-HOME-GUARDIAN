def recover(analysis):

    return {
        "recovery_action":
            "RESTART_OR_SCALE_SERVICE",
        "based_on":
            analysis["possible_cause"]
    }

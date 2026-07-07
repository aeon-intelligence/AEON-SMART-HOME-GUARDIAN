def optimize(issue):

    return {
        "issue": issue,
        "action":
            "RETRAIN_AND_TUNE"
            if "MODEL" in issue
            else "RESOURCE_BALANCE"
    }

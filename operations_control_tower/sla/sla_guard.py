def check_sla(metrics):

    return {
        "sla_status":
            "PROTECTED"
            if metrics >= 95
            else "RISK"
    }

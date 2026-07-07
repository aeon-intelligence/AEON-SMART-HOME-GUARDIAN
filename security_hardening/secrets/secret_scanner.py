def scan_secrets(config):

    findings = []

    keywords = [
        "PASSWORD",
        "SECRET",
        "TOKEN",
        "API_KEY"
    ]

    for key in config.keys():

        if key.upper() in keywords:
            findings.append(key)

    return {
        "secret_findings": findings,
        "status":
            "WARNING"
            if findings
            else "CLEAN"
    }

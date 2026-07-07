def calculate_kpi(metrics):

    return {
        "OTIF": metrics["otif"],
        "Productivity": metrics["productivity"],
        "Accuracy": metrics["accuracy"]
    }

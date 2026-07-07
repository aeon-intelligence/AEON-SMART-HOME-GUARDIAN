def calculate_score(outcome):

    if outcome["actual_result"] == "SUCCESS":
        return 100

    return 50

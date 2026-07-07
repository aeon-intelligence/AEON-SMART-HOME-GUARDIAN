def recommend(risk):

    if risk > 80:
        return "EXECUTE_CONTINGENCY_PLAN"

    return "CONTINUE_OPTIMIZATION"

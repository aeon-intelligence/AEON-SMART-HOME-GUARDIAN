def analyze_skill(activity):

    if activity.get("ai_usage") < 50:
        return "AI_OPERATION"

    return "ADVANCED_AI_USAGE"

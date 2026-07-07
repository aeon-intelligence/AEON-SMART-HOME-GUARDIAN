def check_access(user, level):

    if level == "RESTRICTED":
        permission = "APPROVAL_REQUIRED"
    else:
        permission = "GRANTED"

    return {
        "user": user,
        "permission": permission
    }

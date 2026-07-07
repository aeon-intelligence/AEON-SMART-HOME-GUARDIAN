def protect(request):

    return {
        "request": request,
        "gateway": "SECURED",
        "access": "ALLOW"
    }

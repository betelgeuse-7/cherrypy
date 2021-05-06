"""
Authentication middleware for this app.
#TODO
"""

def is_authenticated(request):
    print(request.cookie)
    return False



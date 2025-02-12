from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        if username is None:
            return None
        
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            raise AuthenticationFailed("User not found") from e
        return (user, None)
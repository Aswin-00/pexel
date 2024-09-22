# myapp/authentication.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class EmailBackend(ModelBackend):
    
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        
        if username is None:
            username = kwargs.get('email')
            print('username')
        try:
            user = User.objects.get(email=username)
            print(user)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
    

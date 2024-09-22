from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Image
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')  
        print('here')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('A user with this email already exists.')
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'profile_picture']


# email change
class EmailAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Email')

    
    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        print(email,password)
        
        if email and password:
        # Call the default backend for authentication
            self.user_cache = authenticate(
                request=self.request,
                username=email,  # Email will be used as the username
                password=password
            )
        
            print(self.user_cache)
            if self.user_cache is None:
                raise forms.ValidationError(
                    'invalid email',
                    code='invalid_login',
                    )
        return self.cleaned_data
    
# images upload view


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'description', 'tags']

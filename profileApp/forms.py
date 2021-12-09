from django import forms
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    """
    user updateform to update user info
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    """
    model form to update user profile
    """
    class Meta:
        model = Profile
        fields = ['image']

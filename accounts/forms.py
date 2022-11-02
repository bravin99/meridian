from django import forms
from accounts.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar']
        widgets = {
            "avatar": forms.FileInput(),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["country", ]
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import UserProfile


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('email',)

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar',)
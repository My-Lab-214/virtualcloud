from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserFile

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ['file']

from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    FirstName=forms.CharField()
    LastName=forms.CharField()

    class Meta:
        model=User
        fields=["username","password1","FirstName","LastName","password2"]
        
        """def __init__(self) -> None:
            self.fields['email'].widget.attrs["class"]="form-control  form-control-lg form-outline form-white mb-4"
            self.fields['password1'].widget.attrs["class"]="form-control  form-control-lg form-outline form-white mb-4"
            self.fields['FirstName'].widget.attrs["class"]="form-control  form-control-lg form-outline form-white mb-4" 
            self.fields['LastName'].widget.attrs["class"]="form-control  form-control-lg form-outline form-white mb-4"
            self.fields['password2'].widget.attrs["class"]="form-control  form-control-lg form-outline form-white mb-4" 
        """
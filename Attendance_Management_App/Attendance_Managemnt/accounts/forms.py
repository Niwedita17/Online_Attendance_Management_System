from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models


class StudentSignupForm(forms.ModelForm):
    class Meta:
        model = models.StudentInfo
        fields = ('sid', 's_fname', 's_lname', 'email', 'phone', 'degree', 'house_no', 'street', 'city', 'state', 'pincode', 'password' )


class SignUpForm_Student(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
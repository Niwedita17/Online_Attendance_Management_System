from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from django.contrib.auth import get_user_model

user_instance = get_user_model()


class StudentSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password"
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password"
        }))

    class Meta:
        model = models.StudentInfo
        fields = ('sid', 's_fname', 's_lname', 'email', 'phone', 'degree', 'house_no', 'street', 'city', 'state', 'pincode', 'password', 'password2' )


class FacultySignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password"
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password"
        }))

    class Meta:
        model = models.FacultyInfo
        fields = ('fid', 'f_fname', 'f_lname', 'email', 'phone', 'area_of_interest', 'btech', 'mtech','phd', 'house_no', 'street', 'city', 'state', 'pincode', 'password', 'password2' )


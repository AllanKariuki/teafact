from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from .models import Reviews, Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['farmer_name', 'title', 'description']
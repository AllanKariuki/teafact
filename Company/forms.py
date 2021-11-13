from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models.fields import EmailField
from django.forms import fields
from django.contrib.auth.models import User
from .models import Staffs, Farmers, Payments, Records

class AddStaffForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Staffs
        fields = ['staff_name', 'email', 'phone_number', 'department', 'position']

class AddFarmerForm(forms.ModelForm):
    class Meta:
        model = Farmers
        fields = ['farmer_name', 'farm_name', 'email', 'location', 'phone_number']

class PaymentsForm(forms.ModelForm):
    class Meta:
        model = Payments
        fields = ['farmer_name', 'amount']

class RecordsForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['farmer_name', 'title', 'quantity', 'quality']

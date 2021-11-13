from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm

def registerpage(request):
    reg_form = RegisterForm()
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request, f'Register successful')
            return redirect('login')
        else:
            messages.error(request, f'registration failed')
    context = {
        'reg_form' : reg_form
    }
    return render(request, 'Company/signup.html', context)

def loginpage(request):
    return render(request, 'Company/login.html')
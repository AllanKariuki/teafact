from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm

def registerpage(request):
    reg_form = RegisterForm()
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            username = reg_form.cleaned_data.get('username')
            messages.success(request, f'Register successful')
            return redirect('login')
        else:
            messages.error(request, f'registration failed')
    context = {
        'reg_form' : reg_form
    }
    return render(request, 'Company/signup.html', context)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, f'login successful')
            return redirect('home')
        else: 
            messages.error(request, f'login unsuccessful')

    return render(request, 'Company/login.html')

def logoutpage(request):
    logout(request)
    return redirect(request, 'login')


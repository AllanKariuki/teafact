from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group
from Company.models import Farmers, Staffs

@unauthenticated_user
def registerpage(request):
    reg_form = RegisterForm()
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            username = reg_form.cleaned_data.get('username')
            email = reg_form.cleaned_data.get('email')
            
            email1 = Farmers.objects.get(email = email)
            email2 = Staffs.objects.get(email = email)

            if email1 is not None:

                group_farmer = Group.objects.get(name = 'farmer')
                user.group.add(group_farmer)
            
            elif email2 is not None:

                group_staff = Group.objects.get(name= 'staff')
                user.group.add(group_staff)

            else:   
                messages.info(request, f'sorry you do not match with any of our records, your account will null and void')

            messages.success(request, f'Register successful for {username}')
            return redirect('login')
        else:
            messages.error(request, f'registration failed')
    context = {
        'reg_form' : reg_form
    }
    return render(request, 'Company/signup.html', context)

@unauthenticated_user
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
    return redirect('logout')


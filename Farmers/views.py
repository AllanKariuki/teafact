from django.core.checks import messages
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from Company.models import Farmers, Records, Payments
from .models import Reviews, Profile
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

@login_required
def home(request):
    user = request.user
    username = user.username
    context = {
        'username' : username
    }
    return render(request, 'Farmers/index.html', context)

@login_required  
def profile(request):
    #farmers page in company or records
    return render(request, 'Farmers/profile.html')

@login_required  
def editprofile(request):
    #farmers page in company or records
    return render(request, 'Farmers/editprofile.html')

#records views
@login_required
def records(request):
    user = request.user
    email = user.email
    # return HttpResponse(email)
    try:
        name = Farmers.objects.get(email = email)
    except Farmers.DoesNotExist:
        return HttpResponse('<p>Farmer Does not exist</p>')
    farm_record = Records.objects.get(farmer_name = name)
    context ={
        'farm_record' : farm_record
    } 
    return render(request, 'Farmers/records.html', context)

@login_required
def record_detail(request):
    return render(request, 'Farmers/record_detail.html')

#payments views
@login_required
def payments(request):
    user = request.user
    email = user.email
    # return HttpResponse(email)
    try:
        name = Farmers.objects.get(email = email)
    except Farmers.DoesNotExist:
        return HttpResponse('<p>Farmer Does not exist</p>')
    farm_payment = Payments.objects.get(farmer_name = name)
    context ={
        'farm_payment' : farm_payment
    } 
    return render(request, 'Farmers/payments.html', context)

@login_required
def payment_detail(request):
    return render(request, 'Farmers/payment_detail.html')

#Review Views
@login_required
def create_review(request):
    return render(request, 'Farmers/createreview.html')

@login_required
def reviews(request):
    return render(request, 'Farmers/reviews.html')

@login_required
def review_detail(request):
    return render(request, 'Farmers/review_detail.html')

# @login_required
# def page3(request):
#     #profile form and petition form
#     return render(request, 'Farmers/page3.html')
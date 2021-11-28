from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from Company.models import Farmers, Records, Payments
from .models import Reviews, Profile
from .forms import ProfileForm, ReviewForm
from Account.decorators import allowed_users

@login_required
@allowed_users(allowed_roles = ['farmer'])
def home(request):
    user = request.user
    username = user.username
    email = user.email

    try:
        name = Farmers.objects.get(email = email)
    except Farmers.DoesNotExist:
        return HttpResponse('<p>Farmer Does not exist</p>')
    farm_record = Records.objects.filter(farmer_name = name)
    farm_payment = Payments.objects.filter(farmer_name = name)
    farmer_reviews = Reviews.objects.filter(farmer_name = name)

    context = {
        'username' : username,
        'farm_record' : farm_record,
        'farm_payment' : farm_payment,
        'farmer_reviews' : farmer_reviews,
    }
    return render(request, 'Farmers/index.html', context)

@login_required
@allowed_users(allowed_roles = ['farmer'])  
def profile(request):
    #farmers page in company or 
    user = request.user
    # profile = Profile.objects.get(instance = request.user)
    farmer = Farmers.objects.get(email = user.email)
    context = {
        'profile': profile,
        'user' : user,
        'farmer' : farmer,
    }
    return render(request, 'Farmers/profile.html', context)

@login_required  
@allowed_users(allowed_roles = ['farmer'])
def editprofile(request):
    #farmers page in company or records

    profile_form = ProfileForm()
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, f'profile created successfully')
        else:
            messages.error(request, f'failed to create profile')
            return redirect('profile')
    context = {
        'profile_form' : profile_form
    }
    return render(request, 'Farmers/editprofile.html', context)

#records views
@login_required
@allowed_users(allowed_roles = ['farmer'])
def records(request):
    user = request.user
    email = user.email
    # return HttpResponse(email)
    try:
        farmer = Farmers.objects.get(email = email)
    except Farmers.DoesNotExist:
        return HttpResponse('<p>Farmer Does not exist</p>')
    farm_records = Records.objects.filter(farmer_name = farmer)
    context ={
        'farm_records' : farm_records,
        'farmer' : farmer,
    } 
    return render(request, 'Farmers/records.html', context)

@login_required
@allowed_users(allowed_roles = ['farmer'])
def recordDetail(request,id):
    record = Records.objects.get(id = id)
    context = {
        'record': record
    }
    return render(request, 'Farmers/record_detail.html', context)

#payments views
@login_required
@allowed_users(allowed_roles = ['farmer'])
def payments(request):
    user = request.user
    email = user.email
    # return HttpResponse(email)
    try:
        farmer = Farmers.objects.get(email = email)
    except Farmers.DoesNotExist:
        return HttpResponse('<p>Farmer Does not exist</p>')
    farm_payments = Payments.objects.filter(farmer_name = farmer)
    context ={
        'farm_payments' : farm_payments,
        'farmer' : farmer,
    } 
    return render(request, 'Farmers/payments.html', context)

@login_required
@allowed_users(allowed_roles = ['farmer'])
def paymentDetail(request, id):
    payment = Payments.objects.get(id = id)
    farmer = payment.farmer_name
    record = Farmers.objects.get(farmer_name = farmer)
    context = {
        'payment' :  payment,
        'record' : record,
    }
    return render(request, 'Farmers/payment_detail.html', context)

#Review Views
@login_required
@allowed_users(allowed_roles = ['farmer'])
def createReview(request):
    user = request.user
    email = user.email
    # return HttpResponse(email)
    try:
        name = Farmers.objects.get(email = email)
    except Farmers.DoesNotExist:
        return HttpResponse('<p>Farmer Does not exist</p>')
    r_form = ReviewForm()
    if request.method == 'POST':
        r_form = ReviewForm(request.POST)
        r_form.instance.farmer_name = name
        if r_form.is_valid:
            
            r_form.save()
            messages.success(request, f'form submitted')
            return redirect('reviews')
        else:
            messages.info(request, f'form not submitted')
    context = {
        'r_form' : r_form
    }
    return render(request, 'Farmers/createreview.html', context)

@login_required
@allowed_users(allowed_roles = ['farmer'])
def reviews(request):
    user = request.user
    email = user.email
    # return HttpResponse(email)

    try:
        farmer = Farmers.objects.get(email = email)
    except Farmers.DoesNotExist:
        return HttpResponse('<p>Farmer Does not exist</p>')

    farmer_reviews = Reviews.objects.filter(farmer_name = farmer)

    context ={
        'farmer_reviews' : farmer_reviews,
        'farmer' : farmer,
    } 
    return render(request, 'Farmers/reviews.html', context)

@login_required
@allowed_users(allowed_roles = ['farmer'])
def reviewDetail(request, id):
    review = Reviews.objects.get(id= id)
    farmer = review.farmer_name
    context = {
        'review' : review,
        'farmer' : farmer,
    }
    return render(request, 'Farmers/review_detail.html', context)

# @login_required
# def page3(request):
#     #profile form and petition form
#     return render(request, 'Farmers/page3.html')
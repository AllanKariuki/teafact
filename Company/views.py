from django.shortcuts import render
from django.contrib import messages
from .models import Farmers, Staffs, Records, Payments
from Farmers.models import Reviews
from .forms import AddStaffForm, AddFarmerForm, EditFarmerForm, PaymentsForm, RecordsForm

def dashboard(request):
    return render(request, 'Company/index.html')

def records(request):
    records = {
        'records' : Records.objects.all()
    }
    return render(request, 'Company/records.html', records)

def reviews(request):
    reviews = {
        'reviews' : Reviews.objects.all()
    }
    return render(request, 'Company/reviews.html', reviews)

def farmers(request):
    context = {
    'farmers' : Farmers.objects.all()
    }
    return render(request, 'Company/farmers.html', context)

def staffs(request):
    context = {
        'staffs' : Staffs.objects.all()
    }
    return render(request, 'Company/staffs.html', context)

def payments(request):
    context = {
        'payments' : Payments.objects.all()
    }
    return render(request, 'Company/payments.html', context)

#view functions

def view_farmer(request, name):
    farmer = Farmers.objects.get(farmer_name = name)
    content = {
        'farmer': farmer
    }
    return render(request, 'Company/viewfarmer.html', content)


def view_staff(request, name):
    staffs = Staffs.objects.get(farmer_name = name)
    context = {
        'staffs' : staffs
    }
    return render(request, 'Company/viewstaff.html', context)


def view_record(request, title):
    records = Records.objects.get(title = title)
    context = {
        'records' : records
    }
    return render(request, 'Company/viewrecord.html', context)


def view_payment(request, name):
    payments = Payments.objects.get(farmer_name = name)
    context = {
        'payments' : payments
    }
    return render(request, 'Company/viewpayment.html', context)


#form views

def add_farmer(request):
    form = AddFarmerForm()
    if request.method== 'POST':
        form = AddFarmerForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, f'added succefully')
        else:
            messages.error(request, f'unable to add details')
    context = {'form' : form}
    return render(request, 'Company/addfarmer.html', context)


def add_staff(request):
    staff_form = AddStaffForm()
    if request.method == 'POST':
        staff_form = AddStaffForm(request.POST)
        if staff_form.is_valid():
            staff_form.save()
            messages.success(request, f'Staff added succesfully')
        else:
            messages.error(request, f'unable to add staff')
    context = {'staff_form' : staff_form}
    return render(request, 'Company/addstaff.html', context)

def add_record(request):
    rec_form = RecordsForm()
    if request.method == 'POST':
        rec_form = RecordsForm(request.POST)
        if rec_form.is_valid():
            rec_form.save()
            messages.success(request, f'Record added succesfully')
        else:
            messages.error(request, f'unable to add record')
    context = {'rec_form' : rec_form}
    return render(request, 'Company/addrecord.html', context)

def add_payment(request):
    payment_form = PaymentsForm()
    if request.method == 'POST':
        payment_form = PaymentsForm(request.POST)
        if payment_form.is_valid():
            payment_form.save()
            messages.success(request, f'payment added successfully')
        else:
            messages.error(request, f'failed to add payment')
    context = {'payment_form' : payment_form}
    return render(request, 'Company/addpayment.html', context)


# def update_farmer(request, name):
#     farmer = Farmers.objects.get(farmer_name = name)
#     form = EditFarmerForm()
#     if request.method== 'PUT':
#         form = EditFarmerForm(request.POST, farmer)
#         if form.is_valid:
#             form.save()
#             messages.success(request, f'added succefully')
#         else:
#             messages.error(request, f'unable to add details')
#     context = {'form' : form,
#                 'farmer': form,
#     }
#     return render(request, 'Company/updatefarmer.html', context)


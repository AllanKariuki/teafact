from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Farmers, Staffs, Records, Payments
from Farmers.models import Reviews
from .forms import AddStaffForm, AddFarmerForm, EditFarmerForm, EditStaffForm, PaymentsForm, RecordsForm
from Account.decorators import  allowed_users, admins_only
from django.contrib.auth.decorators import login_required

@login_required
@admins_only
def dashboard(request):
    return render(request, 'Company/index.html')

@login_required
@allowed_users(allowed_roles = ['admin', 'staff'])
def records(request):
    user = request.user
    email = user.email
    try:
        staff = Staffs.objects.get(email = email)
    except Staffs.DoesNotExist:
        return HttpResponse('<p>staff does not exist</p>')
    
    records = {
        'records' : Records.objects.all(),
        'staff': staff,
    }
    return render(request, 'Company/records.html', records)

@login_required
@allowed_users(allowed_roles = ['admin', 'staff'])
def reviews(request):
    farmer_reviews = {
        'farmer_reviews' : Reviews.objects.all(),
    }
    return render(request, 'Company/reviews.html', farmer_reviews)

@login_required
@allowed_users(allowed_roles = ['admin', 'staff'])
def farmers(request):
    context = {
    'farmers' : Farmers.objects.all()
    }
    return render(request, 'Company/farmers.html', context)

@login_required
@allowed_users(allowed_roles = ['admin'])
def staffs(request):
    context = {
        'staffs' : Staffs.objects.all()
    }
    return render(request, 'Company/staffs.html', context)

@login_required
@allowed_users(allowed_roles = ['admin', 'staff'])
def payments(request):
    context = {
        'payments' : Payments.objects.all()
    }
    return render(request, 'Company/payments.html', context)

#view functions
@login_required
@allowed_users(allowed_roles = ['admin', 'staff'])
def view_farmer(request, name):
    farmer = Farmers.objects.get(farmer_name = name)
    content = {
        'farmer': farmer
    }
    return render(request, 'Company/viewfarmer.html', content)


@login_required
@allowed_users(allowed_roles = ['admin'])
def view_staff(request, name):
    staff = Staffs.objects.get(staff_name = name)
    context = {
        'staff' : staff
    }
    return render(request, 'Company/viewstaff.html', context)


@login_required
@allowed_users(allowed_roles = ['admin', 'staff'])
def view_record(request, id):
    record = Records.objects.get(id = id)
    context = {
        'record' : record,
    }
    return render(request, 'Company/viewrecord.html', context)


@login_required
@allowed_users(allowed_roles = ['admin', 'staff'])
def view_payment(request, name):
    payments = Payments.objects.get(farmer_name = name)

    context = {
        'payments' : payments
    }
    return render(request, 'Company/viewpayment.html', context)

@login_required
@allowed_users(allowed_roles = ['admin', 'staff'])
def view_review(request, id):
    review = Reviews.objects.get(id = id)

    context = {
        'review' : review
    }
    return render(request, 'Company/viewpayment.html', context)



#form views

@login_required
@allowed_users(allowed_roles = ['admin', 'staff'])
def add_farmer(request):
    form = AddFarmerForm()
    if request.method== 'POST':
        form = AddFarmerForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, f'added succefully')
            return redirect('farmers')
        else:
            messages.error(request, f'unable to add details')
    context = {'form' : form}
    return render(request, 'Company/addfarmer.html', context)


@login_required
@allowed_users(allowed_roles = ['admin'])
def add_staff(request):
    staff_form = AddStaffForm()
    if request.method == 'POST':
        staff_form = AddStaffForm(request.POST)
        if staff_form.is_valid():
            staff_form.save()
            messages.success(request, f'Staff added succesfully')
            return redirect('farmers')
        else:
            messages.error(request, f'unable to add staff')
    context = {'staff_form' : staff_form}
    return render(request, 'Company/addstaff.html', context)

@login_required
@allowed_users(allowed_roles = ['admin', 'staff'])
def add_record(request, name):
    rec_form = RecordsForm()
    #farmer = Farmers.objects.get(farmer_name = name)
    if request.method == 'POST':
        rec_form = RecordsForm(request.POST)
        if rec_form.is_valid():
            # rec_form.instance.farmer_name = farmer
            rec_form.save()
            messages.success(request, f'Record added succesfully')
            return redirect('farmers')
        else:
            messages.error(request, f'unable to add record')
    context = {'rec_form' : rec_form}
    return render(request, 'Company/addrecord.html', context)

@login_required
@allowed_users(allowed_roles = ['admin', 'staff'])
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


@login_required
@allowed_users(allowed_roles = ['admin', 'staff'])
def edit_farmer(request, name):
    farmer = Farmers.objects.get(farmer_name = name)
    form = EditFarmerForm()
    if request.method== 'POST':
        form = EditFarmerForm(request.POST, instance = farmer)
        if form.is_valid:
            form.save()
            messages.success(request, f'added succefully')
        else:
            messages.error(request, f'unable to add details')
    context = {'form' : form,
                'farmer': form,
    }
    return render(request, 'Company/editfarmer.html', context)

@login_required
@allowed_users(allowed_roles = ['admin'])
def edit_staff(request, name):
    staff = Staffs.objects.get(farmer_name = name)
    form = EditStaffForm()
    if request.method== 'POST':
        form = EditStaffForm(request.POST, instance = staff)
        if form.is_valid:
            form.save()
            messages.success(request, f'added succefully')
        else:
            messages.error(request, f'unable to add details')
    context = {
        'form' : form,
    }
    return render(request, 'Company/editfarmer.html', context)


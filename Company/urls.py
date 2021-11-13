from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.dashboard, name='home'),
    path('records/', views.records, name = 'records'),
    path('reviews/', views.reviews, name='reviews'),
    path('farmers/', views.farmers, name = 'farmers'),
    path('staffs/', views.staffs, name = 'staffs'),
    path('payments/', views.payments, name = 'payments'),

    # form urls 
    path('add-farmer/', views.add_farmer, name='add-farmer'),
    path('add-staff/', views.add_staff, name='add-staff'),
    path('add-record/', views.add_record, name= 'add-record'),
    path('add-payment/', views.add_payment, name='add-payment'),
]

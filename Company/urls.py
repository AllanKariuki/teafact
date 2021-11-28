from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.dashboard, name='home'),
    path('records/', views.records, name = 'company-records'),
    path('reviews/', views.reviews, name='company-reviews'),
    path('farmers/', views.farmers, name = 'farmers'),
    path('staffs/', views.staffs, name = 'staffs'),
    path('payments/', views.payments, name = 'company-payments'),
    path('farmers/<name>/', views.view_farmer, name='view-farmer'),
    path('farmers/<name>/edit', views.edit_farmer, name='edit-farmer'),
    path('<name>/staffs/', views.view_staff, name='view-staff'),
    path('staffs/<name>/edit', views.edit_staff, name='edit-staff'),
    path('records/<id>/', views.view_record, name='view-record'),
    path('payments/<title>', views.view_payment, name='view-payment'),    
    path('review/<id>', views.view_review, name = 'review-detail'),

    # form urls 
    path('add-farmer/', views.add_farmer, name='add-farmer'),
    path('add-staff/', views.add_staff, name='add-staff'),
    path('add-record/<name>/', views.add_record, name= 'add-record'),
    path('add-payment/', views.add_payment, name='add-payment'),

    path('logout/', auth_views.LogoutView.as_view(template_name = 'Farmer/logout.html'), name='logout'),
    #update urls
    # path('farmers/<name>/edit/', views.update_farmer, name ='edit-farmer')
]

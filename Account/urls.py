from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from Company import views as company_views
from Farmers import views as farmer_views

urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('register/', views.registerpage, name='register'),
    path('', company_views.dashboard, name='home'),
    path('dashboard/', farmer_views.home, name = 'farmer-page'),
    # path('logout/', views.logoutpage, name='logout-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'Company/logout.html'), name='logout'),
]

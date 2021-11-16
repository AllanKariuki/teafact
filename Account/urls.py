from django.urls import path
from . import views
from Company import views as company_views

urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('register/', views.registerpage, name='register'),
    path('', company_views.dashboard, name='home'),
    path('logout/', views.logoutpage, name='logout-page'),
]

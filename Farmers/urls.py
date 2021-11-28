from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from Account import views as account_views
urlpatterns = [
      path('dashboard/', views.home, name = 'farmer-page'),

      path('records/', views.records, name='records'),
      path('<id>/record-detail/', views.recordDetail, name = 'record-detail'),

      path('payments/', views.payments, name='payments'),
      path('<id>/payment-detail/', views.paymentDetail, name='payment-detail'),

      path('profile/', views.profile, name='profile'),
      path('editprofile/', views.editprofile, name='editprofile'),

      path('reviews/', views.reviews, name='reviews'),
      path('<id>/review-detail/', views.reviewDetail, name='rdetail'),
      path('add-review/', views.createReview, name='add-review'),

      path('logout/', auth_views.LogoutView.as_view(template_name = 'Company/logout.html'), name='logout'),
      
#     path('page3/', views.page3, name= 'page3'),
#     path('page1/', views.page1, name='page1'),
]
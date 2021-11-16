from django.urls import path
from . import views

urlpatterns = [
      path('dashboard/', views.home, name = 'home'),

      path('records/', views.records, name='records'),
      path('record-detail', views.record_detail, name = 'record-detail'),

      path('payments/', views.payments, name='payments'),
      path('payment-detail/', views.payment_detail, name='payment-detail'),

      path('profile/', views.profile, name='profile'),
      path('editprofile/', views.editprofile, name='profile'),

      path('reviews/', views.reviews, name='reviews'),
      path('review-detail/', views.review_detail, name='view-review'),
      path('add-review/', views.create_review, name='add-review'),
      
#     path('page3/', views.page3, name= 'page3'),
#     path('page1/', views.page1, name='page1'),
]
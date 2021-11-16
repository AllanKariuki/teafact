from django.urls import path
from . import views
from Account import views as account_views
urlpatterns = [
      path('dashboard/', views.home, name = 'home'),

      path('records/', views.records, name='records'),
      path('<id>/record-detail/', views.recordDetail, name = 'record-detail'),

      path('payments/', views.payments, name='payments'),
      path('<id>/payment-detail/', views.paymentDetail, name='payment-detail'),

      path('profile/', views.profile, name='profile'),
      path('editprofile/', views.editprofile, name='editprofile'),

      path('reviews/', views.reviews, name='reviews'),
      path('<id>/review-detail/', views.reviewDetail, name='review-detail'),
      path('add-review/', views.createReview, name='add-review'),

      path('logout/', account_views.logoutpage, name='logout-page'),
      
#     path('page3/', views.page3, name= 'page3'),
#     path('page1/', views.page1, name='page1'),
]
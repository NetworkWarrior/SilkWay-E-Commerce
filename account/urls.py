from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    
    #email verification URL's
    path('email-verification/<str:uidb64>/<str:token>/', views.email_verification, name='email-verification'),
    path('email-verification-sent', views.email_verification_sent, name='email-verification-sent'),
    path('email-verification-success', views.email_verification_succes, name='email-verification-success'),
    path('email-verification-failed', views.email_verification_failed, name='email-verification-failed'),

    #login and logout
    path('my-login', views.my_login, name='my-login'),
    path('user-logout', views.user_logout, name='user-logout'),
    path('dashboard', views.dashboard, name='dashbaord'),
]


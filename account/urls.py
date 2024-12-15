from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    
    #email verification URL's
    path('email-verification', views.email_verification, name='email-verification'),
    path('email_sent', views.email_sent, name='email_sent'),
    path('email_success', views.email_succes, name='email_success'),
    path('email_failed', views.email_failed, name='email_failed'),
]


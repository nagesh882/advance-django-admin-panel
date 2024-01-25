from django.urls import path
from login import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('otp_verify/', views.otp_verify, name='otp_verify'),
    path('HomePage/', views.HomePage, name='HomePage'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]
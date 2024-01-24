from django.urls import path
from login import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('', views.login, name='login'),
    path('HomePage/', views.HomePage, name='HomePage'),
    path('indexPage/', views.indexPage, name='indexPage'),
    path('logout/', views.user_logout, name='logout'),
]
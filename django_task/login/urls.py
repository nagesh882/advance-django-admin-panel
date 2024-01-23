from django.urls import path
from login import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('HomePage/', views.HomePage, name='HomePage'),
    path('', views.indexPage, name='indexPage'),
]
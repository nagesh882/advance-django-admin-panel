from django.urls import path
from login import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('otp_verify/', views.otp_verify, name='otp_verify'),
    path('HomePage/', views.home_page, name='home_page'),
    path('logout/', views.user_logout, name='logout'),
    path('update/<int:user_id>', views.update, name="update"),
    path('web_base/<int:user_id>', views.web_base, name='web_base'),
    path('edit/', views.edit, name='edit'),
    path('update_data/', views.update_data, name='update_data'),

]
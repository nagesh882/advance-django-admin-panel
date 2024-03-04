from django.urls import path
from login import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('otp_verify/', views.otp_verify, name='otp_verify'),
    path('HomePage/', views.home_page, name='home_page'),
    path('logout/', views.user_logout, name='logout'),
    path('update/<int:user_id>/', views.update, name="update"),
    path('web_base/<int:user_id>/', views.web_base, name='web_base'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('product/', views.product_details, name='product'),
    path('product_update/<int:product_id>/', views.product_update, name='product_update'),
    path('product_create/', views.product_create, name='product_create'),
    path('delete/<int:product_id>/', views.delete, name='delete'),
 
]
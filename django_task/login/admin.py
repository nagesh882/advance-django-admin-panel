from django.contrib import admin
from login.models import Register, Products


# Model 1
@admin.register(Register)
class productAdmin(admin.ModelAdmin):   
    list_display = ["user_id", "user_name", "user_email", "city"]


# Model 2
@admin.register(Products)
class productAdmin(admin.ModelAdmin):   
    list_display = ["product_id", "product_name", "product_price", "hsn_code"]

from django.db import models
from products.models import Products
from login.models import Register

class Products(models.Model):
    product_id = models.AutoField(primary_key=True, unique=True)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    hsn_code = models.CharField(max_length=20)
    manufacture_date = models.DateField()
    expiry_date = models.DateField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Register, on_delete=models.CASCADE)

    def __str__(self):
        return f'Product ID: {self.product_id}, Product Name: {self.product_name}'


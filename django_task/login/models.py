from django.db import models
import datetime
# Create your models here.
class Register(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    user_phone = models.CharField(max_length=50)
    # user_dob = models.DateField(default=datetime.date.today)
    user_dob = models.DateField()
    gender = models.CharField(max_length=100)
    aadhar = models.CharField(max_length=20) 
    pan = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=20)

    def __str__(self):
        return f'User ID: {self.user_id}, User Name: {self.user_name}'
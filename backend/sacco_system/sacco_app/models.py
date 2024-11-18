from tkinter.constants import CASCADE

from django.db import models
from django.template.defaultfilters import length, default


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField (max_length=30)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    gender=models.CharField(max_length=10)
    weight=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='customers'

class Deposit(models.Model):
    amount= models.IntegerField()
    status= models.BooleanField(default=False)
    customer= models.ForeignKey(Customer,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='deposits'

#python manage.py makemigrations
 #python manage.py migrate
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=20,null=False,default="12345")
    phone = PhoneNumberField(null=False, blank=False, unique=True)

class staff(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(null=False)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    address = models.TextField(max_length=30)
    choice = (('manager','manager'),('staff','staff'))
    position = models.CharField(max_length=7,choices=choice,default="staff")
    password = models.CharField(max_length=20,null=False,default="12345")

class MenuItems(models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    choice = (('melt','melt'),('sandwich','sandwich'),('drink','drink'),('crisp','crisp'))
    type = models.CharField(max_length=8,choices=choice)
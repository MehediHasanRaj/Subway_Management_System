from django.db import models


# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(null=False)
    phone = models.IntegerField()

class staff(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.TextField(max_length=30)
    choice = (('manager','manager'),('staff','staff'))
    position = models.CharField(max_length=7,choices=choice,default="staff")

class Items(models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=2,decimal_places=2)
    choice = (('melt','melt'),('sandwich','sandwich'))
    type = models.CharField(max_length=8,choices=choice)
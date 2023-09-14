from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Users)
# admin.site.register(staff)

@admin.register(MenuItems)

class Admin(admin.ModelAdmin):
    list_display = ['id','name','price','type','picture']

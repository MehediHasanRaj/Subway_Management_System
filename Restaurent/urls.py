"""
URL configuration for Subway_Management_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', home,name = "home"),
    path('about/',about, name = "about"),
    path('order/',order, name = "order"),
    path('menu/',menu, name = "menu"),
    path('items/',items, name = "items"),
    path('delete-menu/<int:menu_id>',delete_menu),
    path('update-menu/<int:menu_id>',update_menu),
    path('add-item/',addItem,name = 'add-item'),
    path('registration/',Registration,name ='Registration'),
    path('login/', Login, name='Login'),
    path('logout/',Logout,name='Logout'),
    path('item-view/',item_view, name = 'item_view'),
    path('item-add/',item_add, name = 'item_add'),
    path('item-delete/',item_delete, name = 'item_delete'),
    path('item-update/',item_update, name = 'item_update'),
    path('profile/',profile)



]

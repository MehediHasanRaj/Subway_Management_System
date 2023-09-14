
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
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
    path('profile/',profile),
    path('orderadd/',orderadd, name = 'orderadd'),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

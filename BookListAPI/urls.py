
from django.urls import path,include
from . import views

urlpatterns = [
    path('books/',views.Booklist.as_view()),
    path('books/<int:pk>',views.Book.as_view()),


]

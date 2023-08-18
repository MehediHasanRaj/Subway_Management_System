from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'base.html',{} )
def about(request):
    return render(request,'about.html',{})
def menu(request):
    return render(request,'menu.html',{} )
def order(request):
    return render(request, 'order.html', {})
def login(request):
    return render(request,'login.html',{} )
def items(request):
    return render(request,'items.html',{})

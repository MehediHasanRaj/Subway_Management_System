from django.shortcuts import render
from django.http import HttpResponse
from .form import StaffForm,UserForm,ItemsForm

# Create your views here.
def home(request):
    return render(request,'home.html',{} )
def about(request):
    return render(request,'about.html',{})
def menu(request):
    return render(request,'menu.html',{} )
def order(request):
    return render(request, 'order.html', {})
def signinup(request):
    return render(request, 'SignInOrUP.html', {})
def items(request):
    return render(request,'items.html',{})

def formView(request):
    form = StaffForm()
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'userform.html',{'form':form})
def usersignin(request):
    return render(request, 'userlogin.html',{})
def stafflogin(request):
    return render(request,'stafflogin.html',{})
def staffregistration(request):
    form = StaffForm()
    return render(request,'staffregistration.html',{'form':form})
def userregistration(request):
    form = UserForm()
    return render(request,'userregistration.html',{'form':form})
def signin(request):
    return render(request, 'signin.html',{})
def signup(request):
    return render(request,'signup.html',{})


#newly added for api tutorials
from rest_framework import generics
from. models import MenuItems
from .serializers import MenuItemSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer

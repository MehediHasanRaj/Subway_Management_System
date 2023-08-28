from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import StaffForm,UserForm,ItemsForm
from .models import MenuItems
# Create your views here.
def home(request):
    return render(request,'home.html',{} )
def about(request):
    return render(request,'about.html',{})
def menu(request):
    data = MenuItems.objects.all()
    print(data)
    return render(request,'menu.html',{"data":data} )
def order(request):
    return render(request, 'order.html', {})
def signinup(request):
    return render(request, 'SignInOrUP.html', {})
def items(request):
    form = ItemsForm()
    return render(request,'items.html',{'form':form})
def addItem(request):
    text = ""
    if request.method == "POST":
        form = ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            text = "Create or Update successfully!!!"
    else:
        form = ItemsForm()
    return render(request,"items.html",{'form':form,'text':text})

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
    thanks = ""
    if request.method=="POST": #initiall clicking on the form just pass get if we click submit button then post methond
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            thanks = "successfully submitted"
        else:
            print("this form is not valid")
    else:
        form = StaffForm()
    return render(request,'staffregistration.html',{'form':form,'thanks':thanks})
def userregistration(request):
    thanks = ""
    if request.method == "POST":  # initiall clicking on the form just pass get if we click submit button then post methond
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            thanks = "successfully submitted"
        else:
            print("this form is not valid")
    else:
        form = UserForm()
    return render(request,'userregistration.html',{'form':form,'thanks':thanks})
def signin(request):
    return render(request, 'signin.html',{})
def signup(request):
    return render(request,'signup.html',{})

def delete_menu(request,menu_id):
    menuItem = MenuItems.objects.get(pk=menu_id)
    menuItem.delete()
    return redirect("/menu/")

def update_menu(request,menu_id):
    menuitem = MenuItems.objects.get(pk=menu_id)
    form = ItemsForm(instance = menuitem)
    return render(request,"update_menu.html",{'form':form})


# #newly added for api tutorials
# from rest_framework import generics
# from. models import MenuItems
# from .serializers import MenuItemSerializer
#
# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItems.objects.all()
#     serializer_class = MenuItemSerializer

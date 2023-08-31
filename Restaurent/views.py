from django.shortcuts import render, redirect
from .form import ItemsForm  # ,UserForm
from .models import MenuItems
from django.contrib import messages
from .form import CustomUserCreationForm,userloginform

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def menu(request):
    data = MenuItems.objects.all()
    print(data)
    return render(request, 'menu.html', {"data": data})

def order(request):
    return render(request, 'order.html', {})



def items(request):
    form = ItemsForm()
    return render(request, 'items.html', {'form': form})


def addItem(request):
    text = ""
    if request.method == "POST":
        form = ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            text = "Create or Update successfully!!!"
    else:
        form = ItemsForm()
    return render(request, "items.html", {'form': form, 'text': text})



def delete_menu(request, menu_id):
    menuItem = MenuItems.objects.get(pk=menu_id)
    menuItem.delete()
    return redirect("/menu/")


def update_menu(request, menu_id):
    menuitem = MenuItems.objects.get(pk=menu_id)
    form = ItemsForm(instance=menuitem)
    return render(request, "update_menu.html", {'form': form})

def Registration(request):
    method = request.method
    print('type of method is ',end='')
    print(type(method))

    if method == "POST":
        print("I am at post method")

        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("user creation successfulyyy")
            messages.success(request, "Account created successfully")
            # return redirect('')
        else:
            print("not created user")
    else:
        print("I am in else method")
        form = CustomUserCreationForm()
    return render(request, 'Registration.html', {'form':form})


def login(request):
    if request.method=="POST":
        print("i am post")
        print(request.POST)
        return redirect('home')
    form = userloginform()
    return render(request,'login.html',{'form':form})







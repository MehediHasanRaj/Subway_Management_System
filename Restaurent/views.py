from django.shortcuts import render, redirect
from .form import ItemsForm  # ,UserForm
from .models import MenuItems
from django.contrib import messages
from .form import CustomUserCreationForm,userloginform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/login/")
def home(request):
    return render(request, 'home.html', {})

def orderadd(request):
    print('this is product id' + str(request.POST.get('product')))
    print('this is reqeust', request.POST)
    product = request.POST.get('product')
    cart = request.session.get('cart')
    if cart:
        quantity = cart.get(product)
        print('this is the quantity ', quantity)
        if quantity:
            cart[product] = quantity + 1
        else:
            cart[product] = 1
    else:
        cart = {}
        cart[product] = 1
    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect('/menu/')
def about(request):
    return render(request, 'about.html', {})

def menu(request):
    data = MenuItems.objects.all()
    print(data)
    return render(request, 'menu.html', {"data": data})

def order(request):
    return render(request, 'order.html', {})



def items(request):
    data = MenuItems.objects.all()
    form = ItemsForm()
    return render(request, 'items.html', {'form': form,'d':data})

def item_view(request):
    data = MenuItems.objects.all()
    return render(request,'item-view.html',{'data':data})

def item_add(request):
    sms = ""
    print(request.POST)
    print(request.FILES)
    if request.method == "POST":
        form = ItemsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            sms="Item added successfully!!"
        else:
            sms = "Something went wrong!!!"
    else:
        form = ItemsForm()
    return render(request,'item-add.html',{'form':form,'sms':sms})
def addItem(request):
    text = ""
    if request.method == "POST":
        form = ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            text = "Create or Update successfully!!!"
    else:
        form = ItemsForm()
    return render(request, "item-add.html", {'form': form, 'text': text})

def profile(request):
    return render(request,'test.html',{'User':User})

def delete_menu(request, menu_id):
    menuItem = MenuItems.objects.get(pk=menu_id)
    menuItem.delete()
    return redirect("/item-delete/")

def item_delete(request):
    data = MenuItems.objects.all()
    return render(request,'item-delete.html',{'data':data})


def update_menu(request, menu_id):
    menuitem = MenuItems.objects.get(pk=menu_id)
    form = ItemsForm(instance=menuitem)
    menuitem.delete()
    return render(request, "item-add.html", {'form': form})

def item_update(request):
    data = MenuItems.objects.all()
    return render(request,'item-update.html',{'data':data})
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



def Login(request):
    # print("this --method is ---")
    # print(request.method)
    # print('end method')
    if request.method=="POST":
        # print('i am it post')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'username does not exist')
            # print('username doesnot')
            return redirect('Login')

        user = authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'invalid username or password!!')
            return redirect('Login')
        else:
            login(request,user)
            return redirect('home')

    form = userloginform()
    return render(request,'login.html',{'form':form})

def Logout(request):
    logout(request)
    return redirect('Login')








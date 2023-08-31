from django.forms import ModelForm
from Restaurent.models import MenuItems#,Users
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import ValidationError
from django.forms.fields import EmailField
from django.forms. forms import Form
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username', min_length=5, max_length=150,widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control form-control-lg'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}))


    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email Already Exist")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],

        )
        return user

class userloginform(Form):
    username = forms.CharField(label='Username', min_length=5, max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))



class ItemsForm(ModelForm):
    class Meta:
        model = MenuItems
        fields = '__all__'

# class StaffForm(ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = staff
#         fields = '__all__'




# class UserForm(UserCreationForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = Users
#         fields = '__all__'

from django.forms import ModelForm
from Restaurent.models import Users,staff,MenuItems
from django import forms
class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Users
        fields = '__all__'

class StaffForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = staff
        fields = '__all__'
class ItemsForm(ModelForm):
    class Meta:
        model = MenuItems
        fields = '__all__'
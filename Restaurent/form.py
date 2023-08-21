from django.forms import ModelForm
from Restaurent.models import Users,staff

class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'

class StaffForm(ModelForm):
    class Meta:
        model = staff
        fields = '__all__'
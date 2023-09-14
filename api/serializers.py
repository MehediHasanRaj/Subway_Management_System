from rest_framework import serializers
from Restaurent.models import MenuItems

class MenuItemsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    price = serializers.DecimalField(max_digits=4,decimal_places=2)
    choice = (('melt','melt'),('sandwich','sandwich'),('drink','drink'),('crisp','crisp'))
    type = serializers.ChoiceField(choices=choice)

    def create(self,validate_data):
        return MenuItems.objects.create(**validate_data)
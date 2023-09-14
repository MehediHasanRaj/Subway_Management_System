import io

from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .serializers import MenuItemsSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def menu_create_api(request): #data inserting using api
    if request.method =="POST":
        json_data = request.body # json data
        stream = io.BytesIO(json_data) # convert to bytes stream
        python_data = JSONParser().parse(stream) # convert python data
        serializer = MenuItemsSerializer(data=python_data) #  convert complex data
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


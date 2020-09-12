# django_Api
In this Repo i will design Django API for get item,post item,get individual item or update item through model view.

steps 1: Create project and install django rest framework.
step2: define app and rest_framework inside installed app in django setting.
step3:create model for database table like:

```
class Signup(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=8)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

```
step4: create serializer.py iinside app and import serializer from django_resstframework or model write code like:

```
from rest_framework import serializers
from learnrest.models import Signup


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ['id','name','password','phone','address']

```
step5: now create function in views.py for get all item, add item into db, get indvidual item,and update item.
first import module

```
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from learnrest.serializers import SignupSerializer
from learnrest.models import Signup
from rest_framework import status

#get all item.
@api_view(['GET'])
def product_list(request):
    if request.method =="GET":
        obj = Signup.objects.all()
        serializer = SignupSerializer(obj,many=True)
        return Response(serializer.data)
    
# add item
@api_view(['POST'])    
def product_save(request):
    if request.method=="POST":
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

#for update and getting individual item.
@api_view(['GET','PUT'])
def get_individual(request, id):
    try:
        obj = Signup.objects.get(id = id)
    except Signup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SignupSerializer(obj)
        return Response(serializer.data)
    if request.method =='PUT':
        serializer = SignupSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


```
step6: define url against views.
```
 path('',views.product_list),
    path('save',views.product_save),
    path('dist/<int:id>',views.get_individual),

```

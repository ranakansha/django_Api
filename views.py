from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from learnrest.serializers import SignupSerializer
from learnrest.models import Signup
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def product_list(request):
    if request.method =="GET":
        obj = Signup.objects.all()
        serializer = SignupSerializer(obj,many=True)
        return Response(serializer.data)
    

@api_view(['POST'])    
def product_save(request):
    if request.method=="POST":
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


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

from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import Users
from accounts.serializers import UsersSerializer
from content.models import User

@api_view(['POST' , 'GET'])
def user_list_or_create(request):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UsersSerializer(users, many=True)
        return Response(users_serializer.data)

    if request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT' , 'DELETE' , 'PATCH'])
def user_update_or_delete(request , pk):
    if request.method == 'PUT':
        users = Users.objects.get(pk=pk)
        serializer = UsersSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PATCH':
        users = Users.objects.get(pk=pk)
        serializer = UsersSerializer(users, data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils.representation import serializer_repr
from django.shortcuts import get_object_or_404

from content.models import Post, Like
from content.serializers import PostSerializer, LikeSerializer


@api_view(['GET', 'POST'])
def post_cr_views(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts , many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def post_rud_views(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST','DELETE'])
def like_views(request,pk=None):
    if request.method == 'GET':
        post_id = request.GET.get("post_id")
        if post_id:
            likes = Like.objects.filter(post_id=post_id)
        else:
            likes = Like.objects.all()

        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if not pk:
            return Response({"errors": "pk kiritilmadi"},status=status.HTTP_400_BAD_REQUEST)
        try:
            like = Like.objects.get(pk=pk)
        except Like.DoesNotExist:
            return Response({"errors":"like not founds"},status=status.HTTP_404_NOT_FOUND)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def postfeedview(request):
    pass



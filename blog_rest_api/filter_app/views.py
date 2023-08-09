from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializer import PostSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from django_filters import rest_framework as filter
from rest_framework import filters
# Create your views here.


class Postfilter(filter.FilterSet):
    title = filter.CharFilter(field_name='title')
    age = filter.NumberFilter(field_name='age',lookup_expr="gt")


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    # filterset_fields = ["title"]
    filterset_class =Postfilter
    search_fields =['title','content']
    ordering_fields='__all__'


class PostAPI(APIView):

    def get(self,request):
        obj = Post.objects.all()
        serializer =PostSerializer(obj, many=True)
        return Response(serializer.data)
    def post(self,request):
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self,request):
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self,request):
        data = request.data
        obj = Post.objects.get(id=data['id'])
        serializer = PostSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        blog = Post.objects.get(pk=pk)
        blog.delete()
        return Response (status=status.HTTP_200_OK)
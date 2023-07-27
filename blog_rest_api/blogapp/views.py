from django.shortcuts import render
from django.http.response import JsonResponse
from . models import *
from rest_framework.response import Response
from .serializera import BlogSerializers,CategorySerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
# Create your views here.


def blog_list(request):
    data ={
        'messages':'Hello World'
    }
    return JsonResponse(data)


def blog_lists(request):
    blogs = Blog.objects.all()
    data ={
        "blogs":list(blogs.values())
    }
    return JsonResponse(data)


def blog_detail(request,pk):
    blogs = Blog.objects.get(pk=pk)
    data ={
        'name':blogs.name,
        'description':blogs.blog_description,
        'slug':blogs.slug
    }
    return JsonResponse(data)


@api_view(['GET', 'POST'])
def list_blog(request):
    all_blogs = Blog.objects.filter(is_public=True)
    serializer = BlogSerializers(all_blogs, many=True)
    return Response(serializer.data)


@api_view(['GET','POST'])
def detail_blog(request,pk):
    blogs = Blog.objects.get(pk=pk)
    serializer = BlogSerializers(blogs)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def list_blogs(request):
    if request.method == "GET":
        all_blogs = Blog.objects.filter(is_public=True)
        serializer = BlogSerializers(all_blogs, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BlogSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#
@api_view(['GET',"PUT",'DELETE'])
def put_blog_list(request,pk):
    if request.method == 'GET':
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializers(blog)
        return Response(serializer.data)
    if request.method == 'PUT':
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializers(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.views import APIView


class BlogListView(APIView):
    def get(self, request):
        all_blogs = Blog.objects.filter(is_public=True)
        serializer = BlogSerializers (all_blogs, many=True)
        return Response (serializer.data, status=status.HTTP_200_OK)

    def post (self, request):
        serializer = BlogSerializers (data=request.data)
        if serializer.is_valid():
            serializer. save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response (serializer.errors, status=status. HTTP_400_BAD_REQUEST)
# GET, PUT, DELETE


class Blog_DetailView (APIView):
    def get(self, request,pk):
        all_blogs = Blog.objects.get(pk=pk)
        serializer = BlogSerializers(all_blogs)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put (self, request, pk):
        blog =Blog.objects.get(pk=pk)
        serializer = BlogSerializers (blog, data=request.data)
        if serializer.is_valid ():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_200_OK)
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response (status=status.HTTP_200_OK)


class CategoryListView(APIView):
    def get (self, request):
        all_category = category.objects.all()
        serializers = CategorySerializer(all_category, many=True,context={'request': request})
        return Response(serializers.data)


class CategoryDetailView (APIView):
    def get (self, request, pk):
        single_category = category.objects.get(pk=pk)
        serializers = CategorySerializer (single_category,context={'request': request})
        return Response (serializers.data)

#generic views

from rest_framework import mixins
class BlogListGenericView (mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    def get (self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post (self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BlogDetailGenericView (mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers

    def get(self, request, *args, **kwargs) :
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs) :
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs) :
        return self.destroy(request, *args, **kwargs)
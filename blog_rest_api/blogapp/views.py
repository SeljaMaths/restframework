from django.shortcuts import render
from django.http.response import JsonResponse
from . models import *
from rest_framework.response import Response
from .serialziers import BlogSerializers,CategorySerializer,BlogCommentserializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from .permissions import IsAdminUserReadOnly,IsOwneronly
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle,ScopedRateThrottle
from .throttle import CategoryListCreateViewThrottle
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
        # 'name':blogs.name,
        'description':blogs.description,
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
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs) :
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs) :
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs) :
        return self.destroy(request, *args, **kwargs)

# concerate view classes


class Blogcreatecon (generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers


class BlogListCon (generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers


class BlogRetrieveCon (generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers


class BlogdeleteCon (generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    lookup_field = 'slug'


class BlogUpdateCon (generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers


class BlogretrieveUpdateCon (generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers


class BlogretrievedeleteeCon (generics.RetrieveDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers


class BlogListDestroyApiView (generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers


class BloglistUPdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers


#creating view sets and routes in django


from rest_framework import viewsets
from django.shortcuts import get_object_or_404



class BlogViewsets(viewsets.ViewSet):
    def list(self,request):
        queryset = Blog.objects.filter(is_public=True)
        serializer = BlogSerializers(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        queryset = Blog.objects.filter(is_public=True)
        blog_list = get_object_or_404(queryset, pk=pk)
        serializer = BlogSerializers(blog_list)
        return Response(serializer.data)

    def create(self, request):
        serializer = BlogSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializers(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return Response({"Message": "Your blog has been deleted"}, status=status.HTTP_204_NO_CONTENT)

# Modelviewsets


class BlogViewModelset(viewsets.ModelViewSet):
    queryset = Blog.objects.filter(is_public =True)
    serializer_class = BlogSerializers


class BlogListCreateView (generics.ListCreateAPIView):
    queryset = Blog.objects.filter(is_public = True)
    serializer_class = BlogSerializers

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BlogSerializers(queryset, many=True, context={'request': request})
        if queryset.exists():
            return Response (serializer.data, status=status. HTTP_200_OK)
        else:
            return Response({ 'Message': 'No blogs found'}, status=status.HTTP_204_NO_CONTENT)

    def create(self,request,*args,**kwargs):
        serializer = BlogSerializers(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED, headers=headers)


class BlogLiseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Blog.objects.filter(is_public=True)
    serializer_class = BlogSerializers
    filed = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance:
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'Message':'No blog found'},status=status.HTTP_404_NOT_FOUND)


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer

    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
    #username throotale and annorate
    # throttle_classes = [UserRateThrottle,AnonRateThrottle]
    # scope
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'blog-list'
    # custom
    throttle_classes = [CategoryListCreateViewThrottle]


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True, context={'request': request})
        if queryset.exists():
            return Response (serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({ 'Message': 'No category found'}, status=status.HTTP_204_NO_CONTENT)


class Category_Detail_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer
    liikup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance:
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'Message':'No category found'},status=status.HTTP_404_NOT_FOUND)


class BLogcommentLIstCreateview(generics.ListCreateAPIView):
    queryset =BlogComment.objects.all()
    serializer_class = BlogCommentserializer

    def get_queryset(self):
        blog_id = self.kwargs.get('blog_id')
        return BlogComment.objects.filter(blog_id=blog_id)

    def perform_create(self, serializer):
        blog_id = self.kwargs.get('blog_id')
        blog = get_object_or_404(Blog,id=blog_id)
        if BlogComment.objects.filter(blog=blog,author = self.request.user).exists():
            raise serializer.ValidationError({'Messages':'you have  already added  comment on this blog'})
        serializer.save(author = self.request.user,blog=blog)


class BlogCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentserializer
    permission_classes = [IsOwneronly]

    def get_object(self):
        comment_id = self.kwargs.get('comment_id')
        comment = get_object_or_404(BlogComment,id = comment_id)
        blog_id = self.kwargs.get('blog_id')
        if comment.blog_id != blog_id:
            raise serializers.ValidationError({'message':'this comment is not related to the request blog'})
        return comment



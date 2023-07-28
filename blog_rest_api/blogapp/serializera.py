from rest_framework import serializers
from . models import *
from .urls import  *



# nested serializers

class BlogSerializers (serializers. ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)


    class Meta:
        model = Blog
        fields = "__all__"


class CategorySerializer (serializers.HyperlinkedModelSerializer):
    category_name = serializers.CharField()
    category = BlogSerializers(many=True,read_only=True)
    class Meta:
        model = category
        fields ='__all__'
    # category=serializers.StringRelatedField(many=True)
    # category = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # category = serializers.SlugRelatedField(many=True,read_only=True,slug_field='slug')
    # category = serializers.HyperlinkedRelatedField(
    #     many=True,
    # read_only=True,
    #     view_name='Blog_DetailView'
    #
    #
    # )
    #


# class CategorySerializer (serializers. ModelSerializer):
#     # category_name = serializers.CharField()
#     # category = BlogSerializers(many=True,read_only=True)
#     # category=serializers.StringRelatedField(many=True)
#     # category = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
#     # category = serializers.SlugRelatedField(many=True,read_only=True,slug_field='slug')
#     category = serializers.HyperlinkedRelatedField(
#         many=True,
#     read_only=True,
#         view_name='Blog_DetailView'
#
#
#     )
#
#     class Meta:
#         model = category
#         exclude = ['id', ]

# def validate_title(value):
#     if len(value) < 4:
#         raise serializers.ValidationError("Blog title is very short")
#
#     else:
#         return value
# class BlogSerializers (serializers. ModelSerializer):
#         id = serializers.IntegerField(read_only=True)
#         name = serializers.CharField(validators=[validate_name])
#         blog_title = serializers.CharField()
#         is_public = serializers.BooleanField()
#         blog_description = serializers.CharField()
#         post_date = serializers.DateField()
#         slug = serializers.CharField()


# class BlogSerializers (serializers. ModelSerializer):
#     len_title = serializers.SerializerMethodField()
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(validators=[validate_title])
    # description = serializers.CharField()
    # is_public = serializers.BooleanField()
    # post_date = serializers.DateField()
    # slug = serializers.CharField()

    # class Meta:
    #     model = Blog
    #     fields ='__all__'
    #
    # def get_len_title(self,object):
    #     return len(object.title)
        # fields = ['id','name','blog_title']
        # exclude =['slug']

        # Field-level validation
        # def validate_name(self, value):
        #     if len(value) < 4:
        #         raise serializers.ValidationError("Blog title is very short")
        #
        #     else:
        #         return value

        # def validate(self, data):
        #     if data['name'] == data['description']:
        #         raise serializers.ValidationError("Blog title and description can not be same")
        #
        #     else:
        #         return data
# class BlogSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     blog_title = serializers.CharField()
#     is_public = serializers.BooleanField()
#     blog_description = serializers.CharField()
#     post_date = serializers.DateField()
#     slug = serializers.CharField()
#
#     def create(self, validated_data):
#         return Blog.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',  instance.name)
#
#         instance.blog_title = validated_data.get('blog_title',  instance.blog_title)
#         instance.is_public = validated_data.get('is_public',  instance.is_public)
#         instance.blog_description = validated_data.get('blog_description',  instance.blog_description)
#         instance.post_date = validated_data.get('post_date',  instance.post_date)
#         instance.slug = validated_data.get('slug',  instance.slug)
#         instance.save()
#         return instance

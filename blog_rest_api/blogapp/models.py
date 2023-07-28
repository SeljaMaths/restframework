
import random
import string
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Create your models here.
from datetime import date


class category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(category, on_delete=models.SET_NULL, null=True,related_name='category')
    post_date = models.DateField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    slug = models.CharField(max_length=1000, null=True, blank=True)

# class Blog(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     blog_title = models.CharField(max_length=100, null=True)
#     is_public = models.BooleanField(default=True)
#     blog_description = models.TextField()
#     post_date = models.DateField(default=date.today)
#     slug = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title

    # def save(self, *args,**kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args,**kwargs)


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title + " " + self.author.username + " " + self.category.category_name)
            self.slug = base_slug + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
            return super().save(*args, **kwargs)


class BlogComment(models.Model):
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.blog)

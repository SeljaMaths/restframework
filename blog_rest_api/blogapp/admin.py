from django.contrib import admin
from .models import BlogComment,Blog,category

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','post_date','is_public')
    list_display_links = ['id','title']
    search_fields = ('title',)
    list_per_page = 1
    list_editable = ("is_public",)


admin.site.register(Blog,BlogAdmin)
admin.site.register(BlogComment)
admin.site.register(category)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blog_lists/', views.blog_lists, name='blog_lists'),
    path('blog_detail/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('list_blog/', views.list_blog, name='list_blog'),
    path('detail_blog/<int:pk>/', views.detail_blog, name='detail_blog'),
    path('list_blogs/', views.list_blogs, name='list_blogs'),
    path('put_blog_list/<int:pk>/', views.put_blog_list, name='put_blog_list'),
    path('BlogListView/', views.BlogListView.as_view(), name='BlogListView'),
    path('Blog_DetailView/<int:pk>/', views.Blog_DetailView.as_view(), name='Blog_DetailView'),
    path('CategoryListView/', views.CategoryListView.as_view(), name='Category-ListView'),
    path('CategoryDetailView/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('BlogListGenericView/', views.BlogListGenericView.as_view(), name='BlogListGenericView')


]

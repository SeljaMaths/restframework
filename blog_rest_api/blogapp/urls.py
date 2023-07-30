
from django.urls import path,include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'blogs',views.BlogViewsets,basename='blogs')
router.register(r'blogs',views.BlogViewModelset,basename='blogs')

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    # category
    path('CategoryListCreateView/', views.CategoryListCreateView.as_view(), name='CategoryListCreateView'),
    path('Category_Detail_View/<int:pk>/', views.Category_Detail_View.as_view(), name='Category_Detail_View'),
    path('BLogcommentLIstCreateview/<int:blog_id>/', views.BLogcommentLIstCreateview.as_view(), name='BLogcommentLIstCreateview'),


















    path('', include(router.urls)),
    # path('', views.blog_list, name='blog_list'),
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
    path('BlogListGenericView/', views.BlogListGenericView.as_view(), name='BlogListGenericView'),
    # path('BlogDetailGenericView/<int:pk>/', views.BlogDetailGenericView.as_view(), name='BlogDetailGenericView'),
    path('BlogDetailGenericView/<str:slug>/', views.BlogDetailGenericView.as_view(), name='BlogDetailGenericView'),
    path('BlogListCon/', views.BlogListCon.as_view(), name='BlogListCon'),
    path('Blogcreatecon/', views.Blogcreatecon.as_view(), name='Blogcreatecon'),
    path('BlogRetrieveCon/<int:pk>/', views.BlogRetrieveCon.as_view(), name='BlogRetrieveCon'),
    path('BlogdeleteCon/<str:slug>/', views.BlogdeleteCon.as_view(), name='BlogdeleteCon'),
    path('BlogUpdateCon/<int:pk>/', views.BlogUpdateCon.as_view(), name='BlogUpdateCon'),
    path('BlogretrieveUpdateCon/<int:pk>/', views.BlogretrieveUpdateCon.as_view(), name='BlogretrieveUpdateCon'),
    path('BlogretrievedeleteeCon/<int:pk>/', views.BlogretrievedeleteeCon.as_view(), name='BlogretrievedeleteeCon'),
    path('BlogListDestroyApiView/', views.BlogListDestroyApiView.as_view(), name='BlogListDestroyApiView'),
    path('BloglistUPdateDeleteApiView/<int:pk>/', views.BloglistUPdateDeleteApiView.as_view(), name='BloglistUPdateDeleteApiView'),
    path('BlogListCreateView/', views.BlogListCreateView.as_view(), name='BlogListCreateView'),
    path('BlogLiseDetailView/<int:pk>/', views.BlogLiseDetailView.as_view(), name='BlogLiseDetailView'),




]

from . import views
from django.urls import path,include

urlpatterns = [

    path('YourModelView/', views.YourModelView.as_view(), name='YourModelView'),
    path('YourDetailView/<int:pk>/', views.YourDetailView.as_view(), name='YourDetailView'),
    path('new_list/<str:name>/',views.new_list.as_view(), name='new_list'),
    path('new/', views.new_list_back.as_view(),name='new_list_back')
    ]
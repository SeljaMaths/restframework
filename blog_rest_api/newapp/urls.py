from . import views
from django.urls import path,include

urlpatterns = [

    path('YourModelView/', views.YourModelView.as_view(), name='YourModelView'),
    path('YourDetailView/<int:pk>/', views.YourDetailView.as_view(), name='YourDetailView'),
    ]
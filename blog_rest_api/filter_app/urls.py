from django.urls import path,include
from rest_framework import routers
from . import views
from filter_app.views import PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename="posts")
#
urlpatterns = [

    path('', include(router.urls)),
    path('PostAPI/', views.PostAPI.as_view(), name='PostAPI'),
]

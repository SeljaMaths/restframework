from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('posts', PostViewSet, basename="posts")
#
urlpatterns = [
    # path('', include(router.urls)),
]

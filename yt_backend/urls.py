from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideoViewSet

from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'videos', VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


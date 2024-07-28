from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import VideoSerializer
from .models import YtVideos

# Create your views here.


class VideoViewSet(viewsets.ModelViewSet):
    queryset = YtVideos.objects.all()
    serializer_class = VideoSerializer


def redirect_to_api(request):
    return redirect('/api/videos/')
from rest_framework import serializers
from .models import YtVideos


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YtVideos
        fields = '__all__'
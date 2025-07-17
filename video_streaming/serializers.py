from rest_framework import serializers
from .models import *

class streaming_videoSerializers(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ("id", "title", "description", "video_file", "created_at")
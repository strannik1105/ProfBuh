from rest_framework import serializers

from App.models.video_info import VideoInfo


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoInfo
        fields = "__all__"

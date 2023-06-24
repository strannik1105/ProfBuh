from profile import Profile

from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer

from App.serializers.video_serializer import VideoSerializer


class VideoView(generics.CreateAPIView):
    serializer_class = VideoSerializer

    def perform_create(self, serializer):
        url = self.request.POST["url"]
        start_video = self.request.POST["start_video"]
        end_video = self.request.POST["end_video"]
        length = self.request.POST["length_of_annotation"]
        screenshot_delay = self.request.POST["screenshot_delay"]
        serializer.save(url=url)
        serializer.save(start_video=start_video)
        serializer.save(end_video=end_video)
        serializer.save(length_of_annotation=length)
        serializer.save(screenshot_delay=screenshot_delay)

from profile import Profile

from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer

from App.serializers.video_serializer import VideoSerializer
from App.services.rabbitmq.rabbitmq import rabbitmq


class VideoView(generics.CreateAPIView):
    serializer_class = VideoSerializer

    def perform_create(self, serializer: VideoSerializer):
        url = self.request.POST["url"]
        start_video = self.request.POST["start_video"]
        end_video = self.request.POST["end_video"]
        length_of_annotation = self.request.POST["length_of_annotation"]
        screenshot_delay = self.request.POST["screenshot_delay"]
        video = serializer.create({
            'url': url,
            'start_video': start_video,
            'end_video': end_video,
            'length_of_annotation': length_of_annotation,
            'screenshot_delay': screenshot_delay,
        })
        serializer.save()
        rabbitmq.send_message(routing_key="mlmodel.input_data", message=str(video))

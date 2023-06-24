from profile import Profile

from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer




class CreateVallet(generics.CreateAPIView):

    def perform_create(self, serializer):
        foo = request.POST['url']
        serializer.save(owner=self.request.user)
        serializer.save(money=5)
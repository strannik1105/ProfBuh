from django.http import JsonResponse, Http404
from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer


class ArticleView(generics.ListAPIView):
    def get(self, request):
        a = request.query_params
        try:
            data = {"id": a["id"]}
        except Exception as e:
            raise Http404
        return JsonResponse(data)

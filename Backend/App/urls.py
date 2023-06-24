from django.contrib import admin
from django.urls import path, include
#from .views import ChawoView, TestTemplate, LkTemplate, MyTokenObtainPairView, CreateUserView, CreateVallet,CreateOwner,CreateGood,MainTemplate
from django.views.generic import TemplateView

from App.viewsets.video import VideoView

from App.viewsets.article import ArticleView

urlpatterns = [
path('send_url_video/', VideoView.as_view()),
path('get_article/', ArticleView.as_view()),

]

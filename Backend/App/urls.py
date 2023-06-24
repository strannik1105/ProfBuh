from django.contrib import admin
from django.urls import path, include
#from .views import ChawoView, TestTemplate, LkTemplate, MyTokenObtainPairView, CreateUserView, CreateVallet,CreateOwner,CreateGood,MainTemplate
from django.views.generic import TemplateView
urlpatterns = [
path('send_url_video/', ChawoView.as_view()),
path('get_article/', TestTemplate.as_view()),

]

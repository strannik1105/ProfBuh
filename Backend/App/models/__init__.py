from django.contrib import admin

from .article import Article
from .image import Image
from .video_info import VideoInfo

admin.site.register(Article)
admin.site.register(Image)
admin.site.register(VideoInfo)
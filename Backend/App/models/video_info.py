
from django.contrib.auth.models import User
from django.db import models

class VideoInfo(models.Model):
    url = models.TextField(max_length=100)
    start_video = models.TextField(max_length=8)
    end_video = models.TextField(max_length=8)
    length_of_annotation = models.IntegerField()
    screenshot_delay = models.IntegerField()

    def __str__(self):
        return f'Url: {self.url}, ' \
               f'start_video: {self.start_video}, '\
               f'end_video: {self.end_video}, '\
               f'length: {self.length_of_annotation}, '\
               f'screenshot delay: {self.screenshot_delay}'


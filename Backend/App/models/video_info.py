from django.contrib.auth.models import User
from django.db import models


class VideoInfo(models.Model):
    url = models.TextField(max_length=100)
    start_video = models.TextField(max_length=8)
    end_video = models.TextField(max_length=8)
    length_of_annotation = models.IntegerField()
    screenshot_delay = models.IntegerField()
    contact = models.TextField(max_length=2)
    # tg или vk

    def __str__(self):
        payload = {
            'utl': self.url,
            'start_video': self.start_video,
            'end_video': self.end_video,
            'length_of_annotation': self.length_of_annotation,
            'screenshot_delay': self.screenshot_delay,
            'contact': self.contact
        }
        return str(payload)

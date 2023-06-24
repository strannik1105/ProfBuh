
from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    json_name = models.TextField(max_length=51)

    def __str__(self):
        return f'json_name: {self.json_name}, ' \


from django.contrib.auth.models import User
from django.db import models

from Backend.App.models.article import Article


class Image(models.Model):
    article = models.ForeignKey(Article.json_name, on_delete=models.CASCADE,)
    img_name = models.TextField(max_length=51)

    def __str__(self):
        return f'article: {self.article}, ' \
                f'img: {self.img_name}'

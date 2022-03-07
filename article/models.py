from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Article(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=2000)
    tags = models.ManyToManyField(Tags)





from django.contrib.gis.db import models


class Stop(models.Model):
    name = models.CharField(max_length=50, unique=True)
    location = models.TextField()


class Route(models.Model):
    name = models.CharField(max_length=50)
    bus = models.CharField(max_length=15)
    location = models.TextField()

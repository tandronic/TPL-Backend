from django.contrib.gis.db import models


class Stop(models.Model):
    name = models.CharField(max_length=50, unique=True)
    location = models.PointField()

    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField(max_length=50)
    bus = models.CharField(max_length=15)
    location = models.PolygonField()

    def __str__(self):
        return self.name

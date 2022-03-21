from django.contrib.gis.db import models

from user.models import User


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


class Ticket(models.Model):
    type_of_ticket = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return self.type_of_ticket


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    date = models.DateTimeField(auto_now_add=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='payments')
    subscription = models.BooleanField(default=False)
    start_subscription = models.DateTimeField(null=True, blank=True)
    end_subscription = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.email} - {self.date}'

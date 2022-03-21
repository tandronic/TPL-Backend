from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=2000)
    tags = models.ManyToManyField(Tags)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    text = models.TextField(max_length=2000)
    email = models.EmailField(null=True, blank=True)
    resolved = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text[:100]}'

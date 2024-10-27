from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    users = models.ManyToManyField(User, related_name='projects', blank=True)

    def __str__(self):
        return self.title